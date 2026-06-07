# Paper Type Classification: A-J (Mechanism/Biomarker Reviews)

> This is the default paper classification system. It is designed for reviews focused on
> biological mechanisms, biomarkers, and translational research.
>
> For other review types (epidemiology, clinical comparison, health policy),
> create custom systems in this directory and reference them in config.yaml.

---

## 10-Type Definitions

| Code | Type | Definition | Key Features |
|------|------|-----------|-------------|
| **A** | Mechanism Experiment | In vitro/in vivo causal mechanism experiments | knockout, knockdown, siRNA, CRISPR, western blot, xenograft, mouse model + functional experiments |
| **B** | Translational Research | Human samples + experimental validation | patient samples/tissues + IHC/IF/flow + functional assay |
| **C** | Multi-omics + Validation | scRNA-seq/spatial transcriptomics/proteomics + experimental validation | single-cell, spatial, proteomics + validation/qPCR/IHC |
| **D** | Clinical + Mechanism Endpoint | Clinical trials with biomarker/mechanism endpoints | pubType: Clinical Trial/RCT + biomarker/correlative/translational endpoint |
| **E** | Pure Bioinformatics | TCGA/GEO mining, gene signatures, prognostic models — no experimental validation | TCGA, GEO, LASSO, Cox, nomogram, signature, CIBERSORT — without functional validation |
| **F** | Systematic Review/Meta-Analysis | Evidence synthesis with explicit methodology (PRISMA, etc.) | pubType: Systematic Review/Meta-Analysis; or explicit search strategy + inclusion criteria |
| **G** | Narrative Review | Expert review, opinion pieces | pubType: Review; narrative summary without systematic search |
| **H** | Clinical Efficacy | Pure efficacy/safety data, no mechanism analysis | pubType: Clinical Trial/RCT; reports ORR/PFS/OS/safety only, no biomarker |
| **I** | Case Report | Single or small case series | pubType/title: Case Report/Case Series |
| **J** | Methods/Protocol | Trial protocols, methodology papers | pubType: methods-article; or "study protocol"/"trial design" in title |

**Classification Priority**: If a paper matches multiple types, use the higher evidence level (A > B > C > D > E; F > G).

**Borderline Cases**: C vs E (multi-omics but uncertain validation) → default to E; upgrade to C in Round 2 full-text.

---

## Citation Scope Matrix

| Type | Supports Mechanism | Supports Clinical | Can Be Primary Ref | Abstract-Only OK |
|------|-------------------|------------------|-------------------|-----------------|
| A | Primary evidence | Yes | Yes | No — full text required |
| B | Primary evidence | Yes | Yes | No — full text required |
| C | Auxiliary evidence | Yes | Yes | No — full text required |
| D | Needs experimental support | Primary evidence | Yes | No — full text required |
| E | Correlation only | Hypothesis-generating | Auxiliary only | Acceptable |
| F | No new data | Gold standard | Consensus only | No — full text required |
| G | **Banned** | Background only | **Banned as primary** | Acceptable |
| H | No | Yes | Yes | No — full text required |
| I | Existence proof only | No | **Banned as sole** | Acceptable |
| J | No | No | Informational only | Acceptable |

### Key Rules
- **"Banned as primary"**: Cannot be the main supporting citation for any claim; may be auxiliary ("see also review by X et al.")
- **"Banned as sole"**: Cannot be the only citation for a general claim
- **"Correlation only"**: Can describe association/heterogeneity/candidate genes, but cannot claim causal mechanism

---

## Type-Conditional Inclusion Thresholds

| Type | Round 1 Inclusion Condition | Threshold |
|------|---------------------------|-----------|
| A/B/C | Population + exposure + mechanism → direct inclusion | Minimal |
| D | Population + exposure + biomarker/translational endpoint → direct inclusion | Minimal |
| E | Population + exposure + provides mechanism hypothesis → include, mark CORRELATIVE_ONLY; pure prognostic → EXCLUDE | Medium |
| F | Recent (3yr+), relevant focus, explicit methodology → include | Medium |
| G | Only highly cited or key journal → mark REVIEW_SOURCE | High |
| H | Population + exposure + efficacy data → include, mark NO_MECHANISM | Medium |
| I | Reports novel mechanism or special scenario → include; routine cases → EXCLUDE | High |
| J | Informational → include, mark INFO_ONLY | High |

## Exclusion Reason Codes
- `PURE_PROGNOSTIC` — pure prognostic model/gene signature, no mechanism hypothesis
- `WRONG_POPULATION` — wrong population per config.yaml exclusion keywords
- `REVIEW_OUTDATED` — review but outdated (pre-2022)
- `CASE_ROUTINE` — routine case report, no novel mechanism

## Round 2 Type-Specific Quality Assessment

| Type | Full-Text Focus |
|------|----------------|
| A/B/C | Experimental design sound? Data complete? Validation sufficient? |
| D | Biomarker analysis prespecified or post hoc? |
| E | Data source clear (TCGA/GEO accession)? Methods reproducible? |
| F | Search strategy complete? Bias risk assessment performed? |
| G | Journal reputation? Author authority? Arguments supported by original papers? |
| H | Trial design? Sample size? Statistical power? |
| I | Mechanism analysis adequate (not purely clinical description)? |

## Type Distribution Health Checks

| Check | Threshold | Action if Failed |
|-------|-----------|-----------------|
| A+B+C % of final inclusion | >= 20% (mechanism reviews) | Severe warning: mechanism review lacks mechanism experiments |
| A+B = 0 | Never acceptable for mechanism reviews | Critical: zero mechanism experiment papers |
| E type % | < 50% | Warning: review built on correlational evidence |
| F+G type % | < 30% | Warning: over-reliance on secondary sources |
| Abstract-only % | <= 20% | Warning: prioritize Tier 2/3 full-text acquisition |
| A/B/C/D/F abstract-only | Must be 0% | Error: these types require full text |
