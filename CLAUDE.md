# 医学综述写作项目

## 启动顺序

每次会话开始，按顺序读取：
1. `memory/project-status.md` — 当前阶段、稿件路径、目标期刊
2. `memory/active-focus.md` — 当前综述主题与 PICO
3. `features/FEATURE_LIST.md` — 第一个未完成任务

一句话告知用户当前状态，给出简洁选项。

**详细规则全文** → `AGENTS.md`（本文件为每次自动加载的核心摘要）

## 项目路由 ⛔

禁止假设历史项目参数。从 `memory/project-status.md` 和 `memory/active-focus.md` 动态解析：
- `current_manuscript` / `target_journal` / `review_type` / `topic_scope` / `evidence_dataset`

**禁止默认使用**: `manuscript/jitc_submission.md`、JITC、LUSC、Pediatric Research、旧 NRDS 参数。

冲突时以 `memory/project-status.md` 为准。

## 命令速查

| 用户说 | 动作 | Agent |
|--------|------|-------|
| `1` `搜索` | 文献搜索 + 筛选 | Agent 1（含原 Agent 6 筛选） |
| `2` `分析` | 深度分析论文 | Agent 2 |
| `3` `写作` | 综述写作 + 合成推理 | Agent 3（含原 Agent 7 合成） |
| `4` `审校` | 审校检查 | Agent 4 |
| `5` `评估` | 质量评估 | Agent 5 |
| `编码` | 进度+效率+安全+Git | Agent 0 |
| `快记` | 轻量进度+Git | Agent 0 轻量 |
| `投稿` | 格式化+合规检查 | 脚本（非独立Agent） |
| `gen` | 生成Word+自检 | `scripts/gen_word_full.py` |
| `状态` | 查看项目状态 | — |
| `教训` | 记录流程缺陷 | 根因→修改项目文件→追加演进记录 |

输入简略指令时 → **先一句话确认理解**，再执行。

## 核心规则（每次必须遵守）

### 引用铁律
- 每条声明必须有至少一篇引用文献的**摘要**直接支撑
- **禁止**从训练数据中提取知识贴到不相关的引用上
- 扩展段落前必须先验证引用-声明配对
- **所有引用必须包含 PMID 或 DOI**
- 跨人群/跨疾病/跨干预/跨结局外推时必须加限定语

### 写作纪律
- **单源真理**: 稿件内容唯一源文件是 `current_manuscript`。Word 由脚本生成，不含内容
- **修改流程**: 改源文件 → `gen` 生成 Word → 自检
- **图表**: 编号全局唯一；删除图表 = 删除所有正文引用 + 重新编号
- **仅摘要论文** ≤ 纳入总数 20%，不支撑核心论点

### 引用范围纪律
- ❌ G 类（叙述性综述）不得作为声明**主引用**——引用原始论文
- ❌ I 类（病例报告）不得**单独支撑**通用性声明
- ❌ E 类（纯生信）不得支撑**因果机制**声明——用 "is associated with" 非 "causes"
- ⚠️ D 类支撑机制 → 加 "clinical evidence suggests" / "translational data indicate"

### 语言自然度 — Must Fix（审校强制检查）

| # | 反模式 | 检测 | 级别 |
|---|--------|------|------|
| 2 | 过渡词单调 | 连续 ≥3 段以同类型过渡词开头 | **Must Fix** |
| 6 | 空洞强调词 | "Interestingly," "Notably," "Of note," "Importantly," "Surprisingly," 等 | **Must Fix（直接删除）** |

Nice to Have: 名词化链(≥5个→Must Fix) / 句子长度均质 / 被动语态堆积(≥4句) / 段落结构模板化(≥3段)

**自然度目标**: ≥ 80% 段落通过

## Gate 体系

### 核心 Gate（每次 Phase 结束强制执行）

| Gate | 内容 | 脚本 |
|------|------|------|
| **G0** | 流程完整性：项目路由、硬编码扫描、脚本可配置性 | `scripts/process_integrity_check.py` |
| **G1** | 文献检索 → 筛选：检索式完整、seed papers 命中、去重 | `scripts/gate_search_check.py` |
| **G2** | 筛选 → 分析：screening log 覆盖、排除原因、仅摘要≤20% | `scripts/gate_screening_check.py` |
| **G3** | 全文获取：VPN 清单、PDF 匹配、核心证据有全文 | 手动检查 |
| **G4** | 引用-声明验证：提取 [N] → PMID 摘要 → 关键词匹配 ≥90% | 审校Agent |
| **G5** | 格式完整性：图表引用、标题层级、段间距 | 审校Agent |
| **G6** | 引用范围合规：类型标签 vs 引用方式 | 审校Agent |

### 增强 Gate（条件激活，详见 `harness/quality-gate.md`）

| Gate | 激活条件 |
|------|---------|
| **G7** 领域本体 | 综述涵盖 ≥5 种干预时 |
| **G8** 写作前规划 | 使用 Priority-Weighted Section Allocation 时 |
| **G9** 合成推理 | 干预间存在竞争性选择 + 假设密集时 |
| **G10** 增强审校 | 追求 Cochrane 批判充分性 + 视角切换覆盖时 |
| **G11** 投稿合规 | 正式投稿前 |

## Tier 2 资源（按需加载）

`memory/project-status.md` · `memory/active-focus.md` · `memory/agent-specializations.md` · `features/FEATURE_LIST.md` · `memory/key-findings.md` · `memory/decisions.md` · `memory/workflow-evolution.md`

## Tier 3 资源（主动检索）

`docs/index.md` · `docs/methods/` · `docs/glossary.md` · `knowledge/domain-ontology.md` · `harness/quality-gate.md` · `harness/safety-policy.md` · `harness/search-screening-protocol.md` · `harness/review-revision-protocol.md` · `AGENTS.md`（规则全文）
