# Pre-writing Plan — NRDS Life-Course Review — 2026-06-06

> **生成**: Agent 3 Steps 0a-0f
> **基于**: `knowledge/domain-ontology.md` + `manuscript/outline.md`
> **用途**: Agent 3 写作步骤的强制性写作简报

---

## 1. Priority-Weighted Section Allocation

| Outline Section | Primary Interventions | Composite Urgency | Priority Tier | Target Words | Justification |
|----------------|----------------------|-------------------|---------------|-------------|---------------|
| §2 ACS | I01 | 7.30 | **Deep** | ~1200 | Highest evidence base, longest follow-up, broadest population impact |
| §3 Postnatal CS | I02, I03, I04, I05 | 5.25–6.05 | Standard | ~1000 | Critical risk-benefit trade-off; well-studied but follow-up incomplete |
| §4 Ventilation | I11, I12, I13, I14, I15, I16, I17 | 3.65–7.15 | Standard (weighted) | ~1000 | VTV/CPAP important; PLV/HFNC/nHFOV brief only |
| §5 Surfactant | I06, I07, I08, I09, I10 | 4.45–8.55 | **Deep** (LISA) + Standard | ~1200 | LISA (G4, Urgency 8.55) dominates this section |
| §6 Oxygen | I18 | 7.55 | **Deep** | ~800 | Best long-term follow-up of any NICU intervention; mortality signal unresolved |
| §7 BPD | (cross-cutting) | — | Standard | ~800 | Mediator framework; definition evolution critical |
| §8 Neurodevelopment | (cross-cutting) | — | Standard | ~600 | Synthesis section; avoid rehashing per-intervention detail |
| §9 QoL | (cross-cutting) | — | Brief | ~400 | Only 8 papers; acknowledge sparsity, don't inflate |
| §10 Gaps | (cross-cutting) | — | Standard | ~600 | Add missing intervention alert from domain ontology |
| §11 Conclusions | (cross-cutting) | — | Standard | ~500 | Add clinical decision framework reference |

### Deep vs Brief Designations

| Priority Tier | Sections | Rule |
|--------------|----------|------|
| **Deep** (≥7.0) | §2 ACS, §5 Surfactant (LISA focus), §6 Oxygen | Mechanism + evidence + gap analysis + clinical framework + 2+ perspective switches |
| **Standard** (4.0–6.9) | §3 Postnatal CS, §4 Ventilation, §7 BPD, §8 Neuro, §10 Gaps, §11 Conclusions | Evidence summary + key gaps + 1 perspective switch |
| **Brief** (<4.0) | §9 QoL, HFOV sub-section, PLV sub-section | What is known + major question; no clinical framework |

### ❌ ERROR CHECK
- [x] No priority ≥7 intervention assigned to Brief
- [x] No priority <4 intervention assigned to Deep
- [ ] ⚠️ WARNING: Caffeine (I19, Urgency 7.75, DEEP-tier) is NOT in outline → see Coverage Report below

---

## 2. Evidence Gap to Emphasis Mapping

| Section | Gap Grade(s) | Writing Strategy |
|---------|-------------|-----------------|
| §2 ACS | G1 (data to 5yr, no adult data) | **Efficient summary of strong evidence + highlight adult data gap**: "The first ACS recipients are in their 50s; we have no data on their cardiovascular or cognitive health." |
| §3 Postnatal CS | G1–G2 | **Risk-benefit framework**: Lead with the clinical tension; emphasize that "Bayley at 18-24mo is a poor predictor of school-age IQ" |
| §4 Ventilation | G2–G3 | **The follow-up gap as central narrative**: "VTV reduces BPD by 27% — but whether this translates to better adult FEV₁ is unproven." |
| §5 Surfactant (LISA) | **G4** | **ALARM**: Lead with the gravity of the absence. "LISA is being adopted across Europe as first-line surfactant delivery — with zero long-term follow-up data of any kind. The first LISA cohort are now adolescents, and we know nothing about their lungs." |
| §6 Oxygen | G1 | **Best-case evidence**: NeOProM IPD-MA with 5-year follow-up is the gold standard. Highlight that even this gold standard has gaps (no lung function at 15yr). |
| §10 Knowledge Gaps | — | **Integrate missing intervention alert** from domain ontology: caffeine, vitamin A, iNO, diuretics, nutrition. Diuretics = G4 + widely used = perfect "evidence gap" case study. |

---

## 3. Time Annotation Schedule

| Key Citation | Pub Year | Study Type | Chronological Age | Effective Age* | Band | Treatment |
|-------------|---------|-----------|-------------------|---------------|------|-----------|
| Liggins & Howie (ACS landmark) | 1972 | RCT | 54 yr | ~67 yr (×1.25 practice change) | **Band 4** | Historical context only; do NOT quote effect size |
| Cochrane ACS | 2020 | SR | 6 yr | ~9 yr (×1.5 SR decay from last search) | **Band 1** | Current evidence; check search date |
| Cochrane Early CS | 2021 | SR | 5 yr | ~8 yr | **Band 1** | Current; note 2017→2021 version change |
| Cochrane VTV | 2017 | SR | 9 yr | ~14 yr (×1.5) | **Band 2** | Add caveat: "data from pre-LISA/pre-VTV era; applicability to current practice requires interpretation" |
| Cochrane LISA | 2021 | SR | 5 yr | ~8 yr | **Band 1** | Current for short-term; G4 gap highlighted |
| NeOProM IPD-MA (oxygen) | 2018 | IPD-MA | 8 yr | ~12 yr | **Band 2** | Add: "the most rigorous long-term follow-up in neonatology — yet still only to age 5" |
| CAP trial (caffeine) | 2007 | RCT | 19 yr | ~23 yr (×1.25) | **Band 3** | Historical framing; contemporary caffeine protocols differ |
| CAP 11yr follow-up | 2017 | RCT follow-up | 9 yr | ~11 yr | **Band 2** | Best available; but cohort from pre-LISA era |
| NICHD Vitamin A | 1999 | RCT | 27 yr | ~33 yr | **Band 4** | Historical; no contemporary vitamin A trials exist → ⚠️ FIELD_STAGNANT |

*\*Effective age accounts for study-type decay factor + age-accelerating factors (see `harness/time-annotation.md`)*

### ⚠️ AGING_EVIDENCE_SOLE_SOURCE
- Vitamin A (I21): NICHD 1999 is literally the only large RCT → ⚠️ FIELD_STAGNANT
- PLV data: Most evidence predates VTV era → external validity severely limited

---

## 4. Coverage Report

### Domain Ontology vs Outline Cross-Check

| Ontology Intervention | Priority | Covered in Outline? | Status |
|----------------------|----------|---------------------|--------|
| I01 ACS | 7.30 Deep | ✅ §2 | OK |
| I02-I05 Postnatal CS | 4.65–6.05 Standard | ✅ §3 | OK |
| I06 LISA | 8.55 Deep | ✅ §5 | OK |
| I08-I10 Surfactant preparations | 5.00–6.40 Standard | ✅ §5 | OK |
| I11 VTV | 6.85 Standard | ✅ §4 | OK |
| I13 HFOV | 4.40 Standard | ✅ §4 | OK |
| I15 NIPPV | 6.55 Standard | ✅ §4.2 | OK |
| I16 CPAP | 7.15 Deep | ✅ §4 | OK |
| I18 Oxygen targets | 7.55 Deep | ✅ §6 | OK |
| **I19 Caffeine** | **7.75 Deep** | **❌ NOT COVERED** | **⚠️ CRITICAL_GAP** |
| **I20 iNO** | **4.40 Standard** | **❌ NOT COVERED** | **⚠️ COVERAGE_GAP** |
| **I21 Vitamin A** | **3.35 Brief** | **❌ NOT COVERED** | **COVERAGE_GAP** |
| **I22 Diuretics** | **6.45 Standard** | **❌ NOT COVERED** | **⚠️ COVERAGE_GAP** |
| **I23 Nutrition** | **7.05 Deep** | **❌ NOT COVERED** | **⚠️ CRITICAL_GAP** |
| I24 Breast Milk | 6.90 Standard | ❌ | COVERAGE_GAP |
| I25 MgSO₄ | 7.20 Deep | ❌ | ⚠️ CRITICAL_GAP (antenatal, relevant to ACS section) |
| I26 DCC | 7.05 Deep | ❌ | COVERAGE_GAP (delivery room, less central to respiratory theme) |

### Missing by Priority Tier
- **Deep (≥7.0) missing**: Caffeine (7.75), Nutrition (7.05), MgSO₄ (7.20)
- **Standard (4.0–6.9) missing**: iNO (4.40), Diuretics (6.45), Breast Milk (6.90)
- **Brief (<4.0) missing**: Vitamin A (3.35)

### Recommended Actions
1. **Caffeine (§新增 or §8 expansion)**: Most critical omission. 2025 EU Guidelines now recommend prophylactic caffeine for ALL <32wk (A1). CAP trial has 11-year cognitive and pulmonary follow-up — the best in neonatology. Add as §3.5 or dedicated box in §8.
2. **Diuretics (§10)**: Perfect "evidence gap" case study — widely used in BPD for months, G4 (zero long-term data). Include in §10 Knowledge Gaps as exemplar.
3. **MgSO₄ (§2)**: Brief mention in ACS section — both are antenatal neuroprotective interventions.
4. **Nutrition/Breast Milk (§10 limitation)**: Acknowledge as scope limitation in Discussion.

---

## 5. Summary

| Metric | Value |
|--------|-------|
| Sections with allocation | 10/10 (100%) |
| Deep sections | 3 (§2 ACS, §5 LISA focus, §6 Oxygen) |
| G4 gap interventions with alarm treatment | 2 (LISA, Diuretics — identified post-hoc) |
| Band 2+ citations with caveat plan | 5 |
| ⚠️ AGING_EVIDENCE_SOLE_SOURCE | 1 (Vitamin A) |
| ⚠️ FIELD_STAGNANT | 1 (Vitamin A) |
| Interventions in ontology | 26 |
| Interventions covered in outline | 16 |
| Critical gaps (Deep missing) | 3 (Caffeine, Nutrition, MgSO₄) |
| Coverage gaps (Standard missing) | 3 (iNO, Diuretics, Breast Milk) |
