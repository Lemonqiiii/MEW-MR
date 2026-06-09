# Domain Ontology: [Topic] — [YYYY-MM-DD]

> **自动构建**: Agent 1 Step 7
> **用途**: 写作前规划 (Agent 3 Steps 0a-0f) + 合成推理 (Agent 7) + 审校增强 (Agent 4 Pre-Pass 2)
> **更新**: 每次新增检索或发现新干预时增量更新

---

## 1. Intervention Inventory

| ID | Intervention | Type | Guideline Source | Year | Recommendation Level | Notes |
|----|-------------|------|-----------------|------|---------------------|-------|
| I01 | [name] | pharmacologic / device / strategy / combination | [guideline ref] | [year] | strong / conditional / weak | [additional context] |

**Type 定义**:
- `pharmacologic`: 药物干预
- `device`: 设备/技术干预
- `strategy`: 策略/方案干预
- `combination`: 联合干预

**Recommendation Level**: strong = 强推荐, conditional = 条件推荐, weak = 弱推荐/无明确推荐

---

## 2. Evidence Gap Grading (G0–G4)

| Intervention ID | Gap Grade | Follow-up Horizon | Data Type Available | Key Data Sources | Gap Description |
|----------------|-----------|-------------------|---------------------|-----------------|-----------------|
| I01 | G0/G1/G2/G3/G4 | [max follow-up years] | RCT / Cohort / Registry / None | [PMIDs] | [specific description of what's missing] |

### Gap Grade Definitions

| Grade | Label | Definition | Clinical Implication |
|-------|-------|-----------|---------------------|
| **G0** | Definitive | Multiple RCTs + long-term follow-up to adulthood + meta-analysis available | Evidence sufficient for confident clinical decision-making |
| **G1** | Strong | High-quality RCT data with follow-up to early childhood (5+ years) | Direction clear but adolescent/adult data incomplete |
| **G2** | Moderate | RCT data available but follow-up limited to infancy (18–36 months) | No school-age or later data; significant uncertainty remains |
| **G3** | Severe | Only short-term/physiologic endpoints available; no meaningful long-term follow-up | Clinically urgent gap; practice based on short-term surrogates |
| **G4** | Null | No data exists for any meaningful clinical endpoint | Cannot inform practice; any use is empiric |

---

## 3. Clinical Urgency Scores (0–10)

| Intervention ID | Frequency (0.30) | Adoption Trend (0.25) | Clinical Stakes (0.25) | Knowledge Gap Risk (0.20) | Composite Urgency | Priority Tier |
|----------------|-------------------|----------------------|------------------------|--------------------------|-------------------|---------------|
| I01 | [score] | [score] | [score] | [score] | [weighted score] | Deep / Standard / Brief |

### Scoring Dimensions

| Dimension | Weight | 0–3 (Low) | 4–6 (Moderate) | 7–10 (High) |
|-----------|--------|-----------|----------------|-------------|
| **Frequency of Use** | 0.30 | Obsolete / rarely used | Common in specific subgroups | Universal standard of care |
| **Adoption Trend** | 0.25 | Declining rapidly | Stable usage | Rapidly expanding |
| **Clinical Stakes** | 0.25 | Cosmetic / minor symptoms | Moderate morbidity, reversible | Life-or-death, lifelong consequences |
| **Knowledge Gap Risk** | 0.20 | Gap is clinically irrelevant | Gap creates moderate uncertainty | Gap leaves clinicians blind for high-stakes decisions |

### Composite Urgency Formula
```
Composite = Frequency×0.30 + Trend×0.25 + Stakes×0.25 + GapRisk×0.20
```

### Priority Tier Assignment
- Composite ≥ 7.0 → **Deep** treatment (mechanism + evidence + gap analysis + clinical framework)
- Composite 4.0–6.9 → **Standard** treatment (evidence summary + key gaps)
- Composite < 4.0 → **Brief** treatment (what is known + major question)

---

## 4. Intervention Interaction Map

| Intervention Pair | Interaction Status | Evidence | Mechanism (if known) | Clinical Relevance |
|-------------------|-------------------|----------|---------------------|-------------------|
| I01 × I02 | KNOWN / UNEXPLORED / HYPOTHESIZED | [PMIDs or ⚠️ NONE] | [pathway description] | HIGH / MODERATE / LOW |

### Interaction Status Definitions
- **KNOWN**: Direct evidence exists (RCT, observational study, or systematic review)
- **UNEXPLORED**: No published evidence found; mechanism-based inference possible
- **HYPOTHESIZED**: Mechanism-based inference generated, awaiting empirical testing

---

## 5. Missing Intervention Alert

> **⚠️ SILENCE BLINDNESS CHECK**: The following interventions are clinically relevant to [topic] but were NOT covered in the original scope/outline. They were discovered during domain ontology construction.

| Intervention | Clinical Relevance | Why Not in Original Scope | Recommended Action |
|-------------|-------------------|--------------------------|-------------------|
| [name] | HIGH / MODERATE / LOW | [reason] | INCLUDE / MENTION_AS_LIMITATION / NOTE_ONLY |

---

## 6. Construction Metadata

| Field | Value |
|-------|-------|
| **Construction Date** | [YYYY-MM-DD] |
| **Built By** | Agent 1 Step 7 |
| **Guideline Sources Used** | [N guidelines: list] |
| **Interventions Identified** | [N total] |
| **Gaps Graded** | [N graded] |
| **Interactions Mapped** | [N pairs] |
| **Missing Interventions Flagged** | [N flagged] |
| **Confidence Level** | HIGH / MODERATE / LOW (based on guideline coverage and search completeness) |
| **Last Updated** | [YYYY-MM-DD] |
