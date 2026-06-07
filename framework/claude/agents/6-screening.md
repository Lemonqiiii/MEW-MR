# Agent 6: Screening

## Metadata
- **id**: 6
- **type**: execution (horizontal)
- **triggers**: `2` `screen` `筛选` `筛` `screening`
- **pre_gate**: Gate 1
- **post_gate**: Gate 2

## Input
- Literature Search Agent Handoff (master list + five-layer validation + full-text status)
- `state.json` → `active_focus` — inclusion/exclusion criteria (PICO)
- `config.yaml` → `paper_type_system` — paper classification system to use
- `templates/paper-types/<system>.md` — paper type definitions

## Output Schema
```json
{
  "round0_type_distribution": {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0},
  "round1_included": 0,
  "round1_excluded": 0,
  "round2_final_included": 0,
  "round2_excluded": 0,
  "abstract_only_count": 0,
  "abstract_only_pct": 0,
  "type_health_checks": {
    "a_b_c_pct": 0,
    "e_pct": 0,
    "f_g_pct": 0,
    "abstract_only_pct": 0
  },
  "handoff_path": "data/screening_final_inclusion.json"
}
```

---

## Paper Type Classification System

The active classification system is loaded from `templates/paper-types/<config.paper_type_system>.md`.

### Default System: A-J (for mechanism/biomarker reviews)

| Code | Type | Definition | Key Features |
|------|------|-----------|-------------|
| **A** | Mechanism Experiment | In vitro/in vivo causal mechanism experiments | knockout, knockdown, siRNA, CRISPR, western blot, xenograft, mouse model + functional experiments |
| **B** | Translational Research | Human samples + experimental validation | patient samples/tissues + IHC/IF/flow + functional assay |
| **C** | Multi-omics + Validation | scRNA-seq/spatial transcriptomics/proteomics + experimental validation | single-cell, spatial, proteomics + validation/qPCR/IHC |
| **D** | Clinical + Mechanism Endpoint | Clinical trials with biomarker/mechanism endpoints | pubType: Clinical Trial/RCT + biomarker/correlative/translational endpoint |
| **E** | Pure Bioinformatics | TCGA/GEO mining, gene signatures, prognostic models — **no experimental validation** | TCGA, GEO, LASSO, Cox, nomogram, signature, CIBERSORT — without functional validation |
| **F** | Systematic Review/Meta-Analysis | Evidence synthesis with explicit methodology (PRISMA, etc.) | pubType: Systematic Review/Meta-Analysis; or explicit search strategy + inclusion criteria |
| **G** | Narrative Review | Expert review, opinion pieces | pubType: Review; narrative summary without systematic search |
| **H** | Clinical Efficacy | Pure efficacy/safety data, no mechanism analysis | pubType: Clinical Trial/RCT; reports ORR/PFS/OS/safety only, no biomarker |
| **I** | Case Report | Single or small case series | pubType/title: Case Report/Case Series |
| **J** | Methods/Protocol | Trial protocols, methodology papers | pubType: methods-article; or "study protocol"/"trial design" in title |

**Classification Priority**: If a paper matches multiple types, use the higher evidence level (A > B > C > D > E; F > G).

### Citation Scope Matrix

| Type | Supports Mechanism | Supports Clinical | Can Be Primary Ref | Abstract-Only OK |
|------|-------------------|------------------|-------------------|-----------------|
| A | ✅ Primary | ✅ | ✅ | ❌ Full text required |
| B | ✅ Primary | ✅ | ✅ | ❌ Full text required |
| C | ✅ Auxiliary | ✅ | ✅ | ❌ Full text required |
| D | ⚠️ Needs experimental | ✅ Primary | ✅ | ❌ Full text required |
| E | ❌ Correlation only | ⚠️ Hypothesis-generating | ⚠️ Auxiliary only | ⚠️ Acceptable |
| F | ❌ No new data | ✅ Gold standard | ⚠️ Consensus only | ❌ Full text required |
| G | ❌ **Banned** | ⚠️ Background only | ❌ **Banned as primary** | ⚠️ Acceptable |
| H | ❌ | ✅ | ✅ | ❌ Full text required |
| I | ❌ Existence proof only | ❌ | ❌ **Banned as sole** | ⚠️ Acceptable |
| J | ❌ | ❌ | ❌ Informational only | ✅ Acceptable |

**Key Rules**:
- "Banned as primary": Cannot be the main supporting citation for any claim; may be auxiliary ("see also review by X et al.")
- "Banned as sole": Cannot be the only citation for a general claim
- "Correlation only": Can describe association/heterogeneity/candidate genes, but not causal mechanism

---

## Steps

### Round 0: Paper Type Classification (MANDATORY — before PICO screening)

1. For each paper, classify based on title + abstract + pubTypeList → type code A-J
2. Mark classification confidence (HIGH / MEDIUM / LOW)
3. For C vs E borderline (multi-omics but uncertain validation) → default to E; upgrade to C in Round 2 full-text
4. Identify and mark **hard exclusions**:
   - Domain-specific wrong population keywords from `config.yaml` → `exclusion_keywords.population`
   - Abbreviation conflicts → flag for verification
5. Output: type label + confidence per paper

### Round 1: Title/Abstract Screening (PICO + Type Conditions) (MANDATORY)

#### PICO Assessment (all types)
| PICO Dimension | Judgment |
|---------------|----------|
| Population match | YES → pass; NO (critical) → EXCLUDE; UNCERTAIN → INCLUDE |
| Intervention/Exposure match | YES → pass; NO → EXCLUDE; UNCERTAIN → INCLUDE |
| Outcome match | YES → pass; pure prognosis no mechanism → flag; NO → EXCLUDE |
| Study design acceptable | See type conditions below |

#### Type-Conditional Inclusion Thresholds
| Type | Round 1 Inclusion Condition | Threshold |
|------|---------------------------|-----------|
| A/B/C | Population + exposure + mechanism → **direct inclusion** | Minimal |
| D | Population + exposure + biomarker/translational endpoint → **direct inclusion** | Minimal |
| E | Population + exposure + **provides mechanism hypothesis** (not pure prognostic model) → **include, mark ⚠️ CORRELATIVE_ONLY**; pure prognostic → **EXCLUDE** (`PURE_PROGNOSTIC`) | Medium |
| F | Recent (3yr+), relevant focus, explicit methodology → include | Medium |
| G | Only highly cited or key journal → mark ⚠️ REVIEW_SOURCE | High |
| H | Population + exposure + efficacy data → include, mark ⚠️ NO_MECHANISM | Medium |
| I | Reports novel mechanism or special scenario → include; routine cases → EXCLUDE | High |
| J | Informational → include, mark ⚠️ INFO_ONLY | High |

**Exclusion reason codes**: `PURE_PROGNOSTIC`, `WRONG_POPULATION`, `REVIEW_OUTDATED`, `CASE_ROUTINE`, plus domain-specific codes from `config.yaml`.

**Default-inclusion principle**: Any UNCERTAIN → INCLUDE. Only explicit violation of key criteria → EXCLUDE.

### Round 2: Full-Text Screening + Citation Scope Assignment (MANDATORY)

1. **Verify paper type**: Re-assess based on full text (C vs E upgrades happen here)
2. **Type-specific quality assessment**:
   - A/B/C: Experimental design sound? Data complete? Validation sufficient?
   - D: Biomarker analysis prespecified or post hoc?
   - E: Data source clear (TCGA/GEO accession)? Methods reproducible?
   - F: Search strategy complete? Bias risk assessment performed?
   - G: Journal reputation? Author authority? Arguments supported by original papers?
   - H: Trial design? Sample size? Statistical power?
   - I: Mechanism analysis adequate (not purely clinical description)?
3. **Assign citation scope**: Per Citation Scope Matrix above
4. **Final judgment**: INCLUDE + type label + citation scope, or EXCLUDE + evidence
5. **Type distribution health check**:
   - Mechanism reviews: A+B+C ≥20% of final inclusion
   - A+B = 0 → ⚠️ **SEVERE WARNING**: mechanism review with zero mechanism experiment papers
   - E > 50% → ⚠️ Warning: review may be built on correlational evidence
   - F+G > 30% → ⚠️ Warning: over-reliance on secondary sources
6. **Abstract-only ratio control**: ≤20% of final inclusion; A/B/C/D/F types cannot be abstract-only

---

## Output: Screening Report Structure

```markdown
## Screening Report — [Topic] — YYYY-MM-DD

### Round 0: Paper Type Classification
- Total classified: N
- Type distribution: [table with counts and %]

### Round 1: Title/Abstract Screening
- Pre-screening: N
- Excluded: M (reason distribution table)
- Included: K

### Round 2: Full-Text Screening + Citation Scope
- Pre-screening: K
- Full text accessible: P (XX%)
- Abstract-only: Q (XX%) — [✅ ≤20% / ⚠️ >20%]
- Final included: J

### Citation Scope Summary
[table: can_support_mechanism, can_support_clinical, can_be_primary_ref counts]

### Type Distribution Health Check
[table: check, threshold, actual, status]

### PRISMA Flowchart Data
[numbers for PRISMA: retrieved → deduped → screened → full-text → included]
```

### Quality Hedge: Agent 4 Spot-Check
Agent 4 randomly samples 15-20% from Round 2 excluded list:
- Verify exclusion reasons are sound
- If sample error rate >10% → entire screening batch marked unreliable → re-review
