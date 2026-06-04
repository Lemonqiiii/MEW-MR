# 医学与生物学综述写作项目

## 项目身份
- **目标**: 撰写高质量的医学/生物学英文综述论文
- **领域**: 医学与生物学（肿瘤学、免疫学、神经科学、遗传学等）
- **当前阶段**: 初始化
- **目标期刊**: 待定

## 核心规则
1. 所有论文笔记必须遵循 `docs/papers/template.md` 模板
2. 每完成一个工作阶段或会话结束前，必须调用**编码Agent**记录增量进展
3. 文献搜索优先使用 PubMed / Semantic Scholar / Europe PMC
4. 综述正文使用**英文**写作，项目文档和内部交流使用**中文**
5. 所有引用必须包含 PMID 或 DOI，确保可追溯
6. 做出范围、方法、目标期刊等关键决策时，记录到 `memory/decisions.md`

## Tier 2 资源（按需加载）
以下文件在需要时读取，不要全部加载到会话：
- **项目状态**: `memory/project-status.md` — 当前阶段、进度百分比、文献统计
- **当前聚焦**: `memory/active-focus.md` — 本次综述的具体研究方向、PICO 框架
- **子Agent定义**: `memory/agent-specializations.md` — 各子Agent的触发条件与prompt
- **功能清单**: `features/FEATURE_LIST.md` — 任务清单（优先级排序）
- **关键发现**: `memory/key-findings.md` — 已从文献中提取的核心论点
- **决策记录**: `memory/decisions.md` — 选刊、范围界定等方法决策

## Tier 3 资源（主动检索）
Agent 在需要文献背景时主动搜索以下路径：
- **文献索引**: `docs/index.md` → 按主题/方法/年份导航 → `docs/papers/[topic]/`
- **方法论**: `docs/methods/` — 系统综述、荟萃分析、统计方法指南
- **术语表**: `docs/glossary.md` — 常用医学术语与缩写

## 当前任务
读取 `features/FEATURE_LIST.md` 获取最高优先级的未完成任务。

## 推荐会话流程
1. 读取 `memory/project-status.md` 了解当前项目状态
2. 读取 `features/FEATURE_LIST.md` 选择下一个任务
3. 执行任务（搜索文献 / 分析论文 / 撰写草稿 / 审校）
4. 会话结束前调用**编码Agent**更新进度和项目状态
