# Agent 专业化定义

本文件定义了综述写作项目中的5个横向执行Agent + 2个纵向基础设施Agent（共7个）。每个Agent有极简命令触发、完整的输入输出规范和prompt模板。

---

## Agent 0: 编码Agent (Infrastructure) — 双模式 (2026-06-05 修订)

### 设计理念
编码Agent从原始的单模式（4 Parts全部执行）拆分为两种模式，以降低执行门槛、提高触发频率：

| 模式 | 触发命令 | 频率 | 包含Parts | 预计耗时 |
|------|---------|------|----------|---------|
| **轻量编码** | `快记` `记` `quick` | 每2-3个子任务 | Part A + Git提交 | 低（秒级） |
| **完整编码** | `编码` `6` `commit` | 每Phase结束 | Part A + B + C + D | 中（需审计扫描） |

### 自动提示规则
- 完成2-3个子任务后 → Agent主动建议"快记"
- Phase结束时 → Agent展示检查清单，提示"编码"
- Stop hook → 提醒用户执行"快记"或"编码"

---

### 轻量编码模式 (`快记` / `记`)

#### 触发条件
- **手动极简命令**: `快记` `记` `quick`
- **自动提示**: 完成2-3个子任务后Agent主动建议

#### 工作流
1. 检查 git 变更状态
2. 读取 `features/FEATURE_LIST.md`，更新已完成任务的勾选状态
3. 更新 `memory/project-status.md` 统计数据（progress_pct、words_written、last_update、last_session_id）
4. 追加 `progress/SESSION_LOG.md` 一条精简记录（格式：日期+完成事项+下一步+阻碍）
5. git add -A && git commit（结构化 message: `[phase] 简短描述`）

#### 跳过项
- Part B 效率数据收集（完整编码时执行）
- Part C 安全审计（完整编码时执行）
- MILESTONES.md 更新（仅Phase结束时更新）

#### 输出
- 一句话确认：提交了哪些变更

---

### 完整编码模式 (`编码` / `6`)

#### 触发条件
- **手动极简命令**: `编码` `6` `commit`
- **自动提示**: Phase结束时Agent展示检查清单后提示

#### 工作流
执行轻量编码全部内容 + 以下补充：

##### Part A+: 进度记录（含里程碑）
1-5. 同轻量编码
6. 更新 `progress/MILESTONES.md`（将本Phase对应的里程碑标记为✅+填写日期）
7. 如有新发现或决策，更新 `memory/key-findings.md` 或 `memory/decisions.md`

##### Part B: 效率数据收集
8. 从会话上下文提取效率指标，写入 `progress/metrics-raw.json`:
   - **wall_time_sec**: 任务耗时
   - **tool_calls**: 工具调用总次数
   - **tools**: 各工具调用次数明细
   - **tokens_in / tokens_out**: Token消耗
   - **compactions**: 上下文压缩次数

##### Part C: 安全审计
9. 扫描会话操作，对照 `harness/safety-policy.md` 检测越权
10. 将违规写入 `progress/metrics-raw.json`

##### Part D: Git 提交
11. git commit（含 metrics-raw.json），使用结构化 message

#### 输出
- 表格总结本次更新内容
- 效率指标摘要
- 安全审计摘要（如有违规）
- 建议的下一步任务
- `progress/metrics-raw.json` 文件（供评估Agent读取）

---

## Agent 1: 文献搜索Agent

### 定位
横向执行层。负责多数据库系统检索、五层全面性验证、全文获取策略。**不负责筛选**（由 Agent 6 筛选Agent 负责）。

### 触发条件
**极简命令**: `搜索` `搜` `1` `检索` `search` `find papers`
启动时如果当前 Phase 为 literature-search 且用户说 `下一步` → 自动触达

### 输入
- `memory/active-focus.md` — PICO 框架、检索关键词、纳入排除标准
- `docs/methods/database-coverage.md` — 数据库覆盖目录与激活决策表
- `docs/index.md` — 了解已有文献分布
- 用户指定的额外检索参数（年份范围、研究类型等）

---

### 工作流

#### Step 0: 数据库需求评估

1. 读取 `memory/active-focus.md` 获取 PICO 和研究设计类型
2. 读取 `docs/methods/database-coverage.md` 的激活决策表
3. 自动判定需要激活的数据库列表:

| 条件 | 激活 |
|------|------|
| 所有综述 | PubMed + Semantic Scholar + Europe PMC (Tier 1 自动) |
| 涉及药物/生物制剂 | Embase (Tier 2 高优先级) |
| 涉及 RCT/临床试验 | Cochrane CENTRAL + ClinicalTrials.gov |
| 涉及中国人群/中医药/亚洲流行病学 | CNKI + 万方 (Tier 2 必需) |
| 涉及中医药/中西医结合 | + SinoMed (Tier 2 必需) |
| 涉及最新进展 | Europe PMC 预印本模式（自动） |
| 系统综述/荟萃分析 | Embase + Cochrane (标记为强烈建议) |

4. 输出数据库清单，标注优先级和访问方式

#### Step 1: Tier 1 自动检索

1. **PubMed**: 构建 MeSH + 自由词检索式 → E-utilities API 或 WebFetch → 获取 PMID 列表 + 摘要
2. **Semantic Scholar**: 关键词 + 语义搜索 → API → 获取论文详情（含 TLDR 摘要、引用计数）
3. **Europe PMC**: 自由词 + 预印本 → API → 获取论文详情（含 OA 全文链接）
4. **ClinicalTrials.gov** (如激活): API → 获取已完成/进行中的试验记录
5. **检索式诊断**: 提交检索式前:
   - 敏感性检验: 用已知应命中的术语验证
   - 精确性检验: 随机抽取前 20 篇 → Agent 判断相关性 (目标 ≥ 85%)
   - 漏洞分析: 检查潜在的同义词/上位词遗漏
6. 将 Tier 1 结果合并为初始 PMID 列表

#### Step 2: 生成 Tier 2 手动检索清单

1. 按各数据库语法预编译检索式:
   - **Embase**: MeSH → Emtree 术语映射 → Ovid 检索式
   - **Cochrane**: 适配 Cochrane Library 检索语法
   - **CNKI**: 英文关键词 → 中文关键词 → CNKI 专业检索语法
   - **万方**: 适配万方高级检索语法
   - **SinoMed**: 适配 CBM 检索语法

2. 写入 `docs/search-results/manual-search-checklist.md`:
   - 每个数据库的完整操作步骤
   - 预编译检索式（可直接粘贴）
   - 导出格式说明 (RIS) 和文件命名规则
   - 预计耗时

3. 提示用户:

> "Tier 1 自动检索完成，共命中约 N 篇。请连接医学院 VPN，按 manual-search-checklist.md 中的清单执行 Tier 2 数据库检索。完成后将 RIS 文件放入 docs/search-results/，对我说'检索结果已就绪'。"

#### Step 3: 合并去重

用户完成 Tier 2 后触发:

1. 读取 `docs/search-results/` 下所有 RIS 文件
2. 解析 PMID/DOI/标题
3. 统一去重: PMID 精确匹配 → DOI 匹配 → 标题相似度 > 95%
4. 去重后生成统一格式的初筛列表

#### Step 4: 五层全面性验证

##### Layer 1: 多策略检索覆盖
- 四路独立检索已执行 (PubMed + S2 + EPMC + 可选 ClinicalTrials.gov)
- 确认每个数据库的成功响应状态

##### Layer 2: 多点引文扩散
- **锚点A — 共识端**: 三方共识集 (PubMed ∩ S2 ∩ EPMC) 中引用最高的 5 篇
  → 反向查参考文献 + 前向查引文 → 补充至检索结果
- **锚点B — 时间端**: 三方共识集中最新的 5 篇 (2024-2025)
  → 它们的参考文献 → 确保新兴方向不遗漏
- **锚点C — 方法学端**: 不同研究设计的论文各 2 篇
  (RCT × 2, 队列 × 2, 系统综述 × 2, 基础实验 × 2)
  → 不同方法学社群引用不同的文献圈 → 交叉验证
- **锚点D — 地域端**: 如元数据支持，从不同国家各取 1 篇
  → 非英美研究者的引用网络 → 防止欧美文献中心化
- 多点回溯的新增论文与 Layer 1 结果合并

##### Layer 3: 外部金标准验证
1. 在检索结果中识别最近 2-3 篇高质量系统综述/荟萃分析
   (标记: 发表于 2023-2025, 高引, 系统综述)
2. 提取这些系统综述的纳入文献列表（参考文献）
3. 交叉验证: 已发表系统综述的纳入文献中，有多少被我们的检索命中？
   - 命中率 ≥ 90% → ✅ 检索覆盖度可接受
   - 命中率 85-90% → ⚠️ 标记，分析遗漏文献特征
   - 命中率 < 85% → ❌ 检索策略可能有重大漏洞 → 报告给用户

##### Layer 4: 灰色文献补充
1. 如果涉及临床试验: 检查 ClinicalTrials.gov 已完成未发表的试验
2. 会议摘要: Europe PMC 已自动覆盖部分
3. 预印本: Europe PMC bioRxiv/medRxiv 已自动覆盖
4. 灰色文献单独标记: 不作为核心论点主要证据, 引用时标注类型

##### Layer 5: 饱和 + 对抗检验
1. **饱和检验**: 连续扩展检索式（增加同义词、上位词）→ PMID 增量 < 5% → 检索饱和
2. **对抗检验**: 评估Agent 在收到检索结果后独立排查:
   - 从已纳入论文中随机抽 5 篇 → 阅读 Discussion 段落
   - Discussion 中引用的关键前人工作 → 是否已在检索结果中？
   - ≥ 2 篇缺失 → 🔴 标记: 检索可能有盲区

#### Step 5: 全文获取分级

对去重后的论文按获取难度分级:

| Tier | 来源 | Agent 动作 | 预计覆盖 |
|------|------|-----------|---------|
| **Tier 1** | PMC OA, Europe PMC OA, bioRxiv/medRxiv | Agent 自动获取全文 | 30-50% |
| **Tier 2** | 需要 VPN (机构订阅期刊) | 生成下载清单 → 用户 VPN 批量下载 | 20-30% |
| **Tier 3** | 付费墙 | 生成清单 → 标注获取途径 → 用户决定 | 10-20% |
| **Tier 4** | 无法获取全文 | 标记为仅摘要 → 降级处理 | 余量 |

Tier 2 操作:
1. 生成 VPN 下载清单 (PMID + 标题 + 期刊 + DOI + 直接 PDF 链接)
2. 用户在 VPN 窗口批量下载 → 放入 `docs/papers/fulltext/`
3. Agent 按文件名中的 PMID 自动匹配 PDF → 论文

**仅摘要比例控制**:
- 目标: 仅摘要论文 ≤ 纳入总数的 20%
- 搜索Agent 在 Step 5 结束时自动估算仅摘要比例
- 如果预估 > 20% → ⚠️ 预警 → 建议用户优先获取 Tier 2 全文
- 仅摘要论文在笔记中标注 `⚠️ Abstract Only — Not Full Text Verified`

#### Step 6: 更新索引

1. 更新 `docs/index.md` 文献统计数据
2. 生成 Handoff 给筛选 Agent:
   - 初筛列表路径
   - 数据库覆盖度报告（哪些库检索了/哪些未检索）
   - Layer 1-5 验证摘要
   - 全文获取比例预估
   - 已知问题和建议

---

### Handoff 格式 (传递给筛选Agent)

```markdown
## 文献搜索 Handoff — [检索主题] — YYYY-MM-DD

### 检索概要
| 数据库 | 命中 | 状态 |
|--------|------|------|
| PubMed | XXX | ✅ |
| Semantic Scholar | XXX | ✅ |
| Europe PMC | XXX | ✅ |
| Embase | XXX | ✅/⚠️ 未检索 |
| CNKI | XXX | ✅/⚠️ 未激活 |
| ... | ... | ... |

去重后总计: N 篇

### 五层验证结果
| 层级 | 结果 | 说明 |
|------|------|------|
| L1 多策略 | ✅ | 四路自动检索完成 |
| L2 多点引文 | ✅/⚠️ | 新增 X 篇，锚点D未执行(元数据不支持) |
| L3 外部金标准 | 92% | 两篇系统综述的参考文献覆盖度 |
| L4 灰色文献 | ✅ | 预印本已覆盖，无未发表试验 |
| L5 饱和+对抗 | ⚠️ | 待评估Agent 对抗检验 |

### 全文获取
- 预估 OA 自动获取: XX%
- 需要 VPN 手动下载: XX 篇 (清单已生成)
- 预估仅摘要: XX% (目标 ≤ 20%)
- ⚠️ 如预估仅摘要 > 20%: [具体建议]

### 已知问题
1. [问题描述和影响]
2. ...

### 建议
- [对筛选Agent的建议，如某数据库结果的质量注意事项]
- **注意**: 筛选Agent (Agent 6) 将在 Round 0 对每篇论文做类型分类（A-J），请确保初筛列表包含 pubTypeList 和完整摘要以支持分类
```

### 输出结构
```
docs/search-results/
├── manual-search-checklist.md  # VPN 手动检索清单
├── pubmed-export.json          # PubMed 检索结果
├── s2-export.json              # Semantic Scholar 检索结果
├── epmc-export.json            # Europe PMC 检索结果
├── embase-export.ris           # Embase 检索结果 (用户放入)
├── cnki-export.txt             # CNKI 检索结果 (用户放入)
└── merged-deduplicated.json    # 合并去重后的初筛列表
```

---

## Agent 2: 论文分析Agent

### 触发条件
**极简命令**: `分析` `读` `3` `分析这篇` `analyze` `take notes`

### 输入
- 论文 PMID/DOI/URL 或已有 PDF
- `docs/papers/template.md` — 笔记模板

### 工作流
1. 通过 PMID/DOI 获取论文元数据和摘要
2. 如有全文访问权限，读取全文；否则基于摘要做初步笔记
3. **确认论文类型**: 从筛选Agent Handoff 中读取该论文的类型代码（A-J）和引用范围标签，填入笔记模板的"论文类型"和"引用范围"字段
4. 按 `docs/papers/template.md` 模板结构化提取:
   - 元数据 (PMID, 期刊, 年份, 作者, 引用数, **论文类型, 引用范围**)
   - PICO (临床研究) 或研究框架 (基础研究)
   - 核心方法
   - 关键发现与数据
   - 局限性
   - 与本综述的关联
5. 写入 `docs/papers/[topic]/[第一作者姓氏][年份]-[关键词].md`
6. 更新 `docs/index.md` 文献统计（含论文类型字段）
7. 如发现重要论点，提示更新 `memory/key-findings.md`

### 输出
- 论文笔记文件路径
- 关键发现的一句话摘要
- 重要性评级 (★★★ 核心 / ★★ 重要 / ★ 辅助)

---

## Agent 3: 综述写作Agent

### 触发条件
**极简命令**: `写作` `写` `4` `撰写` `draft` `开始写`

### 输入
- `manuscript/outline.md` — 综述大纲
- `memory/key-findings.md` — 核心论点
- `memory/active-focus.md` — 写作方向和范围
- `docs/papers/` — 对应主题的论文笔记（每篇笔记包含论文类型和引用范围标签）
- `docs/index.md` — 文献索引（含类型分布概览）
- 用户指定的目标章节

### 工作流
1. 读取大纲确定写作位置
2. 加载相关论文笔记 (根据章节主题从 `docs/papers/` 检索)
3. **新增**: 确认每篇论文的类型代码（A-J）和引用范围标签（来自筛选Agent 的 Handoff）
4. 加载 `memory/key-findings.md` 对应主题的论点
5. 按学术综述写作规范撰写:
   - 逻辑流: 背景 → 现状 → 进展 → 争议 → 展望
   - 引用管理: 每句话如来自文献，标注 PMID/DOI
   - **引用范围匹配**: 每条声明与引用论文的类型进行配对验证:
     - 机制声明 → 必须由 A/B/C 类支撑（E 类不可）
     - 临床关联 → 可由 D/E/F/H 类支撑
     - 背景陈述 → 可由 G 类辅助引用
     - 病例报告（I 类）→ 不可单独支撑通用声明
   - 避免简单的 "A found X, B found Y" 堆砌 → 改为主题式综合
6. 写出初稿到 `manuscript/jitc_submission.md`（单源真理——唯一的稿件源文件）
7. **新增**: 运行 `python3 scripts/gen_word_full.py` 生成 Word 文档
8. **新增**: 运行 Gate 4 引用验证 + Gate 5 格式验证 + Gate 6 引用范围合规
9. 标记引用了哪些论文笔记 + 每条声明的引用类型匹配状态

### 输出
- 写入 `manuscript/jitc_submission.md` 的段落
- 运行 `gen_word_full.py` 生成的 Word 文档（8 项自检必须全部通过）
- 引用的 PMID 列表 + 每篇的类型代码
- **新增**: 引用范围合规自查表（声明类型 × 引用类型的交叉检查）
- 标记哪些论点需要更多文献支撑（特别是标记哪些核心机制声明目前只有 E 类支撑 → 需要补充 A/B/C 类文献）

### 写作风格要求
- 英文写作，学术正式但不晦涩
- 主动语态为主，避免过度被动
- 段落结构: Topic sentence → Evidence synthesis → Transition（**但禁止连续 3 段使用相同结构，见自然度反模式 5**）
- 避免: "Interestingly", "It is worth noting that" 等冗余表达（**直接删除，见自然度反模式 6**）
- 数据陈述必须精确: "increased by 34% (95% CI: 28-40%, p<0.001)" 而非 "significantly increased"
- **语言方差**: 每段至少 1 句短句（< 12 词）；不允许整段所有句子均在 22-35 词范围内
- **完整自然度规范**: 见 CLAUDE.md 写作纪律 → 语言自然度（6 反模式）

---

## Agent 4: 审校Agent

### 触发条件
**极简命令**: `审校` `审` `5` `review` `核查` `检查草稿`

### 输入
- `manuscript/jitc_submission.md` — 待审草稿（单源真理）
- `docs/papers/` — 对应论文笔记（交叉验证引用 + 论文类型标签 + 引用范围标签）
- `memory/decisions.md` — 关键决策记录（检查一致性）

### 工作流
1. **事实核查**: 逐条验证引用是否准确反映原始论文
2. **逻辑审查**: 检查段落间过渡、论证链条完整性
3. **语言润色**: 检查语法、拼写、学术表达规范
4. **引用完整性**: 检查每个声明是否有文献支撑
5. **一致性检查**: 术语使用、缩写定义、数字格式
6. **语言自然度扫描** (2026-06-05 新增): 逐段检测 6 个僵硬反模式（见 CLAUDE.md 写作纪律 → 语言自然度），统计段落通过率
7. **引用范围合规检查** (2026-06-05 新增): 逐条声明，对照 CLACDE.md 引用范围纪律，验证引用方式是否越权:
   - 机制声明的主引用是否来自 A/B/C 类？
   - 是否有 G 类（综述）被用作主引用？
   - 是否有 I 类（病例报告）单独支撑通用声明？
   - 是否有 E 类（纯生信）被用于支撑因果机制声明？
   - 违规标记为 MUST FIX
8. 输出审校报告: 严重问题 (must fix) + 建议改进 (nice to have) + 自然度统计 + 引用范围合规统计

### 输出格式
```markdown
## 审校报告 — [章节名] — YYYY-MM-DD

### 严重问题 (Must Fix)
| # | 位置 | 问题类型 | 描述 | 建议修改 |
|---|------|---------|------|---------|
| 1 | 第X段 | 事实错误 | ... | ... |

### 建议改进 (Nice to Have)
| # | 位置 | 改进点 | 建议 |
|---|------|--------|------|
| 1 | ... | ... | ... |

### 统计
- 总问题数: X
- 严重: X
- 建议: X
- 引用准确率: X%
- **语言自然度**: X/X 段落通过 (XX%) — 目标 ≥ 80%
- **引用范围合规**: X 条违规 (MUST FIX) — 引用越权详情见下方
```

---

## Agent 6: 筛选Agent (Screening)

### 定位
横向执行层。负责按纳入/排除标准对初筛列表进行两轮筛选。**独立于搜索Agent**——搜索负责"找到"，筛选负责"判断"。

### 触发条件
**极简命令**: `筛选` `筛` `2` `screening` `开始筛选`
**自动**: 文献搜索Agent 完成 Handoff 后自动提示

### 输入
- 文献搜索Agent 的 Handoff（初筛列表 + 五层验证摘要 + 全文获取状态）
- `memory/active-focus.md` — 纳入/排除标准（PICO）
- `docs/methods/systematic-review.md` — PRISMA 方法学指南

---

### 工作流

#### 论文类型分类体系 (2026-06-05 新增)

在 PICO 筛选之前，**先对每篇论文做类型判定**。论文类型决定了它在综述中的纳入门槛和引用范围——不同类型的论文不能放在同一把尺子下判断。

##### 10 类型定义

| 代码 | 类型 | 定义 | 识别特征 |
|------|------|------|---------|
| **A** | 机制实验 | 体外/体内实验验证因果机制 | 摘要含: knockout, knockdown, siRNA, CRISPR, western blot, xenograft, mouse model, in vitro, in vivo + 功能实验 |
| **B** | 转化研究 | 人源样本 + 实验验证 | 摘要含: patient samples/tissues + IHC/IF/flow + functional assay |
| **C** | 多组学+验证 | scRNA-seq/空间转录组/蛋白组 + 实验验证 | 摘要含: single-cell, spatial transcriptomics, proteomics + validation/qPCR/IHC |
| **D** | 临床+机制终点 | 临床试验含生物标志物/机制相关终点 | pubTypeList 含 Clinical Trial/RCT + 摘要含 biomarker/correlative/translational endpoint |
| **E** | 纯生信/计算 | TCGA/GEO挖掘、基因签名、预后模型，**无实验验证** | 摘要含: TCGA, GEO, LASSO, Cox regression, nomogram, prognostic model, signature, CIBERSORT — **但无 functional validation** |
| **F** | 系统综述/荟萃 | 有明确方法学（PRISMA等）的证据综合 | pubTypeList 含 Systematic Review/Meta-Analysis；或摘要明确描述检索策略+纳入排除标准 |
| **G** | 叙述性综述 | 专家综述、观点文章 | pubTypeList 含 Review；摘要为叙述性总结，无系统检索方法 |
| **H** | 临床疗效 | 纯疗效/安全性数据，无机制分析 | pubTypeList 含 Clinical Trial/RCT；摘要仅报告 ORR/PFS/OS/安全性，无 biomarker/translational |
| **I** | 病例报告 | 单个或少量病例 | pubTypeList/title 含 Case Report/Case Series |
| **J** | 方法/方案 | 试验方案、方法学论文 | pubTypeList 含 methods-article；或 title 含 "study protocol"/"trial design" |

**分类优先级**: 摘要含 HTML 标签时，先提取纯文本再分类。一篇论文同时匹配多种类型时，取证据等级较高者（A > B > C > D > E；F > G）。

##### 引用范围矩阵

每种类型在综述中的**证据功能**是预定义的，Agent 3（写作）和 Agent 4（审校）均需遵守：

| 类型 | 支撑机制声明 | 支撑临床关联 | 可作为主引用 | 仅摘要可接受 |
|------|------------|------------|------------|------------|
| A 机制实验 | ✅ 主证据 | ✅ | ✅ | ❌ 必须全文 |
| B 转化研究 | ✅ 主证据 | ✅ | ✅ | ❌ 必须全文 |
| C 多组学+验证 | ✅ 辅助证据 | ✅ | ✅ | ❌ 必须全文 |
| D 临床+机制 | ⚠️ 需实验辅助 | ✅ 主证据 | ✅ | ❌ 必须全文 |
| E 纯生信 | ❌ 仅相关性 | ⚠️ 假说生成 | ⚠️ 仅辅助引用 | ⚠️ 可接受 |
| F 系统综述 | ❌ 无新数据 | ✅ 金标准 | ⚠️ 仅共识声明 | ❌ 必须全文 |
| G 叙述性综述 | ❌ 禁引用综述 | ⚠️ 仅背景 | ❌ **禁做主引用** | ⚠️ 可接受 |
| H 临床疗效 | ❌ | ✅ | ✅ | ❌ 必须全文 |
| I 病例报告 | ❌ 仅存在性证明 | ❌ | ❌ **禁单独支撑** | ⚠️ 可接受 |
| J 方法/方案 | ❌ | ❌ | ❌ 仅信息性引用 | ✅ 可接受 |

**关键规则**:
- "禁做主引用": 该类型的论文不能作为某条声明的主要支撑文献，但可以作为辅助引用（如 "see also review by X et al."）
- "禁单独支撑": 病例报告不能是一条通用性声明的唯一引用
- "仅相关性": 纯生信论文可以描述关联/异质性/候选基因，但不能声称因果机制
- "仅辅助引用": 引用编号放在辅助位置（如 `[42]` 而非主引用位置）

---

#### Round 0: 论文类型分类 (新增 — 2026-06-05)

**在 PICO 筛选之前执行**:

1. 对每篇论文，基于标题 + 摘要 + pubTypeList 判定类型代码（A-J）
2. 标记分类置信度（HIGH / MEDIUM / LOW）
3. 对于 C vs E 的边界情况（多组学但不确定是否有验证）→ 默认为 E，在 Round 2 全文阶段升级为 C
4. 识别并标记以下**硬排除**:
   - 喉鳞癌/头颈鳞癌（laryngeal, head and neck, oral, esophageal, cutaneous, cervical, thymic）→ `WRONG_POPULATION_LUSC`
   - "LSCC" 缩写无法确认为 lung squamous → 标记待核验
5. 输出: 每篇论文的类型标签 + 置信度

---

#### Round 1: 标题/摘要筛选 (PICO + 类型条件)

基于 Round 0 的类型标签，**应用类型特定的纳入门槛**:

##### PICO 判定 (所有类型通用)

| PICO 维度 | 判定 |
|-----------|------|
| Population 匹配 (LUSC) | YES → 通过; NO(关键) → EXCLUDE; UNCERTAIN → INCLUDE |
| Intervention/Exposure 匹配 | YES → 通过; NO → EXCLUDE; UNCERTAIN → INCLUDE |
| Outcome 匹配 (耐药/免疫逃逸) | YES → 通过; 纯预后无机制 → 标记; NO → EXCLUDE |
| 研究设计可接受 | 见下方类型条件 |

##### 类型条件判定

| 类型 | Round 1 纳入条件 | 阈值 |
|------|----------------|------|
| A/B/C | LUSC + ICI/immune + mechanism → **直接纳入** | 最低 |
| D | LUSC + ICI + biomarker/translational endpoint → **直接纳入** | 最低 |
| E | LUSC + immune + **提供机制假说**（非纯预后模型）→ **纳入但标记 `⚠️ CORRELATIVE_ONLY`**；纯预后模型无机制假说 → **EXCLUDE** (`PURE_PROGNOSTIC`) | 中 |
| F | 2023+, NSCLC/LUSC focus, 明确方法学 → 纳入 | 中 |
| G | 仅纳入高引或关键期刊 → 标记 `⚠️ REVIEW_SOURCE` | 高 |
| H | LUSC + ICI efficacy data → 纳入但标记 `⚠️ NO_MECHANISM` | 中 |
| I | 记录新机制或特殊场景 → 纳入；常规病例 → EXCLUDE | 高 |
| J | 信息性 → 纳入但标记 `⚠️ INFO_ONLY` | 高 |

**新增排除原因代码**:
- `PURE_PROGNOSTIC` — 纯预后模型/基因签名，无任何机制假说
- `WRONG_POPULATION_LUSC` — 非肺鳞癌（喉鳞癌/头颈鳞癌等）
- `REVIEW_OUTDATED` — 综述但过时（2022以前）
- `CASE_ROUTINE` — 常规病例报告，无新机制

**宁滥勿缺底线保持不变**: 任何 UNCERTAIN → INCLUDE。只有明确违反关键纳入标准 → EXCLUDE。

---

#### Round 2: 全文筛选 + 引用范围分配

1. **核实论文类型**: 基于全文信息重新判定类型（C vs E 的升级在此完成）

2. **类型特定的全文质量评估**:

| 类型 | 全文检查重点 |
|------|------------|
| A/B/C | 实验设计是否合理？数据是否完整？验证是否充分？ |
| D | 生物标志物分析是否为预设终点（prespecified）？还是事后分析（post hoc）？ |
| E | 数据来源是否明确（TCGA/GEO accession）？方法是否可复现？ |
| F | 检索策略是否完整？偏倚风险评估是否执行？ |
| G | 期刊声誉？作者权威性？论点是否有原始文献支撑？ |
| H | 试验设计？样本量？统计效能？ |
| I | 机制分析是否充分（非纯临床描述）？ |

3. **分配引用范围**: 按引用范围矩阵，为每篇纳入论文标记:
   - `can_support_mechanism`: true/false
   - `can_support_clinical`: true/false  
   - `can_be_primary_ref`: true/false
   - `abstract_only_ok`: true/false

4. **最终判定**:
   - 符合该类型的纳入门槛 → **INCLUDE + 类型标签 + 引用范围**
   - 有疑虑但可接受 → **INCLUDE + 标注疑虑**
   - 不符合 → **EXCLUDE + 证据**

5. **类型分布检查** (2026-06-05 新增):
   - 计算各类型占比
   - **如果是机制综述**: A+B+C 类应 ≥ 纳入总数的 20%
   - 如果 A+B = 0 → ⚠️ **严重警告**: 机制综述无机制实验论文！
   - 如果 E 类 > 50% → ⚠️ 警告: 综述可能建立在相关性证据之上
   - 如果 F/G 类 > 30% → ⚠️ 警告: 综述可能过度依赖二手来源

6. **仅摘要比例控制** (保持不变):
   - 计算当前仅摘要论文占 INCLUDE 的比例
   - 如果 > 20% → ⚠️ 标记 → 建议优先获取 Tier 2/3 全文
   - 仅摘要论文在最终列表中标注 `⚠️ ABSTRACT ONLY`
   - **额外约束**: A/B/C/D/F 类论文不得为仅摘要

---

### 输出

#### 筛选报告结构

```markdown
## 筛选报告 — [主题] — YYYY-MM-DD

### Round 0: 论文类型分类
- 分类总数: N 篇
- 类型分布:

| 类型 | 数量 | 占比 |
|------|------|------|
| A 机制实验 | X | X% |
| B 转化研究 | X | X% |
| C 多组学+验证 | X | X% |
| D 临床+机制 | X | X% |
| E 纯生信 | X | X% |
| F 系统综述 | X | X% |
| G 叙述性综述 | X | X% |
| H 临床疗效 | X | X% |
| I 病例报告 | X | X% |
| J 方法/方案 | X | X% |

- 硬排除 (WRONG_POPULATION_LUSC等): X 篇

### Round 1: 标题/摘要筛选 (PICO + 类型条件)
- 筛选前: N 篇
- 排除: M 篇 (原因分布见下表)
- 纳入: K 篇

| 排除原因 | 数量 |
|---------|------|
| WRONG_POPULATION | 45 |
| PURE_PROGNOSTIC | 12 |
| WRONG_POPULATION_LUSC | 3 |
| ... | ... |

### Round 2: 全文筛选 + 引用范围分配
- 筛选前: K 篇
- 全文可获取: P 篇 (XX%)
- 仅摘要: Q 篇 (XX%) — [✅ ≤20% / ⚠️ >20%]
- 排除: L 篇
- **最终纳入: J 篇**

#### 引用范围概要

| 可支撑 | 数量 | 占比 |
|--------|------|------|
| 机制声明 (can_support_mechanism) | X | X% |
| 临床关联 (can_support_clinical) | X | X% |
| 可作为主引用 (can_be_primary_ref) | X | X% |

#### 类型分布健康检查

| 检查项 | 阈值 | 实际 | 状态 |
|--------|------|------|------|
| A+B+C 占比 | ≥ 20% | X% | ✅/⚠️/❌ |
| E 类占比 | < 50% | X% | ✅/⚠️ |
| F+G 类占比 | < 30% | X% | ✅/⚠️ |
| 仅摘要占比 | ≤ 20% | X% | ✅/⚠️ |
| A+B 是否为零 | > 0 | X | ⚠️ 严重警告 |

### PRISMA 流程图数据
- 检索命中: N
- 去重后: N'
- Round 1 纳入: K
- Round 2 纳入: J
- (提供完整 PRISMA 流程图所需数字)

### Handoff 给分析Agent
- 最终纳入列表: [J 篇 PMID + 标题 + 类型代码 + 引用范围 + 全文状态]
- **类型标签持久化**: 将纳入论文的类型代码和引用范围标签写入 `data/screening_final_inclusion.json`（供 Agent 2/3/4 按 PMID 查询）
- ⚠️ 仅摘要论文: Q 篇 (标注在列表中)
- ⚠️ E 类论文 (仅相关性): X 篇 — 写作Agent 注意引用范围约束
- ⚠️ 禁做主引用 (G/I/J类): X 篇
- 已知问题:
  1. [如"XX 篇中文文献摘要信息不足，已纳入但标注待全文核实"]
  2. [如"类型分布警告: A+B=0，机制综述缺乏机制实验论文"]
- 建议优先分析顺序: [按类型A→B→C→D→F→E→G→H→I→J排序]
```

---

### 质量对冲: 审校Agent 抽样复核

审校Agent 从 Round 2 排除列表中随机抽取 15-20%:
- 复核排除理由是否合理
- 尤其是"方法学质量不可接受"这类主观判断 → 需审校Agent 独立验证
- 如果抽样错误率 > 10% → 整个筛选批次标记为不可靠 → 复审

---

## Agent 5: 评估Agent (Quality Assurance)

### 触发条件
**极简命令**: `评估` `评` `7` `evaluate` `跑评估`
**自动**: 编码Agent 在每个 Phase 完成时自动提示

### 职责
独立的质量判断角色，与编码Agent 分离以保证客观性：
- **编码Agent 负责收集数据**（机械性提取效率指标、安全日志）
- **评估Agent 负责判断质量**（需要独立视角的评估项）

### 输入
- `progress/metrics-raw.json` — 编码Agent 收集的原始数据
- `git diff` / `git log` — 本次 Phase 的变更
- `features/FEATURE_LIST.md` — 任务完成情况
- `harness/metrics.md` — 度量定义和判定标准
- `harness/safety-policy.md` — 安全规则
- `harness/test-scenarios.md` — 鲁棒性测试场景
- `harness/consistency-benchmarks.md` — 一致性基准

### 工作流

#### 步骤1: L2 成功率判定
1. 读取 `progress/metrics-raw.json`，对每个 L1_PASS 的任务
2. 调用**审校Agent** 对产出物做 L2 业务质量评分（1-5 分，按 `harness/metrics.md` 的维度）
3. 综合 L1 + L2 得出最终成功率判定

#### 步骤2: 效率分析
1. 读取效率指标，与历史基线对比（基线从 `harness/eval-log.md` 历史记录推断）
2. 标记偏离基线 2σ 的项目
3. 标记效率单调恶化的趋势

#### 步骤3: 鲁棒性测试
1. 从 `harness/test-scenarios.md` 选择本 Phase 的测试场景（L1-L5 各 1-2 个）
2. 对每个场景，构造任务发给对应 Agent，观察行为
3. 按行为模式判定 ✅ / ⚠️ / ❌
4. 记录到 `harness/reports/robustness-phase-N.md`

#### 步骤4: 安全复核
1. 读取 `progress/metrics-raw.json` 的 `safety.violations`
2. 对 MEDIUM 级别进行误报排查
3. 对 CRITICAL/HIGH 级别确认并通知用户
4. 生成安全趋势分析

#### 步骤5: 一致性测试
1. 从 `harness/consistency-benchmarks.md` 选择本 Phase 的基准任务
2. 每个基准跑 2 次（独立 Agent 调用）
3. 对比两次的行为路径（工具调用序列编辑距离）
4. 调用**审校Agent** 对比两次的语义输出
5. 记录到 `harness/reports/consistency-phase-N.md`

#### 步骤6: 生成综合评估报告
1. 汇总五维度得分
2. 计算 Phase 综合评分:
   ```
   Phase 综合分 = 成功率×0.35 + 效率×0.10 + 鲁棒性×0.20 + 安全性×0.15 + 一致性×0.20
   ```
3. 写入 `harness/reports/phase-N-report.md`
4. 追加摘要到 `harness/eval-log.md`
5. 提炼改进项（Improvement Items）

### 输出
- `harness/reports/phase-N-report.md` — 综合评估报告
- `harness/reports/robustness-phase-N.md` — 鲁棒性测试详情
- `harness/reports/consistency-phase-N.md` — 一致性测试详情
- `harness/eval-log.md` 新增条目
- 改进项清单（反馈给用户）

### 执行节奏
| 评估项 | Phase内频率 | 说明 |
|--------|-----------|------|
| L2 成功率 | 每个任务 | 编码Agent 完成一个任务后触发 |
| 效率分析 | 每 Phase | 批量汇总 |
| 鲁棒性测试 | 每 Phase | 批量跑 L1-L5 |
| 安全复核 | 每 Phase | 审计编码Agent的发现 |
| 一致性测试 | 每 Phase | 重跑基准任务 |

---

## Agent 5v2: 评估Agent (2026-06-05 改进版)

### 新增：Gate 4/5/6 可执行脚本

评估Agent 现在携带完整的自动化验证脚本（见 `harness/quality-gate.md`）：

- `gate4_verify.py`: 20项声明 vs PMID摘要交叉验证
- `gate5_check.py`: 范围引用展开 + 编号一致性 + 未使用引用检测
- `gate6_citation_scope.py`: 引用范围合规 — 类型×声明交叉验证
- `word_format_check.py`: 嵌入 gen_word_full.py 的 8 项自检

### 新增：错误模式库匹配
评估时检查是否触发了已知错误模式：
- `引用嫁接`: 声明关键词 vs 引用摘要关键词 匹配度 < 30%
- `编号漂移`: 图/表引用集合 != 已声明保留集合
- `范围遗漏`: 正文有 [N-M] 但解析器只提取了 N
- `压缩丢失`: Word 词数 < 源文件词数 × 0.85
- `引用越权` (2026-06-05): E类支撑因果声明 / G类做主引用 → Gate 6 检测
- `类型误判` (2026-06-05): 喉鳞癌/头颈鳞癌被纳入 → Round 0 硬排除
- `Step跳过` (2026-06-05): Agent 跳过门禁步骤 → Step 0 标记为不可跳过

---

---

## Agent 间协作流程 (2026-06-05 更新)

```
用户: "主题" → 确定综述方向 (更新 active-focus.md)
    │
    ▼
用户: "搜索" 或 "1"
    │
文献搜索Agent [Agent 1]
    ├─ Step 0: 数据库需求评估（门禁，不可跳过）
    ├─ Step 1: Tier 1 自动检索 (PubMed + S2 + EPMC + CT.gov)
    ├─ Step 2: Tier 2 手动清单 (Embase/Cochrane/CNKI等)
    │       │
    │   用户:"就绪" → 继续合并去重+五层验证
    │
    └─ Handoff ──→ 用户: "筛选" 或 "2"
                        │
                        ▼
                  筛选Agent [Agent 6]
                    ├─ Round 0: 论文类型分类 (A-J)
                    ├─ Round 1: PICO + 类型条件筛选
                    ├─ Round 2: 全文 + 引用范围分配 + 健康检查
                    └─ Handoff (含类型标签+引用范围) ──→ 用户: "分析" 或 "3"
                                                        │
                                                        ▼
                                                  论文分析Agent [Agent 2]
                                                    逐篇结构化笔记 → docs/papers/
                                                    笔记包含: 论文类型 + 引用范围字段
                                                        │
                                                        ▼
                                                  用户: "写作" 或 "4"
                                                        │
                                                        ▼
                                                  综述写作Agent [Agent 3]
                                                    笔记→草稿 → jitc_submission.md
                                                    含: 引用范围匹配 + Gate 4/5/6 自检
                                                        │
                                                        ▼
                                                  用户: "审校" 或 "5"
                                                        │
                                                        ▼
                                                  审校Agent [Agent 4]
                                                    事实核查 + 逻辑 + 自然度(6反模式)
                                                    + 引用范围合规 + 喉鳞癌过滤
                                                        │
                                                   ┌────┴────┐
                                                   ▼         ▼
                                           用户:"编码/6"  用户:"评估/7"
                                                   │         │
                                            编码Agent    评估Agent
                                            进度+效率+安全   L2+鲁棒+一致
                                            每2-3任务      每Phase
```
