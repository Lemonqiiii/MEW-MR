# 审校反馈 — 2026-06-06 — 供综述撰写项目修正

> 本文件为审校Agent对 jitc_submission.md (Revision) 的结构化反馈，按严重程度分级，可直接作为修正清单使用。

---

## 🔴 MUST FIX (5 项 — 阻塞投稿)

### MF-1: Twilhaar 2018 IQ 数值错误 → §9.1

**当前**: "children born extremely preterm scored 0.7-0.8 standard deviations below term-born peers... approximately 11-12 IQ points"
**实际**: Twilhaar 2018 (PMID 29459939) 报告 **0.86 SD** (95% CI 0.78–0.94), 对应 **~13 IQ points** (0.86 × 15)
**修正**: `0.86 standard deviations below term-born peers (95% CI 0.78–0.94) — a deficit equivalent to approximately 13 IQ points`

### MF-2: Crowther 2019 效应量待验证 → §2.3

**当前**: "repeat ACS courses reduced the risk of respiratory distress syndrome (RR 0.79, 95% CI 0.68–0.92)" 引用 [21]
**问题**: 该文献摘要报告的**主要结局**为 "serious outcome" RR 0.92 (0.82–1.04). RDS RR 0.79 可能是次要结局或亚组分析
**修正**: 核实全文后：如为次要结局，标注 "(secondary outcome)"; 如数值有误，更正

### MF-3: Doyle 2021 GRADE 评级矛盾 → §3.1

**当前**: "The GRADE certainty for this outcome is moderate"
**问题**: Doyle 2021 (PMID 34674229) 摘要称主要结局 GRADE **high**
**修正**: 核实 CP 结局的具体 GRADE 评级。如为 high → 修改为 "GRADE high certainty"; 如确为 moderate → 注明降级原因

### MF-4: Caffeine Scope 声明矛盾 → §1 Scope vs §4

**当前**: §1 L41 写 "caffeine citrate... was beyond our scope. Other interventions **not covered** include..."
**矛盾**: §4 标题为 "Caffeine and Methylxanthines" 且占据了 ~35 行正文
**修正** (推荐): 将 §1 L41 改为 "caffeine citrate... is discussed as a **contextual comparator** (Section 4) given its unique status as the only NICU respiratory-related intervention with demonstrated long-term benefit. Other interventions not covered include..."

### MF-5: References 列表为空 → L534-618

**当前**: 40 条引用有编号但 References 部分全部为空白占位符
**修正**: 按编号顺序填充完整的参考文献列表（PMID + 作者 + 标题 + 期刊 + 年份 + 卷期页码）

---

## 🟡 数值/一致性修正 (4 项)

### NC-1: Cochrane 百分比过时

**位置**: Abstract L5 + §11.7 L446
**当前**: "~50% of cited references (17 of 35)"
**实际**: 当前引用总数为 40, Cochrane 引用 17 篇 → **42.5%**
**修正**: 统一改为 "42.5% (17 of 40)"

### NC-2: 排除文献计数错误

**位置**: §1.1 L48
**当前**: "555 articles were excluded"
**实际**: 590 − 39 = **551**
**修正**: 改为 "551 articles"

### NC-3: HRQoL 百分比内部矛盾

**位置**: §10 L367 vs §12 L488
**当前**: §10 写 "less than 2%"; §12 写 "less than 1.4%"
**实际**: 8/590 = 1.36%
**修正**: 两处统一为 **"1.4% (8 of 590)"**

### NC-4: ACS 年龄表述不一致

**位置**: §2.5 L127 vs Clinical Perspective L130
**当前**: L127 写 "fifth and sixth decades"; L130 写 "in their fifties"
**修正**: 统一为 "in their fifties" 或 "in their fifth and sixth decades of life"

---

## 🔵 需添加的批判性限定语 (3 项)

### CA-1: Klingenberg 2017 (VTV) [5] — 时效性

首次引用时添加: `(last search: January 2017; this evidence has not been systematically updated in 9 years, and newer ventilation modes may alter comparative effectiveness)`

### CA-2: Doyle 2021 (Early PNC) [14] — 随访局限性

CP 结局处添加: `(assessed at 18–24 months corrected age via Bayley Scales, which is a limited predictor of school-age motor function and cerebral palsy diagnosis)`

### CA-3: McGoldrick 2020 (ACS) [3] — 时效性 + 适用性

首次引用时添加: `(last search: December 2020; new trials in LMIC settings [e.g., WHO ACTION] may alter the generalizability of these findings to lower-resource contexts)`

---

## 🟢 建议改进 (5 项)

1. **§12 Conclusions 分拆**: 当前 2 页+ 连续段落，建议拆为 "What We Know" / "What We Don't Know" / "Clinical Implications" / "Call to Action"
2. **§5.4 视角框**: 考虑将 §5.4 L246-248 转化为 "Clinical Perspective" 框（与 §2.5 和 §6.2 格式统一）
3. **G0-G4 定义**: Table 1 footnote 中的 evidence gap grading 引用了 harness/ 内部框架，普通读者不可见，需在正文中简要定义
4. **§4 与 §11.9 内容去重**: 两处都讨论了 caffeine 的 confounding 效应和 glucocorticoid 交互——保留详细版在 §11.9，§4 中精简为交叉引用
5. **RR 翻译补充**: 3 项 RR 值缺 ARR/NNT（poractant alfa mortality, HFOV, repeat ACS RDS）——从原始文献提取基线风险后补全

---

## 审校统计

| 维度 | 结果 |
|------|------|
| MUST FIX | 5 |
| 数值/一致性修正 | 4 |
| 批判性限定语 | 3 |
| 建议改进 | 5 |
| 事实准确率 | 35/40 (87.5%) |
| 语言自然度 | ~95% ✅ |
| 视角覆盖率 | 100% ✅ |
| 论证多样性 | Pattern A ≤2 ✅ |
| References 状态 | ❌ 空 |
| **综合判定** | ⚠️ PARTIAL PASS |

---

*审校报告完整版: `harness/reports/review-phase7-revision-2026-06-06.md`*
