# 审稿报告 — Revision R5

## 基本信息
- **审稿ID**: RA-2026-06-06-003
- **稿件**: Life-Course Consequences of Early-Life Respiratory Interventions for Neonatal Respiratory Distress Syndrome: A Narrative Review
- **目标期刊**: Pediatric Research (IF ~3, Springer Nature)
- **审稿日期**: 2026-06-06
- **审稿方式**: 6维度深度审查 + R4修复完整性验证 + 逐节深读
- **前置版本**: R4 (ALL REVIEW ITEMS RESOLVED)

---

## 总体评价

The R4 revision substantially improved the manuscript's citation integrity and structural coherence. The manuscript now contains 42 references with proper coverage of the CAP trial follow-up literature, the Introduction–Methods duplication has been resolved, and the Conclusions section is properly anchored to cited evidence. All 12 R4 verification checks passed — the revision was executed thoroughly.

This R5 review is a **cleanup round** focused on smaller structural, stylistic, and precision issues that remain. Two structural issues (empty section body, metric-type mixing) and two precision concerns were identified. The overall quality is high, and all findings are minor enough that a **single revision pass** should address them.

**Overall Assessment: MINOR REVISE**

---

## 审稿维度汇总

| 维度 | 评分 | 主要发现 |
|------|:--:|------|
| 结构完整性 | 8/10 | ⚠️ §5.4节标题下无正文段落 |
| 数据精确性 | 8/10 | ⚠️ §2.2 OR/HR度量混用未说明；§5.2 结局与比较可能不匹配 |
| 引用覆盖 | 9/10 | §12 "What We Know" 无引用（可接受但有提升空间） |
| 语言自然度 | 9/10 | 空洞强调词已清除；无新自然度问题 |
| 叙事一致性 | 9/10 | 重复统计量出现4次可精简 |
| R4修复完整性 | 10/10 | 全部12项验证通过，无回归 |

---

## 🔴 必须修改

### MF-R5-1: §5.4 Empty Section Body

**Location**: §5.4 (L247–251)
**Severity**: MODERATE

Section heading `### 5.4 The Follow-up Gap: Why It Matters` at L247 is followed by two blank lines (L248–250) then directly by a `**Clinical Perspective**:` box at L251. There is no expository paragraph between the heading and the perspective box. Every other Clinical Perspective in the manuscript (§2.5, §3.4 "Family Context") has at least a brief lead-in paragraph.

**Action**: Add a 2–3 sentence paragraph before the Clinical Perspective box that introduces the follow-up gap as the section's theme. Example:
> "The absence of long-term follow-up for ventilation strategies is not merely an academic gap — it has practical consequences for clinical decision-making. Every day, neonatologists choose between ventilation modes based on short-term evidence, with no data on whether that choice matters for the child's respiratory health a decade later."

### MF-R5-2: Mixed Metric Types (OR vs HR) Without Explanation

**Location**: §2.2 (L114)
**Severity**: MODERATE

The key sentence reads: "ACS was associated with reduced neurodevelopmental impairment in extremely preterm infants (adjusted OR 0.69, 95% CI 0.57–0.84) but increased adverse neurocognitive outcomes in term-born children (adjusted HR 1.47, 95% CI 1.36–1.60)."

The text switches from **OR** (odds ratio) to **HR** (hazard ratio) in the same sentence. These metrics differ fundamentally: OR compares odds (case-control/cohort), HR compares instantaneous risk over time (time-to-event/survival). While the Ninan 2022 meta-analysis [20] legitimately used both metrics for different sub-analyses, the reader should be told why: the HR comes from registry-based time-to-event analyses of term-born children.

**Action**: Add a brief note after the HR value, e.g.: "...term-born children (adjusted HR 1.47, 95% CI 1.36–1.60; this hazard ratio derives from registry-based time-to-event analyses, in contrast to the odds ratios from cohort studies above)."

---

## 🟡 数值与一致性

### NC-R5-1: "Extubation Failure" Outcome Context for NIPPV vs NCPAP

**Location**: §5.2 (L237)
**Severity**: LOW — requires source verification

The text states: "Early nasal intermittent positive pressure ventilation (NIPPV) compared with early nasal continuous positive airway pressure (NCPAP) reduces the rate of extubation failure (RR 0.56, 95% CI 0.41–0.78; ARR ~17%, NNT ~6)."

The intervention is described as "early" (suggesting primary/prophylactic support), but the outcome is "extubation failure" (which implies prior intubation). The Lemyre 2016 Cochrane review [29] may include both primary-support and post-extubation trials. If the review pooled both contexts, the "extubation failure" outcome applied only to the post-extubation subset.

**Action**: Verify against the Lemyre 2016 Cochrane review [29]. If the extubation failure result is from a post-extubation subgroup, add a qualifier: "...reduces the rate of extubation failure in post-extubation trials (RR 0.56...)". If the Cochrane review itself pools primary and post-extubation data, note that the pooled estimate includes heterogeneous clinical contexts.

### NC-R5-2: "1.4% (8 of 590)" Appears 4 Times

**Location**: Abstract L16, Impact Statement L16, §10 L376, §12 L497
**Severity**: LOW

The key finding "1.4% (8 of 590) of the relevant literature addressed quality of life" appears in four locations. While this is the review's most striking statistic and repetition serves emphasis, four occurrences may feel redundant to readers.

**Action**: Reduce to three occurrences by removing one instance. Recommended: keep Abstract, §10 (primary reporting), and §12 (conclusions synthesis); remove from Impact Statement or merge it into the existing Impact Statement prose.

---

## 🔵 批判限定语

### CA-R5-1: Conclusions "What We Know" Lacks Citation Anchors

**Location**: §12 (L491)
**Severity**: LOW

The "What We Know" summary (L491) is a single sentence covering six interventions without any references. While conclusions typically summarize previously cited material, this particular sentence makes specific factual claims ("volume-targeted ventilation reduces BPD and pneumothorax") that would benefit from anchor citations — especially since the R4 Clinical Implications fix added citations to the very next subsection.

**Action**: Add key citations to the "What We Know" sentence: e.g., "...reduces BPD and pneumothorax [5]; less invasive surfactant administration reduces death or BPD [16]; late postnatal corticosteroids reduce BPD [15]; caffeine...benefit extending to 11 years [39,41,42]; and lower oxygen saturation targets reduce ROP at the cost of increased mortality [17,37]."

### CA-R5-2: "Victorian Cohort" Mentioned Without Citation

**Location**: §12 (L495)
**Severity**: LOW

The "What We Don't Know" subsection mentions "Victorian cohort for adult outcomes" without a formal citation. The Victorian Infant Collaborative Study (VICS) data is cited in the body via Gibson 2015 [9], but a reader encountering "Victorian cohort" in the Conclusions may not know which reference this refers to.

**Action**: Add [9] after "Victorian cohort for adult outcomes": "...(e.g., Gibson et al. 2015 for VLBW adult lung function [9]; Victorian cohort for adult outcomes [9])..." — or cite a VICS-specific reference if one exists in the list.

---

## 🟢 建议改进

### SI-R5-1: Parenthetical Multi-Sentence Structure

**Location**: §2.1 (L108), §5.1 (L228)
**Severity**: STYLISTIC

Both sections contain parentheticals with internal sentence breaks:

- §2.1: "(last search: December 2020; GRADE high certainty for neonatal outcomes. New trials in LMIC settings...)"
- §5.1: "(last search: January 2017; GRADE moderate-to-high certainty. This evidence has not been systematically updated in 9 years...)"

The period inside the parentheses creates a sentence fragment. Consider restructuring: split the parenthetical, move the search-date/GRADE information into the main text flow, or replace the period with a semicolon.

### SI-R5-2: Section 4 Word Count vs Status

**Location**: Section 4
**Severity**: STYLISTIC

Caffeine is described as a "contextual comparator" (Scope paragraph, L48), yet Section 4 is ~951 words — comparable to the shorter primary intervention sections. This creates a perceived mismatch between the stated scope limitation and the actual coverage. Consider either:
- Trimming Section 4 to ~700 words to better reflect its comparator status
- Or noting in the Scope paragraph that caffeine receives "detailed discussion as a benchmark comparator"

### SI-R5-3: §5.4 and §5.3 Heading Structure

**Location**: §5.3–5.4

§5.3 ("High-Frequency Oscillatory Ventilation: A Technology in Search of an Indication") is a specific technology subsection, while §5.4 ("The Follow-up Gap: Why It Matters") is a synthesis subsection. Consider renaming §5.4 to better indicate its synthesis role, e.g., "### 5.4 Synthesis: The Ventilation Follow-up Gap."

### SI-R5-4: NEUROSIS Trial 5-Year Follow-up — Redundant Across Sections

**Location**: §3.3 (L167–168)

The NEUROSIS 5-year follow-up data is mentioned both in §3.3 (inhaled corticosteroids) and in §11.8 (attrition bias). The §3.3 mention says "though the follow-up rate was below 60% and imprecision limits definitive conclusions" while §11.8 says "follow-up rates below 60%, with no systematic analysis of how attrition may have affected the estimated treatment effect." These are complementary but slightly redundant — consider cross-referencing between them.

---

## 改进优先级

### 第一优先级（<30分钟）
1. **MF-R5-1**: 在§5.4添加2-3句引导段落
2. **MF-R5-2**: 在§2.2添加OR/HR度量差异说明
3. **CA-R5-2**: 在§12添加"Victorian cohort"引用[9]

### 第二优先级（<30分钟）
4. **NC-R5-1**: 验证§5.2的extubation failure上下文
5. **CA-R5-1**: 在§12 "What We Know"添加支撑引用
6. **SI-R5-1**: 修正§2.1和§5.1的括号内断句

### 第三优先级（建议执行）
7. **NC-R5-2**: 减少"1.4% (8 of 590)"重复次数
8. **SI-R5-2~4**: 字数优化、标题调整、交叉引用

---

## 验证命令

```bash
# 验证MF-R5-1: §5.4有正文段落
sed -n '247,252p' manuscript/jitc_submission.md
# 期望: L248-250包含正文，非纯空行

# 验证MF-R5-2: OR/HR说明已添加
grep -n "hazard ratio derives from" manuscript/jitc_submission.md
# 期望: 返回匹配行

# 验证CA-R5-2: Victorian cohort已加引用
grep -n "Victorian cohort.*\[9\]" manuscript/jitc_submission.md
# 期望: 返回匹配行
```

---

## 审稿后预估

| 如果只修复第一优先级 | 如果修复全部 |
|:--:|:--:|
| 9/10 | 9+/10 |

The manuscript is in excellent shape. The R5 findings are all in the "polish" category — structural refinements, metric clarifications, and citation hygiene. Once addressed, the manuscript should be ready for journal submission.

---

*审稿完成: 2026-06-06 | 6维度深度审查 + R4完整性验证 + 逐节深读*
