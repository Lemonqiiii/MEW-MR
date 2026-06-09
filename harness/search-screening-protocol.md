# Search and Screening Protocol

> Purpose: standardize literature retrieval, screening, full-text access, and evidence-use decisions across review projects.
> Scope: applies before drafting begins and whenever a new review topic is created.

---

## 1. Search Protocol

Before any database search, create or update `docs/search-results/search-protocol.md`.

Required fields:

| Field | Requirement |
|-------|-------------|
| Review question | PICO/PECO/SPIDER, matching `memory/active-focus.md` |
| Review type | Narrative, systematic narrative, systematic review, or meta-analysis |
| Databases | PubMed, Europe PMC, Semantic Scholar, plus topic-triggered Tier 2 databases |
| Search date | Exact date for each database |
| Search strings | Complete database-specific query strings |
| Limits | Year, language, species, article type, population, and full-text limits |
| Known key papers | 5-10 seed papers that the strategy must retrieve |
| Search diagnostics | Sensitivity, precision sample, and missing-term analysis |
| API/model provenance | Model/API used to generate or refine search terms |

Searches are not considered complete until the protocol records the exact query used.

---

## 2. Database Activation Rules

| Trigger | Required databases |
|---------|--------------------|
| Any biomedical review | PubMed + Europe PMC |
| Recent/emerging topic | Europe PMC including preprints |
| Clinical trials or interventions | ClinicalTrials.gov + Cochrane CENTRAL if accessible |
| Systematic review / meta-analysis | Cochrane Library + Embase strongly recommended |
| Drug/device safety | Embase strongly recommended |
| Chinese/Asian population focus | CNKI + Wanfang + SinoMed if feasible |
| Guidelines or clinical recommendations | Guideline repositories + society guidelines |

If a recommended database is not accessible, record the reason in `search-protocol.md` and compensate with citation chasing or another accessible source.

---

## 3. Search Quality Checks

### Gate Search

| Check | Pass standard |
|-------|---------------|
| Known-paper retrieval | 100% of seed papers retrieved or justified |
| Precision sample | At least 15/20 top records relevant, or query revised |
| Missing-term scan | Major synonyms and spelling variants recorded |
| Database coverage | All required databases searched or access limitation documented |
| Deduplication | PMID, DOI, and fuzzy-title deduplication performed |
| Search log | Query, date, result count, and export file recorded |

Failure blocks screening until fixed or explicitly justified.

---

## 4. Screening Decision Log

All screened records should be written to `docs/search-results/screening-decisions.csv` or `.json`.

Minimum fields:

| Field | Meaning |
|-------|---------|
| record_id | Internal record id |
| pmid | PMID if available |
| doi | DOI if available |
| title | Article title |
| year | Publication year |
| source_database | PubMed, Europe PMC, Embase, etc. |
| screening_round | R0, R1, R2 |
| decision | include, exclude, maybe, fulltext_required |
| reason_code | Controlled exclusion/inclusion reason |
| confidence | high, medium, low |
| reviewer | Human or model/API identifier |
| conflict_status | none, conflict, resolved |
| fulltext_status | see Section 6 |
| citation_scope | mechanism, clinical, background, methods, not_citable |
| notes | Short free-text rationale |

---

## 5. Screening Workflow

### Round 0: Intake and Hard Exclusion

Tasks:
- Deduplicate by PMID, DOI, and title similarity.
- Classify article type.
- Exclude obvious wrong population, wrong species, wrong disease area, and duplicate records.
- Mark missing abstracts as `maybe` unless title clearly violates scope.

### Round 1: Title/Abstract Screening

Tasks:
- Apply current PICO/PECO/SPIDER.
- Record inclusion/exclusion reason codes.
- Mark uncertain studies as `maybe` rather than excluding silently.
- Flag high-impact papers as `fulltext_required` if the abstract is insufficient.

### Round 2: Full-Text Screening

Tasks:
- Verify eligibility against full text where available.
- Assign citation scope.
- Record whether claims can rely on abstract, full text, or neither.
- Update evidence table and full-text access log.

---

## 6. Full-Text Access and VPN Workflow

Full-text access is tracked in `docs/search-results/fulltext-access-log.csv`.

Minimum fields:

```csv
pmid,doi,title,journal,year,access_tier,status,pdf_path,attempts,notes
```

### Access Tiers

| Tier | Source | Agent action | Evidence-use rule |
|------|--------|--------------|-------------------|
| Tier 1 | PMC, Europe PMC OA, publisher OA, preprints | Agent may retrieve automatically | Can support claims if quality appropriate |
| Tier 2 | Institutional subscription / VPN required | Generate VPN checklist for user | Can support claims after PDF/full text is available |
| Tier 3 | Paywall without access | Try legal alternatives; mark unresolved | Do not use for core claims unless full text obtained |
| Tier 4 | Abstract only | Mark `ABSTRACT_ONLY` | Background only; not core evidence |

### VPN Checklist

When Tier 2 records exist, generate `docs/search-results/vpn-download-checklist.md` with:
- PMID/DOI
- title
- journal/year
- DOI URL
- publisher URL if known
- suggested filename: `PMID_FirstAuthor_Year.pdf`
- reason full text is needed

After the user downloads PDFs into `docs/papers/fulltext/`, the Agent should:
1. Match files to PMID/DOI.
2. Update `fulltext-access-log.csv`.
3. Update `screening-decisions` and the evidence table.
4. Re-run abstract-only proportion checks.

---

## 7. Abstract-Only Evidence Discipline

Abstract-only records must be labeled `ABSTRACT_ONLY`.

Allowed:
- background context
- existence of a study
- search/screening completeness
- evidence-gap statements

Not allowed:
- core conclusions
- numerical conclusions not fully visible in abstract
- mechanistic claims
- practice recommendations
- sole support for a contested statement

Thresholds:
- Abstract-only records must be <=20% of included studies.
- Abstract-only core-candidate records trigger `FULLTEXT_REQUIRED`.
- If a full text remains unavailable, the manuscript must either omit the claim or explicitly state the limitation.

---

## 8. AI Double-Pass Screening

When no human second reviewer is available:
1. Run two independent screening passes using different prompts or model/API configurations.
2. Compare decisions on at least 10-20% of records or all `maybe` records.
3. Send conflicts to a resolution pass.
4. Record conflict status and final reason.

This does not replace human dual screening for formal systematic reviews, but it reduces single-prompt bias.

---

## 9. Evidence Table Requirements

Create or update `data/<topic>/evidence_table.*` before drafting.

Minimum fields:
- PMID/DOI
- study design
- population
- intervention/exposure
- comparator
- follow-up duration
- outcomes
- key effect estimates
- bias/quality concerns
- full-text status
- citation scope
- manuscript claim anchors

Drafting should use the evidence table as the primary input, not raw search exports.

---

## 10. Gate Screening

| Check | Pass standard |
|-------|---------------|
| Decision log completeness | >=95% screened records have decision + reason |
| Conflict resolution | 100% conflicts resolved or escalated |
| Full-text status | 100% included records assigned an access tier |
| Abstract-only ratio | <=20% included records, with no core claim relying on abstract only |
| Citation scope | 100% included records have citation scope |
| Evidence table | All cited studies represented |

Failure blocks drafting unless the limitation is documented and accepted.
