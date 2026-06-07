# Quality Gate System

> Each Phase's output must pass its quality gate before entering the next Phase.
> Unchecked output = incomplete.
>
> **Enforcement**: `python3 scripts/verify_gates.py --gate <N>`
> Gates marked `MANDATORY` block progress to the next agent.

---

## Gate 1: Literature Search → Screening

| Check | Method | Pass Standard |
|-------|--------|---------------|
| Recall | Spot-check 5 known key papers — verify they were retrieved | 5/5 hit |
| Dedup accuracy | Random sample of 50 papers — verify no duplicates | 0 duplicates |
| Data completeness | Check PMID/DOI/abstract missing rate | <5% missing |
| Population contamination | Scan titles + abstracts for domain-specific exclusion keywords | 0 wrong-population papers |
| Year distribution | Verify coverage range | Covers last 5+ years |

## Gate 2: Screening → Deep Reading

| Check | Method | Pass Standard |
|-------|--------|---------------|
| Inclusion consistency | Independent dual screening of 20 papers | Cohen's Kappa > 0.7 |
| Exclusion reason validity | Random sample of 10 excluded papers | 10/10 reasonable |
| False positive check | Verify included papers' titles match domain | 0 misclassified |
| Paper type distribution | Type A+B+C ≥20% (mechanism reviews) | Config-defined threshold |
| Abstract-only ratio | ≤20% of final inclusion | Config-defined threshold |

## Gate 3: Deep Reading → Writing

| Check | Method | Pass Standard |
|-------|--------|---------------|
| Note quality | Random sample of 10 notes, 4-dimension scoring | ≥8/10 score ≥3/4 |
| Theme coverage | Check for uncovered key mechanism categories | 0 blank categories |
| Citation traceability | Each cross-theme finding has ≥2 independent literature sources | 100% |
| Note-to-outline mapping | Outline has sufficient subsection detail | ≥15 subsections |

## Gate 4: Writing — Citation Verification

| Check | Method | Pass Standard |
|-------|--------|---------------|
| Claim-citation verification | Open each cited paper's abstract; verify claim content actually comes from that paper | ≥95% pass rate |
| Logical coherence | Check section transitions accurately reflect next section content | All transitions accurate |
| Data accuracy | Verify all frequency numbers, trial names, drug names | 0 factual errors |

## Gate 5: Revision — Format Integrity

| Check | Method | Pass Standard |
|-------|--------|---------------|
| New claim traceability | Every new claim must note specific source (citation + paragraph) | 100% traceable |
| Modification scope | Diff before/after — verify modifications stay within citation support | 0 overreach modifications |
| Figure/table references | Body citations match figure/table file set | 100% match |
| Reference number consistency | Body [N] references all exist in reference list | 0 dangling references |

## Gate 6: Final — Citation Scope Compliance

| Check | Method | Pass Standard |
|-------|--------|---------------|
| Type G as primary citation | Scan all primary citations for type G papers | 0 violations |
| Type I sole support | Scan all single-citation claims for type I papers | 0 violations |
| Type E causal claims | Scan mechanism claims for type E primary citations — verify qualifier present | 0 violations |
| Cochrane count update | If reference total changed, Cochrane percentage recalculated | All positions updated |

## Gate 7: Domain Ontology Completeness (Module A)

| Check | Pass Standard |
|-------|---------------|
| Intervention inventory covers ≥2 guideline sources | ≥90% guideline interventions captured |
| All interventions assigned G0-G4 gap grade | 100% |
| All interventions have Composite Urgency score | 100% |
| Intervention interaction map enumerates all pairs | 100% pairs enumerated |
| Missing intervention alert generated | YES |

## Gate 8: Pre-writing Planning (Module D)

| Check | Pass Standard |
|-------|---------------|
| Priority-weighted section allocation covers all outline sections | 100% |
| No priority ≥7 intervention assigned to Brief | 0 violations |
| Gap-to-emphasis mapping for all G3-G4 interventions | 100% |
| Time annotation schedule for all Band 2+ references | 100% |
| Coverage report generated | YES |

## Gate 9: Synthesis Quality (Module B)

| Check | Pass Standard |
|-------|---------------|
| Cross-intervention matrix covers all intervention pairs | 100% |
| All hypotheses have complete trail in reasoning log | 100% traceable |
| Pattern A ("elegant vacuity") count | ≤3 |
| Time evolution notes for all Band 3+ sections | 100% |
| Coverage gap report generated | YES |
| Zero unlabeled hypotheses | 0 |

## Gate 10: Enhanced Review (Module C)

| Check | Pass Standard |
|-------|---------------|
| 5 perspective types attempted at trigger positions | ≥80% coverage |
| All RR/HR/OR values have ARR/NNT or baseline-unknown annotation | 100% |
| Pattern A final count | ≤2 |
| Every Cochrane review cited ≥2 times has ≥1 critical qualifier | 100% |
| Cochrane concentration ≤60% or ≥3 supplementary critiques | YES |

## Gate 11: Submission Ready (Module E)

| Check | Pass Standard |
|-------|---------------|
| HTML audit tags | 0 remaining |
| Editor placeholders | 0 `[To be completed]` / `[TBD]` |
| Journal match | MATCH or flagged with alternatives |
| Completeness sections | 5/5 complete (Author Contributions, Funding, Data Availability, etc.) |
| AI disclosure | PRESENT or flagged ⚠️ MISSING |
| Figure files | All referenced figures exist |
| Submission readiness report | Generated |
