# 审校反馈 — PNCS_Systematic_Review.docx — 2026-06-09

**审校对象**: `E:\medical-review\manuscript\PNCS_Systematic_Review.docx`
**审校日期**: 2026-06-09
**审校范围**: 全文审校（标题→结论→参考文献），含外部事实核查（PubMed / Cochrane Library / Web Search 交叉验证）
**综合判定**: ❌ **CRITICAL FAIL** — 8 项 MUST FIX（含 4 项引用/数值事实错误），阻塞投稿；另 4 项结构性/方法学缺陷需大幅修订

---

## 一、MUST FIX（阻塞投稿）

### MF-1 (§6.1, ¶2): NEUROSIS 随访数据严重失实 🔴

**稿件原文**: "The 5-year follow-up [39] found that among survivors, budesonide was associated with higher moderate-to-severe NDI (16.9% vs. 12.0%; RR 1.41, 95% CI 1.01–1.96)."

**实际数据** (Bassler et al., *NEJM* 2018;378:148–57, PMID 29320647):
- 该参考文献 [39] 报告的是 **18–22 个月矫正年龄** 的随访，**并非 5 年**
- NDI 实际数据: **48.1% vs 51.4%; adjusted RR 0.93 (0.80–1.09), P = 0.40** — 两组无显著差异
- 显著差异仅在**死亡率**: 19.9% vs 14.5%; RR 1.37 (1.01–1.86)

**问题严重性**: 稿件声称 budesonide 增加了 NDI（RR 1.41），而实际数据表明 NDI 无显著差异（RR 0.93）。稿件中 "16.9% vs 12.0%; RR 1.41" 这组数字**在任何已知 NEUROSIS 出版物中均不存在**。这是事实性捏造级错误 — 将实际报告的死亡率 RR 1.37 嫁接到了 NDI 上，同时虚构了百分比数据。

**修正**: 
- 将 "5-year follow-up" 改为 "2-year (18–22 month) follow-up"
- 删除 "16.9% vs. 12.0%; RR 1.41 (1.01–1.96)" 
- 替换为正确数据：死亡率 RR 1.37；NDI 无显著差异
- 如确实存在 5 年随访数据，需提供准确引用（当前文献 [39] 不支持）

---

### MF-2 (References [17], [18]): 两篇关键 NMA 的作者归属完全错误 🔴

**2a. Reference [17]**: 
- **稿件写**: "Ramaswamy VV, Bandyopadhyay T, Nanda D, et al. ... *Cochrane Database Syst Rev* 2023;(8):CD014603. PMID: 37650547."
- **实际**: PMID 37650547 对应 **Hay S, Ovelman C, Zupancic JA, Doyle LW, Onland W, Konstantinidis M, Shah PS, Soll R.** *Cochrane Database Syst Rev* 2023;(8):**CD013730** (非 CD014603).
- 作者列表全员错误 + Cochrane 文章编号错误

**2b. Reference [18]**:
- **稿件写**: "Zeng L, Tian J, Song F, et al. ... *JAMA Pediatr* 2021;175:e206826. PMID: 33720274."
- **实际**: PMID 33720274 对应 **Ramaswamy VV, Bandyopadhyay T, Nanda D, Bandiya P, et al.** (not Zeng)
- Zeng 等人 2018 年的 NMA 发表于 *Arch Dis Child Fetal Neonatal Ed* (PMID 29475879)，并非此篇

**问题严重性**: 将两篇关键论文的作者混淆/调换——Ramaswamy 的 JAMA Pediatrics 2021 论文被错误地归于 Zeng，而 Hay 的 Cochrane 2023 NMA 被错误地归于 Ramaswamy。这使得 §3.3 整段的文献引用基础不可靠。

**修正**: 
- [17] → 更正为 Hay S, Ovelman C, Zupancic JA, Doyle LW, Onland W, Konstantinidis M, Shah PS, Soll R. Systemic corticosteroids for the prevention of bronchopulmonary dysplasia, a network meta-analysis. *Cochrane Database Syst Rev* 2023;(8):CD013730.
- [18] → 更正为 Ramaswamy VV, Bandyopadhyay T, Nanda D, Bandiya P, Ahmed J, Garg A, Roehr CC, Nangia S. Assessment of Postnatal Corticosteroids for the Prevention of Bronchopulmonary Dysplasia in Preterm Neonates: A Systematic Review and Network Meta-analysis. *JAMA Pediatr* 2021;175(6):e206826.
- 如果确实需要引用 Zeng 2018 NMA，需单独列为一条参考文献

---

### MF-3 (Reference [23]): 引用作者、期刊、年份全部错误 🔴

**稿件原文**: "[23] Zeng L, Tian J, Song F, et al. Effect of dexamethasone on intelligence and hearing in preterm infants: a meta-analysis. *Pediatrics* 2014;134:898–906. PMID: 25206867."

**实际**: PMID 25206867 对应 **Zhang R, Bo T, Shen L, Luo S, Li J.** *Effect of dexamethasone on intelligence and hearing in preterm infants: a meta-analysis.* **Neural Regeneration Research** 2014;9(6):637–645.

- 第一作者是 **Zhang**，不是 **Zeng**
- 期刊是 **Neural Regeneration Research**，不是 **Pediatrics**
- 卷/页是 **9(6):637–645**，不是 **134:898–906**

**问题严重性**: 期刊名、作者名、卷号/页码三重错误。稿件系统中存在模式性的引用生成错误——多篇"Zeng"引用实为不同作者。

---

### MF-4 (§2.2, ¶1): Shinwell CP 率数据将分子当百分比 🔴

**稿件原文**: "Shinwell et al. (1996), who reported CP rates of 39% versus 13% (P < 0.01)"

**实际** (Shinwell et al., *Arch Dis Child Fetal Neonatal Ed* 2000;83:F177–F181):
- 地塞米松组: **49%** (39/80) — 39 是**分子**，非百分比
- 安慰剂组: **15%** (12/79) — 12 是**分子**
- 稿件将 39/80 误解为 39%，实际应为 49%

**修正**: "CP rates of 49% (39/80) versus 15% (12/79)"

---

### MF-5 (§1 Header / Title Block): 双重目标期刊 + 双重体裁标签 🔴

**稿件原文** (line 6): "Narrative Review"
**稿件原文** (line 11): "Target Journal: Pediatric Research"
**稿件原文** (line 13): "A Systematic Narrative Review"
**稿件原文** (line 15): "Target Journal: Archives of Disease in Childhood: Fetal & Neonatal Edition (BMJ)"

**问题**:
1. 稿件同时自称 "Narrative Review" 和 "A Systematic Narrative Review"——体裁自相矛盾
2. 同时列出两个目标期刊（Pediatric Research 和 ADC Fetal & Neonatal Edition）——投稿前必须确定一个
3. Running title "NRDS Interventions: Life-Course Consequences" 与稿件标题（关于 Postnatal Corticosteroids & Neurodevelopment）不匹配——NRDS（新生儿呼吸窘迫综合征）不是本文主题

**修正**: 
- 确定体裁标签（建议 "Systematic Narrative Review" 或 "Narrative Review" 择一）
- 删除多余的目标期刊行
- 修正 Running title（建议 "Postnatal Corticosteroids & Neurodevelopment"）

---

### MF-6 (§3.3, ¶1): "MoLdDX" 分类法不存在于所引文献中 🔴

**稿件原文**: "moderately-early, low-dose dexamethasone (MoLdDX)"

**实际**: 
- Ramaswamy 2021 (*JAMA Pediatr*): 使用 **MoMdDX**（moderately-early, **medium** cumulative dose 2–4 mg/kg），不是 "low-dose"
- Hay 2023 Cochrane NMA: 使用 high-dose (≥4 mg/kg) / moderate-dose (≥2 to <4 mg/kg) / low-dose (<2 mg/kg) 三层分类

**修正**: 核实实际引用来源使用的术语：如果是 Ramaswamy 2021 → "MoMdDX"（medium-dose）；如果是 Hay 2023 → 使用 "moderate-dose dexamethasone"

---

### MF-7 (§8.2, Table Row 3): 临床决策表中 "HC school-age data emerging" 陈述模糊且可能误导 🔴

**稿件原文**: "Mortality reduction; HC school-age data emerging [15, 33, 36]"

**问题**: 
- [15] 是 Doyle 2021 Cochrane late corticosteroid review——不包含 school-age 数据
- 将 school-age 数据描述为 "emerging" 在 2026 年已不准确：SToP-BPD 5.5-year (de Baat 2025) 和 NICHD NRN school-age (DeMauro 2026) 均已**正式发表**，不是 "emerging"

**修正**: "HC school-age data now published (SToP-BPD 5.5y, NICHD NRN school-age) [33, 36]"

---

### MF-8 (Reference [12]): Jenkinson 合著者姓名错误 🔴

**稿件原文**: "[12] Jenkinson A, O'Connell O, Ryan CA, et al."

**实际**: **Jenkinson AC, Kaltsogianni O, Dassios T, Greenough A.** *J Perinat Med* 2023;51:951–60. PMID: 37606507.

合著者全员错误：O'Connell, Ryan 均不是本文作者；实际作者为 Kaltsogianni, Dassios, Greenough。

---

## 二、数值/一致性修正

### NC-1 (§3.1): Early corticosteroids CP RR 数值偏差
- **稿件**: RR 1.42, 95% CI 1.08–1.87
- **Cochrane Doyle 2021 实际**: RR **1.43**, 95% CI **1.07–1.92** (all early corticosteroids vs control)
- Cochrane dexamethasone-specific (more relevant to manuscript's argument): RR **1.77**, 95% CI 1.21–2.58
- **建议**: 核实引用数值；如确实引用 all-corticosteroids pooled → 更正为 1.43 (1.07–1.92)；如强调 dexamethasone-specific CP risk → 使用 1.77 (1.21–2.58)

### NC-2 (§3.1): Late corticosteroids CP RR 置信区间
- **稿件**: RR 1.12, 95% CI 0.81–1.54
- **需验证**: 与 Doyle 2021 Cochrane late review 原文对照

### NC-3 (§3.3): "14 corticosteroid regimens" + "MoLdDX" 的来源混淆
- 14-regimen 分类来自 **Ramaswamy 2021** (JAMA Pediatr)，但该文使用 MoMdDX (not MoLdDX) 且第一作者为 Ramaswamy 非 Zeng
- "moderately-early, low-dose dexamethasone and late low-dose hydrocortisone" 这一结论更接近 Ramaswamy 2021 的叙述，但术语不一致
- **建议**: 重写 §3.3，明确每篇 NMA 的具体发现、术语和作者归属

### NC-4 (§6.1): NEUROSIS 吸入 budesonide 的 BPD RR
- **稿件**: RR 0.74, 95% CI 0.60–0.91
- **原始文献** (Bassler 2015): survival with BPD among survivors RR 0.74 (0.60–0.91) ✓ 数值本身正确
- 但稿件用 "Budesonide reduced BPD" 概括不够精确——primary endpoint 是 death or BPD (RR 0.86, P=0.05)，secondary analysis 才是 BPD among survivors

### NC-5 (§3.4): Dexamethasone vs Hydrocortisone indirect comparison
- **稿件**: "dexamethasone has larger BPD effect sizes (RR 0.72) than hydrocortisone (RR 0.86, crossing the null)"
- 需要标出具体来源：这组 RR 来自哪篇 meta-analysis？是 direct comparison 还是 network indirect estimate？当前引用 [21] (Onland 2017 Cochrane) 可能不支持这两个确切数字

---

## 三、方法学/结构性缺陷

### MS-1: 单数据库检索与 "Systematic" 标签的矛盾
- 稿件标注 "Systematic Narrative Review" 且在 Abstract 中声明 "Systematic search"
- 但方法学仅有 **Europe PMC 单一数据库**检索
- 系统综述的最低标准（Cochrane Handbook / PRISMA 2020）要求检索 ≥ 2 个数据库（至少 PubMed + Embase 或 Cochrane CENTRAL）
- 未检索 Tier 1 数据库 PubMed (via E-utilities)、Semantic Scholar、ClinicalTrials.gov
- 数据库覆盖度 = 20% (仅 1/5 Tier 1 数据库)，远低于项目规范 > 80% 的最低门槛
- **建议**: ① 补充至少 PubMed 和 Cochrane CENTRAL 检索；② 或在 Methods 中明确标注 "non-systematic search" 并在 Limitations 中讨论数据库覆盖缺口；③ 考虑将体裁从 "systematic" 改为 "narrative"（但会降低证据等级声明）

### MS-2: 无 PRISMA 流程图
- 系统综述必须包含 PRISMA 2020 flow diagram
- 稿件提到 "8,406 unique records → 309 included" 但没有记录排除流程、全文筛选步骤、排除原因

### MS-3: 无正式偏倚风险评估
- 任何标注 "systematic" 的综述应使用 Cochrane RoB 2 (RCT)、ROBINS-I (非随机研究)、AMSTAR 2 (已有系统综述)
- 稿件未报告任何纳入研究的偏倚风险评估
- 使 GRADE 证据质量评级（稿件中提及但未系统报告）失去基础

### MS-4: 无 PROSPERO 注册 / 无 Protocol
- 系统综述研究方案应预先在 PROSPERO 注册
- 稿件未提及 Protocol 或注册号

---

## 四、内部一致性矛盾

### IC-1: 体裁标签不一致
- Line 6: "Narrative Review"
- Line 13: "A Systematic Narrative Review"
- 两种体裁的方法学要求不同——narrative review 的检索可以非系统，systematic review 必须系统检索

### IC-2: Scope 声明与内容矛盾
- 稿件自称聚焦于 "dexamethasone–hydrocortisone evidence base" 
- 但 §6 全文讨论吸入性皮质类固醇（inhaled budesonide）
- 如要保留 §6，应在 Introduction 中声明 inhaled corticosteroids 为 "secondary comparative pathway"（如当前 §1 ¶3 所述但不够突出）

### IC-3: Cochrane GRADE 评级
- §3.1: "high-certainty GRADE" for CP — 需核实是否确实来自 Doyle 2021 Cochrane review 的 GRADE assessment
- §8.2: 表格中 "CP RR 1.42, NNH 20 [14]" — 与 §3.1 的 RR 1.42 一致但实际应为 1.43

---

## 五、语言/呈现质量

### LP-1: Abstract 中 "moderate-to-severe NDI" 的引用
- Abstract 提到 "two major trials now have school-age follow-up (SToP-BPD 5.5-year and NICHD NRN school-age outcomes), providing the first randomized school-age evidence that hydrocortisone did not increase measured functional or neurodevelopmental impairment" 
- 措辞为正面结论，但 SToP-BPD 5.5y 原文结论为 "did not affect death or moderate-severe NDI"（中性）且 DeMauro 2026 显示两组均约 71-73% 有 functional impairment（基线极高）
- 应将结论调整为更中性："showed no significant difference in functional or neurodevelopmental outcomes"

### LP-2: §10 Conclusions 语气偏乐观
- "Hydrocortisone ... represents the preferred agent when postnatal corticosteroids are necessary" 这一结论比现有证据支持的更强
- Hay 2023 Cochrane NMA 结论: "certainty of the evidence is low" + 仅 6/59 RCTs 提供了头对头比较
- 建议添加限定语："based on the currently available indirect evidence, acknowledging the absence of head-to-head trials"

### LP-3: §7.1 "Sensitivity and specificity of Bayley-III <85 for predicting school-age IQ <85"
- 引用 [42] Luttikhuizen dos Santos 2013
- 需核实 50-60% sensitivity / 70-80% specificity 是否来自此文献

---

## 六、批判性评论 & 建议

### CR-1: 证据合成的批判性不足
综述对 Cochrane 综述的批判性审视不足。例如：
- Doyle 2021 Cochrane reviews 的最后检索日期是何时？如检索日期较早，新近发表的 school-age 数据可能未被纳入
- GRADE 评级由 Cochrane 综述作者做出 — 综述应说明是否接受这些评级或对某些评级存在疑虑
- 应与 `review-feedback-2026-06-06.md` 中的审校模式一致：需对关键引用添加时效性/方法学限定语

### CR-2: 偏倚风险评估缺失 → 证据强度声明无基础
稿件多处使用 "high-certainty GRADE" 但未独立进行偏倚风险评估。Cochrane 综述的 GRADE 评级不等于作者独立评估。综述应至少报告：
- 纳入 RCT 的 RoB 2 总体评估
- 是否存在普遍的高偏倚风险领域（如 blinding of outcome assessment for CP diagnosis）

### CR-3: 建议添加 "异质性来源" 讨论
- §3.1-3.2 引用的 Cochrane RR 为 pooled estimates，但未讨论 I² 或 τ²
- 早期地塞米松试验间的剂量/时机异质性极大——报告的 pooled RR 可能掩盖重要的亚组差异

### CR-4: LMIC 议题 (§9.4) 
- 这是一个有价值且原创的讨论点
- 建议补充引用（如 WHO 基本药物清单中地塞米松 vs 氢化可的松的可用性差异）

### CR-5: 项目规范符合性
按 `harness/metrics.md` 五维度度量：
- **L2 业务成功率**: 综述写作审校维度评分：
  - 论点充分性: 3/5（论点清晰但部分过度断言）
  - 逻辑连贯性: 4/5（结构合理，§2→§3→§4→§5→§6→§7→§8 流畅）
  - **引用准确性: 1/5**（4 篇关键引用存在作者/期刊/数据事实错误，见 MF-1 至 MF-4, MF-8）
  - **综合 L2 判定**: ❌ L2_FAIL — 引用准确性 < 2 分

---

## 七、综合评分

| 评估维度 | 得分 | 评语 |
|---------|------|------|
| 论点清晰度 | 3/5 | 中心论点明确 (dex vs HC 差异化的神经发育风险)，但部分结论过于肯定 |
| 引用准确性 | 1/5 | 48 篇参考文献中发现至少 5 篇存在作者名/期刊/数据错误 |
| 方法学严谨性 | 2/5 | 单数据库检索、无 PRISMA、无 RoB、无 PROSPERO |
| 逻辑结构 | 4/5 | 历史→Cochrane→Dex→HC→Inhaled→Synthesis 流畅 |
| 内部一致性 | 2/5 | 体裁标签、目标期刊、Running title 自相矛盾 |
| 批判性平衡 | 3/5 | 对 HC 证据的批判性评估合理，但对 Cochrane 综述的审视不足 |
| 数据准确性 | 2/5 | CP RR、Shinwell %、NEUROSIS NDI 数据均存在不同程度的错误 |

**综合判定**: ❌ **CRITICAL FAIL** — 8 MUST FIX (含 4 项引用/数值错误) 阻塞投稿。在修正 MF-1 至 MF-8 之前，本综述不应进入下一步（Word 生成、外部投稿）。

**建议下一步**:
1. 逐项修正 MF-1 至 MF-8
2. 补充 PubMed + Cochrane CENTRAL 检索（或明确将体裁降级为 narrative review）
3. 生成 PRISMA 流程图
4. 重新验证全部 48 条参考文献的作者/期刊/PMID
5. 修正后重新运行审校验证

---

*审校完成于 2026-06-09 | 审校范围: 全文事实核查 + 参考文献交叉验证*
