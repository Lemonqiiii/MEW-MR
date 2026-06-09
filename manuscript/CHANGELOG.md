# Changelog — Current Manuscript

**Current manuscript:** `manuscript/pncs_systematic_review.md`
**Current revision workspace:** `docs/review/review-action-log.json`

All notable changes to this manuscript are documented here. Each revision maps to a review round.

---

## Revision R5 — Format Cleanup + Internal Review Response — 2026-06-09

**Review source:** Codex internal review after format cleanup

**Review Outcome:** format warnings resolved; R5 review actions verified

### Changes

| ID | Location | Change |
|----|----------|--------|
| R5-FMT | Title/section layout | Removed excess horizontal rules and updated revision marker to R5. |
| R5-001 | Section 5.2 | Replaced "first long-term hydrocortisone safety data" with qualified language: randomized school-age follow-up rather than definitive proof of long-term safety. |
| R5-002 | Sections 1, 9, 10 | Removed stale date framing and absolute "completely unstudied" language; added controlled-follow-up qualification. |
| R5-003 | Declarations | Replaced bracketed declaration placeholders with draft declaration text requiring final author confirmation where appropriate. |
| R5-004 | Acknowledgements | Updated AI disclosure to include Claude Code/Anthropic and Codex/OpenAI. |

### Verification

- `python scripts/audit_manuscript.py manuscript/pncs_systematic_review.md` -> passed with no warnings
- `python scripts/run_harness_checks.py` -> 7/7 passed

---

## Revision R4 — Search/Screening Audit Repair + Claim Tightening — 2026-06-09

**Review source:** Codex internal audit requested by user

**Review Outcome:** blocking audit issues resolved

### Blocking Audit Fixes

| ID | Location | Change |
|----|----------|--------|
| R4-1 | Abstract Results | Replaced overstrong "long-term neurodevelopmental safety" wording with "did not increase measured functional or neurodevelopmental impairment." |
| R4-2 | Conclusions | Replaced categorical hydrocortisone safety language with measured-harm qualifiers. |
| R4-3 | Section 2.2 | Weakened mechanistic neurotoxicity paragraph to match the broad scope of the cited glucocorticoid neurobiology source. |
| R4-4 | Section 6 | Removed unsupported inhaled-budesonide pharmacokinetic detail and retained outcome-based caution. |
| R4-5 | Reference 33 | Corrected SToP-BPD 5.5-year citation to *J Pediatr* 2025:114954, doi:10.1016/j.jpeds.2025.114954, PMID:41391545. |

### Process/Data Fixes

| ID | File | Change |
|----|------|--------|
| R4-6 | `docs/search-results/search-protocol.md` | Materialized actual PNCS search protocol from `data/pncs_search/*.json`. |
| R4-7 | `docs/search-results/screening-decisions.csv` | Materialized 8,406 screening rows with decision, reason_code, fulltext_status, and citation_scope. |
| R4-8 | `docs/search-results/fulltext-access-log.csv` | Materialized 80 evidence-table access rows. |
| R4-9 | `scripts/materialize_search_screening_logs.py` | Added reproducible script to regenerate audit logs from JSON data. |
| R4-10 | `scripts/run_harness_checks.py` | Gate Search and Gate Screening now run by default. |

### Verification

- `python scripts/gate_search_check.py` -> 0 errors, 0 warnings
- `python scripts/gate_screening_check.py` -> 0 errors, 0 warnings
- `python scripts/audit_manuscript.py manuscript/pncs_systematic_review.md` -> passed

---

## Revision R2 — pending

**Review source:** pending

**Review Outcome:** pending

No current R2 review actions have been logged yet. When review comments arrive, normalize them into `docs/review/review-action-log.json`, update `docs/review/response-to-reviewers.md`, then record verified fixes here.

---
**Convention:** Each revision round gets a new `## Revision R<N>` section above.
**Legacy records:** Previous NRDS Life-Course changelog archived to `archive/nrds-2025/CHANGELOG.md`.

