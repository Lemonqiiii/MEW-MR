# Harness Architecture

> Purpose: define the quality, safety, and observability architecture for reusable medical review projects.

---

## 1. Architectural Layers

| Layer | Purpose | Required files |
|-------|---------|----------------|
| Context routing | Determine current manuscript, topic, phase, journal, and data paths | `memory/project-status.md`, `memory/active-focus.md`, `scripts/process_integrity_check.py` |
| Search/screening governance | Make retrieval, screening, VPN access, and abstract-only use reproducible | `harness/search-screening-protocol.md`, `docs/search-results/search-protocol.md`, `docs/search-results/screening-decisions.csv`, `docs/search-results/fulltext-access-log.csv`, `scripts/materialize_search_screening_logs.py` |
| Evidence synthesis | Prevent shallow summarization and missing-clinical-context failures | `knowledge/domain-ontology.md`, `knowledge/pre-writing-plan.md`, `harness/synthesis-reasoning.md`, `harness/cross-intervention-matrix.md` |
| Drafting and revision | Ensure source-of-truth editing, review action tracking, response drafting, and revision traceability | current manuscript, `harness/review-revision-protocol.md`, `docs/review/review-action-log.json`, `docs/review/response-to-reviewers.md`, `manuscript/CHANGELOG.md`, `manuscript/REVISION_MAP.md`, `scripts/review_revision_check.py` |
| Quality gates | Define pass/fail criteria for each transition | `harness/quality-gate.md`, `scripts/audit_manuscript.py` |
| Evaluation harness | Measure success, efficiency, robustness, safety, and consistency | `harness/metrics.md`, `harness/test-scenarios.md`, `harness/consistency-benchmarks.md`, `progress/metrics-raw.json` |
| Safety | Prevent out-of-scope file/network/command behavior and leakage | `harness/safety-policy.md` |
| Submission readiness | Convert internal drafts into journal-ready files | `harness/submission-compliance.md`, `harness/journal-profiles.md`, `scripts/gen_word_full.py` |
| Process evolution | Record workflow failures and permanent fixes | `memory/workflow-evolution.md`, `features/FEATURE_LIST.md`, `progress/SESSION_LOG.md` |

---

## 2. Required Execution Order

For a new review topic:

1. **Gate 0**: resolve context and remove blocking hard-coded legacy defaults.
2. **Gate Search**: search protocol complete and seed papers retrieved.
3. **Gate Screening**: decisions, access tiers, citation scopes, and conflicts logged.
4. **Gate Fulltext**: VPN/full-text barriers resolved or evidence downgraded.
5. **Gate Evidence**: evidence table and claim map complete enough for drafting.
6. **Gate Draft**: citation, structure, and manuscript audit pass.
7. **Gate Revision**: review feedback mapped to CHANGELOG and REVISION_MAP.
8. **Gate Submission**: journal compliance, declarations, AI disclosure, and Word export pass.

---

## 3. Minimum Executable Checks

The harness is considered operational only if these commands run:

```bash
python scripts/process_integrity_check.py
python scripts/harness_architecture_check.py
python scripts/harness_test_inventory.py
python scripts/materialize_search_screening_logs.py
python scripts/gate_search_check.py
python scripts/gate_screening_check.py
python scripts/review_revision_check.py
python scripts/audit_manuscript.py
python scripts/run_harness_checks.py
```

Optional topic-specific checks may be added, but they must accept explicit input paths and must not hard-code historical manuscripts.

---

## 4. Legacy-File Policy

Historical project scripts and reports may remain in the repository, but they must be one of:

- inside `archive/`
- clearly named as legacy
- deprecated with a non-writing failure message
- excluded from current Gate 0 blocking checks

Any script that writes files and contains historical manuscript content is unsafe unless it accepts explicit current-project paths.

---

## 5. Remaining Desired Capabilities

These are not yet fully automated:

- claim-map generation and validation
- seed-paper retrieval verification against live databases
- automatic conversion of free-text reviewer letters into action log entries
- response-letter completeness beyond blocking action ID coverage
- safety audit extraction from live tool telemetry
- full robustness and consistency test runner (current inventory check is structural only)
- model/API provenance extraction into `progress/metrics-raw.json`

Until automated, Agents must document these checks manually in reports.
