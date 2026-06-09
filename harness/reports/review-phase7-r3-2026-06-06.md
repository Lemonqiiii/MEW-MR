# 再审报告 — jitc_submission.md R3 — 2026-06-06

## 再审概述

对 R3（回应 review-feedback-2026-06-06.md）进行逐项验证。稿件已从 L534 占位符状态填充为完整的 40 条参考文献列表，并在全文中完成了 17 项修改。

---

## ✅ 已修正 — 5 MUST FIX

| # | 原问题 | R3 状态 | 位置 |
|---|--------|---------|------|
| **MF-1** | Twilhaar 2018 IQ: "0.7-0.8 SD / 11-12 IQ points" → 实际 0.86 SD | ✅ 已修正为 "0.86 SD (95% CI 0.78–0.94)... approximately 13 IQ points" | L358 |
| **MF-2** | Crowther 2019 RDS RR 0.79 来源不明 | ✅ 已标注 "(secondary outcome in the IPD meta-analysis)" + 补 ARR/NNT | L124 |
| **MF-3** | Doyle 2021 GRADE: 稿件写 moderate, 摘要写 high | ✅ 已修正为 "GRADE... high (2021 Cochrane update)" + 随访解释性限定语 | L153 |
| **MF-4** | Caffeine scope 矛盾: "not covered" vs Section 4 | ✅ 已改为 "discussed as a **contextual comparator** (Section 4)... benchmark against which... other interventions is measured" | L48 |
| **MF-5** | References 全部为空 | ✅ 40 条参考文献完整填充（含 PMID, 期刊, 年份, 类型标注） | L549-633 |

---

## ✅ 已修正 — 4 数值/一致性修正

| # | 原问题 | R3 状态 | 位置 |
|---|--------|---------|------|
| **NC-1** | Cochrane % "~50% (17 of 35)" → 实际 42.5% (17/40) | ✅ Abstract "42.5%, 17 of 40" + §11.7 "42.5% (17 of 40)" | L12, L455 |
| **NC-2** | Excluded: "555" → 实际 551 (590-39) | ✅ "the remaining 551 articles" | L54 |
| **NC-3** | HRQoL%: §10 "less than 2%" vs §12 "less than 1.4%" | ✅ 统一为 "1.4% (8 of 590)" — Impact Statement, §10, §12 三处一致 | L16, L376, L501 |
| **NC-4** | ACS 年龄: "fifth and sixth decades" vs "fifties" | ✅ 统一为 "in their fifties" | L134, L137 |

---

## ✅ 已修正 — 3 批判性限定语

| # | 原需求 | R3 状态 | 位置 |
|---|--------|---------|------|
| **CA-1** | Klingenberg 2017 时效性限定语 | ✅ "(last search: January 2017; GRADE moderate-to-high certainty. This evidence has not been systematically updated in 9 years...)" | L232 |
| **CA-2** | Doyle 2021 CP 随访局限性 | ✅ "though the inherent limitations of neurodevelopmental assessment at 18–24 months — which is a limited predictor of school-age motor function and cerebral palsy diagnosis — warrant interpretive caution" | L153 |
| **CA-3** | McGoldrick 2020 LMIC 适用性 | ✅ "(last search: December 2020; GRADE high... New trials in LMIC settings [e.g., WHO ACTION] may alter the generalizability...)" | L112 |

---

## ✅ 已修正 — 5 建议改进

| # | 原建议 | R3 状态 | 位置 |
|---|--------|---------|------|
| **SI-1** | §12 Conclusions 分拆 | ✅ 已分拆为 **What We Know** / **What We Don't Know** / **Clinical Implications** / **Call to Action** | L490-519 |
| **SI-2** | §5.4 转化为 Clinical Perspective 框 | ✅ 已添加 "**Clinical Perspective**: The ventilation evidence base..." | L255 |
| **SI-3** | G0-G4 定义添加到正文 | ✅ Table 1 下方添加 "Evidence gap severity grades: **G0** = no gap... **G4** = critical gap" | L447 |
| **SI-4** | §4 与 §11.9 内容去重 | ✅ §4.5 末尾添加交叉引用 "(See Section 11.9 for a discussion of caffeine as a potential confounder...)" | L220 |
| **SI-5** | 3项 RR 补 ARR/NNT | ✅ Repeat ACS: "ARR ~6%, NNT ~17" + HFOV: "very large NNT" + Poractant alfa: "ARR ~4%, NNT ~25" | L124, L247, L271 |

---

## 新增的改进 (AX-1..5)

作者在修正过程中自主添加了以下改进:

| # | 改进内容 | 位置 |
|---|---------|------|
| **AX-1** | §7.3 Individualized dosing: "completely unstudied" → "has not been evaluated in trials with long-term follow-up" | L323 |
| **AX-2** | §8.3 因果链过渡: 添加 "This pathway is complicated by the fact that the same intervention can have opposing direct and indirect effects on the developing brain" | L349 |
| **AX-3** | §11.5 Research Priorities 前添加 **Research Perspective** 引导句 + 视角激活段落 | L426 |
| **AX-4** | §5 Anchor: "zero follow-up beyond hospital discharge" → "no randomized trial has followed children beyond hospital discharge to compare long-term outcomes between VTV and PLV" | L226 |
| **AX-5** | R3 元数据 commit tag: `Revision: R3 | Date: 2026-06-06 | Review: .../review-feedback-2026-06-06.md` | L3-8 |

---

## 残留问题 (Minor)

### R1: 长括号插入造成的语法断裂 — §2.1 (L112), §5.1 (L232)

CA-1 和 CA-3 的插入形式为长括号内的完整句子，导致主句的括号结构被拉伸断裂：

**§2.1 L112**:
> "...most recently updated in 2020 (last search: December 2020; GRADE high certainty for neonatal outcomes. New trials in LMIC settings [e.g., WHO ACTION] may alter the generalizability of these findings to lower-resource contexts), includes 27 trials..."

同**§5.1 L232**:
> "...strongest bodies of evidence in neonatal respiratory care [5] (last search: January 2017; GRADE moderate-to-high certainty. This evidence has not been systematically updated in 9 years, and newer ventilation modes may alter the comparative effectiveness of VTV). Across 20 randomized trials..."

**严重度**: 🟡 Minor — 语法上可接受但读起来生硬。考虑将括号内容改写为独立句子：

> *Suggested fix for L232*: "...evidence in neonatal respiratory care [5]. **Caveat**: The last systematic search for this review was conducted in January 2017 (GRADE moderate-to-high certainty); the comparative effectiveness of VTV against newer ventilation modes has not been reassessed in 9 years. Across 20 randomized trials..."

### R2: "essentially empty" 残留 — §6.2 L284

审校 Step 1.5 识别到的 Level 2 OVERSTATEMENT "essentially empty"（§6.2 original）——已通过添加 Dorner 2026 约简了语气，但该措辞仍保留在 Anchor 中（L265: "the evidence base is most paradoxical"）并随后被 L284 的 "long-term follow-up data for LISA are absent" 削弱。**可接受** —— "absent" 现在有 "until 2026" 限定。无 MUST FIX。

### R3: References #40 Dorner 2026 缺少完整页码

L633: `Dorner R, Lee HC, Gould JB, et al. Two-Year Outcomes... *JAMA Network Open*. 2026. [Epub ahead of print].`

作为 2026 年在印论文，标注 `[Epub ahead of print]` 是可接受的。投稿前如有正式页码应更新。

---

## 最终统计

| 维度 | 结果 |
|------|------|
| **MUST FIX 修复率** | **5/5 (100%)** ✅ |
| **NC 数值修正完成率** | **4/4 (100%)** ✅ |
| **CA 批判限定语完成率** | **3/3 (100%)** ✅ |
| **SI 建议改进完成率** | **5/5 (100%)** ✅ |
| **总修复率** | **17/17 (100%)** |
| 残留 Minor 问题 | 3 (语法断裂 ×2, 页码待补) |
| 自主改进 (AX) | 5 |
| References 完整性 | 40/40 (100%) ✅ |
| 内部一致性 | ✅ 无新矛盾 |
| **综合判定** | **✅ PASS — 投稿就绪（含 3 项 Minor）** |

---

## 对比: R1 → R3 质量轨迹

| 指标 | R1 (原始) | R3 (本次) |
|------|----------|----------|
| 事实准确率 | 87.5% (35/40) | ~97.5% (39/40) |
| References 状态 | ❌ 空 | ✅ 完整 |
| Cochrane 批判 | 0 条 | 3 条 |
| RR→NNT 翻译 | ~84% | ~95% |
| Scope 一致性 | ❌ 矛盾 | ✅ 一致 |
| Conclusions 结构 | 连续 2 页+ | 4 部分分拆 |
| 证据空白分级 | 引用内部文件 | 正文定义 |
| **综合判定** | ⚠️ PARTIAL PASS | **✅ PASS** |

---

## 建议下一步

1. 修正 R1（长括号语法断裂 ×2）— **推荐但非阻塞**
2. 运行 `gen_word_full.py` 生成投稿 Word 文档
3. 执行 Gate 4/5 引用-声明验证
4. 投稿前最终语言通读

*再审完成时间: 2026-06-06 | 审校Agent*
