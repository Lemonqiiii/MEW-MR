"""NRDS Life-Course Review — Phase 3 Automated Screening.
Adapts Agent 6 A-J classification & PICO screening for neonatal respiratory research.
"""
import json, os, re

OUTPUT_DIR = "E:/medical-review/data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load corpus
with open(os.path.join(OUTPUT_DIR, "pubmed_relevant_for_screening.json"), "r", encoding="utf-8") as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers for screening\n")

# ═══════════════════════════════════════════════════════════════
# NRDS-ADAPTED TYPE CLASSIFICATION (Round 0)
# ═══════════════════════════════════════════════════════════════

def classify_paper(p):
    """Classify paper A-J, adapted for neonatal respiratory research."""
    title = (p.get("title") or "").lower()
    abstract = (p.get("abstractText") or "").lower()
    pub_types = [t.lower() for t in p.get("pubTypeList", [])]
    text = title + " " + abstract[:3000]
    year = p.get("pubYear", "")

    # J: Protocol / methods
    if any(kw in title for kw in ["protocol", "trial design", "study protocol"]):
        return ("J", "HIGH", "protocol")
    if "methods-article" in pub_types:
        return ("J", "HIGH", "methods_article")

    # I: Case report
    if any(kw in title for kw in ["case report", "case series", "a case of"]):
        return ("I", "HIGH", "case_report")
    if "case report" in pub_types or "case-reports" in pub_types:
        return ("I", "HIGH", "pubtype_case")

    # F: Systematic review / meta-analysis
    if any(kw in title for kw in ["systematic review", "meta-analysis", "meta analysis"]):
        return ("F", "HIGH", "title_sr")
    if any(kw in abstract[:500] for kw in ["systematic review", "meta-analysis", "prisma"]):
        return ("F", "MEDIUM", "abstract_sr")
    if "systematic review" in pub_types or "meta-analysis" in pub_types:
        return ("F", "HIGH", "pubtype_sr")

    # A: Mechanism experiment (animal/cell models of neonatal lung)
    animal_kw = ["mouse", "mice", "rat", "rabbit", "lamb", "piglet", "animal model",
                 "knockout", "transgenic", "in vivo", "in vitro", "alveolar epithelial",
                 "lung explant", "organoid", "primary culture", "cell line"]
    mechanism_kw = ["signaling pathway", "nf-kb", "nlrp3", "tlr4", "mapk", "pi3k",
                    "wnt", "notch", "hedgehog", "vegf", "pdgf", "tgf-β", "il-6",
                    "il-1β", "tnf-α", "inflammasome", "autophagy", "apoptosis",
                    "oxidative stress", "inflammation", "fibrosis", "alveolarization"]
    has_animal = sum(1 for kw in animal_kw if kw in text)
    has_mechanism = sum(1 for kw in mechanism_kw if kw in text)
    if has_animal >= 2 and has_mechanism >= 2:
        return ("A", "HIGH" if has_mechanism >= 3 else "MEDIUM", "animal_mechanism")
    if has_mechanism >= 4 and has_animal >= 1:
        return ("A", "MEDIUM", "mechanism_heavy")

    # C: Multi-omics / genomics with some validation
    omics_kw = ["single-cell", "scrna-seq", "transcriptom", "proteom", "metabolom",
                "spatial transcriptom", "rna-seq", "microarray", "gene expression profiling"]
    validation_kw = ["qPCR", "rt-pcr", "western blot", "immunohistochemistry", "ihc",
                     "immunofluorescen", "flow cytometry", "elisa", "validated"]
    has_omics = sum(1 for kw in omics_kw if kw in text)
    has_validation = sum(1 for kw in validation_kw if kw in text)
    if has_omics >= 2 and has_validation >= 1:
        return ("C", "HIGH", "omics_validated")
    if has_omics >= 2:
        return ("E", "MEDIUM", "omics_no_validation")  # Downgrade to E without validation

    # B: Translational (human samples + experiments)
    human_sample_kw = ["patient sample", "lung tissue", "tracheal aspirate", "balf",
                       "bronchoalveolar lavage", "cord blood", "umbilical cord",
                       "placenta", "amniotic fluid", "neonatal blood", "preterm infant"]
    has_human_samples = sum(1 for kw in human_sample_kw if kw in text)
    if has_human_samples >= 1 and has_validation >= 2:
        return ("B", "HIGH", "translational")
    if has_human_samples >= 1 and has_mechanism >= 1:
        return ("B", "MEDIUM", "translational_partial")

    # D: Clinical trial with biomarker/mechanism endpoint
    clinical_trial_kw = ["clinical trial", "randomized", "randomised", "rct",
                         "controlled trial", "phase ii", "phase iii", "phase 2", "phase 3"]
    biomarker_kw = ["biomarker", "cytokine", "chemokine", "inflammatory marker",
                    "crp", "procalcitonin", "il-", "cortisol", "protein", "gene expression"]
    is_trial = any(kw in text[:500] for kw in clinical_trial_kw) or \
               any(t in pub_types for t in ["clinical trial", "clinical-trial", "randomized controlled trial"])
    has_biomarker = any(kw in text for kw in biomarker_kw)
    if is_trial and has_biomarker:
        return ("D", "HIGH", "trial_biomarker")

    # H: Clinical efficacy (pure outcome data, no mechanism)
    if is_trial:
        return ("H", "HIGH", "trial_efficacy_only")

    # E: Pure observational / association without mechanistic experiments
    observational_kw = ["cohort", "retrospective", "prospective", "registry",
                        "observational", "cross-sectional", "case-control",
                        "follow-up study", "longitudinal", "population-based"]
    if any(kw in text[:500] for kw in observational_kw) and has_mechanism < 3:
        # Check if it's a clinical study with long-term follow-up
        if any(kw in text for kw in ["follow-up", "long-term", "childhood", "adolescen",
                                      "school age", "adult outcome"]):
            return ("E", "MEDIUM", "observational_followup")
        return ("E", "MEDIUM", "observational")

    # G: Narrative review
    if "review" in pub_types or "review-article" in pub_types:
        return ("G", "HIGH", "pubtype_review")
    if any(kw in title for kw in ["review", "overview", "update", "perspective",
                                   "consensus", "guideline", "recommendation"]):
        return ("G", "MEDIUM", "title_review")

    # Default: check if clinical
    if any(kw in text[:500] for kw in ["neonat", "preterm", "infant", "nicu",
                                        "newborn", "birth", "gestational"]):
        return ("H", "LOW", "clinical_default")

    return ("G", "LOW", "default_review")


# ═══════════════════════════════════════════════════════════════
# NRDS-SPECIFIC PICO SCREENING (Round 1)
# ═══════════════════════════════════════════════════════════════

# Hard exclusion keywords (NRDS context)
HARD_EXCLUDE_TITLE = [
    # Adult conditions
    "adult respiratory distress syndrome", "acute respiratory distress syndrome",
    "ARDS", "acute lung injury", "acute respiratory failure in adults",
    # Non-neonatal populations
    "chronic obstructive pulmonary disease", "COPD", "emphysema",
    "idiopathic pulmonary fibrosis", "IPF", "interstitial lung disease",
    "cystic fibrosis", "pulmonary hypertension in adults",
    "lung cancer", "pulmonary embolism", "pneumonia in adults",
    "asthma in adults", "adult asthma", "occupational lung disease",
    # Non-respiratory neonatal (clearly off-topic)
    "necrotizing enterocolitis", "retinopathy of prematurity screening",
    "hypoxic-ischemic encephalopathy", "HIE", "therapeutic hypothermia",
    "patent ductus arteriosus", "PDA ligation", "congenital heart disease",
    "gastroschisis", "omphalocele", "intestinal atresia",
    "neonatal abstinence syndrome", "neonatal opioid withdrawal",
    "hyperbilirubinemia", "jaundice", "phototherapy",
    "retinopathy of prematurity treatment", "ROP treatment",
    "intraventricular hemorrhage", "IVH", "periventricular leukomalacia",
    "cerebral sinovenous", "neonatal stroke",
    # Maternal-only (not infant outcome)
    "preeclampsia", "gestational diabetes", "maternal mortality",
    "maternal obesity", "GDM", "placenta previa", "placental abruption",
    "chorioamnionitis", "premature rupture of membranes",
    # Non-neonatal
    "pediatric ARDS", "childhood interstitial lung disease",
    "sickle cell", "thalassemia", "hemophilia",
    # COVID (unless specifically about neonatal ventilation lessons)
    "COVID-19", "SARS-CoV-2", "coronavirus disease 2019",
]

EXCLUDE_REASONS = {
    "ADULT_POPULATION": "Adult/non-neonatal population",
    "WRONG_CONDITION": "Not NRDS or neonatal respiratory condition",
    "SHORT_TERM_ONLY": "No long-term follow-up (> 1 year)",
    "NO_INTERVENTION": "No relevant early-life intervention",
    "WRONG_OUTCOME": "Not pulmonary/neurodevelopment/quality of life outcome",
    "METHODS_ONLY": "Protocol/trial design without results",
    "ANIMAL_ONLY": "Animal study without clinical translation",
    "NO_ABSTRACT": "No abstract available for screening",
    "NON_ENGLISH": "Non-English language",
    "PRE_2000": "Published before 2000 (unless landmark)",
    "MATERNAL_ONLY": "Maternal outcome only, no infant follow-up",
    "PURE_NEONATAL": "Short-term neonatal outcome only, no follow-up",
}

def screen_pico(p, paper_type):
    """PICO screening adapted for NRDS life-course review."""
    title = (p.get("title") or "").lower()
    abstract = (p.get("abstractText") or "").lower() if p.get("abstractText") else ""
    text = (title + " " + abstract[:3000])
    year_str = p.get("pubYear", "")
    year = int(year_str) if year_str.isdigit() else 0

    # Check abstract availability
    if not abstract.strip():
        return ("EXCLUDE", "NO_ABSTRACT", 0.0)

    # Year check (pre-2000 only if landmark/highly cited)
    if year < 2000 and int(p.get("citedByCount", 0)) < 50:
        return ("EXCLUDE", "PRE_2000", 0.0)

    # Population check
    pop_neonatal = any(kw in text for kw in [
        "neonat", "preterm", "prematur", "infant", "newborn",
        "very low birth", "extremely low birth", "elbw", "vlbw",
        "nicu", "neonatal intensive", "gestational age", "birth weight",
        "rds", "nrds", "respiratory distress syndrome", "hyaline membrane"
    ])

    # Adult contamination
    pop_adult = any(kw in title for kw in [
        "adult respiratory distress", "acute respiratory distress syndrome", "ards",
        "chronic obstructive pulmonary", "copd", "emphysema",
        "adult asthma", "elderly", "geriatric"
    ])

    if pop_adult and not pop_neonatal:
        return ("EXCLUDE", "ADULT_POPULATION", 0.0)

    if not pop_neonatal:
        # Check if it's about early-life programming / DOHaD
        dohad = any(kw in text for kw in [
            "dohad", "developmental origin", "life course", "fetal origin",
            "early life programming", "fetal programming"
        ])
        if not dohad:
            return ("EXCLUDE", "WRONG_CONDITION", 0.0)

    # Intervention check
    has_intervention = any(kw in text for kw in [
        "ventilat", "cpap", "surfactant", "steroid", "corticosteroid",
        "dexamethasone", "betamethasone", "hydrocortisone", "budesonide",
        "oxygen therap", "oxygen saturat", "oxygen target",
        "high frequency", "hfov", "nippv", "non-invasive",
        "mechanical ventilation", "respiratory support",
        "inhaled nitric", "caffeine", "vitamin a", "diuretic",
        "antenatal steroid", "antenatal corticosteroid",
        "less invasive surfactant", "lisa", "mist", "insure",
        "volume-targeted", "volume guarantee", "pressure-limited"
    ])

    if not has_intervention:
        # Maybe about NRDS risk factors or epidemiology
        has_nrds = any(kw in text for kw in ["rds", "nrds", "respiratory distress"])
        if not has_nrds:
            return ("EXCLUDE", "NO_INTERVENTION", 0.0)

    # Outcome check: must have long-term follow-up
    has_long_term = any(kw in text for kw in [
        "follow-up", "follow up", "long-term", "long term",
        "childhood", "child ", "children", "adolescen",
        "school age", "school-age", "school performance",
        "academic", "adult outcome", "adulthood",
        "life course", "lifelong", "trajector",
        "neurodevelopment", "neuro-development", "cognitive",
        "cerebral palsy", "bayley", "iq", "intelligence",
        "developmental delay", "developmental outcome",
        "motor outcome", "motor function", "behavioral",
        "pulmonary function", "lung function", "fev1",
        "spirometry", "respiratory function", "asthma",
        "wheez", "bronchopulmonary dysplasia", "bpd",
        "respiratory morbidity", "respiratory outcome",
        "quality of life", "hrqol", "functional outcome",
        "functional status", "health status", "well-being",
        "chronic lung disease", "respiratory symptom",
        "rehospitali", "hospitali", "healthcare utiliz",
        "health service use", "economic outcome"
    ])

    if not has_long_term:
        # Check for short-term only
        short_term_only = any(kw in abstract[:500] for kw in [
            "primary outcome", "death", "mortality", "survival",
            "discharge", "length of stay", "nicu stay",
            "nec", "sepsis", "infection", "pda",
            "ivh", "pneumothorax", "air leak",
            "extubation", "weaning", "ventilator days"
        ])
        if short_term_only:
            return ("EXCLUDE", "SHORT_TERM_ONLY", 0.0)
        return ("EXCLUDE", "SHORT_TERM_ONLY", 0.0)

    # Maternal-only check
    if any(kw in title for kw in [
        "preeclampsia", "gestational diabetes", "maternal",
        "pregnancy outcome", "obstetric", "antenatal care",
        "prenatal diagnosis", "chorioamnionitis", "pprom"
    ]) and not any(kw in text for kw in [
        "infant", "neonat", "child", "preterm infant", "offspring"
    ]):
        return ("EXCLUDE", "MATERNAL_ONLY", 0.0)

    # Protocol without results
    if paper_type[0] == "J":
        return ("EXCLUDE", "METHODS_ONLY", 0.0)

    # Calculate relevance score (0-1)
    score = 0.5  # Base
    if pop_neonatal: score += 0.1
    if has_intervention: score += 0.15
    if has_long_term: score += 0.25

    # Score boost for direct relevance
    if any(kw in text for kw in ["neurodevelopment", "cognitive", "bayley", "cerebral palsy"]):
        score += 0.05
    if any(kw in text for kw in ["pulmonary function", "lung function", "fev1", "asthma"]):
        score += 0.05
    if any(kw in text for kw in ["quality of life", "hrqol"]):
        score += 0.03

    score = min(score, 1.0)

    if score >= 0.7:
        return ("INCLUDE", None, score)
    elif score >= 0.5:
        return ("INCLUDE", "BORDERLINE", score)
    else:
        return ("EXCLUDE", "LOW_RELEVANCE", score)


# ═══════════════════════════════════════════════════════════════
# EXECUTE SCREENING
# ═══════════════════════════════════════════════════════════════

print("=" * 60)
print("NRDS Life-Course Review — Automated Screening")
print("=" * 60)

# Round 0: Classification
print("\n── Round 0: Paper Type Classification ──")
type_counts = {t: 0 for t in "ABCDEFGHIJ"}
classified = []
hard_excluded_round0 = []

for p in papers:
    type_code, confidence, reason = classify_paper(p)
    p["paper_type"] = type_code
    p["type_confidence"] = confidence
    p["type_reason"] = reason
    type_counts[type_code] = type_counts.get(type_code, 0) + 1
    classified.append(p)

print(f"Classified {len(classified)} papers")
total = len(classified)
for t in "ABCDEFGHIJ":
    count = type_counts.get(t, 0)
    pct = count / total * 100 if total > 0 else 0
    bar = "#" * int(pct)
    print(f"  {t}: {count:5d} ({pct:5.1f}%) {bar}")

# Round 1: PICO Screening
print("\n── Round 1: PICO Screening ──")
included = []
excluded = []
borderline = []

for p in classified:
    decision, reason, score = screen_pico(p, p["paper_type"])
    p["screen_decision"] = decision
    p["screen_reason"] = reason
    p["relevance_score"] = score

    if decision == "INCLUDE":
        if reason == "BORDERLINE":
            borderline.append(p)
        else:
            included.append(p)
    else:
        excluded.append(p)

print(f"Included: {len(included)}")
print(f"Borderline (included but low confidence): {len(borderline)}")
print(f"Excluded: {len(excluded)}")

# Exclusion reasons
from collections import Counter
exclusion_reasons = Counter(p["screen_reason"] for p in excluded)
print("\nExclusion reasons:")
for reason, count in exclusion_reasons.most_common():
    desc = EXCLUDE_REASONS.get(reason, reason)
    print(f"  {reason}: {count} ({desc})")

# Merge borderline into included
included_all = included + borderline
print(f"\nTotal after Round 1: {len(included_all)} papers (incl {len(borderline)} borderline)")

# Sort by relevance
included_all.sort(key=lambda x: (-x.get("relevance_score", 0), -int(x.get("citedByCount", 0))))

# Round 2 checks
print("\n── Round 2: Quality & Coverage Checks ──")

# Type distribution in included
included_types = Counter(p["paper_type"] for p in included_all)
print("Included type distribution:")
for t in "ABCDEFGHIJ":
    count = included_types.get(t, 0)
    pct = count / len(included_all) * 100 if included_all else 0
    bar = "#" * int(pct)
    print(f"  {t}: {count:5d} ({pct:5.1f}%) {bar}")

# Coverage checks (adapted for NRDS)
# For NRDS: D+H+F should be dominant (clinical trials + SRs), A+B should have some mechanistic support
a_plus_b = included_types.get("A", 0) + included_types.get("B", 0)
d_plus_h = included_types.get("D", 0) + included_types.get("H", 0)
f_count = included_types.get("F", 0)
g_count = included_types.get("G", 0)
e_count = included_types.get("E", 0)

print(f"\nCoverage health:")
print(f"  A+B (mechanistic): {a_plus_b} papers — {'OK' if a_plus_b >= 10 else 'WARNING: low mechanistic evidence'}")
print(f"  D+H (clinical): {d_plus_h} papers — {'OK' if d_plus_h >= 20 else 'LOW'}")
print(f"  F (systematic reviews): {f_count} papers — {'OK' if f_count >= 5 else 'LOW: few SRs for L3 gold standard'}")
print(f"  G (narrative reviews): {g_count} papers — {'OK' if g_count <= len(included_all)*0.2 else 'WARNING: >20% narrative reviews'}")
print(f"  E (observational/no mechanism): {e_count} papers")

# Abstract-only check
abstract_only = [p for p in included_all if not p.get("abstractText")]
print(f"\nAbstract-only: {len(abstract_only)}/{len(included_all)} ({len(abstract_only)/len(included_all)*100:.1f}%)")

# Year coverage
years = [int(p.get("pubYear")) for p in included_all if p.get("pubYear", "").isdigit()]
if years:
    print(f"Year range: {min(years)}-{max(years)}")
    recent = sum(1 for y in years if y >= 2020)
    print(f"2020-2026: {recent}/{len(years)} ({recent/len(years)*100:.0f}%)")

# Save results
screening_output = {
    "included": included_all,
    "excluded": excluded,
    "borderline": borderline,
    "total_screened": len(papers),
    "total_included": len(included_all),
    "total_excluded": len(excluded),
    "type_distribution": dict(included_types),
    "exclusion_reasons": dict(exclusion_reasons),
}

with open(os.path.join(OUTPUT_DIR, "screening_final_included.json"), "w", encoding="utf-8") as f:
    json.dump(included_all, f, ensure_ascii=False, indent=2)

with open(os.path.join(OUTPUT_DIR, "screening_excluded.json"), "w", encoding="utf-8") as f:
    json.dump(excluded, f, ensure_ascii=False, indent=2)

with open(os.path.join(OUTPUT_DIR, "screening_borderline.json"), "w", encoding="utf-8") as f:
    json.dump(borderline, f, ensure_ascii=False, indent=2)

print(f"\n{'=' * 60}")
print(f"Saved:")
print(f"  screening_final_included.json: {len(included_all)} papers")
print(f"  screening_excluded.json: {len(excluded)} papers")
print(f"  screening_borderline.json: {len(borderline)} papers")

# Top 20 overview for manual review
print(f"\n=== Top 20 most relevant papers (for spot check) ===")
for i, p in enumerate(included_all[:20]):
    print(f"{i+1}. [{p['paper_type']}] score={p['relevance_score']:.2f} | [{p.get('pubYear','?')}] {p.get('title','')[:100]}")
    print(f"   PMID:{p.get('pmid','N/A')} | cites:{p.get('citedByCount',0)} | {p.get('journal','')[:50]}")
