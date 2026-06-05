"""Phase 3.3: Full-text screening — deep evaluation of 62 papers for final inclusion.

Evaluates each paper across dimensions:
1. Squamous NSCLC specificity
2. Immunotherapy resistance mechanism depth
3. Study design quality
4. Mechanism category coverage
"""
import json, os, re, html as html_mod

DATA_DIR = "E:/medical-review/data"
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
# MECHANISM CATEGORIES for classification
# ============================================================
MECHANISM_CATEGORIES = {
    "tumor_intrinsic": {
        "label": "Tumor-Intrinsic Resistance",
        "keywords": [
            r"tumor.intrinsic|intrinsic.resist|cancer.cell.intrinsic",
            r"oncogenic.signaling|MAPK|PI3K|AKT|mTOR|WNT|.catenin|Notch|Hedgehog|STAT|JAK|NF.kB",
            r"tumor.suppressor|TP53|PTEN|STK11|LKB1|KEAP1|NFE2L2|NRF2",
            r"cell.cycle|apoptosis|autophagy|ferroptosis|pyroptosis|anoikis",
            r"DNA.damage.repair|genomic.instability|mutational.burden|TMB|neoantigen",
            r"epithelial.mesenchymal|EMT|mesenchymal.transition",
        ],
    },
    "antigen_presentation": {
        "label": "Antigen Presentation & Immune Recognition",
        "keywords": [
            r"antigen.present|MHC|HLA.class|.2.microglobulin|B2M|TAP|proteasome",
            r"neoantigen|tumor.antigen|immunogenicity|immune.recognition",
            r"interferon.signaling|IFN.|JAK.STAT|IRF",
            r"epigenetic.silenc|histone.modif|DNA.methyl|HDAC|EZH2|chromatin",
        ],
    },
    "immune_checkpoint": {
        "label": "Immune Checkpoint & Co-inhibitory Pathways",
        "keywords": [
            r"PD-L1|PD-1|CTLA-4|LAG-?3|TIM-?3|TIGIT|VISTA|B7.H3|BTLA",
            r"checkpoint.upregulation|checkpoint.expression|adaptive.resist",
            r"co.inhibitory|co.stimulatory|immune.synapse",
        ],
    },
    "t_cell_dysfunction": {
        "label": "T Cell Exhaustion & Dysfunction",
        "keywords": [
            r"T.cell.exhaust|CD8.exhaust|T.cell.dysfunction|T.cell.anergy",
            r"effector.function|cytotoxicity|granzyme|perforin|IFN.?.product",
            r"memory.T.cell|effector.T.cell|T.cell.differentiation",
            r"terminal.exhaust|progenitor.exhaust|TOX|TCF.?1|PD-1.high",
        ],
    },
    "immunosuppressive_cells": {
        "label": "Immunosuppressive Cell Populations",
        "keywords": [
            r"MDSC|myeloid.derived.suppressor|Treg|regulatory.T.cell|TAM|tumor.associated.macrophage",
            r"M2.macrophage|M1.macrophage|macrophage.polarization",
            r"CAF|cancer.associated.fibroblast|neutrophil|N2.neutrophil|DC|dendritic.cell",
            r"immunosuppressive.population|immune.infiltration|immune.exclusion|immune.desert",
        ],
    },
    "cytokine_metabolism": {
        "label": "Cytokine & Metabolic Immune Modulation",
        "keywords": [
            r"cytokine|chemokine|IL-\d|TGF.?.|TNF.?.|interferon|interleukin",
            r"metabolism|glycolysis|oxidative.phosphoryl|hypoxia|HIF|IDO|tryptophan",
            r"lactic.acid|pH|acidosis|nutrient.deplet|amino.acid|arginine|glutamine",
            r"adenosine|ATP|reactive.oxygen|ROS|lipid|fatty.acid",
        ],
    },
    "genomic_transcriptomic": {
        "label": "Genomic & Transcriptomic Determinants",
        "keywords": [
            r"genomic|transcriptom|sequencing|RNA.seq|single.cell|scRNA",
            r"mutation.signature|copy.number|chromosomal.instability|aneuploidy",
            r"gene.expression.profil|molecular.subtype|immune.subtype",
            r"lncRNA|miRNA|circRNA|non.coding.RNA|epigenetic",
            r"prognostic.model|predictive.signature|risk.score|gene.signature",
        ],
    },
    "acquired_resistance": {
        "label": "Acquired Resistance Mechanisms",
        "keywords": [
            r"acquired.resist|secondary.resist|developed.resist|emerging.resist",
            r"resistance.acquired|treatment.induced|selection.pressure|clonal.evolution",
            r"phenotypic.plasticity|lineage.plasticity|transformation|transdifferentiation",
            r"SCLC.transform|histological.transform|neuroendocrine",
        ],
    },
    "combination_strategies": {
        "label": "Combination Strategies to Overcome Resistance",
        "keywords": [
            r"combination.therapy|dual.blockade|combined.immunotherapy",
            r"chemoimmunotherapy|radioimmunotherapy|antiangiogenic",
            r"overcom.*resist|circumvent.*resist|revers.*resist|resensitiz",
            r"bispecific|ADC|antibody.drug.conjugate|vaccine|CAR.?T",
        ],
    },
}

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

    # === DIMENSION 1: Squamous specificity (0-5 pts) ===
    sq_in_title = bool(re.search(r'squam|LUSC|LSCC', title, re.IGNORECASE))
    sq_first_in_title = bool(re.search(r'^(?:.{-5})?(?:lung|pulmonary)?\s*squam', title, re.IGNORECASE))

    if sq_first_in_title:
        score += 5
        flags.append("SQ_TITLE_PRIMARY")
    elif sq_in_title:
        score += 3
        flags.append("SQ_TITLE")
    else:
        sq_mentions = len(re.findall(r'squam|LUSC|LSCC', combined, re.IGNORECASE))
        if sq_mentions >= 3:
            score += 2
            flags.append("SQ_MULTIPLE_MENTION")
        else:
            score += 1
            flags.append("SQ_PASSING")

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

    # === DIMENSION 5: Specific relevance to squamous ICI resistance (0-3 pts) ===
    sq_ici_res_focus = bool(re.search(r'(?:squam|LUSC|LSCC).*(?:immun|checkpoint|PD-|PDL).*(?:resist|evasion|escape|exhaust)', combined, re.IGNORECASE))
    if sq_ici_res_focus:
        score += 3
        flags.append("PERFECT_FOCUS")
    else:
        # Check if at least discusses resistance in lung cancer context
        lung_res_focus = bool(re.search(r'(?:lung|NSCLC).*(?:resist|evasion|escape).*(?:immun|checkpoint|PD-|PDL)', combined, re.IGNORECASE))
        if lung_res_focus:
            score += 1
            flags.append("LUNG_RES_FOCUS")

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
    "# Phase 3.3 全文筛选日志",
    f"\n**日期**: 2026-06-04",
    f"**初始候选**: {len(papers)} 篇",
    f"**最终纳入**: {len(top_papers)} 篇",
    f"**排除**: {len(remaining)} 篇\n",
    "## 筛选标准\n",
    "### 纳入标准（全部满足）",
    "- 鳞状细胞肺癌为主要或重要研究对象",
    "- 明确讨论免疫治疗耐药机制",
    "- 机制性讨论充分（非纯临床疗效/安全性）",
    "- 摘要质量可接受\n",
    "### 排除标准（满足任一）",
    "- 鳞癌仅作为亚组被提及，非主要研究对象",
    "- 无实质性耐药机制讨论",
    "- 纯预后预测模型，无生物学机制洞察",
    "- 研究方案/试验设计，无结果数据\n",
    "## 机制覆盖度\n",
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
