# Evidence Freshness Decay Framework

> **用途**: 写作前规划 (Agent 3 Step 0d) + 合成推理 (Agent 7 Step 5) + 审校增强 (Agent 4 Pre-Pass 2)
> **原则**: 证据的"保质期"因证据类型和研究领域而异。旧证据不丢弃，但需要显式标注外部有效性风险。

---

## Time Bands

| Band | Age | Freshness Label | Citation Treatment |
|------|-----|----------------|-------------------|
| **Band 0** | ≤3 years | Current | Standard citation, no temporal caveat needed |
| **Band 1** | 4–7 years | Recent | Standard citation; check if superseded by newer review |
| **Band 2** | 8–15 years | Aging | Cite + add: "data from [era], applicability to current practice may be limited" |
| **Band 3** | 16–25 years | Historical | Explicitly frame as historical context; do NOT use as primary evidence for current effect size estimates |
| **Band 4** | >25 years | Archival | Cite only for historical trajectory or mechanism; NEVER quote effect size as current |

---

## Study-Type-Specific Decay Factors

Different study types age at different rates. The "effective age" of a study is calculated as:

```
effective_age = chronological_age × decay_factor
```

| Study Type | Decay Factor | Half-life | Rationale |
|-----------|-------------|-----------|-----------|
| **RCT (clinical practice)** | 1.25 | ~8 years | Clinical practice evolves; older RCT populations differ from current patients |
| **RCT (pharmacology)** | 1.0 | ~10 years | Drug effects more stable, but drug approvals/formulations change |
| **Cohort study** | 0.67 | ~15 years | Observational patterns more stable; but diagnostic criteria and confounders evolve |
| **Systematic Review / MA** | 1.67 | ~5 years from **last search date** | Reviews age from their last search, NOT publication date |
| **Mechanistic / laboratory** | 0.5 | ~20 years | Biological mechanisms age slowly; core pathways stable across decades |
| **Case series / case reports** | 2.0 | ~5 years | Rapid obsolescence; current cases differ substantially from historical ones |
| **Guideline** | 1.0 | ~10 years | Guidelines typically updated every 5-10 years; validity depends on underlying evidence age |

---

## Special Age-Accelerating Factors

A study's effective age should be INCREASED (i.e., it's functionally older than its chronological age) if:

| Factor | Age Multiplier | Rationale |
|--------|---------------|-----------|
| Diagnostic criteria have changed since publication | ×1.5 | e.g., BPD definition changed from Northway 1967 → NIH 2001 → NIH 2018 |
| Survival rate in target population has changed >20% since publication | ×1.5 | e.g., 24-week survival was 50% in 1990s → >70% today |
| Standard of care comparator has been replaced | ×2.0 | e.g., trial compared to placebo when active comparator is now standard |
| Study population no longer representative | ×1.5 | e.g., trial enrolled only term infants but current practice includes extreme preterm |
| Key technology/device has been replaced | ×2.0 | e.g., older ventilators vs microprocessor-controlled current devices |

---

## Mandatory Time Annotation Rules

### Rule 1: Citation Aging Detection

For **each key citation** in the manuscript:
1. Extract publication year
2. Calculate chronological age = current_year − publication_year
3. Identify study type → apply decay factor
4. Check for age-accelerating factors → apply multipliers
5. Determine effective age → assign Band 0-4
6. If source is a systematic review: use **last search date**, not publication date

### Rule 2: Band-Based Language Rules

| Band | Required Language |
|------|------------------|
| **Band 0** | No special treatment |
| **Band 1** | If this is the ONLY evidence for a claim → add: "(based on data from [year]; contemporary replication would strengthen confidence)" |
| **Band 2** | Must add: "(data from [era]; the extent to which these findings apply to current [population/practice] is uncertain)" |
| **Band 3** | Frame as: "Historical data from the [era] suggested that... More recent studies in contemporary populations are needed to confirm..." |
| **Band 4** | Frame as: "In the pre-[modern intervention] era, [Author] reported that... This finding reflects a fundamentally different clinical context and should not be interpreted as a current effect estimate." |

### Rule 3: Sole-Source Aging Evidence Flag

If a Band 2+ source is the **ONLY** evidence for a clinically important claim:
- Flag: `⚠️ AGING_EVIDENCE_SOLE_SOURCE`
- In manuscript: add an explicit caveat paragraph explaining the evidence's age and the need for contemporary replication

### Rule 4: Stagnant Field Detection

If the **newest** primary data for an intervention is >10 years old:
- Flag: `⚠️ FIELD_STAGNANT`
- In manuscript: add: "Notably, the most recent primary data for this intervention dates from [year]. The absence of contemporary studies represents a research gap in itself."

---

## Time Annotation Schedule Template

For the pre-writing plan (`knowledge/pre-writing-plan.md`), generate per section:

| Source | Pub Year | Study Type | Chronological Age | Decay Factor | Effective Age | Band | Treatment |
|--------|---------|-----------|-------------------|-------------|--------------|------|-----------|
| [First author year] | [year] | [type] | [N years] | [factor] | [effective N] | [0-4] | [Standard / Caveat / Historical / Archival] |
