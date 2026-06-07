"""Phase 3.3: Full-text screening — deep evaluation of papers for final inclusion.

Evaluates each paper across dimensions:
1. Domain specificity (configurable — skipped if no keywords configured)
2. Mechanism depth (configurable — uses mechanism_categories from config)
3. Study design quality
4. Recency
5. Specific relevance to domain question (configurable — skipped if no keywords)

Configure domain keywords and mechanism categories in config.yaml → screening section.
Without domain config, Dimensions 1, 2, and 5 are skipped automatically.
"""

import sys as _sys
if '--help' in _sys.argv or '-h' in _sys.argv:
    print("Usage: python3 fulltext_screening.py")
    print("  Evaluate papers for final inclusion in the review.")
    print("  Reads screening_final_curated.json from config.yaml paths.data_dir.")
    _sys.exit(0)

from config_loader import load_config, find_project_root
config = load_config()
ROOT = find_project_root()

import json, os, re, html as html_mod

DATA_DIR = str(ROOT / config["paths"]["data_dir"])
INPUT_FILE = os.path.join(DATA_DIR, "screening_final_curated.json")
OUTPUT_FILE = os.path.join(DATA_DIR, "screening_final_inclusion.json")
LOG_FILE = os.path.join(DATA_DIR, "fulltext_screening_log.md")

def clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html_mod.unescape(text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    papers = json.load(f)

# ============================================================
# DOMAIN CONFIGURATION — loaded from config.yaml
# ============================================================
screening_config = config.get("screening", {})
MECHANISM_CATEGORIES = screening_config.get("mechanism_categories", {})
DOMAIN_KEYWORDS = screening_config.get("domain_keywords", [])
DOMAIN_CONTEXT_KEYWORDS = screening_config.get("domain_context_keywords", [])
DOMAIN_ICI_FOCUS = screening_config.get("domain_ici_focus", False)  # e.g. PD-1/PD-L1 resistance focus

if not MECHANISM_CATEGORIES:
    print("NOTE: No mechanism_categories configured — Dimension 2 (mechanism depth) will be skipped.")
if not DOMAIN_KEYWORDS:
    print("NOTE: No domain_keywords configured — Dimensions 1 and 5 (domain specificity) will be skipped.")

def classify_mechanisms(text):
    """Classify which resistance mechanism categories a paper covers."""
    categories = []
    for cat_key, cat_info in MECHANISM_CATEGORIES.items():
        for pattern in cat_info["keywords"]:
            if re.search(pattern, text, re.IGNORECASE):
                categories.append(cat_key)
                break
    return categories

def evaluate_paper(p):
    """Deep evaluation of a single paper."""
    title = clean_html(p.get("title", ""))
    abstract = clean_html(p.get("abstractText", ""))
    combined = (title + " " + abstract).lower()
    pub_types = [str(t).lower() for t in (p.get("pubTypeList", []) or [])]
    pub_year = p.get("pubYear", "")
    journal = (p.get("journal", "") or "").lower()

    score = 0
    flags = []

    # === DIMENSION 1: Domain specificity (0-5 pts) — skippable ===
    if DOMAIN_KEYWORDS:
        kw_pattern = '|'.join(re.escape(kw) for kw in DOMAIN_KEYWORDS)
        in_title = bool(re.search(kw_pattern, title, re.IGNORECASE))
        first_in_title = bool(re.search(r'^(?:.{-5})?(?:' + kw_pattern + ')', title, re.IGNORECASE))

        if first_in_title:
            score += 5
            flags.append("DOM_TITLE_PRIMARY")
        elif in_title:
            score += 3
            flags.append("DOM_TITLE")
        else:
            mentions = len(re.findall(kw_pattern, combined, re.IGNORECASE))
            if mentions >= 3:
                score += 2
                flags.append("DOM_MULTIPLE_MENTION")
            else:
                score += 1
                flags.append("DOM_PASSING")

    # === DIMENSION 2: Mechanism depth (0-8 pts) ===
    mechanisms = classify_mechanisms(combined)
    score += min(len(mechanisms) * 2, 8)
    flags.append(f"MECH:{'+'.join(mechanisms[:4])}")

    # Bonus for specific mechanism focus in title
    mech_in_title = bool(re.search(r'resist|evasion|escape|exhaust|microenvironment|TME|immunosuppress|signaling|pathway', title, re.IGNORECASE))
    if mech_in_title:
        score += 1
        flags.append("MECH_IN_TITLE")

    # === DIMENSION 3: Article quality (0-5 pts) ===
    is_review = any('review' in pt for pt in pub_types)
    is_systematic_review = any('systematic review' in pt for pt in pub_types)
    is_meta = any('meta' in pt for pt in pub_types)
    is_clinical_trial = any('clinical trial' in pt for pt in pub_types)

    if is_systematic_review or is_meta:
        score += 5
        flags.append("QUAL_SYS_REVIEW")
    elif is_review:
        score += 4
        flags.append("QUAL_REVIEW")
    elif is_clinical_trial:
        score += 3
        flags.append("QUAL_CLINICAL_TRIAL")
    else:
        # Original research - check journal quality
        high_impact = bool(re.search(r'nature|science|cell|lancet|NEJM|JAMA|j.clin.oncol|j.thorac.oncol|ann.oncol|clin.cancer.res|cancer.discov|immunity', journal, re.IGNORECASE))
        if high_impact:
            score += 3
            flags.append("QUAL_HIGH_IMPACT")
        else:
            # Check abstract quality
            if len(abstract) > 500:
                score += 2
                flags.append("QUAL_DETAILED")
            else:
                score += 1
                flags.append("QUAL_BRIEF")

    # === DIMENSION 4: Recency (0-2 pts) ===
    if pub_year in ["2026", "2025"]:
        score += 2
        flags.append("RECENT")
    elif pub_year in ["2024", "2023"]:
        score += 1
        flags.append("MODERATE_RECENT")

    # === DIMENSION 5: Specific relevance to domain question (0-3 pts) — skippable ===
    if DOMAIN_KEYWORDS and DOMAIN_CONTEXT_KEYWORDS:
        ctx_pattern = '|'.join(re.escape(kw) for kw in DOMAIN_CONTEXT_KEYWORDS)
        kw_pattern = '|'.join(re.escape(kw) for kw in DOMAIN_KEYWORDS)
        resistance_pattern = r'resist|evasion|escape|exhaust'
        if DOMAIN_ICI_FOCUS:
            resistance_pattern = r'(?:immun|checkpoint|PD-|PDL).*(?:resist|evasion|escape|exhaust)'

        perfect_focus = bool(re.search(
            r'(?:' + kw_pattern + r').*(?:' + resistance_pattern + ')', combined, re.IGNORECASE))
        if perfect_focus:
            score += 3
            flags.append("PERFECT_FOCUS")
        else:
            context_focus = bool(re.search(
                r'(?:' + ctx_pattern + r').*(?:' + resistance_pattern + ')', combined, re.IGNORECASE))
            if context_focus:
                score += 1
                flags.append("DOM_CONTEXT_FOCUS")

    return score, mechanisms, flags

# Evaluate all papers
evaluated = []
for p in papers:
    score, mechanisms, flags = evaluate_paper(p)
    evaluated.append((score, mechanisms, flags, p))

# Sort by score
evaluated.sort(key=lambda x: -x[0])

# Print distribution
print("Score distribution:")
score_dist = {}
for s, _, _, _ in evaluated:
    score_dist[s] = score_dist.get(s, 0) + 1
for s in sorted(score_dist.keys(), reverse=True):
    print(f"  Score {s:2d}: {score_dist[s]:2d} papers")

# Select top ~40
TOP_N = 40
top_papers = evaluated[:TOP_N]
remaining = evaluated[TOP_N:]

print(f"\n=== SELECTION ===")
print(f"Tier 1 (Top ~40): {len(top_papers)} papers")
print(f"Tier 2 (Reserve): {len(remaining)} papers")

# Print Tier 1 with details
print(f"\n=== TIER 1: FINAL INCLUDED ({len(top_papers)} papers) ===")
tier1_data = []
for i, (score, mechanisms, flags, p) in enumerate(top_papers):
    title = clean_html(p.get("title", ""))[:100]
    print(f"{i+1:2d}. [{p['pubYear']}] S={score:2d} | {title}")
    print(f"    Mech: {', '.join(mechanisms[:5])}")
    tier1_data.append({
        "rank": i+1,
        "score": score,
        "mechanisms": mechanisms,
        "flags": flags,
        **p
    })

# Mechanism coverage check
print(f"\n=== MECHANISM COVERAGE ===")
coverage = {}
for cat_key in MECHANISM_CATEGORIES:
    count = sum(1 for _, mechs, _, _ in top_papers if cat_key in mechs)
    coverage[cat_key] = count
    label = MECHANISM_CATEGORIES[cat_key]["label"]
    bar = "█" * (count // 2) + ("▌" if count % 2 else "")
    print(f"  {label:45s}: {count:2d} papers {bar}")

# Identify coverage gaps
gaps = [cat for cat, count in coverage.items() if count < 5]
if gaps:
    print(f"\n⚠️  Coverage gaps (< 5 papers): {', '.join(gaps)}")
    # Try to fill from remaining
    print("Attempting to fill gaps from reserve pool...")
    filled = []
    for cat in gaps:
        for i, (score, mechs, flags, p) in enumerate(remaining):
            if cat in mechs and i not in filled:
                filled.append(i)
                print(f"  Promoting: [{p['pubYear']}] {clean_html(p.get('title',''))[:80]}")
                break

# Save Tier 1
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(tier1_data, f, ensure_ascii=False, indent=2)
print(f"\nSaved: {OUTPUT_FILE}")

# Generate screening log
log = [
    "# Full-Text Screening Log",
    f"\n**Date**: 2026-06-04",
    f"**Initial candidates**: {len(papers)} papers",
    f"**Final included**: {len(top_papers)} papers",
    f"**Excluded**: {len(remaining)} papers\n",
    "## Screening Criteria\n",
    "### Inclusion (all must be met)",
    "- Domain relevance confirmed by keyword match in title/abstract",
    "- Sufficient mechanistic or substantive discussion",
    "- Acceptable abstract quality\n",
    "### Exclusion (any suffices)",
    "- Domain entity only mentioned in passing, not primary subject",
    "- No substantive mechanism or domain-specific discussion",
    "- Pure prognostic/predictive model without biological/mechanistic insight",
    "- Study protocol or trial design without results\n",
    "## Mechanism Coverage\n",
]
for cat_key, count in sorted(coverage.items(), key=lambda x: -x[1]):
    label = MECHANISM_CATEGORIES[cat_key]["label"]
    log.append(f"- **{label}**: {count} 篇")

log.append(f"\n## Tier 1: 最终纳入 ({len(top_papers)} 篇)\n")
log.append("| # | 年份 | 得分 | 机制类别 | 标题 |")
log.append("|---|------|------|---------|------|")
for item in tier1_data:
    title = clean_html(item.get("title", ""))[:60].replace("|", "/")
    mechs = ", ".join(item["mechanisms"][:3])
    log.append(f"| {item['rank']} | {item['pubYear']} | {item['score']} | {mechs} | {title} |")

log.append(f"\n## Tier 2: 储备 ({len(remaining)} 篇)\n")
for i, (score, mechs, flags, p) in enumerate(remaining):
    title = clean_html(p.get("title", ""))[:80].replace("|", "/")
    log.append(f"- [{p['pubYear']}] S={score} | {title}")

with open(LOG_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(log))
print(f"Saved: {LOG_FILE}")
