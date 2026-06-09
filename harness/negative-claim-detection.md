# Absolute Negative Claim Contradiction Detection

> **用途**: Agent 4 Step 1.5 — 检测稿中绝对否定声称与被引文献实际内容之间的矛盾
> **原则**: "no data" 这类声称必须能经得起被引文献内容的检验。绝对声称必须有精确的范围限定。

---

## Detection Patterns

### Absolute Negative Keywords

```
"no data" | "absent" | "zero" | "none" | "never been studied" |
"never been investigated" | "completely unknown" | "essentially empty" |
"total absence" | "entirely absent" | "no studies have" |
"has not been studied" | "have not been conducted" | "no published data"
```

### Claim Extraction

对每个检测到的绝对否定声称：
1. 提取声称涉及的具体范围（干预 + 结局 + 人群）
   例: "no data on adult pulmonary function for LISA-treated infants"
   范围 = {干预: LISA, 结局: adult pulmonary function, 人群: preterm infants}
2. 提取声称引用的 PMID（如有）
3. 记录声称的精确度等级:
   - **Level 0**: "no data at all" / "completely absent" → 要求最严格
   - **Level 1**: "no long-term data" / "no follow-up beyond X" → 要求中等
   - **Level 2**: "no intervention-specific data" / "no comparative data" → 要求较宽松

---

## Two-Step Verification

### Verification A: Cited Source Verification

对声称引用的每个 PMID：
1. 提取该文献的摘要
2. 检查摘要是否报道了声称所否认的结局
3. 判定:
   - 文献明确支持"无数据"结论 → ✅ CITATION_SUPPORTS_CLAIM
   - 文献实际上报道了声称所否认的数据 → ❌ CONTRADICTION
   - 文献未直接讨论该结局 → ⚠️ CITATION_IRRELEVANT

**最关键的错误类型**: 文献本身包含了声称所否认的数据。
例: 声称 "no adult pulmonary function data exist" → 引用 Gibson 2015 → Gibson 2015 报告了成人 FEV₁
→ ❌ CONTRADICTION: 引用的文献本身就包含成人肺功能数据

### Verification B: Reverse Verification Against Full Citation Pool

1. 扫描稿件中所有引用文献的摘要
2. 是否有任何一篇报道了声称所否认的结局？
3. 判定:
   - 所有引用文献均不包含该结局 → ✅ NO_CONTRADICTION
   - 至少一篇文献包含该结局，但不够具体（如非干预特异性） → ⚠️ PARTIAL_CONTRADICTION
   - 至少一篇文献包含该结局且有足够特异性 → ❌ CONTRADICTION

**最关键的错误类型**: 稿件中引用了某篇文献用于支撑其他论点，但这篇文献恰好包含了声称所否认的数据。
例: 声称 "no adult lung function data" → 引用了 Gibson 2015 用于其他目的 → Gibson 2015 确实报告了成人肺功能
→ ⚠️ PARTIAL_CONTRADICTION: 成人肺功能数据存在，但不是干预特异性的（不区分 VTV vs PLV）

### Verification C: Claim Precision Grading

根据声称范围的精确度判定处理方式:

| Precision Level | Example | If Verification Finds Related Data |
|----------------|---------|-----------------------------------|
| **Level 0** (Unqualified Absolute) | "no data exist" | ❌ MUST FIX: 任何相关数据都构成矛盾 |
| **Level 1** (Temporally Bounded) | "no data beyond 5 years" | ⚠️ MUST FIX: 如果存在 >5 年数据 |
| **Level 2** (Specifically Qualified) | "no intervention-specific adult data" | ✅ ACCEPTABLE: 只要数据确实不区分干预 |

---

## Processing Rules

| Detection Result | Severity | Required Action |
|-----------------|----------|----------------|
| ❌ CONTRADICTION | MUST FIX | 修正声称的绝对性（如: "no adult data" → "no adult data for this specific comparison"），或更换引用 |
| ⚠️ PARTIAL_CONTRADICTION | MUST FIX | 添加上下文限定语，精确化声称范围（如: "no intervention-specific long-term data" 而非 "no long-term data"） |
| ⚠️ OVERSTATEMENT | MUST FIX | 降级声称的绝对性（如: "absent" → "limited"、"zero" → "near-zero"、"completely unknown" → "incompletely characterized"） |

---

## Required Qualifying Language

### For PARTIAL_CONTRADICTION cases

当数据存在但不够具体时，使用以下模板之一：

> "No [intervention-specific] long-term follow-up data exist for [intervention] — though generic [outcome] data have been reported in broader preterm cohorts (see [citation]), these studies do not distinguish between [intervention A] and [intervention B]."

> "While adult [outcome] data exist for preterm survivors as a group ([citation]), intervention-stratified analyses are absent. Whether the choice of [intervention] in the NICU affects [outcome] at age [X] is unknown."

### For OVERSTATEMENT cases

| Original | Replacement |
|----------|------------|
| "no data" | "no intervention-specific data" 或 "limited data" |
| "completely absent" | "absent for this specific comparison" |
| "zero" | "near-zero" 或 "essentially none" |
| "the evidence base is essentially empty" | "the intervention-specific evidence base for outcomes beyond early childhood is limited" |
| "we know nothing" | "we lack systematic data" |

---

## Integration with Agent 4

### Position in Workflow
Agent 4 Step 1 (事实核查) → **Step 1.5 (绝对否定声称检测)** → Step 2 (逻辑审查)

### Execution Protocol
1. Scan full manuscript for absolute negative keywords
2. For each detected claim:
   a. Extract claim scope (intervention, outcome, population)
   b. Run Verification A against cited PMID
   c. Run Verification B against full citation pool
   d. Assign precision level (0/1/2)
   e. Determine detection result (CONTRADICTION / PARTIAL_CONTRADICTION / OVERSTATEMENT)
3. Generate detection report with MUST FIX items
4. For each MUST FIX: suggest replacement language

### Output in Agent 4 Report
```markdown
- **绝对否定声称检测** (Step 1.5): N absolute negative claims detected
  - ❌ CONTRADICTION: N claims — cited source itself contains the denied data
  - ⚠️ PARTIAL_CONTRADICTION: N claims — other cited sources contain related data
  - ⚠️ OVERSTATEMENT: N claims — scope needs narrowing
  - ✅ ACCEPTABLE: N claims — verification passed
```
