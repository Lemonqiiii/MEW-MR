# 医学与生物学综述写作项目

## 项目身份
- **目标**: 撰写高质量的医学/生物学英文综述论文
- **领域**: 新生儿医学 / 呼吸病学 / 全生命周期流行病学
- **综述主题**: NRDS 生命早期干预的远期影响（全生命周期视角）
- **当前阶段**: Phase 7 — AI 写作缺陷系统性修复 (Modules A-D 已部署，待端到端测试)
- **目标期刊**: Pediatric Research (IF ~3, Springer Nature)
- **上一轮**: LUSC ICI耐药综述已归档至 `archive/lusc-2025/`（8,969词 | 41引用 | 1图2表 | JITC）

## 交互原则 (最高优先级)

### 启动行为
**每次会话开始时**，自动执行：
1. 读取 `memory/project-status.md` — 了解当前阶段
2. 读取 `features/FEATURE_LIST.md` — 找到第一个未完成任务
3. **交叉验证**: 如果 CLAUDE.md 中"当前阶段"与 project-status.md 的 phase 不一致 → 以 project-status.md 为准，并提示用户"CLAUDE.md 阶段字段可能过时"
4. 用**一句话**告诉用户当前状态，然后用**简洁的选项列表**告诉用户接下来可以做什么

示例:
```
📍 Phase 6 revision | 下一步: 最终定稿与投稿准备

你可以这样说:
  1 或 写作    → 修改稿件内容
  5 或 审校    → 审校检查
  gen          → 重新生成Word文档
  状态          → 查看详细项目状态
  编码          → 保存当前进度
  帮助          → 查看所有可用命令
```

### 命令极简化
用户只需要用**最少的字**触发动作。Agent 在看到简短指令时，**先确认理解再执行**：

| 用户说 | Agent 理解为 | 触发哪个Agent |
|--------|------------|-------------|
| `1` `搜索` `搜` | 文献搜索 | Agent 1 文献搜索 |
| `2` `筛选` `筛` | 文献筛选 | Agent 6 筛选Agent |
| `3` `分析` | 分析论文 | Agent 2 论文分析 |
| `4` `写作` `写` | 综述写作 | Agent 3 综述写作 |
| `5` `审校` `审` | 审校 | Agent 4 审校Agent |
| `6` `编码` | 完整编码（进度+效率+安全+Git） | Agent 0 编码Agent |
| `快记` `记` | 轻量编码（仅进度+Git，不含审计） | Agent 0 轻量模式 |
| `7` `评估` `评` | 质量评估 | Agent 5 评估Agent |
| `8` `合成` `synthesis` | 合成推理（跨干预比较+假设循环+决策框架+论证多样性） | Agent 7 合成Agent |
| `9` `投稿` `submit` | 投稿格式化（清理+转化+合规检查） | Agent 8 投稿Agent |
| `就绪` `好了` `done` | 手动操作完成 | (上下文相关) |
| `状态` `进度` | 查看项目状态 | (展示当前状态) |
| `帮助` `?` `help` | 显示命令和当前阶段 | (展示帮助) |
| `下一步` `next` | 自动判断并建议下一步 | (读取状态后建议) |
| `主题` | 确定综述主题 | (引导填写 active-focus.md) |
| `gen` `生成` | 重新生成Word文档+自检 | 运行 gen_word_full.py |
| `教训` `lesson` | 记录流程缺陷并修改项目文件 | 根因分析 → 修改项目文件 → 追加演进记录 |

### 确认规则
- 用户输入简略指令时 → **先一句话确认理解**，再执行
- 禁止在确认前执行任何写操作或网络请求
- 确认格式: `理解为: [你要做什么]。确认吗？(直接回复"是"或"1"开始)`

## 核心规则
1. 所有论文笔记遵循 `docs/papers/template.md` 模板
2. 每完成一个工作阶段，调用**编码Agent**（用户说"编码"或"6"）
3. 文献搜索优先使用 PubMed / Semantic Scholar / Europe PMC
4. 综述正文使用**英文**写作，项目文档和内部交流使用**中文**
5. 所有引用必须包含 PMID 或 DOI
6. 做出关键决策时记录到 `memory/decisions.md`
7. 仅摘要论文 ≤ 纳入总数 20%，核心论点不得基于仅摘要论文

## Tier 2 资源（按需加载）
- **项目状态**: `memory/project-status.md`
- **当前聚焦**: `memory/active-focus.md`
- **子Agent定义**: `memory/agent-specializations.md` — Agent 0-7 完整定义 (Phase 7 新增 Agent 7 合成Agent)
- **功能清单**: `features/FEATURE_LIST.md`
- **关键发现**: `memory/key-findings.md`
- **决策记录**: `memory/decisions.md`
- **流程演进**: `memory/workflow-evolution.md`

## Tier 3 资源（主动检索）
- **文献索引**: `docs/index.md` → `docs/papers/[topic]/`
- **方法论**: `docs/methods/`
- **数据库目录**: `docs/methods/database-coverage.md`
- **术语表**: `docs/glossary.md`
- **领域本体**: `knowledge/domain-ontology.md` — 自动构建的干预清单 + 证据空白分级 + 临床紧迫性评分 (Module A)
- **证据缺口分级**: `harness/evidence-gap-grading.md` — G0-G4 分级框架 (Module A)
- **证据时间标注**: `harness/time-annotation.md` — 证据新鲜度衰减规则 (Module D)
- **跨干预比较矩阵**: `harness/cross-intervention-matrix.md` — 7 维度模板 (Module B)
- **合成推理规则**: `harness/synthesis-reasoning.md` — Agent 7 工作流规则 (Module B)
- **临床决策框架**: `harness/clinical-decision-framework.md` — 决策框架模板 (Module B)
- **视角切换规则**: `harness/perspective-switching.md` — 5 种强制视角 (Module C)
- **数据翻译规则**: `harness/data-translation.md` — RR→ARR/NNT 协议 (Module C)
- **论证多样性规则**: `harness/argument-diversity-enforcement.md` — Pattern A 检测与转换 (Module C)
- **批判吸收规则**: `harness/critical-absorption.md` — Cochrane 批判检查 (Module C)
- **绝对否定声称检测**: `harness/negative-claim-detection.md` — 声称绝对性 vs 文献实际内容矛盾检测 (Phase 7.6b)
- **投稿合规规则**: `harness/submission-compliance.md` — Agent 8 三阶段工作流规范 (Phase 7.6a)
- **期刊格式模板**: `harness/journal-profiles.md` — 目标期刊格式参数 (Phase 7.6a)

## 写作纪律 (2026-06-04 编码)

### 单源真理原则
- **稿件内容**的唯一源文件是 `manuscript/jitc_submission.md`
- Word 文档由 `scripts/gen_word_full.py` 自动生成，该脚本只负责格式化，**不包含内容**
- 任何修改：先改源文件 → 运行生成器 → 运行自检

### 引用铁律
- 每条声明必须有至少一篇引用文献的**摘要**直接支撑（全文支撑更好）
- **禁止**从训练数据中提取知识贴到不相关的引用上
- 扩展段落前必须先验证引用-声明配对
- 引用非鳞NSCLC文献支撑LUSC论点时，必须加限定语

### 引用范围纪律 (2026-06-05 新增)

每篇论文在纳入时已被分配**引用范围标签**（见 Agent 6 筛选Agent 的引用范围矩阵）。写作和审校时必须遵守：

**绝对禁止**:
- ❌ 用 G 类（叙述性综述）作为声明的**主引用**——综述不产生新数据，引用原始论文
- ❌ 用 I 类（病例报告）**单独支撑**一条通用性声明——单病例不能代表群体
- ❌ 用 E 类（纯生信）支撑**因果机制声明**——相关性 ≠ 因果性，必须用 A/B/C/D 类

**需要加限定语**:
- ⚠️ E 类支撑的声明 → 必须加 "is associated with" / "correlates with"（非 "causes" / "drives"）
- ⚠️ D 类单独支撑机制声明 → 必须加 "clinical evidence suggests" / "translational data indicate"
- ⚠️ G 类作为辅助引用 → 标注 "(reviewed in [N])" 而非作为主引用编号

**审校时逐条核查**: Agent 4 在 Step 6（自然度扫描后）追加 Step 7 引用范围合规检查，对照每篇论文的类型标签验证其引用方式是否越权。

### 图表纪律
- 图表编号必须在源文件中全局唯一
- 删除图表 = 删除所有正文引用 + 更新Title Page声明 + 重新编号
- 自检必须同时验证：正文引用编号、图片标题文字、Word Caption

### 喉鳞癌过滤规则
- 筛选时必须显式排除: laryngeal, head and neck, oral, esophageal, cutaneous, cervical, thymic squamous
- "LSCC" 缩写在纳入前必须验证为 lung squamous cell carcinoma

### 引用解析规则
- 所有引用计数脚本必须处理三种格式: `[N]`, `[N,M]`, `[N-M]`

### 语言自然度 (2026-06-05 新增)

**核心洞察**: "自然"无法被正面规定（规定出来的东西恰是自然的反面）。但僵硬可以被精确检测。**自然 = 不僵硬 = 高方差**。以下反模式是僵硬的具体来源，审校Agent 在每次审校时逐条检查。

#### 反模式 1: 名词化链 (Nominalization Chain)
**检测**: 单个句子中 ≥ 3 个动作被转为名词（-tion, -ment, -ence, -sis, -ance 结尾 + "of" 结构）
**示例**: "The administration of ICIs imposes potent immunologic selective pressure on genetically heterogeneous tumor cell populations, driving a Darwinian process of clonal evolution" → 6 个名词化动作堆积，无呼吸点
**方向**: 打断名词化链 → 拆成两句，至少让一个动作回归动词
**级别**: Nice to Have（单句 ≥ 5 个 → Must Fix）

#### 反模式 2: 过渡词单调 (Transition Monotony)
**检测**: 连续 ≥ 3 段以同类型过渡词开头（"Furthermore / Moreover / In addition" 归为"追加型"；"However / In contrast / Conversely" 归为"转折型"；"Consequently / Therefore / Thus" 归为"因果型"）
**方向**: 交替过渡词类型，或用具体陈述代替过渡词
**级别**: Must Fix

#### 反模式 3: 句子长度均质 (Sentence-Length Entropy)
**检测**: 段落内所有句子均在 22-35 词之间（无短句 < 12 词，无长句 > 35 词）
**方向**: 每段至少 1 句短句（< 12 词）用于节奏打断；关键论点可用短句独立成行以强调
**示例短句**: "This matters. Because KEAP1 mutation alone can doom an immune response."
**级别**: Nice to Have

#### 反模式 4: 被动语态堆积 (Passive Voice Stacking)
**检测**: 连续 ≥ 4 句均为被动语态（be + past participle）
**方向**: 将连续被动句中的至少 1 句转为主动语态。被动语态本身无错——连续使用才产生僵硬感
**级别**: Nice to Have

#### 反模式 5: 段落结构模板化 (Template Paragraph)
**检测**: ≥ 3 个连续段落使用完全相同结构（如：主题句 → 证据A → 证据B → 证据C → 总结句）
**方向**: 变化段落结构——部分段落以问题开头，部分以数据开头，部分以争议开头
**级别**: Nice to Have

#### 反模式 6: 空洞强调词 (Empty Intensifiers)
**检测**: "Interestingly," "Notably," "Of note," "It is worth noting that," "Importantly," "Of particular importance," "Surprisingly,"
**方向**: **直接删除**。被强调的内容本身应有说服力，不需要前置词告诉你它"有趣"
**级别**: 删除类 — Must Fix（直接删，不留痕）

### 语言自然度检查流程

审校Agent 在每次审校时，在原有 5 步基础上附加：

**Step 6 — 自然度扫描**:
1. 逐段扫描 6 个反模式
2. 标记命中位置（段落号 + 反模式编号）
3. 对 Must Fix 项给出修改建议
4. 统计"自然度得分"：`通过段落数 / 总段落数`（通过 = 无反模式1-5命中，反模式6直接删除不计分）

**自然度目标**: ≥ 80% 段落通过（Phase 6 当前；Phase 7+ 提升至 ≥ 90%）

## 质量关卡 (每次 Phase 结束时强制执行)

### Gate 4: 引用-声明验证
```bash
python3 -c "
验证脚本: 提取所有 [N] 引用 → 查 PMID 摘要 → 关键词匹配
通过标准: ≥90% 声明可直接验证"
```

### Gate 5: 格式完整性
```bash
python3 -c "
检查项:
1. Figure refs ∈ {已保留集合}
2. Table refs ∈ {已保留集合}  
3. 正文引用 == 列表引用 (含范围展开)
4. Word 文档: 标题层级 + 段间距 + 图片嵌入数"
```

### Gate 6: 引用范围合规 (2026-06-05 新增)
```bash
审校Agent Step 7 自动执行:
1. 逐条机制声明 → 验证主引用为 A/B/C 类
2. 扫描 G 类引用 → 验证未被用作主引用
3. 扫描 I 类引用 → 验证未单独支撑通用声明
4. 扫描 E 类引用 → 验证声明含相关性限定语
通过标准: 0 条 MUST FIX 违规
```

### Gate 7: 领域本体完整性 (2026-06-06 新增 — Module A)
```bash
Agent 1 Step 7 自动执行:
1. 干预清单交叉对照 ≥2 指南 → 覆盖率 ≥90%
2. 所有干预分配 G0-G4 空白分级 → 100% 覆盖
3. 所有干预计算 Composite Urgency → 100% 覆盖
4. 干预交互地图枚举所有配对 → 100% 枚举
5. 与标准治疗清单交叉对比 → 缺失干预报警已生成
通过标准: 所有检查项通过
```

### Gate 8: 写作前规划完整性 (2026-06-06 新增 — Module D)
```bash
Agent 3 Steps 0a-0f 自动执行:
1. Priority-Weighted Section Allocation 覆盖所有大纲章节 → 100%
2. 无 priority ≥7 干预分配至 Brief → 0 违规
3. 所有 Band 2+ 引用有限定语计划 → 100%
4. Gap-to-Emphasis 映射覆盖所有 G3-G4 干预 → 100%
5. 覆盖率报告（本体 vs 大纲）已生成 → YES
通过标准: 所有检查项通过
```

### Gate 9: 合成推理质量 (2026-06-06 新增 — Module B)
```bash
Agent 7 全部 7 步执行后自动检查:
1. 跨干预比较矩阵覆盖所有干预对 → 100%
2. 每个假设在 synthesis-reasoning-log.md 中有完整 trail → 100%
3. Pattern A ("推断不是证据→需要更多研究") 次数 → ≤3
4. 所有 Band 3+ 章节有时间演变小结 → 100%
5. coverage-gap-report.md 已生成 → YES
6. 无未标注假设（所有假设显式标注 [Hypothesis]） → 0
通过标准: 所有检查项通过
```

### Gate 10: 增强审校完整性 (2026-06-06 新增 — Module C)
```bash
Agent 4 增强 Pass 1-4 执行后自动检查:
1. 5 种视角切换尝试 ≥ 触发位置的 80% → ≥80% 覆盖
2. 所有 RR 值有 ARR/NNT 或显式 baseline-unknown 标注 → 100%
3. Pattern A ("优雅空洞") 最终计数 → ≤2
4. 每篇被引 ≥2 次的 Cochrane 综述有 ≥1 条批判性限定语 → 100%
5. Cochrane 集中度 ≤60% 或 ≥3 条批判性补充 → YES
通过标准: 所有检查项通过
```

### Gate 11: 投稿就绪 (2026-06-06 新增 — Phase 7.6a)
```bash
Agent 8 三阶段执行后自动检查:
1. HTML 审计标签 → 0 个残留
2. 编辑占位符 → 0 个 [To be completed]/[TBD]
3. 期刊匹配 → MATCH 或已标记不匹配 + 建议替代期刊
4. 完整性 → Author Contributions/Acknowledgements/Funding/Data Availability 均已完成
5. AI 披露 → 根据目标期刊政策存在，或已标记缺失
6. 图表文件 → 所有引用图表存在
7. submission-readiness-report.md 已生成
通过标准: 所有检查项通过
```

### 自检嵌入
`gen_word_full.py` 每次生成后自动运行 8 项自检：
Figure refs, Table refs, Bad refs, Body citations, Images embedded, Headings, Word count, Refs used

## 错误模式库 (每遇到一次新错误追加)
- `引用嫁接`: 训练数据知识 + 不匹配的引用 → 回退
- `编号漂移`: 删除图表后手工重编号 → 自动化自检
- `压缩丢失`: 节省token压缩段落 → 用源文件解析
- `范围遗漏`: [8-10] 不被正则匹配 → 展开范围
- `引用越权` (2026-06-05): E类支撑因果声明 / G类做主引用 → Gate 6 检测
- `类型误判` (2026-06-05): 喉鳞癌/头颈鳞癌被纳入LUSC综述 → Agent 6 Round 0 硬排除
- `Step跳过` (2026-06-05): Agent 跳过门禁步骤（如搜索Agent跳过Step 0数据库评估）→ Agent定义中标记为"不可跳过"
- `优雅空洞` (2026-06-06): 同一论证"推断不是证据→需要更多研究"在全文重复 10-12 次 → Agent 7 Step 4 检测 Pattern A + Agent 4 Post-Pass 3 强制转换
- `沉默失明` (2026-06-06): 稿件系统性遗漏临床重要干预（如 NRDS 咖啡因/维生素A/iNO） → Agent 1 Step 7.2 完整性检查 + Agent 7 Step 6 覆盖验证
- `Cochrane崇拜` (2026-06-06): Cochrane 综述被引用但无批判性讨论 → Agent 4 Post-Pass 4 强制批判检查
- `统计翻译缺失` (2026-06-06): RR 值未转换为 ARR/NNT → Agent 4 Pre-Pass 2 数据翻译检查
- `视角单一` (2026-06-06): 整篇综述仅维持抽象综述者视角 → Agent 4 Pre-Pass 1 视角切换
- `管道表格丢失` (2026-06-06): gen_word_full.py 无 Markdown 管道表格解析逻辑 → 表格在 Word 中渲染为乱码。已修复：新增 `_detect_pipe_table` + `_render_md_table` + `_cell_runs` 函数，支持粗体/斜体、表头着色、斑马条纹
- `Table双重渲染` (2026-06-06): `**Table N.**` marker 触发 PNG 嵌入 + 管道表格触发原生渲染 → Table 在 Word 中出现两次。已修复：marker + 管道表格组合时跳过 PNG，用 marker 文字作原生表格标题
- `度量混用未说明` (2026-06-06): 同一句中混合 OR/HR/RR 未说明度量差异来源 → Agent 4 Step 5 检测 + 写作纪律新增度量一致性规则
- `Cochrane计数未自动更新` (2026-06-06): 参考文献增删后正文中的 Cochrane 百分比/分数未自动重新计算 → 审校流程新增引用计数自动检查步骤
- `绝对否定声称矛盾` (2026-06-06): "no data"等绝对声称与被引文献实际内容矛盾（如 Gibson 2015 报告了成人肺功能但稿件声称 no adult data） → Agent 4 Step 1.5 检测
- `硬编码残留` (2026-06-05): gen_word_full.py 硬编码上一项目标题/图表/关键词 → 已修复：重写为通用版。新增 `scripts/audit_manuscript.py` 在生成Word前做10项检查
- `编辑破坏引用段` (2026-06-05): 增量 Edit 重复插入 `## References` → 使用 `scripts/rebuild_refs.py` 批量重建
- `图表插入时机错误` (2026-06-05): gen_word_full.py 把图表插入到节末尾而非标记位置 → 已修复：改为标记处原地插入。**铁律**: 图表插入位置必须与markdown中的`**Figure/Table N.**`标记位置一致；正文引用必须在标记之前出现（先引用，后插图）
- `regex未匹配闭合标记` (2026-06-05): 图表标记`**Figure N. text.**`中`\*\*$`要求闭合但实际标记不闭合 → gen_word_full.py 所有图表regex已改用`.+`移除`\*\*$`要求

## 流程演进协议 (最高优先级 — 自改进机制)

### 核心原则
项目默认**自治运行**。Agent 在明确场景下自主执行，不确认。仅在达成"歧义升级条件"时才暂停并与用户商讨。**每次商讨的产出是对项目文件的直接代码修改**——修改后，同类歧义不再需要人。

```
自治运行 → 遇到歧义 → 人机商讨 → 修改项目文件 → 同类情况自动处理
```

### 自治边界

**Agent 自主执行（不确认）**：
- 操作有唯一合理路径
- 存在 2-3 个合理路径但差异可控 → 选默认 + 在 commit message 中记录选择理由

**Agent 暂停并升级（发起商讨）**：
- 多个路径且**结果差异重大**（如：纳入/排除一篇核心文献会改变综述结论方向）
- 发现**现有规则矛盾**（如：CLAUDE.md 中两条规则给出相反指导）
- **安全边界模糊**（如：不确定某个 WebFetch 域名是否合规）
- Agent 对最佳路径的**置信度 < 70%**

**升级格式**：
```
⚠️ 需要你的判断：

问题：[一句话描述歧义]

选项 A：[...]
  利：[...]
  弊：[...]

选项 B：[...]
  利：[...]
  弊：[...]

我建议：[推荐选项及理由]
```

### 商讨产出：直接修改项目文件

商讨结束后，Agent **必须**回答两个问题：
1. 这次歧义暴露了项目流程中的**什么缺口**？
2. **修改哪个文件的哪个位置**，能让下次同类歧义被自动处理？

典型修改路径：

| 歧义根源 | 修改目标文件 | 示例 |
|---------|------------|------|
| 命令/触发词理解偏差 | CLAUDE.md 命令表 | 新增触发词、确认条件 |
| Agent 工作流缺失分支 | agent-specializations.md | 新增 Step / if-else 分支 |
| 质量判定阈值不合理 | harness/metrics.md | 调整 L2 评分维度或通过线 |
| 写作/引用规范遗漏 | CLAUDE.md 写作纪律 | 新增纪律条目 |
| 已知错误反复发生 | CLAUDE.md 错误模式库 | 追加检测条件 |
| 安全权限边界模糊 | harness/safety-policy.md | 新增 allow/deny 规则 |
| 项目状态/阶段逻辑出错 | memory/project-status.md | 修正 phase 定义或转换条件 |

**禁止行为**：商讨后仅追加日志而不修改流程文件。日志只是修改的副作用，不是主产物。

### 教训即时捕获 (`教训`)

用户或 Agent 在执行中**随时**发现流程缺陷时：

**触发**：用户说 `教训：[描述]` 或 Agent 发现流程缺陷后主动提议

**工作流**：
1. Agent 分析根因：是哪个文件的哪条规则缺失/错误导致了这个问题？
2. Agent 提议具体的文件修改（改哪个文件、改什么内容）
3. 用户确认 → Agent 执行修改
4. Agent 追加一条精简记录到 `memory/workflow-evolution.md`（指向实际修改的文件和 diff）

**示例**：
```
用户: 教训：上次检索时搜索Agent跳过了 Tier 2 数据库评估，直接进入了 Tier 1

Agent:
  根因: agent-specializations.md 中 Agent 1 的 Step 0（数据库需求评估）
        没有强制性——Agent 可以选择跳过
  提议: 在 Agent 1 工作流开头添加 Step 0 门禁——必须输出数据库清单后才能进入 Step 1
  修改文件: memory/agent-specializations.md + CLAUDE.md 错误模式库追加"Step跳过"
  确认吗？
```

### 演进轨迹记录

`memory/workflow-evolution.md` 每条记录格式：

```
## E###: [简短标题] — YYYY-MM-DD
- **触发**: [什么歧义触发了商讨]
- **根因**: [项目文件中缺失/错误了什么规则]
- **修改**: [改了哪个文件、具体改动]
- **效果**: [下次同类情况的新行为]
```

## 编码Agent双模式 (2026-06-05 修订)

### 轻量编码 (`快记` / `记`) — 每次任务后
**触发**: 用户说"快记"或"记"；或每完成2-3个子任务时Agent主动建议
**执行**:
1. 检查 git 变更状态
2. 读取 `features/FEATURE_LIST.md`，更新已完成任务的勾选状态
3. 更新 `memory/project-status.md` 统计数据（progress_pct、words_written、last_update）
4. 追加 `progress/SESSION_LOG.md` 一条精简记录
5. git add + git commit（结构化message: `[phase] 简短描述`）
**跳过**: 效率数据收集、安全审计（完整编码时执行）

### 完整编码 (`编码`) — 每Phase结束时
**触发**: 用户说"编码"；或Phase结束时Agent主动提示
**执行**: 轻量编码全部内容 + 效率数据收集（metrics-raw.json）+ 安全审计 + MILESTONES更新

## Phase结束检查清单 (2026-06-05 新增)

每个Phase结束时，Agent **必须主动展示**以下检查清单：

```
📍 Phase [X] 即将完成。请确认以下检查项：

  □ 编码Agent已记录本Phase进度？  → 说"编码"或"6"
  □ SESSION_LOG已追加本次会话？    → 编码Agent自动完成
  □ MILESTONES已更新？              → 编码Agent自动完成
  □ Gate [N] 已通过？              → 检查 harness/quality-gate.md
  □ Git已提交本Phase变更？          → 编码Agent自动完成
  □ gen_word_full.py 自检通过？    → 说"gen"重新生成验证

建议执行: "编码" 保存所有进度。
```

## 会话流程
1. **启动** → 交叉验证 CLAUDE.md ↔ project-status.md 一致性 → 显示状态 + 选项
2. **用户选择** → Agent 确认 → 执行
3. **遇到歧义** → 见"流程演进协议" → 暂停升级 → 商讨 → 修改项目文件 → 继续
4. **发现流程缺陷** → 用户或Agent说"教训" → 根因分析 → 修改项目文件 → 追加演进记录
5. **需要用户手动操作时** → 生成清单，等待用户说"就绪"
6. **每完成2-3个子任务** → Agent主动建议"快记"保存进度
7. **阶段结束** → 展示 Phase结束检查清单 → 提示用户说"编码"
8. **每次修改稿件后** → 运行 Gate 4/5/6 自检确认无回归
9. **每次生成Word后** → 确认 gen_word_full.py 8项自检全部通过

---

## 增量审校与版本管理 (2026-06-06 新增)

### 审校反馈处理协议

当收到审校报告（审校Agent 或外部评审）时，按以下流程处理：

1. **读取审校报告** → 确认所有问题项及其严重程度（MUST FIX / 数值修正 / 限定语 / 建议）
2. **逐项修改** → 按优先级顺序：MUST FIX → 数值修正 → 限定语 → 建议改进
3. **自行复查** → 用 REVISION_MAP.md 交叉验证所有项均已修复
4. **更新版本记录** → 追加 CHANGELOG.md 和 REVISION_MAP.md
5. **递增版本号** → 更新稿件 HTML 注释中的 Revision 编号

### 版本管理文件

| 文件 | 用途 |
|------|------|
| `manuscript/CHANGELOG.md` | 每个 Revision Round 的完整变更记录 |
| `manuscript/REVISION_MAP.md` | 逐项修复的 line→grep-anchor 映射，供审校Agent快速验证 |
| 稿件 HTML 注释（L2-7） | 嵌入当前版本号、审校来源、变更摘要 |

### 版本号规则

- **R1**: 初稿
- **R2**: 第一次修改
- **R3+**: 每次审校反馈修改后递增
- 每次 Revision 必须：更新 HTML 注释 → 追加 CHANGELOG → 更新 REVISION_MAP

### 自行复查检查清单

每次修改完成后，Agent 必须运行以下检查：

```
📍 增量修改复查 (Revision R<N>):

  □ 所有 MUST FIX grep 验证通过？
  □ 所有数值修正 grep 验证通过（旧值零匹配）？
  □ 所有限定语已插入正确位置？
  □ 所有建议改进已应用？
  □ 无引入新矛盾（跨节交叉检查）？
  □ CHANGELOG.md 已追加本次 Revision？
  □ REVISION_MAP.md 已更新 grep-anchor？
  □ 稿件 HTML 注释 Revision 号已递增？

旧值零匹配验证命令:
  grep -n "旧值1\|旧值2\|旧值3" manuscript/jitc_submission.md
  → 期望输出: No matches found
```

### 防止问题重复的编码约定

1. **数值引用**: 始终包含分子分母 → `42.5% (17 of 40)` 而非 `~50%`
2. **Cochrane 百分比**: 每次引用总数变化时必须重新计算
3. **排除计数**: 必须满足 `初始 − 纳入 = 排除` 的算术约束
4. **年龄表述**: 全文统一一种格式，避免混用 "fifties" / "fifth and sixth decades"
5. **百分比一致性**: 同一统计数据在所有出现位置（Abstract + Impact Statement + 正文 + Conclusions）必须一致
6. **Scope 声明**: 任何在正文中实质性讨论的干预不得在 Scope 中声明 "not covered"
7. **GRADE 评级**: 引用时必须核实 Cochrane 原文，不依赖记忆
