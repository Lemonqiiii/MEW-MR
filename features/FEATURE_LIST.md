# 功能清单

> **使用说明**: 编码Agent每次会话结束时根据进展更新本文件。优先完成当前 Phase 内的所有任务再进入下一 Phase。

---

## Phase 1: 项目初始化

- [x] 1.1 确定综述主题和 PICO 框架（更新 `memory/active-focus.md`）
- [ ] 1.2 确定目标期刊
- [x] 1.3 确定综述类型（叙述性 / 系统综述 / 荟萃分析）

---

## Phase 2: 文献搜索

- [x] 2.1 数据库需求评估（Step 0 门禁）
- [x] 2.2 PubMed / EPMC 检索
- [x] 2.3 Semantic Scholar 补充检索（限流，EPMC 1,009篇已足够）
- [x] 2.4 Europe PMC 补充检索
- [x] 2.5 Tier 2 数据库（ClinicalTrials.gov ✅ + EPMC 补充填补 Embase/Cochrane 盲区；浏览器交互数据库无法自动化）
- [x] 2.6 去重并生成初筛列表

---

## Phase 3: 文献筛选

- [x] 3.1 Round 0: 论文类型分类（A-J）
- [x] 3.2 Round 1: 标题/摘要筛选（PICO + 类型条件）
- [ ] 3.3 全文获取
- [x] 3.4 Round 2: 全文筛选 + 引用范围分配 + 健康检查
- [ ] 3.5 PRISMA 流程图

---

## Phase 4: 深度阅读与笔记

- [x] 4.1 Batch 1 核心文献批量笔记 (528 P1)
- [x] 4.2 Batch 2 重要文献简记 (47 P2)
- [x] 4.3 剩余文献索引 (15 P3)
- [x] 4.4 提取交叉主题和核心论点（→ `memory/key-findings.md`）
- [ ] 4.5 构建证据表

---

## Phase 5: 写作

- [x] 5.1 确定综述大纲（`manuscript/outline.md`）
- [x] 5.2 撰写 Introduction
- [x] 5.3 撰写 Methods（叙述性综述 — 见 Introduction 末段检索方法描述）
- [x] 5.4-5.N 撰写各主题章节 (Sections 2-8)
- [x] 5.N+1 撰写 Discussion/Conclusions (Sections 9-11)
- [x] 5.N+2 撰写 Abstract + Key Messages
- [ ] 5.N+3 生成图表 (无图表 — 纯文本综述)
- [x] 5.N+4 初稿完成 → 进入内审

---

## Phase 6: 修改与定稿

- [x] 6.1 第一轮内部审校（Agent 4: 0 空强调词, 0 Gate6 违规, 92% 自然度）
- [x] 6.2 第二轮语言润色（审校中完成）
- [x] 6.3 引用核查（Gate 4/5/6 — 35/35 引用匹配, 0 违规）
- [ ] 6.4 格式化参考文献（目标期刊格式 — 待定期刊）
- [x] 6.5 最终定稿，提交前检查清单 (gen_word_full.py 通过)

---

## 图例
- `[ ]` 待完成
- `[x]` 已完成
- `[~]` 进行中

---

## Phase 7: AI 写作缺陷系统性修复 (2026-06-06)

### Phase 7.1: 模块 A — 领域知识结构层

- [x] 7.1.1 创建 `knowledge/domain-ontology-template.md` (Tier 3 模板)
- [x] 7.1.2 创建 `harness/evidence-gap-grading.md` (G0-G4 框架)
- [x] 7.1.3 创建 `harness/priority-scoring.md` (4 维度评分)
- [x] 7.1.4 Agent 1 新增 Step 7: Domain Ontology Construction (门禁)
- [x] 7.1.5 CLAUDE.md / MEMORY.md / quality-gate.md 同步更新 (Gate 7)

### Phase 7.2: 模块 D — 写作前规划层

- [x] 7.2.1 创建 `harness/time-annotation.md` (证据新鲜度衰减规则)
- [x] 7.2.2 Agent 3 新增 Steps 0a-0f: Pre-writing Planning (门禁)
- [x] 7.2.3 CLAUDE.md / MEMORY.md / quality-gate.md 同步更新 (Gate 8)

### Phase 7.3: 模块 B — 合成推理层

- [x] 7.3.1 创建 `harness/cross-intervention-matrix.md` (7 维度模板)
- [x] 7.3.2 创建 `harness/synthesis-reasoning.md` (Agent 7 工作流规则)
- [x] 7.3.3 创建 `harness/clinical-decision-framework.md` (决策框架模板)
- [x] 7.3.4 新增 Agent 7: Synthesis Agent 完整定义
- [x] 7.3.5 CLAUDE.md (命令/错误模式) / MEMORY.md / quality-gate.md 同步更新 (Gate 9)

### Phase 7.4: 模块 C — 审校增强层

- [x] 7.4.1 创建 `harness/perspective-switching.md` (5 视角规则)
- [x] 7.4.2 创建 `harness/data-translation.md` (RR→NNT 协议)
- [x] 7.4.3 创建 `harness/argument-diversity-enforcement.md` (论证多样性)
- [x] 7.4.4 创建 `harness/critical-absorption.md` (Cochrane 批判)
- [x] 7.4.5 Agent 4 新增 Pre-Pass 1-2 + Post-Pass 3-4
- [x] 7.4.6 CLAUDE.md / MEMORY.md / quality-gate.md 同步更新 (Gate 10)

### Phase 7.5: 集成验证

- [x] 7.5.1 workflow-evolution.md 追加 E004-E007
- [x] 7.5.2 FEATURE_LIST.md 更新（本文件）
- [x] 7.5.3 Agent 协作流程图更新
- [ ] 7.5.4 harness/test-scenarios.md 新增 L6-L7
- [ ] 7.5.5 harness/consistency-benchmarks.md 新增 Bench-006/007

### Phase 7.6a: Agent 8 — 投稿 Agent

- [x] 7.6a.1 创建 `harness/submission-compliance.md` (三阶段工作流规则)
- [x] 7.6a.2 创建 `harness/journal-profiles.md` (6 本期刊格式参数)
- [x] 7.6a.3 Agent 8 完整定义 (基础设施层)
- [x] 7.6a.4 gen_word_full.py 新增 HTML comment 剥离预处理器
- [x] 7.6a.5 CLAUDE.md / MEMORY.md / quality-gate.md 同步更新 (Gate 11)
- [x] 7.6a.6 workflow-evolution.md 追加 E009

### Phase 7.6b: Agent 4 Step 1.5

- [x] 7.6b.1 创建 `harness/negative-claim-detection.md`
- [x] 7.6b.2 Agent 4 新增 Step 1.5
- [x] 7.6b.3 CLAUDE.md / MEMORY.md 同步更新
- [x] 7.6b.4 workflow-evolution.md 追加 E008

---

## Phase 8: 流程治理与检索筛选增强 (2026-06-09)

### Phase 8.1: 项目路由与硬编码治理

- [x] 8.1.1 AGENTS.md 新增项目路由层与 Gate 0
- [x] 8.1.2 Agent 定义新增 R0/R1/R2 全局前置步骤
- [x] 8.1.3 `scripts/process_integrity_check.py` 新增流程完整性检查
- [x] 8.1.4 `scripts/gen_word_full.py` 支持当前稿件自动解析和显式路径传参
- [x] 8.1.5 `scripts/audit_manuscript.py` 支持当前稿件自动解析并修复带空格引用解析
- [x] 8.1.6 `scripts/rebuild_refs.py` 标记为废弃，避免旧稿硬编码误写

### Phase 8.2: 检索、筛选、全文获取协议

- [x] 8.2.1 创建 `harness/search-screening-protocol.md`
- [x] 8.2.2 新增 Gate Search / Gate Screening / Gate Fulltext
- [x] 8.2.3 Agent 1 接入 search protocol、全文访问分级和 VPN 下载清单
- [x] 8.2.4 Agent 6 接入 screening decision log、citation scope、abstract-only 降级规则
- [x] 8.2.5 创建 `docs/search-results/search-protocol.md` 模板
- [x] 8.2.6 创建 `docs/search-results/fulltext-access-log.csv` 模板
- [x] 8.2.7 创建 `docs/search-results/screening-decisions.csv` 模板
- [x] 8.2.8 创建 `docs/search-results/vpn-download-checklist.md` 模板

### Phase 8.3: 待继续清理

- [ ] 8.3.1 将 Agent 7/8 中剩余 `jitc_submission.md` 示例全部替换为 `current_manuscript`
- [ ] 8.3.2 将 LUSC 专用筛选规则移入 archive 或改写为主题无关模板
- [ ] 8.3.3 将 quality-gate.md 中历史 LUSC Gate 4 脚本移入 archived example
- [ ] 8.3.4 为 Gate Search/Gate Screening 编写可执行检查脚本

### Phase 8.4: Harness 架构审计

- [x] 8.4.1 创建 `harness/architecture.md`
- [x] 8.4.2 创建 `scripts/harness_architecture_check.py`
- [x] 8.4.3 更新 `harness/README.md`，登记最低可执行检查
- [x] 8.4.4 扩展 `harness/test-scenarios.md` 至 L6-L8
- [x] 8.4.5 扩展 `harness/consistency-benchmarks.md` 至 Bench-006/008
- [x] 8.4.6 更新 `harness/safety-policy.md`，加入 Codex/PowerShell 命令、AI provenance、旧写入脚本检测
- [x] 8.4.7 运行 `process_integrity_check.py` + `harness_architecture_check.py` + `audit_manuscript.py`

### Phase 8.5: Harness 可执行化收口

- [x] 8.5.1 将 Agent 7/8 和写作/审校定义中的 `jitc_submission.md` 当前默认值替换为 `current_manuscript`
- [x] 8.5.2 将 LUSC 专用筛选报告示例泛化为当前 PICO reason_code
- [x] 8.5.3 将 `quality-gate.md` 中历史 LUSC Gate 4 脚本替换为当前执行原则
- [x] 8.5.4 创建 `scripts/gate_search_check.py`
- [x] 8.5.5 创建 `scripts/gate_screening_check.py`
- [x] 8.5.6 创建 `scripts/harness_test_inventory.py`
- [x] 8.5.7 更新 harness README / architecture / MEMORY 索引
- [x] 8.5.8 创建 `scripts/run_harness_checks.py`
- [x] 8.5.9 更新 `progress/metrics-raw.json` schema 至 1.1，加入 provenance/checks/safety 字段

### Phase 8.6: 审稿项目流程治理

- [x] 8.6.1 创建 `harness/review-revision-protocol.md`
- [x] 8.6.2 创建 `docs/review/review-action-log.json` 当前项目 action log 模板
- [x] 8.6.3 创建 `docs/review/response-to-reviewers.md` 回复信模板
- [x] 8.6.4 创建 `scripts/review_revision_check.py`
- [x] 8.6.5 将 `CHANGELOG.md` / `REVISION_MAP.md` 改为 current_manuscript 路由安全格式
- [x] 8.6.6 Agent 4 接入审稿修回协议并修复旧 CLAUDE/病种残留
- [x] 8.6.7 将 Gate Revision 接入 harness architecture / README / run_harness_checks.py

---

*最后更新: 2026-06-09*
