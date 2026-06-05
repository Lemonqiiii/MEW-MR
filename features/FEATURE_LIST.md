# 功能清单

> **使用说明**: 编码Agent每次会话结束时根据进展更新本文件。优先完成当前 Phase 内的所有任务再进入下一 Phase。

---

## Phase 1: 项目初始化 ✅

- [x] 1.1 搭建项目目录结构和配置文件
- [x] 1.2 配置 Claude Code hooks 和权限
- [x] 1.3 初始化 git 仓库
- [x] 1.4 搭建 Harness Engineering 框架（质量保证层）
  - [x] 五维度度量定义 (`harness/metrics.md`)
  - [x] 鲁棒性测试场景库 (`harness/test-scenarios.md`)
  - [x] 一致性基准测试 (`harness/consistency-benchmarks.md`)
  - [x] 安全策略与越权检测 (`harness/safety-policy.md`)
  - [x] 评估日志模板 (`harness/eval-log.md`)
  - [x] 编码Agent 扩展（效率数据收集 + 安全审计）
  - [x] 评估Agent 定义（L2判定 + 鲁棒性 + 一致性）

---

## Phase 2: 文献搜索

- [x] 2.1 确定检索策略和关键词（写入 `memory/active-focus.md`）
- [x] 2.2 PubMed 初步检索 (Europe PMC)
- [x] 2.3 Semantic Scholar 补充检索 (429限流)
- [x] 2.4 Europe PMC 补充检索
- [x] 2.5 去重并生成初筛列表（记录到 `docs/index.md`）
- [x] 2.6 导出检索结果（JSON格式）

---

## Phase 3: 文献筛选 ✅

- [x] 3.1 标题/摘要筛选（432 → 62篇）
- [x] 3.2 全文获取 (60/62 PMC开放获取)
- [x] 3.3 全文筛选（62 → 37篇最终纳入）
- [x] 3.4 确定最终纳入文献列表
- [x] 3.5 绘制 PRISMA 流程图

---

## Phase 4: 深度阅读与笔记 ✅

- [x] 4.1 阅读并笔记核心文献 Batch 1 (10篇)
- [x] 4.2 阅读并笔记核心文献 Batch 2 (10篇)
- [x] 4.3 阅读并笔记核心文献 Batch 3 (11篇)
- [x] 4.4 (剩余7篇为纯预后模型，仅做摘要笔记)
- [x] 4.5 提取交叉主题和核心论点（18个主题 → `memory/key-findings.md`）
- [x] 4.6 构建证据表 (Tables 1-4 → `manuscript/figures_tables.md`)

---

## Phase 5: 写作 ✅

- [x] 5.1 确定综述大纲（`manuscript/outline.md`）
- [x] 5.2 撰写 Introduction (~843词) ✅ 审校
- [x] 5.3 (本综述为叙述性综述，无Methods章节)
- [x] 5.4 撰写 Sec 2: Immune Landscape (~1,457词)
- [x] 5.5 撰写 Sec 3: Tumor-Intrinsic (~2,106词)
- [x] 5.6 撰写 Sec 4: TME-Mediated (~1,938词)
- [x] 5.7 撰写 Sec 5: Acquired (~854词) + Sec 6: Strategies (~625词)
- [x] 5.8 撰写 Sec 7: Conclusions (~445词)
- [x] 5.9 撰写 Abstract (~246词)
- [x] 5.10 初稿完成 → 进入内审

---

## Phase 6: 修改与定稿 ~90%

- [x] 6.1 第一轮内部审校（逻辑连贯性 + 事实核查）
- [x] 6.2 第二轮语言润色（合并 + 统一引用 + 摘要）
- [x] 6.3 引用核查（逐一核对 PMID/DOI，移除喉鳞癌文献）
- [ ] 6.4 格式化参考文献（目标期刊格式 — 待定期刊后）
- [x] 6.5 生成图表 (4 Figures + 4 Tables)
- [ ] 6.6 最终定稿，提交前检查清单（→ 待用户最终审阅）

---

## 图例
- `[ ]` 待完成
- `[x]` 已完成
- `[~]` 进行中

*最后更新: 2026-06-04*
