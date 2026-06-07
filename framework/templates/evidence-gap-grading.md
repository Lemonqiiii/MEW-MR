# Evidence Gap Grading Framework (G0–G4)

> **用途**: 领域本体构建 (Agent 1 Step 7.3) + 写作前规划 (Agent 3 Step 0c) + 合成推理 (Agent 7 Step 1)
> **原则**: 每个干预的远期证据空白必须被分级，不同级别的空白叙事策略不同

---

## G0–G4 分级定义

| Grade | Label | Evidence Profile | Follow-up Horizon | Data Types | Example | Writing Strategy |
|-------|-------|-----------------|-------------------|-----------|---------|-----------------|
| **G0** | Definitive | Multiple high-quality RCTs + IPD-MA with follow-up to adulthood | >10 years, ideally lifelong | RCT + meta-analysis + cohort | ACS: 30+ RCTs, 1.2M children followed to age 5, growing adult data | **Efficient summary**: Defer to Cochrane/meta-analyses. Focus on remaining uncertainties only. |
| **G1** | Strong | RCT data with follow-up to early childhood | 5–10 years | RCT + cohort | Late postnatal corticosteroids: RCTs with 18–24mo Bayley | **Confident synthesis**: Evidence direction clear. Note gaps in adolescent/adult data. |
| **G2** | Moderate | RCT data available but follow-up limited to infancy/toddlerhood | 18–36 months | RCT (short-term) + limited cohort | Most ventilation strategies: RCTs report Bayley at 18–24mo only | **Careful interpretation**: Acknowledge that school-age outcomes may differ. |
| **G3** | Severe | Only short-term/physiologic endpoints; no meaningful long-term follow-up | <18 months or physiologic only | RCT (short-term endpoints only) | Oxygen targets: 5-year follow-up exists but no lung function/QoL | **Lead with the gap**: The absence of data IS the main story. This intervention is in clinical use but its long-term consequences are unknown. |
| **G4** | Null | No data exists for any meaningful clinical endpoint beyond the neonatal period | 0 (no follow-up) | None or case reports only | LISA: rapidly adopted across Europe, zero long-term follow-up data of any kind | **Alarm**: The most clinically urgent gap. Intervention is being widely used with NO knowledge of long-term effects. |

---

## 分级判定决策树 / Grading Decision Tree

```
Does any follow-up data exist beyond hospital discharge?
    │
    ├── NO → G4 (Null)
    │
    └── YES → Does follow-up extend beyond 36 months?
                  │
                  ├── NO → Does follow-up include neurodevelopmental assessment?
                  │           │
                  │           ├── YES → G2 (Moderate: infant follow-up available)
                  │           └── NO  → G3 (Severe: only short-term/physiologic)
                  │
                  └── YES → Does follow-up extend to adolescence/adulthood?
                                │
                                ├── NO → G1 (Strong: early childhood data)
                                └── YES → G0 (Definitive: lifelong data)
```

---

## 分级质量约束 / Grading Quality Constraints

- 每个干预必须获得一个 G0-G4 分级
- 分级必须基于**实际存在的最大随访数据**（不是"应该有"的数据）
- 如果某干预的多个 RCT 有不同随访期 → 取最长者
- 如果随访数据来自低质量研究（小样本/高失访率）→ 降一级并标注 `⚠️ LOW_QUALITY_FOLLOWUP`
- 如果某干预正在进行长期随访但数据未发表 → 标注 `⏳ PENDING: [trial name/NCT number]`

---

## 跨干预空白比较规则 / Cross-Intervention Gap Comparison Rules

Agent 7 Step 1 使用此框架做跨干预比较时，必须区分：

1. **量的差异**: 两个干预同级（如均为 G2），但一个随访到 24 月，另一个随访到 36 月——标注"同级别内，随访期差异"
2. **质的差异**: 两个干预差两级或以上（如 G0 vs G4）——标注"空白性质完全不同：一个是数据充足但覆盖面有限，一个是完全无数据"
3. **趋势差异**: 一个干预的空白正在被填补（有进行中研究），另一个没有——标注 `⏳ CLOSING` vs `⚠️ STAGNANT`

---

## 与临床紧迫性的交叉 / Cross-Reference with Clinical Urgency

| Gap Grade | Knowledge Gap Risk Score (for priority-scoring.md) |
|-----------|---------------------------------------------------|
| G0 | 0–2 (gap is clinically irrelevant for most decisions) |
| G1 | 3–4 |
| G2 | 5–6 |
| G3 | 7–8 |
| G4 | 9–10 (maximum risk: no data at all) |

---

## 错误用法警告 / Incorrect Usage Warnings

- ❌ 不要将"作者说需要更多研究"等同于 G3/G4——必须基于实际存在的最大随访数据
- ❌ 不要将 Cochrane 综述中"low certainty evidence"等同于空白——GRADE 低确定性 ≠ 无数据，这是两个不同维度
- ❌ 不要仅因一项干预有"更多 RCT"就给更高分级——分级基于**随访长度和质量**，不是 RCT 数量
