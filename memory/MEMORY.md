# Memory 索引

本目录包含 Tier 2 结构化记忆文件。以下文件在 Agent 需要时按需加载。

---

- [Agent定义](agent-specializations.md) — 核心 Agent 0-5 完整定义与触发条件
- [Harness架构](harness/architecture.md) — 上下文、检索筛选、质量、评估、安全、投稿、流程演进的分层架构
- [质量关卡](harness/quality-gate.md) — Gate 0-11 检查清单
- [检索筛选协议](harness/search-screening-protocol.md) — 检索式、筛选日志、VPN全文获取、仅摘要降级
- [审稿修回协议](harness/review-revision-protocol.md) — 审稿意见 action log、回复信、修回验证
- [安全策略](harness/safety-policy.md) — 越权检测与严重度分级
- [鲁棒性测试](harness/test-scenarios.md) — L1-L8 输入漂移、上下文路由场景
- [一致性基准](harness/consistency-benchmarks.md) — 两次执行结果对比方法
- [效率度量](harness/metrics.md) — 五维度度量定义
- [投稿合规](harness/submission-compliance.md) — 投稿格式化三阶段工作流
- [期刊格式](harness/journal-profiles.md) — 目标期刊格式参数
- [证据缺口分级](harness/evidence-gap-grading.md) — G0-G4 分级框架
- [证据时间标注](harness/time-annotation.md) — 证据新鲜度衰减规则
- [跨干预比较矩阵](harness/cross-intervention-matrix.md) — 7 维度模板
- [合成推理规则](harness/synthesis-reasoning.md) — 合成 Agent 工作流规则
- [临床决策框架](harness/clinical-decision-framework.md) — 决策框架模板
- [视角切换规则](harness/perspective-switching.md) — 5 种强制视角
- [数据翻译规则](harness/data-translation.md) — RR→ARR/NNT 协议
- [论证多样性规则](harness/argument-diversity-enforcement.md) — Pattern A 检测与转换
- [批判吸收规则](harness/critical-absorption.md) — Cochrane 批判检查
- [否定声称检测](harness/negative-claim-detection.md) — 声称绝对性 vs 文献矛盾检测
- [领域本体模板](knowledge/domain-ontology-template.md) — 干预清单 + 空白分级 + 紧迫性评分模板
- [补救计划](harness/remediation-plan.md) — Agent 失败时的补救策略

---

*使用说明：新项目开始时，需创建 `memory/project-status.md` 和 `memory/active-focus.md` 来记录当前综述状态。*
