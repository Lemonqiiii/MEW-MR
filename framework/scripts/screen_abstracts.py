"""Phase 3.1: Title/Abstract Screening for NSCLC Squamous Immunotherapy Resistance Review.

Multi-tier screening based on PICO criteria:
- P: NSCLC squamous cell carcinoma patients
- I: Immune checkpoint inhibitors (anti-PD-1/PD-L1/CTLA-4)
- C: Responders vs non-responders; primary vs acquired resistance
- O: Resistance mechanisms (tumor-intrinsic, TME, genomic, immune evasion)
"""

from config_loader import load_config, find_project_root
config = load_config()
ROOT = find_project_root()

import json, os, re

DATA_DIR = str(ROOT / config["paths"]["data_dir"])
INPUT_FILE = os.path.join(DATA_DIR, "pubmed_relevant_for_screening.json")
OUTPUT_INCLUDED = os.path.join(DATA_DIR, "screening_included.json")
OUTPUT_EXCLUDED = os.path.join(DATA_DIR, "screening_excluded.json")
OUTPUT_UNCERTAIN = os.path.join(DATA_DIR, "screening_uncertain.json")
OUTPUT_LOG = os.path.join(DATA_DIR, "screening_log.md")

# ============================================================
# INCLUSION SIGNALS (strong positive indicators)
# ============================================================
INCLUSION_SIGNALS = {
    # Direct topic match
    "direct_squamous_ici_resistance": [
        r"squamous.*(?:immunotherapy|immune.checkpoint|PD-?1|PD-?L1|CTLA-?4).*resist",
        r"(?:lung|pulmonary)\s+squamous.*(?:immunotherapy|immune.checkpoint).*resist",
        r"LUSC.*(?:immunotherapy|immune).*resist",
        r"LSCC.*(?:immunotherapy|immune).*resist",
    ],
    # Squamous-specific mechanisms
    "squamous_specific_mechanisms": [
        r"squamous.*(?:tumor.microenvironment|TME|immune.evasion|immune.escape)",
        r"squamous.*(?:immune.desert|immune.exclusion|immune.cold)",
        r"squamous.*(?:T.cell.exhaustion|CD8.*exhaust|T.cell.dysfunction)",
        r"squamous.*(?:neoantigen|antigen.presentation|MHC|HLA).*resist",
        r"squamous.*(?:WNT|.catenin|TGF.|MAPK|PI3K|PTEN|STK11|KEAP1).*immun",
    ],
    # Resistance mechanism reviews
    "resistance_mechanism_reviews": [
        r"resist.*mechanism.*(?:immunotherapy|immune.checkpoint).*(?:lung|NSCLC)",
        r"(?:primary|acquired|adaptive).*resist.*(?:immunotherapy|immune).*(?:lung|NSCLC)",
        r"overcom.*resist.*(?:immunotherapy|immune.checkpoint).*(?:lung|NSCLC)",
    ],
    # Squamous NSCLC immunotherapy focused
    "squamous_nsclc_immunotherapy": [
        r"(?:non.small.cell|NSCLC).*squamous.*(?:immunotherapy|immune.checkpoint)",
        r"squamous.*(?:NSCLC|non.small.cell).*(?:immunotherapy|immune.checkpoint)",
    ],
    # Key mechanism keywords
    "key_mechanisms": [
        r"(?:tumor.microenvironment|TME).*(?:squamous|lung.cancer).*resist",
        r"squamous.*(?:immune.landscape|immune.profil|immunophenotyp).*(?:resist|immunotherapy)",
        r"squamous.*(?:genomic|transcriptom|epigen).*(?:immunotherapy|immune).*resist",
        r"squamous.*(?:checkpoint|PD-L1|PD-1|CTLA-4).*(?:resist|evasion|escape)",
    ],
}

# ============================================================
# EXCLUSION SIGNALS (definite rejections)
# ============================================================
EXCLUSION_SIGNALS = {
    # Mild penalties for papers with low mechanistic content
    "limited_mechanism": [
        r"safety|tolerability|dose.escalation",  # Safety/dosing focus
        r"cost.effect|economic|budget.impact",  # Health economics
        r"quality.of.life|patient.reported.outcome",  # QoL only
    ],
    # Not primarily about immunotherapy
    "not_immunotherapy_focus": [
        r"chemotherapy(?!.*(?:immunotherapy|immune.checkpoint|PD-1|PD-L1))",
        r"targeted.therapy.*(?:EGFR|ALK|ROS1|BRAF)(?!.*(?:immunotherapy|immune))",
    ],
    # Wrong publication type
    "wrong_pub_type": [
        r"study\s+protocol|trial\s+protocol",
        r"correction|erratum|retraction",
    ],
    # Too narrow or irrelevant for review
    "limited_scope": [
        r"radiomics|radiogenomics",  # Imaging-only
        r"single.nucleotide.polymorphism|SNP|GWAS(?!.*(?:mechanism|immune|TME))",
    ],
}

# ============================================================
# RELEVANCE BOOST KEYWORDS
# ============================================================
BOOST_KEYWORDS = {
    "high_impact_journals": [
        "nature", "science", "cell", "lancet", "nejm", "jama",
        "cancer.cell", "cancer.discovery", "immunity", "nature.medicine",
        "nature.immunology", "nature.cancer", "journal.of.clinical.oncology",
        "clinical.cancer.research", "cancer.research", "journal.of.thoracic.oncology",
        "annals.of.oncology", "science.translational.medicine",
    ],
    "review_article": [
        "review", "systematic.review", "meta.analysis",
    ],
    "highly_cited_hint": [
        "landmark", "paradigm", "consensus", "guideline",
        "state.of.the.art", "comprehensive.review",
    ],
}

# ============================================================
# HARD EXCLUSION: Non-lung squamous cancers
# ============================================================
NON_LUNG_SQUAMOUS = [
    r"oral\s+squamous|OSCC|mouth\s+squamous",
    r"esophageal\s+squamous|ESCC|esophagus\s+squamous",
    r"head\s+and\s+neck\s+squamous|HNSCC",
    r"cutaneous\s+squamous|cSCC|skin\s+squamous",
    r"cervical\s+squamous|cervix\s+squamous",
    r"anal\s+squamous|vulvar\s+squamous|penile\s+squamous",
    r"laryngeal\s+squamous|pharyn\w*\s+squamous|tongue\s+squamous",
    r"nasopharyngeal\s+squamous|oropharyngeal\s+squamous",
]

def is_lung_squamous(title, abstract):
    """Check if paper is about LUNG squamous (not other squamous cancers)."""
    combined = (title + " " + abstract).lower()

    # Check for non-lung squamous cancers
    for pattern in NON_LUNG_SQUAMOUS:
        if re.search(pattern, combined, re.IGNORECASE):
            # Check if lung is ALSO mentioned prominently
            lung_mentions = len(re.findall(r'\b(?:lung|pulmonary|NSCLC|LSCC|LUSC|SQCC)\b', combined, re.IGNORECASE))
            if lung_mentions < 2:
                return False, f"non_lung_squamous:{pattern}"

    # Must have lung context
    lung_patterns = [
        r'\b(?:lung|pulmonary)\s+squamous',
        r'\b(?:NSCLC|non.small.cell).*squamous',
        r'\bsquamous.*(?:NSCLC|non.small.cell)',
        r'\bLUSC\b', r'\bLSCC\b', r'\bSQCC\b',
        r'\blung\s+cancer\b.*\bsquamous',
    ]
    for pattern in lung_patterns:
        if re.search(pattern, combined, re.IGNORECASE):
            return True, ""

    # If no clear lung context, check title specifically
    title_lower = title.lower()
    has_lung = bool(re.search(r'\b(?:lung|pulmonary|NSCLC)\b', title_lower, re.IGNORECASE))
    has_squamous = bool(re.search(r'\bsquam\w+\b', title_lower, re.IGNORECASE))

    if has_lung and has_squamous:
        return True, ""

    return False, "no_lung_context"

def clean_text(text):
    """Clean HTML tags and normalize text."""
    if not text:
        return ""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.lower().strip()

def check_signals(text, signal_dict):
    """Check how many signal groups match the text."""
    matched_groups = []
    for group_name, patterns in signal_dict.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                matched_groups.append(group_name)
                break  # One match per group is enough
    return matched_groups

def score_paper(paper):
    """Score a paper for relevance. Higher = more likely to include."""
    title = clean_text(paper.get("title", ""))
    abstract = clean_text(paper.get("abstractText", ""))
    combined = title + " " + abstract
    journal = clean_text(paper.get("journal", ""))
    pub_types = [str(t).lower() for t in paper.get("pubTypeList", [])]
    pub_year = paper.get("pubYear", "")

    score = 0
    reasons = []

    # HARD CHECK: Must be lung squamous, not other squamous
    is_lung, non_lung_reason = is_lung_squamous(title, abstract)
    if not is_lung:
        score -= 10  # Heavy penalty for non-lung squamous
        reasons.append(f"HARD_EXCLUDE:{non_lung_reason}")

    # INCLUSION SIGNALS (+2 each)
    inc_groups = check_signals(combined, INCLUSION_SIGNALS)
    score += len(inc_groups) * 2
    if inc_groups:
        reasons.append(f"INC:{','.join(inc_groups)}")

    # EXCLUSION SIGNALS (-1 each, mild penalty)
    exc_groups = check_signals(combined, EXCLUSION_SIGNALS)
    score -= len(exc_groups) * 1
    if exc_groups:
        reasons.append(f"EXC:{','.join(exc_groups)}")

    # BOOST: Journal prestige (+1)
    for kw in BOOST_KEYWORDS["high_impact_journals"]:
        if kw in journal:
            score += 1
            reasons.append(f"BOOST:high_impact_journal({journal[:40]})")
            break

    # BOOST: Review article (+1)
    is_review = any("review" in pt for pt in pub_types)
    if is_review:
        score += 1
        reasons.append("BOOST:review")

    # BOOST: Recent (+1 for 2024-2026)
    if pub_year in ["2024", "2025", "2026"]:
        score += 1
        reasons.append("BOOST:recent")

    # PENALTY: Too short abstract (likely not substantive)
    if len(abstract) < 200:
        score -= 1
        reasons.append("PENALTY:short_abstract")

    # Direct title match bonus
    title_has_squamous = bool(re.search(r'squamous|LUSC|LSCC|SQCC', title, re.IGNORECASE))
    title_has_resistance = bool(re.search(r'resist|refractory|evasion|escape', title, re.IGNORECASE))
    title_has_ici = bool(re.search(r'immunotherapy|immune.checkpoint|PD-?1|PD-?L1|CTLA-?4|checkpoint.inhibitor', title, re.IGNORECASE))

    if title_has_squamous and title_has_resistance and title_has_ici:
        score += 3
        reasons.append("BOOST:perfect_title_match")
    elif title_has_squamous and (title_has_resistance or title_has_ici):
        score += 1
        reasons.append("BOOST:good_title_match")

    return score, reasons

def main():
    print("WARNING: screen_abstracts.py is a LUSC/NSCLC-specific example. Edit PICO signals before using it for a new review.")

    # Load papers
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        papers = json.load(f)

    print(f"Loaded {len(papers)} papers for screening\n")

    # Score all papers
    scored = []
    for paper in papers:
        score, reasons = score_paper(paper)
        scored.append((score, reasons, paper))

    # Sort by score descending
    scored.sort(key=lambda x: -x[0])

    # Distribution
    score_dist = {}
    for s, _, _ in scored:
        score_dist[s] = score_dist.get(s, 0) + 1

    print("Score distribution:")
    for s in sorted(score_dist.keys(), reverse=True):
        print(f"  Score {s:2d}: {score_dist[s]:3d} papers")

    # Decision thresholds
    # Score >= 4: INCLUDE (good relevance)
    # Score 1-3: UNCERTAIN (borderline, needs manual review)
    # Score <= 0: EXCLUDE

    included = []
    uncertain = []
    excluded = []

    for score, reasons, paper in scored:
        entry = {
            "id": paper.get("id"),
            "pmid": paper.get("pmid"),
            "doi": paper.get("doi"),
            "title": paper.get("title"),
            "authorString": paper.get("authorString"),
            "journal": paper.get("journal"),
            "pubYear": paper.get("pubYear"),
            "abstractText": paper.get("abstractText"),
            "pubTypeList": paper.get("pubTypeList"),
            "citedByCount": paper.get("citedByCount"),
            "score": score,
            "reasons": "; ".join(reasons),
        }

        if score >= 4:
            included.append(entry)
        elif score >= 1:
            uncertain.append(entry)
        else:
            excluded.append(entry)

    print(f"\n=== SCREENING RESULTS ===")
    print(f"INCLUDED:   {len(included)} papers (score >= 4)")
    print(f"UNCERTAIN:  {len(uncertain)} papers (score 1-3)")
    print(f"EXCLUDED:   {len(excluded)} papers (score <= 1)")

    # Save results
    for path, data in [
        (OUTPUT_INCLUDED, included),
        (OUTPUT_UNCERTAIN, uncertain),
        (OUTPUT_EXCLUDED, excluded),
    ]:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved: {path}")

    # Generate screening log
    log_lines = [
        "# Phase 3.1 标题/摘要筛选日志",
        f"\n**筛选日期**: 2026-06-04",
        f"**筛选方法**: 自动化 PICO 评分系统",
        f"\n## 筛选标准",
        f"\n### 纳入标准 (Inclusion)",
        f"- 明确讨论 NSCLC 鳞状细胞癌亚型",
        f"- 涉及免疫检查点抑制剂 (anti-PD-1/PD-L1/CTLA-4)",
        f"- 讨论免疫治疗耐药机制",
        f"- 包含机制性讨论（非纯临床疗效）",
        f"\n### 排除标准 (Exclusion)",
        f"- 主要关注肺腺癌，鳞癌仅提及",
        f"- 仅讨论化疗/靶向治疗耐药",
        f"- 无机制性讨论（纯临床/安全性/经济性研究）",
        f"- 病例报告/研究方案/勘误",
        f"\n## 筛选结果",
        f"\n| 类别 | 数量 | 标准 |",
        f"\n|------|------|------|",
        f"\n| ✅ 纳入 | {len(included)} | Score >= 5 |",
        f"\n| ⚠️ 待定 | {len(uncertain)} | Score 2-4 |",
        f"\n| ❌ 排除 | {len(excluded)} | Score <= 1 |",
        f"\n| **总计** | **{len(papers)}** | |",
        f"\n## 得分分布",
        f"\n| 得分 | 篇数 |",
    ]

    for s in sorted(score_dist.keys(), reverse=True):
        log_lines.append(f"\n| {s} | {score_dist[s]} |")

    log_lines.append(f"\n\n## 纳入文献 (Top 20 预览)\n")
    log_lines.append("\n| # | 年份 | 标题 | 得分 |")
    log_lines.append("\n|---|------|------|------|")
    for i, p in enumerate(included[:20]):
        title = (p["title"] or "")[:80]
        log_lines.append(f'\n| {i+1} | {p["pubYear"]} | {title} | {p["score"]} |')

    log_lines.append(f"\n\n*完整列表见 {OUTPUT_INCLUDED}*")

    with open(OUTPUT_LOG, "w", encoding="utf-8") as f:
        f.write("".join(log_lines))
    print(f"Saved: {OUTPUT_LOG}")

    # Print top included for verification
    print(f"\n=== TOP 15 INCLUDED PAPERS ===")
    for i, p in enumerate(included[:15]):
        title = (p["title"] or "")[:100]
        print(f"{i+1:2d}. [{p['pubYear']}] Score={p['score']} | {title}")

if __name__ == "__main__":
    main()
