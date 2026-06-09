# Data Translation Rules (RR → ARR/NNT)

> **用途**: Agent 4 Pre-Pass 2 — 扫描稿件中所有相对效应量，转换为绝对风险度量和 NNT/NNH
> **原则**: 临床医生做决策依据的是绝对风险，而非相对风险。RR 是研究产出；NNT 是决策输入。

---

## Translation Protocol

### Step 1: RR Detection

扫描全稿，匹配以下模式:
- `RR` / `risk ratio` / `relative risk` 后跟数字
- `HR` / `hazard ratio` 后跟数字  
- `OR` / `odds ratio` 后跟数字
- `RRR` / `relative risk reduction` 后跟百分比
- `increased by X%` / `reduced by X%` + 风险语境

### Step 2: Baseline Risk Extraction

对每个检测到的 RR/HR/OR:
1. 首先检查同一篇被引文献（PMID）中是否报告了基线风险
2. 如果是 Cochrane 综述 → 检查 Review 的 `Characteristics of included studies` 或 Results 中的 control group event rate
3. 如果引文未报告 → 搜索 PubMed: `"[outcome] incidence preterm [gestational age]"` 获取人群基线率
4. 如果通用人群率可获取 → 使用并标注来源
5. 如果完全找不到 → 标记 `⚠️ BASELINE_RISK_UNKNOWN`

### Step 3: ARR/NNT Calculation

对保护性效应 (RR < 1):
```
ARR = baseline_risk × (1 − RR)
NNT = 1 / ARR (向上取整)
```

对有害效应 (RR > 1):
```
ARI = baseline_risk × (RR − 1)
NNH = 1 / ARI (向上取整)
```

### Step 4: CI Range Calculation

如有基线风险 CI 和 RR CI:
```
ARR_lower = baseline_risk_lower × (1 − RR_upper)
ARR_upper = baseline_risk_upper × (1 − RR_lower)
NNT_range = [1/ARR_upper, 1/ARR_lower] (取整)
```

---

## Insertion Format

### Standard Format (基线风险已知)

在 RR 值之后插入:

> In the [population], this translates to an absolute risk reduction of approximately [X]% (95% CI [Y]%–[Z]%), corresponding to a number needed to treat of [N] (95% CI [M]–[K]). For context, [clinical benchmark: e.g., "this means 1 in every N treated patients avoids the outcome, compared to..."].

### Format with Unknown Baseline

> The absolute risk reduction cannot be calculated because the baseline risk in the target population is not reported in the cited literature. **[⚠️ BASELINE_RISK_UNKNOWN]** This limits the clinical interpretability of the relative risk estimate.

### Format for Wide CI (Type II Error Risk)

> Although the relative risk of [X] (95% CI [wide range]) was not statistically significant, the confidence interval does not exclude a clinically meaningful effect. The absolute risk difference could be as large as [upper bound ARR]%, meaning the "no difference" conclusion should be interpreted cautiously.

---

## Clinical Benchmarking

对每个计算的 NNT/NNH，在可能时添加临床对照:

| Context | Benchmark Example |
|---------|------------------|
| NNT for mortality benefit | "For comparison, ACS reduces neonatal death with an NNT of approximately [X]" |
| NNH for harm | "This means approximately 1 additional case of cerebral palsy for every 20 infants treated — a magnitude that most clinicians and families would consider clinically important" |
| Preventive intervention | "This NNT of [X] is in the range considered acceptable for preventive interventions in neonatology" |

---

## Detection Rate Targets

| Metric | Target |
|--------|--------|
| RR 值检测 | 100% (所有 RR/HR/OR 被识别) |
| ARR/NNT 计算 | ≥70% (基线风险可获取) |
| 基线未知标注 | 100% (对无法计算的部分) |
| 临床对照 | ≥50% (对主要的、有临床意义的 NNT) |

---

## Edge Cases

| Scenario | Handling |
|----------|----------|
| HR (time-to-event) | 不直接转换为 NNT。注明: "HR of [X] means the [outcome] rate in the treatment group was approximately [100-X]% of the control group rate at any given time." |
| OR from case-control | 不转换（OR 在有不同基线风险的设计中不近似 RR）。标注: ⚠️ ODDS_RATIO_NO_BASELINE |
| Network meta-analysis RR | 如果 NMA 报告了绝对风险 → 直接使用。否则标注: ⚠️ NMA_NO_ABSOLUTE_RISK |
| Subgroup analysis RR | 使用亚组的基线风险（如果报告了）。否则标注: ⚠️ SUBGROUP_BASELINE_UNKNOWN |
