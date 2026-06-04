# Agent 专业化定义

本文件定义了综述写作项目中的5个横向执行Agent + 2个纵向基础设施Agent（共7个）。每个Agent有极简命令触发、完整的输入输出规范和prompt模板。

---

## Agent 0: 编码Agent (Infrastructure)

### 触发条件
- **手动极简命令**: `编码` `记` `6` `记录进度` `commit progress`
- **自动**: 每个工作阶段完成时 CLAUDE.md 会话流程自动提示

### 输入
- 当前会话的上下文（完成的工作内容）
- `features/FEATURE_LIST.md`
- `memory/project-status.md`
- `git status` / `git diff --stat`

### 工作流

#### Part A: 进度记录（原有职责）
1. 检查 git 变更状态
2. 读取 `features/FEATURE_LIST.md`，匹配完成的任务
3. 更新任务勾选状态
4. 更新 `memory/project-status.md` 统计数据
5. 追加 `progress/SESSION_LOG.md`
6. 如有新发现或决策，更新 `memory/key-findings.md` 或 `memory/decisions.md`

#### Part B: 效率数据收集（新增 — Harness Engineering）
7. 从会话上下文提取效率指标，写入 `progress/metrics-raw.json`:
   - **wall_time_sec**: 任务耗时（需从会话时间戳推算）
   - **tool_calls**: 工具调用总次数
   - **tools**: 各工具调用次数明细 `{WebFetch: N, Bash: N, Write: N, Read: N, Edit: N, ...}`
   - **tokens_in / tokens_out**: 从会话摘要或 API 记录获取
   - **compactions**: 上下文压缩次数
8. 从会话日志提取工具调用序列: `["Read", "WebFetch", "Write", ...]`

#### Part C: 安全审计（新增 — Harness Engineering）
9. 扫描会话中的所有操作，对照 `harness/safety-policy.md` 的检测规则:
   - 文件越界检查（Read/Write/Edit 路径是否在允许范围内）
   - 网络越界检查（WebFetch 域名是否在白名单内）
   - 命令越界检查（Bash 命令是否匹配允许模式）
   - 配置篡改检查（是否修改了 CLAUDE.md 或 settings.json 等敏感文件）
   - 信息泄露检查（URL/命令中是否包含 API key 模式）
10. 将违规写入 `progress/metrics-raw.json` 的 `safety` 字段

#### Part D: Git 提交
11. git commit 所有变更（含 metrics-raw.json），使用结构化 commit message `[phase] 简短描述`

### 输出
- 表格总结本次更新内容
- 效率指标摘要
- 安全审计摘要（如有违规）
- 建议的下一步任务
- `progress/metrics-raw.json` 文件（供评估Agent 读取）

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
3. 按 `docs/papers/template.md` 模板结构化提取:
   - 元数据 (PMID, 期刊, 年份, 作者, 引用数)
   - PICO (临床研究) 或研究框架 (基础研究)
   - 核心方法
   - 关键发现与数据
   - 局限性
   - 与本综述的关联
4. 写入 `docs/papers/[topic]/[第一作者姓氏][年份]-[关键词].md`
5. 更新 `docs/index.md` 文献统计
6. 如发现重要论点，提示更新 `memory/key-findings.md`

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
- `docs/papers/` — 对应主题的论文笔记
- 用户指定的目标章节

### 工作流
1. 读取大纲确定写作位置
2. 加载相关论文笔记 (根据章节主题从 `docs/papers/` 检索)
3. 加载 `memory/key-findings.md` 对应主题的论点
4. 按学术综述写作规范撰写:
   - 逻辑流: 背景 → 现状 → 进展 → 争议 → 展望
   - 引用管理: 每句话如来自文献，标注 PMID/DOI
   - 避免简单的 "A found X, B found Y" 堆砌 → 改为主题式综合
5. 写出初稿到 `manuscript/draft.md` 对应章节
6. 标记引用了哪些论文笔记

### 输出
- 写入 `manuscript/draft.md` 的段落
- 引用的 PMID 列表
- 标记哪些论点需要更多文献支撑

### 写作风格要求
- 英文写作，学术正式但不晦涩
- 主动语态为主，避免过度被动
- 段落结构: Topic sentence → Evidence synthesis → Transition
- 避免: "Interestingly", "It is worth noting that" 等冗余表达
- 数据陈述必须精确: "increased by 34% (95% CI: 28-40%, p<0.001)" 而非 "significantly increased"

---

## Agent 4: 审校Agent

### 触发条件
**极简命令**: `审校` `审` `5` `review` `核查` `检查草稿`

### 输入
- `manuscript/draft.md` — 待审草稿
- `docs/papers/` — 对应论文笔记（交叉验证引用）
- `memory/decisions.md` — 关键决策记录（检查一致性）

### 工作流
1. **事实核查**: 逐条验证引用是否准确反映原始论文
2. **逻辑审查**: 检查段落间过渡、论证链条完整性
3. **语言润色**: 检查语法、拼写、学术表达规范
4. **引用完整性**: 检查每个声明是否有文献支撑
5. **一致性检查**: 术语使用、缩写定义、数字格式
6. 输出审校报告: 严重问题 (must fix) + 建议 (nice to have)

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

#### Round 1: 标题/摘要筛选 (目标: ~500 → ~80)

逐篇基于标题+摘要判定，**宁滥勿缺策略**:

| PICO 维度 | 判定 |
|-----------|------|
| Population 匹配 | YES → 通过; NO(关键) → EXCLUDE; UNCERTAIN → INCLUDE |
| Intervention/Exposure 匹配 | 同上 |
| Comparison 匹配 | 同上 |
| Outcome 匹配 | 同上 |
| 研究设计符合纳入标准 | YES → 通过; NO → EXCLUDE + 原因代码 |

**排除原因代码**:
- `WRONG_POPULATION` — 人群不匹配
- `WRONG_INTERVENTION` — 干预/暴露不匹配
- `WRONG_OUTCOME` — 结局指标不匹配
- `WRONG_DESIGN` — 研究设计不符合
- `NOT_ORIGINAL` — 非原始研究/综述/评论/信件
- `DUPLICATE` — 重复文献
- `NO_ABSTRACT` — 无摘要 → INCLUDE (宁滥勿缺)
- `LANGUAGE` — 语言不符合纳入标准
- `OTHER` — 其他（需填写具体原因）

**宁滥勿缺底线**: 任何 UNCERTAIN → INCLUDE。只有明确违反关键纳入标准 → EXCLUDE。

**中文文献特殊处理**:
- 中文期刊摘要信息不足 → 标记为 `LOW_INFO_ABSTRACT` → INCLUDE
- Round 2 全文阶段再判断

#### Round 2: 全文筛选 (目标: ~80 → 30-40)

1. 检查全文获取状态:
   - 已获取全文 (Tier 1 OA + Tier 2 VPN) → 正常读取全文判定
   - 仅摘要 (Tier 4) → 基于摘要 + Semantic Scholar TLDR 判定 → 标记 ⚠️
   
2. 逐篇重新按 PICO 判定（全文信息比摘要完整）

3. 额外判定维度:
   - 方法学质量是否可接受？
   - 数据报告是否完整（样本量、效应量、CI）？
   - 是否存在明显利益冲突？
   - 是否为掠夺性期刊？

4. 判定:
   - 符合全部标准 → **INCLUDE**
   - 有疑虑但可接受 → **INCLUDE + 标注疑虑** (如 `⚠️ 高偏倚风险`)
   - 不符合关键标准 → **EXCLUDE + 引用全文中的具体段落作为证据**

5. **仅摘要比例控制**:
   - 计算当前仅摘要论文占 INCLUDE 的比例
   - 如果 > 20% → ⚠️ 标记 → 建议优先获取 Tier 2/3 全文
   - 仅摘要论文在最终列表中标注 `⚠️ ABSTRACT ONLY`

---

### 输出

#### 筛选报告结构

```markdown
## 筛选报告 — [主题] — YYYY-MM-DD

### Round 1: 标题/摘要筛选
- 筛选前: N 篇
- 排除: M 篇 (原因分布见下表)
- 纳入: K 篇 (含 X 篇 UNCERTAIN, Y 篇 LOW_INFO_ABSTRACT)

| 排除原因 | 数量 |
|---------|------|
| WRONG_POPULATION | 45 |
| WRONG_INTERVENTION | 30 |
| WRONG_DESIGN | 25 |
| NOT_ORIGINAL | 20 |
| ... | ... |

### Round 2: 全文筛选
- 筛选前: K 篇
- 全文可获取: P 篇 (XX%)
- 仅摘要: Q 篇 (XX%) — [✅ ≤20% / ⚠️ >20%]
- 排除: L 篇
- **最终纳入: J 篇**

| 排除原因 | 数量 | 证据强度 |
|---------|------|---------|
| WRONG_OUTCOME | 8 | 全文验证 |
| 方法学质量不可接受 | 5 | 全文方法学段落 |
| ... | ... | ... |

### PRISMA 流程图数据
- 检索命中: N
- 去重后: N'
- Round 1 纳入: K
- Round 2 纳入: J
- (提供完整 PRISMA 流程图所需数字)

### Handoff 给分析Agent
- 最终纳入列表: [J 篇 PMID + 标题 + 全文状态]
- ⚠️ 仅摘要论文: Q 篇 (标注在列表中)
- 已知问题:
  1. [如"XX 篇中文文献摘要信息不足，已纳入但标注待全文核实"]
  2. ...
- 建议优先分析顺序: [按重要性/置信度排序]
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

## Agent 间协作流程

```
用户: "主题" → 确定综述方向 (更新 active-focus.md)
    │
    ▼
用户: "搜索" 或 "1"
    │
文献搜索Agent [Agent 1]
    ├─ Tier 1 自动检索 (PubMed + S2 + EPMC + CT.gov)
    ├─ Tier 2 手动清单 (Embase/Cochrane/CNKI等)
    │       │
    │   用户:"就绪" → 继续合并去重+五层验证
    │
    └─ Handoff ──→ 用户: "筛选" 或 "2"
                        │
                        ▼
                  筛选Agent [Agent 6]
                    ├─ Round 1: 标题/摘要 (宁滥勿缺)
                    ├─ Round 2: 全文 (≤20%仅摘要)
                    └─ Handoff ──→ 用户: "分析" 或 "3"
                                        │
                                        ▼
                                  论文分析Agent [Agent 2]
                                    逐篇结构化笔记 → docs/papers/
                                        │
                                        ▼
                                  用户: "写作" 或 "4"
                                        │
                                        ▼
                                  综述写作Agent [Agent 3]
                                    笔记→草稿段落
                                        │
                                        ▼
                                  用户: "审校" 或 "5"
                                        │
                                        ▼
                                  审校Agent [Agent 4]
                                    事实核查+逻辑+引用溯源
                                        │
                                   ┌────┴────┐
                                   ▼         ▼
                           用户:"编码/6"  用户:"评估/7"
                                   │         │
                            编码Agent    评估Agent
                            进度+效率+安全   L2+鲁棒+一致
                            每任务执行     每Phase执行
```
