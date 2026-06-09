# Cross-Intervention Comparison Matrix

> **用途**: Agent 7 Step 1 — 对每对干预进行结构化 7 维度比较
> **输出**: `harness/cross-intervention-output.md` (可审计产物)

---

## Comparison Dimensions

| Dimension | Definition | Data Source | Scale |
|-----------|-----------|-------------|-------|
| **D1: Evidence Quality** | Overall evidence maturity for long-term outcomes | G0-G4 gap grade from domain ontology | G0 (best) → G4 (null) |
| **D2: Effect Magnitude** | Standardized effect size for primary short-term outcome | Cochrane review / largest RCT | Large / Moderate / Small / Unknown |
| **D3: Follow-up Horizon** | Maximum follow-up duration available | Domain ontology gap assessment | Years (0 = none beyond discharge) |
| **D4: Safety Profile** | Known harm signals and their severity | Cochrane safety outcomes + NNH if available | Favorable / Neutral / Concerning / Unknown |
| **D5: Clinical Adoption** | Current utilization rate and trend | Guidelines + utilization studies | Universal / Widespread / Selective / Rare |
| **D6: Knowledge Gap Urgency** | How clinically pressing the evidence gap is | Composite Urgency from domain ontology | 0-10 (10 = most urgent) |
| **D7: Interaction Evidence** | Known interactions with other interventions | Domain ontology interaction map | Count of known interactions |

---

## Matrix Template

| Intervention | D1: Evidence | D2: Effect | D3: Follow-up | D4: Safety | D5: Adoption | D6: Urgency | D7: Interactions |
|-------------|-------------|-----------|---------------|-----------|-------------|-------------|-----------------|
| I01 | G0 | Large | 5yr | Favorable | Universal | 5.0 | 3 known |
| I02 | G4 | Moderate | 0yr | Unknown | Rapidly ↑ | 8.5 | 0 known |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## Mandatory Qualitative Comparisons (NOT just numbers)

For each intervention pair where the gap grade differs by ≥2 levels:

1. **Quantify the asymmetry**: "Intervention A has [N] patients followed to [age]; Intervention B has zero follow-up data."
2. **State the clinical implication**: "This means clinicians choosing between A and B are making decisions with fundamentally different levels of certainty about long-term consequences."
3. **Flag the paradox**: If B is being adopted more rapidly than A despite having less evidence, explicitly call this out.

Example:
> "ACS has follow-up data on over 1.2 million children extending to age 5; LISA has zero published long-term follow-up data of any kind. Yet LISA is being adopted across European NICUs at an accelerating pace. This asymmetry — rapid adoption of an intervention with no long-term safety data — represents the most clinically urgent evidence gap identified in this review."

---

## Evidence Asymmetry Detection Rules

| Pattern | Detection | Label |
|---------|-----------|-------|
| Gap grade differs by ≥2 levels between commonly compared interventions | G0 vs G2/G3/G4 | `⚠️ SEVERE_ASYMMETRY` |
| Intervention with worse evidence is being adopted faster | G3/G4 + Adoption Trend ≥7 | `⚠️ ADOPTION_PARADOX` |
| Intervention with better evidence is being phased out | G0/G1 + Adoption Trend ≤3 | `⚠️ EVIDENCE_LOSS` |
| Both interventions have G3/G4 but one is considered "standard" | Two G3/G4, different Adoption scores | `⚠️ DOUBLE_BLIND_SPOT` |

---

## Output Format (`harness/cross-intervention-output.md`)

```markdown
# Cross-Intervention Comparison: [Topic] — YYYY-MM-DD

## Matrix
[completed comparison matrix table]

## Asymmetry Analysis
[all detected asymmetries with clinical implications]

## Top 5 Most Clinically Urgent Comparisons
[ranked by clinical urgency of the comparison itself]

## Construction Metadata
- Built by: Agent 7 Step 1
- Date: YYYY-MM-DD
- N interventions compared: [N]
- N asymmetries detected: [N]
```
