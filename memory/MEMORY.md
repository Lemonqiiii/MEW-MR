# Memory 索引

本目录包含 Tier 2 结构化记忆文件。以下文件在Agent需要时按需加载。

---

- [项目状态](project-status.md) — 当前综述阶段、进度百分比、文献统计数据
- [当前聚焦](active-focus.md) — 本次综述的具体研究方向、PICO 框架、检索关键词
- [核心发现](key-findings.md) — 已从文献中提取的关键论点和跨文献主题
- [Agent定义](agent-specializations.md) — 四个领域子Agent的触发条件与prompt模板
- [决策记录](decisions.md) — 选刊、范围界定、方法选择等关键决策（论文主题）
- [流程演进](workflow-evolution.md) — 项目运行歧义的商讨结果与文件修改记录（项目机制）
- [领域本体](../knowledge/domain-ontology.md) — 自动构建的干预清单 + 证据空白分级 + 临床紧迫性评分 (Module A)
- [证据缺口分级框架](../harness/evidence-gap-grading.md) — G0-G4 分级定义 (Module A)
- [临床紧迫性评分](../harness/priority-scoring.md) — 4 维度评分标准 (Module A)
- [证据时间标注](../harness/time-annotation.md) — 证据新鲜度衰减规则 (Module D)
- [跨干预比较矩阵](../harness/cross-intervention-matrix.md) — 7 维度模板 (Module B)
- [合成推理规则](../harness/synthesis-reasoning.md) — Agent 7 工作流规则 (Module B)
- [临床决策框架](../harness/clinical-decision-framework.md) — 决策框架模板 (Module B)
- [视角切换规则](../harness/perspective-switching.md) — 5 种强制视角 (Module C)
- [数据翻译规则](../harness/data-translation.md) — RR→ARR/NNT 协议 (Module C)
- [论证多样性规则](../harness/argument-diversity-enforcement.md) — Pattern A 检测与转换 (Module C)
- [批判吸收规则](../harness/critical-absorption.md) — Cochrane 批判检查 (Module C)
- [绝对否定声称检测](../harness/negative-claim-detection.md) — 声称绝对性 vs 文献矛盾检测 (Phase 7.6b)
- [投稿合规规则](../harness/submission-compliance.md) — Agent 8 三阶段工作流规范 (Phase 7.6a)
- [期刊格式模板](../harness/journal-profiles.md) — 目标期刊格式参数 (Phase 7.6a)
- [Harness架构](../harness/architecture.md) — 上下文、检索筛选、质量、评估、安全、投稿、流程演进的分层架构
- [检索筛选协议](../harness/search-screening-protocol.md) — 检索式、筛选日志、VPN全文获取、仅摘要降级、Gate Search/Gate Screening
- [审稿修回协议](../harness/review-revision-protocol.md) — 审稿意见 action log、回复信、修回验证、Gate Revision
- [鲁棒性测试场景](../harness/test-scenarios.md) — L1-L8 输入漂移、上下文路由、VPN、provenance、安全场景
- [一致性基准](../harness/consistency-benchmarks.md) — Bench-001/008 核心能力基准

---

## 加载策略
- **自动**: 编码Agent每次运行加载 `project-status.md`
- **按需**: 文献搜索Agent加载 `active-focus.md`；写作Agent加载 `key-findings.md`
- **审计**: 需要回顾决策背景时加载 `decisions.md`
