# Synthesis Reasoning Rules

> **用途**: Agent 7 全部 7 个步骤的工作流规则
> **原则**: 所有推理必须有显式 trace log。所有推断必须标注不确定性等级。所有假设必须触发文献检索。无黑箱操作。

---

## Step 1: 跨干预比较矩阵规则

见 `harness/cross-intervention-matrix.md`

### 输入
- `knowledge/domain-ontology.md` — 干预清单 + 空白分级 + 紧迫性评分
- `current_manuscript` — 当前草稿 (所有章节，由 Step R0 解析)

### 执行约束
- 必须比较所有干预对 (N×(N−1)/2 pairs for N interventions)
- 对每个 G0 vs G3/G4 的对 → 强制生成定性比较段落
- 对每个 ADOPTION_PARADOX → 强制标记
- 输出矩阵到 `harness/cross-intervention-output.md`

---

## Step 2: 交互分析与假设循环规则

### 2.1 已知交互处理
- 从 domain ontology interaction map 提取所有 KNOWN 交互
- 验证稿件中是否已提及这些交互
- 如未提及 → 在适当位置插入交互讨论，引用已知文献

### 2.2 未知交互的机制推理协议

对每个 UNEXPLORED 交互对:

1. **机制推断** (基于已知病理生理):
   - 写出推断链的每一步: "Intervention A affects pathway X → Pathway X intersects with pathway Y → Intervention B affects pathway Y → Therefore combined A+B might..."
   - 每一步必须引用已知文献支持（如果是已知通路）
   - 标注不确定性: HIGH_CERTAINTY (多条独立通路支持) / MODERATE (单条通路) / LOW (间接推测)

2. **定向文献检索**:
   - 构建检索式: `"[intervention_A_name] AND [intervention_B_name] [mechanism_keyword]"`
   - 搜索 PubMed / Europe PMC
   - 记录: 检索式、命中数、是否发现直接证据

3. **检索结果处理**:
   - **找到直接证据** → 标注 `✅ VERIFIED` → 引用文献 → 插入稿件
   - **找到间接证据** → 标注 `⚠️ PARTIALLY_SUPPORTED` → 引用文献 + 注明间接性 → 插入稿件
   - **未找到任何证据** → 标注 `⚠️ HYPOTHESIS` → 在稿件中插入假设段落

### 2.3 假设插入格式 (MANDATORY)

每个 HYPOTHESIS 必须按以下格式插入:

```markdown
> **[Hypothesis: mechanism-based inference, not empirically tested.]**
> Based on the known role of [pathway A] in [intervention B]'s mechanism ([citation]), and the interaction between [pathway A] and [pathway C] ([citation]), it is plausible that combined [intervention A] + [intervention B] may [predicted effect]. However, a directed literature search for "[search query]" returned [N] results, none of which directly tested this interaction (search date: YYYY-MM-DD). This hypothesis requires empirical validation before it can inform clinical practice.
```

### 2.4 假设循环记录格式

所有假设循环必须记录到 `harness/synthesis-reasoning-log.md`:

```markdown
## Hypothesis H[N]: [short description] — YYYY-MM-DD

### Inference Chain
1. [Step 1 of reasoning] — Supported by: [citation or "general pathophysiology"]
2. [Step 2 of reasoning] — Supported by: [citation or "general pathophysiology"]
...

### Directed Search
- Search query: "[exact query]"
- Databases searched: PubMed, Europe PMC
- Search date: YYYY-MM-DD
- Results: N hits

### Conclusion
- Status: ✅ VERIFIED / ⚠️ PARTIALLY_SUPPORTED / ⚠️ HYPOTHESIS
- Supporting citation (if found): [PMID]
- Inserted in manuscript at: [section/paragraph]
```

---

## Step 3: 临床决策框架生成规则

见 `harness/clinical-decision-framework.md`

### 3.1 决策节点识别
- 从稿件中提取所有"决策点"——临床医生需要在多个选项中选择的情境
- 每个决策节点: 临床情境 → 可用选项 → 证据状态 → 暂定指导

### 3.2 框架格式要求
- 使用条件分支结构 (if-then)
- 每个分支标注证据等级和不确定性
- 不使用"should"；使用"may consider" / "might guide" / "could inform"
- 必须包含免责声明: "This framework is provisional. It is based on the best available evidence as of [date] and should be revised as new data emerge."

### 3.3 禁止行为
- ❌ 生成未经文献验证的治疗路径
- ❌ 将机制推理伪装成循证建议
- ❌ 忽略"无数据"选项（如："目前没有数据支持 A 优于 B；如果本地条件允许，两者均为合理选择"）
- ❌ 使用绝对的"should" / "must" 语言（除非有 strong guideline recommendation 支撑）

---

## Step 4: 论证多样性扫描规则

见 `harness/argument-diversity-enforcement.md` (Module C 共享)

### 4.1 Pattern A 检测 (优雅空洞)

正则模式 (用于 Agent 7 扫描):

```
(Although|While|Despite).{0,100}(evidence|data|studies|literature).{0,100}(limited|incomplete|scarce|lacking|absent).{0,200}(more|further|additional).{0,50}(research|studies|trials|data|follow-up).{0,50}(needed|required|necessary|warranted)
```

### 4.2 处理规则
- 扫描全稿 → 计数 Pattern A 匹配
- 0-2 次: ✅ 可接受
- 3-4 次: ⚠️ 标记 → 为第 3+ 次提供替换方案
- ≥5 次: ❌ MUST FIX → 强制转换第 3+ 次为其他论证类型

### 4.3 替换策略
对每个标为 MUST FIX 的 Pattern A 实例:
1. 识别该处的具体证据空白
2. 从以下替代方案中选择最合适的:
   - **数据论证**: 用具体数字说明空白的量级
   - **机制论证**: 基于病理生理解释为什么这个空白很重要
   - **比较论证**: 对比另一个干预的数据状况
   - **临床后果论证**: 描述这个空白对患者的具体含义
   - **历史轨迹论证**: 追踪证据如何演变以及趋势指向何方

---

## Step 5: 时间演变标注规则

见 `harness/time-annotation.md` (Module D 共享)

### 5.1 平面时间线检测
- 对每个章节: 提取所有引用文献的出版年份
- 如果年份跨度 >20 年但无任何时间框架语言 → `⚠️ FLAT_TIMELINE`
- 标记所有 FLAT_TIMELINE 章节

### 5.2 演变小结格式
对每个 FLAT_TIMELINE 章节，在章节末尾插入:

```markdown
> **Evolution of Evidence**: The evidence base for [intervention] spans from [earliest year] to [latest year], a period during which [contextual changes: e.g., "neonatal survival for infants <28 weeks increased from ~50% to >90%"]. Early studies ([earliest years]) reflect a fundamentally different clinical context — including [specific differences in standard care, diagnostic criteria, or patient population]. Contemporary data ([latest years]) suggest [summary], though [remaining uncertainties]. Readers should interpret the older literature as historical context rather than current effect estimates.
```

---

## Step 6: 覆盖完整性验证规则

### 6.1 稿件 vs 本体对比
- 从 `knowledge/domain-ontology.md` 的 Intervention Inventory 提取所有干预
- 扫描稿件，对每个干预: 是否在稿件中被讨论？ YES / NO / SUPERFICIAL (仅提及但未实质讨论)

### 6.2 覆盖差距报告
对每个 NO 或 SUPERFICIAL 的干预:
- 从领域本体提取其 priority score
- 如果 priority ≥4 → ⚠️ COVERAGE_GAP: 临床重要干预在稿件中缺失或只有表面讨论
- 如果 priority ≥7 → ❌ CRITICAL_GAP: 必须处理

### 6.3 处理
- CRITICAL_GAP → 建议在稿件中新增讨论（如果仍在范围内）或在 Limitations 中显式声明排除原因
- COVERAGE_GAP → 在 "Missing Perspectives" 段落中列出
- 输出到 `harness/coverage-gap-report.md`

---

## Step 7: 稿件增强规则

### 7.1 插入溯源标签 (MANDATORY)

所有 Agent 7 插入的内容必须使用 HTML comment 标记来源:

| 插入来源 | 标签 |
|---------|------|
| Step 1: 跨干预比较 | `<!-- SYNTH:S1 CROSS_COMPARISON -->` |
| Step 2: 已验证交互 | `<!-- SYNTH:S2 VERIFIED -->` |
| Step 2: 假设 | `<!-- SYNTH:S2 HYPOTHESIS -->` |
| Step 3: 临床决策框架 | `<!-- SYNTH:S3 DECISION_CONTEXT -->` |
| Step 4: 论证替换 | `<!-- SYNTH:S4 PATTERN_REPLACEMENT -->` |
| Step 5: 时间演变 | `<!-- SYNTH:S5 TIME_EVOLUTION -->` |
| Step 6: 覆盖差距 | `<!-- SYNTH:S6 COVERAGE_GAP -->` |

### 7.2 不可覆盖草稿
- Agent 7 的插入是**增量的**——在原草稿上增加内容，不删除或改写原文
- Agent 7 不替代 Agent 3（写作）或 Agent 4（审校）——它只在写作和审校之间进行合成增强
- 如果某处需要改写（非新增），标记为建议，留给 Agent 4 审校时处理

---

## Gate 9: Synthesis Quality

执行 Agent 7 全部 7 步后自动检查:

| 检查项 | 通过标准 |
|--------|---------|
| 跨干预矩阵 | 所有干预对已比较 |
| 假设可追溯 | 每个假设在 `synthesis-reasoning-log.md` 中有完整 trail |
| 论证多样性 | Pattern A 次数 ≤ 3 |
| 时间标注 | 所有 Band 3+ 章节有时间演变小结 |
| 覆盖差距 | `coverage-gap-report.md` 已生成 |
| 无假设伪装事实 | 0 个未标注的假设 |
