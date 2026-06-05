# 医学与生物学综述写作项目

## 项目身份
- **目标**: 撰写高质量的医学/生物学英文综述论文
- **领域**: 肿瘤学 / 免疫学（肺癌免疫治疗）
- **综述主题**: Mechanisms of Immunotherapy Resistance in Squamous Cell Carcinoma of NSCLC
- **当前阶段**: revision（初稿完成，内部审校通过，待最终定稿）
- **目标期刊**: JITC (Journal for ImmunoTherapy of Cancer)
- **初稿统计**: 8,969词正文 + 246词摘要 | 7章节 | 41引用 | 1图2表

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
| `就绪` `好了` `done` | 手动操作完成 | (上下文相关) |
| `状态` `进度` | 查看项目状态 | (展示当前状态) |
| `帮助` `?` `help` | 显示命令和当前阶段 | (展示帮助) |
| `下一步` `next` | 自动判断并建议下一步 | (读取状态后建议) |
| `主题` | 确定综述主题 | (引导填写 active-focus.md) |
| `gen` `生成` | 重新生成Word文档+自检 | 运行 gen_word_full.py |

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
- **子Agent定义**: `memory/agent-specializations.md`
- **功能清单**: `features/FEATURE_LIST.md`
- **关键发现**: `memory/key-findings.md`
- **决策记录**: `memory/decisions.md`

## Tier 3 资源（主动检索）
- **文献索引**: `docs/index.md` → `docs/papers/[topic]/`
- **方法论**: `docs/methods/`
- **数据库目录**: `docs/methods/database-coverage.md`
- **术语表**: `docs/glossary.md`

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

### 图表纪律
- 图表编号必须在源文件中全局唯一
- 删除图表 = 删除所有正文引用 + 更新Title Page声明 + 重新编号
- 自检必须同时验证：正文引用编号、图片标题文字、Word Caption

### 喉鳞癌过滤规则
- 筛选时必须显式排除: laryngeal, head and neck, oral, esophageal, cutaneous, cervical, thymic squamous
- "LSCC" 缩写在纳入前必须验证为 lung squamous cell carcinoma

### 引用解析规则
- 所有引用计数脚本必须处理三种格式: `[N]`, `[N,M]`, `[N-M]`

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

### 自检嵌入
`gen_word_full.py` 每次生成后自动运行 8 项自检：
Figure refs, Table refs, Bad refs, Body citations, Images embedded, Headings, Word count, Refs used

## 错误模式库 (每遇到一次新错误追加)
- `引用嫁接`: 训练数据知识 + 不匹配的引用 → 回退
- `编号漂移`: 删除图表后手工重编号 → 自动化自检
- `压缩丢失`: 节省token压缩段落 → 用源文件解析
- `范围遗漏`: [8-10] 不被正则匹配 → 展开范围

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
3. **需要用户手动操作时** → 生成清单，等待用户说"就绪"
4. **每完成2-3个子任务** → Agent主动建议"快记"保存进度
5. **阶段结束** → 展示 Phase结束检查清单 → 提示用户说"编码"
6. **每次修改稿件后** → 运行 Gate 4/5 自检确认无回归
7. **每次生成Word后** → 确认 gen_word_full.py 8项自检全部通过
