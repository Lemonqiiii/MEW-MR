# Clinical Urgency Priority Scoring

> **用途**: 领域本体构建 (Agent 1 Step 7.4) + 写作前规划 (Agent 3 Step 0b)
> **目标**: 用文献中可获取的代理指标评估每个干预的临床紧迫性，指导篇幅分配

---

## 评分维度

### Dimension 1: Frequency of Use (权重 0.30)

衡量该干预在目标人群中被使用的广泛程度。

| Score | Label | Criteria | Data Source |
|-------|-------|----------|-------------|
| 0–1 | Obsolete | No longer used in modern practice; only historical interest | Guideline: "not recommended" / "should not be used" |
| 2–3 | Rare | Used only in highly specific subgroups or rescue situations | Guideline: "may be considered in selected cases" |
| 4–6 | Common | Used in specific clinical subgroups (e.g., <28wk, severe RDS) | Guideline: "recommended for [subgroup]" |
| 7–8 | Widespread | Near-universal in target population | Guideline: "recommended for all [population]" |
| 9–10 | Universal | Standard of care; administered to virtually all eligible patients | Multiple guidelines: strong recommendation, universal |

**Data source priority**: Clinical practice guidelines > utilization studies > expert reviews

---

### Dimension 2: Adoption Trend (权重 0.25)

衡量该干预的采用趋势是增长、稳定还是下降。

| Score | Label | Criteria | Data Source |
|-------|-------|----------|-------------|
| 0–1 | Phasing out | Being actively de-adopted; new guidelines recommend against | Recent guideline changes reversing prior recommendations |
| 2–3 | Declining | Use decreasing; being replaced by newer alternatives | Trend data or comparison of older vs newer guideline versions |
| 4–6 | Stable | Established practice; no major shift in adoption | Guideline consistency across recent versions |
| 7–8 | Growing | Being adopted in new populations or settings (e.g., LMIC) | Recent guideline expansions of indication |
| 9–10 | Rapidly expanding | New technology/approach being rapidly adopted; first-line in many centers | Recent consensus statements; survey data showing rapid uptake |

**Data source priority**: Adoption surveys > guideline version comparison > expert commentary

---

### Dimension 3: Clinical Stakes (权重 0.25)

衡量该干预做出错误决策的后果严重性。

| Score | Label | Criteria | Outcome Examples |
|-------|-------|----------|-----------------|
| 0–1 | Minimal | Affects minor symptoms or cosmetic outcomes | Minor electrolyte abnormalities, transient tachypnea |
| 2–3 | Low | Affects reversible morbidity without long-term sequelae | Uncomplicated hypoglycemia, transient oxygen need |
| 4–6 | Moderate | Affects morbidity with potential long-term impact | BPD (chronic lung disease), ROP (visual impairment) |
| 7–8 | High | Affects neurodevelopment or organ function with lifelong consequences | Cerebral palsy, cognitive impairment, chronic organ failure |
| 9–10 | Critical | Life-or-death decision; irreversible catastrophic harm | Mortality, severe IVH, lifelong severe disability |

**Data source priority**: PICO outcome severity from active-focus.md > Cochrane primary outcomes > guideline safety warnings

---

### Dimension 4: Knowledge Gap Risk (权重 0.20)

衡量该干预的证据空白对临床决策的风险。**直接从 G0-G4 映射**。

| Gap Grade | Knowledge Gap Risk Score |
|-----------|-------------------------|
| G0 | 0–2 |
| G1 | 3–4 |
| G2 | 5–6 |
| G3 | 7–8 |
| G4 | 9–10 |

**特殊调整**:
- 如果干预的 Gap Grade 为 G3/G4 且 Adoption Trend ≥ 7（快速推广）→ Gap Risk +1
- 如果干预主要在 LMIC 使用且所有数据来自 HIC → Gap Risk +1
- 如果正在进行大型长期随访试验 → Gap Risk −1

---

## 复合紧迫性计算

```
Composite_Urgency = Frequency × 0.30
                  + Trend    × 0.25
                  + Stakes   × 0.25
                  + GapRisk  × 0.20
```

所有维度均标准化为 0–10。复合分数范围 0–10。

---

## Priority Tier 分配

| Composite | Tier | Treatment | Target Word Allocation | Writing Strategy |
|-----------|------|-----------|----------------------|-----------------|
| ≥ 7.0 | **Deep** | Exhaustive treatment | ~2× base allocation | Mechanism + evidence + gap analysis + clinical framework + perspective switches |
| 4.0–6.9 | **Standard** | Balanced coverage | ~1× base allocation | Evidence summary + key gaps + one perspective switch |
| < 4.0 | **Brief** | Concise summary | ~0.5× base allocation | What is known + major question remaining |

---

## 评分溯源要求

每个干预的四个维度分数必须附带：
- 数据来源（guideline/study/PMID）
- 置信度（HIGH/MEDIUM/LOW）
- 如果数据来源不足 → 标注 `⚠️ LOW_CONFIDENCE` 并使用默认保守估计

---

## 特殊情况处理

| Scenario | Handling |
|----------|----------|
| Intervention only used in HIC, not relevant to LMIC | Stakes score unchanged; note in ontology |
| Intervention is preventive (given to healthy population) | Stakes score +1 (preventive interventions have higher safety burden) |
| Multiple competing interventions exist for same indication | Frequency score adjusted for market share |
| Intervention is bundled/co-administered (can't isolate effect) | Flag ⚠️ BUNDLED; Gap Risk +1 |
