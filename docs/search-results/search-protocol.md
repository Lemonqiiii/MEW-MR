# Search Protocol

## Review Context

| Field | Value |
|-------|-------|
| Review topic | Postnatal corticosteroids for preterm infants with NRDS/BPD and long-term neurodevelopment |
| Review type | Focused narrative review with systematic-search transparency elements |
| Current manuscript | manuscript/pncs_systematic_review.md |
| Target journal | Archives of Disease in Childhood: Fetal & Neonatal Edition (BMJ) |
| Search owner | Codex/AI-assisted single reviewer |
| Search date(s) | 2026-06-08 |
| Model/API assistance | Europe PMC API search and Codex-assisted screening |
| Human verification status | Author verification required before submission |

## PICO / PECO / SPIDER

| Element | Definition |
|---------|------------|
| Population | Preterm or very-low-birth-weight infants with NRDS/BPD risk or respiratory support |
| Intervention / Exposure | Postnatal systemic corticosteroids, primarily dexamethasone and hydrocortisone; inhaled budesonide as comparator pathway |
| Comparator | Placebo/no treatment, agent/timing/dose comparisons, or observational untreated controls |
| Outcomes | Neurodevelopment, cerebral palsy, Bayley scores, cognition/IQ, behavior, school-age function, death/BPD as contextual outcomes |
| Study designs | RCTs, RCT follow-up studies, systematic reviews/meta-analyses, cohort studies, guideline statements for context |
| Exclusions | Antenatal corticosteroids, adult ARDS, term-only populations, short-term-only outcomes unless needed for context, non-English records |

## Databases

| Database | Required? | Access route | Search date | Result count | Export file | Notes |
|----------|-----------|--------------|-------------|--------------|-------------|-------|
| Europe PMC | Yes | API | 2026-06-08 | 8406 unique after six search angles | data/pncs_search/all_unique.json | Primary reproducible source |
| Europe PMC core angle | Yes | API | 2026-06-08 | 4123 | data/pncs_search/01_core.json | Broad PICO query |
| Europe PMC systematic reviews | Yes | API | 2026-06-08 | 361 | data/pncs_search/02_systematic_reviews.json | Evidence synthesis angle |
| Europe PMC RCTs | Yes | API | 2026-06-08 | 564 | data/pncs_search/03_rcts.json | Trial angle |
| Europe PMC hydrocortisone focused | Yes | API | 2026-06-08 | 2099 | data/pncs_search/04_hydrocortisone_focused.json | Agent-specific angle |
| Europe PMC inhaled budesonide | Yes | API | 2026-06-08 | 1763 | data/pncs_search/05_inhaled_budesonide.json | Comparator pathway |
| Europe PMC school-age/adult | Yes | API | 2026-06-08 | 5125 | data/pncs_search/06_school_age_adult.json | Long-term follow-up angle |
| ClinicalTrials.gov | Supplementary | Web/API export | 2026-06-08 | See export | docs/search-results/clinicaltrials-export.json | Trial-status context |

## Search Strings

### Europe PMC

```text
(preterm OR premature OR "very low birth weight" OR VLBW OR "extremely low birth weight" OR ELBW OR neonat*) AND ("postnatal corticosteroid*" OR "postnatal steroid*" OR dexamethasone OR hydrocortisone OR budesonide) AND ("bronchopulmonary dysplasia" OR BPD OR "respiratory distress syndrome" OR NRDS) AND (neurodevelopment* OR "cerebral palsy" OR Bayley OR cognition OR IQ OR behavior OR "school age" OR "long-term")
```

### Angle Notes

```text
Six Europe PMC query angles were exported separately: broad core PICO, systematic reviews/meta-analyses, randomized trials, hydrocortisone-focused, inhaled budesonide, and school-age/adult follow-up.
```

## Seed Papers

| PMID/DOI | Title | Expected query hit? | Result |
|----------|-------|---------------------|--------|
| 34674229 | Early systemic postnatal corticosteroids for prevention of BPD | Yes | Retrieved in evidence table |
| 34758507 | Late systemic postnatal corticosteroids for prevention of BPD | Yes | Retrieved in evidence table |
| 28384828 | PREMILOC 2-year neurodevelopmental outcomes | Yes | Retrieved in evidence table |
| 41359352 | Hydrocortisone school-age functional outcomes | Yes | Retrieved in evidence table |
| 41391545 | SToP-BPD 5.5-year neurodevelopmental outcomes | Yes | Retrieved in evidence table |

## Search Diagnostics

| Check | Result | Action |
|-------|--------|--------|
| Known-paper retrieval | Seed papers retrieved in all_unique/evidence table | Passed |
| Precision sample, top 20 | AI-assisted single-reviewer screen | Author verification recommended |
| Missing synonym scan | Six-angle approach used to capture agent, route, and age terms | Passed with residual Embase/Cochrane access limitation |
| Database access gaps | Embase/Cochrane web exports not automated | Disclosed; Cochrane records captured via Europe PMC/PubMed metadata |
| Deduplication method | PMID/DOI/title-based unique merge into all_unique.json | Documented in data/pncs_search |

## Screening Summary

| Stage | Count | File |
|-------|-------|------|
| Unique records | 8406 | data/pncs_search/all_unique.json |
| Title/abstract included | 309 | data/pncs_search/screening_included.json |
| Title/abstract excluded | 8097 | data/pncs_search/screening_excluded.json |
| Evidence table | 80 | data/pncs_search/evidence_table.json |

## Change Log

| Date | Change | Reason | Model/API or human |
|------|--------|--------|--------------------|
| 2026-06-09 | Materialized protocol, screening decisions, and access log from pncs_search JSON | R2 audit found template logs despite real JSON data | Codex |
