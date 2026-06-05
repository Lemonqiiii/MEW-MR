# Memory 索引

本目录包含 Tier 2 结构化记忆文件。以下文件在Agent需要时按需加载。

---

- [项目状态](project-status.md) — 当前综述阶段、进度百分比、文献统计数据
- [当前聚焦](active-focus.md) — 本次综述的具体研究方向、PICO 框架、检索关键词
- [核心发现](key-findings.md) — 已从文献中提取的关键论点和跨文献主题
- [Agent定义](agent-specializations.md) — 四个领域子Agent的触发条件与prompt模板
- [决策记录](decisions.md) — 选刊、范围界定、方法选择等关键决策（论文主题）
- [流程演进](workflow-evolution.md) — 项目运行歧义的商讨结果与文件修改记录（项目机制）

---

## 加载策略
- **自动**: 编码Agent每次运行加载 `project-status.md`
- **按需**: 文献搜索Agent加载 `active-focus.md`；写作Agent加载 `key-findings.md`
- **审计**: 需要回顾决策背景时加载 `decisions.md`
