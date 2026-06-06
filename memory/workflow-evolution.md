# 流程演进轨迹

> 记录每次因项目运行歧义触发的商讨及由此产生的**项目文件修改**。
> 每条记录的核心是"改了什么文件"——日志只是修改的副作用。

## E010: gen_word_full.py 无Markdown表格渲染导致Word表格乱码 — 2026-06-06

- **触发**: 用户发现Word文档§4.4和§11.6的表格显示异常——管道表格（`| col | col |`）被当作普通段落渲染，管道符和分隔线显示为乱码
- **根因**: `gen_word_full.py` 的 block 处理循环（L316-361）完全没有 Markdown 管道表格的检测和渲染逻辑。管道表格行落入"Regular paragraph"分支，被 `' '.join()` 拼接为一行——`| Feature | Caffeine | PCS |` 变成了一行带管道符的乱码文本
- **影响范围**: 稿件中 3 处管道表格均受影响：
  - Methods §Search Strategy: 数据库搜索表（3行×3列）
  - §4.4: 咖啡因 vs 产后皮质激素对比表（6行×3列）
  - §11.6 Table 1: 证据成熟度总表（7行×5列）
- **修改**:
  - `scripts/gen_word_full.py` → 新增 3 个函数：
    - `_detect_pipe_table(block)` — 检测 block 是否为管道表格（所有行以 `|` 开头 + 存在分隔行）
    - `_render_md_table(block)` — 解析管道表格并渲染为 `python-docx` Table 对象（支持 **粗体** 和 *斜体* 内联格式、表头着色、斑马条纹）
    - `_cell_runs(cell, text)` — 单元格格式化渲染，保留 Markdown 内联格式
  - `scripts/gen_word_full.py` → loop 逻辑修改：
    - `for block in blocks` → `while i < len(blocks)` 支持 look-ahead
    - 当 `**Table N.**` marker 的下一 block 是管道表格时，跳过 PNG 嵌入，改为渲染原生表格（避免双重渲染）
    - 在 "Regular paragraph" 前新增管道表格检测分支
  - `CLAUDE.md` 错误模式库 → 追加 `管道表格丢失` (E010)
- **效果**: 所有 Markdown 管道表格自动检测并渲染为可编辑的 Word 原生表格；`**Table N.**` marker + 管道表格组合不再产生双重渲染

## E009: 审校报告修复执行后缺少旧值零匹配验证 — 2026-06-06
- **触发**: R3 审校修复中数值变更（如 17/40→18/42）后，未自动运行 `grep -n "旧值"` 验证旧值已完全消除
- **根因**: CLAUDE.md "增量审校与版本管理"中的"自行复查检查清单"包含旧值零匹配验证命令，但审校 Agent 在修复执行时未将其作为强制性自动化步骤
- **修改**:
  - `CLAUDE.md` 自行复查检查清单 → 旧值零匹配验证命令从手动提示升级为 Agent 强制执行步骤
- **效果**: 所有审校修复后自动运行旧值零匹配验证，防止数值漂移

## E008: Cochrane引用计数在参考文献总数变化后未重新计算 — 2026-06-06
- **触发**: R4修复添加2篇CAP随访论文（ref [41][42]）后，总引用数从40变为42，Abstract和§11.7中的 "42.5% (17 of 40)" 自动失效。且重新计数发现Cochrane实际为18篇（非17篇）
- **根因**: 
  - 引用计数依赖人工，无自动化脚本在每次参考文献变更后重新计算Cochrane占比
  - 初始计数值（17篇）本身可能就有误差
- **修改**:
  - 在审校流程中新增引用计数自动检查（python regex 匹配 `Cochrane Database of Systematic Reviews` 计数）
  - CLAUDE.md Gate 6 追加：引用总数变更时强制重新计算 Cochrane 百分比
- **效果**: 任何参考文献增删后，审校 Agent 自动重新计算并更新所有相关位置

## E007: gen_word_full.py Table marker + 管道表格双重渲染 — 2026-06-06
- **触发**: §11.6 的 `**Table 1. caption**` marker 触发 PNG 图片嵌入，同时下方的管道表格被新增的渲染器渲染为 Word 原生表格，导致 Table 1 在 Word 中出现两次
- **根因**: 管道表格渲染器（见 E010）与现有的 Figure/Table marker 图片嵌入逻辑存在功能重叠——marker 和管道表格本应是同一个表格的"标题"和"内容"，但脚本将它们作为两个独立的 block 处理
- **修改**:
  - `scripts/gen_word_full.py` → block loop 改为 `while i < len(blocks)` 支持 look-ahead
  - 当 `**Table N.**` marker 的下一个 block 是管道表格时，跳过 PNG 嵌入，使用 marker 文字作为表格标题，直接渲染原生表格
  - `**Figure N.**` marker 不受影响（Figure 无管道表格对应物）
- **效果**: Table 1 在 Word 中以单一原生表格呈现（含居中粗体标题），无重复

## E006: §5.4 节标题下无正文段落 — 2026-06-06
- **触发**: R5审查发现§5.4 "The Follow-up Gap: Why It Matters" 标题后仅有空行，直接跳到 Clinical Perspective 框
- **根因**: 写作Agent在生成 Clinical Perspective 框时未检查前方是否有引导段落；标题→空行→框 的结构是部分章节的模板化残留
- **修改**:
  - 在 CLAUDE.md 写作纪律中新增 "Clinical Perspective 框前必须有引导段落" 规则
  - Agent 3 写作Agent 的 Step 5 (Perspective Box Insertion) 追加检查：验证每个 perspective box 之前存在 ≥2 句引导段落
- **效果**: 所有 Clinical Perspective / Family Context 框前均有引导段落

## E005: OR与HR在同一句中混用未说明度量差异 — 2026-06-06
- **触发**: R5审查发现§2.2的 Ninan 2022 meta-analysis 引用在同一句中从 OR 0.69 切换到 HR 1.47，未向读者解释两种度量的本质区别
- **根因**: 源文献(Ninan 2022)本身使用了不同度量——OR用于病例对照/队列研究，HR用于基于注册表的time-to-event分析。稿件忠实复制了源文献的数字，但未向读者说明度量差异的由来
- **修改**:
  - 在 CLAUDE.md 写作纪律中新增 **度量一致性规则**：同一句中混合 OR/RR/HR 时，必须加括号说明每种度量的来源（e.g., "this hazard ratio derives from registry-based time-to-event analyses"）
  - Agent 4 审校Agent Step 5 (数据准确性) 追加：检测 OR/HR/RR 混合使用位置，验证是否存在度量差异说明
- **效果**: 所有跨度量引用均包含来源说明

## E004: Impact Statement中精确统计量重复4次 — 2026-06-06
- **触发**: "1.4% (8 of 590)" 在Abstract/Impact Statement/§10/§12 共出现4次，R5审查建议减少
- **根因**: 无规则约束同一关键统计量的最大出现次数；审校Agent在一致性检查时确保数值相同，但未检测冗余
- **修改**:
  - 在 CLAUDE.md 写作纪律中新增 **统计量去重规则**：同一精确统计量（含分子分母的分数形式）在全文中出现次数 ≤3
  - Agent 4 审校Agent Step 2 (一致性扫描) 追加：统计量出现次数统计，>3次时报警
- **效果**: 关键统计量在 Abstract、首次报告位置、Conclusions 各出现一次，其余位置用概数替代

## E003: 审校修复后参考文献总数变化导致百分比/分数失效 — 2026-06-06
- **触发**: R4修复参考文献后Abstract/§11.7中的"17 of 40 (42.5%)"变为"18 of 42 (42.9%)"，需手动更新两处
- **根因**: 参考文献计数（分子+分母）嵌入正文的4个位置，增删引用后无自动化更新机制
- **修改**:
  - 审校Agent R4+ 修复流程追加 Step 0: 引用增删后自动检测并更新所有引用计数位置
- **效果**: 参考文献增删后自动 re-count 并批量更新所有相关位置

---

## E001: gen_word_full.py 硬编码跨项目残留 — 2026-06-05
- **触发**: NRDS综述生成Word时，标题页显示LUSC标题，Figure/Table插入全部失败
- **根因**: gen_word_full.py 硬编码了上一项目的标题、section名称匹配、图表文件名、关键词、运行标题等所有主题相关内容
- **修改**:
  - `scripts/gen_word_full.py` → 完全重写为通用版：自动检测标题、自动匹配Figure/Table文件、通用声明段提取、基于文件而非硬编码的自检
  - `scripts/audit_manuscript.py` → **新建**：生成Word前运行10项检查（重复Reference段/引用完整性/章节连续/Abstract无图表引用等）
  - `CLAUDE.md` 错误模式库 → 追加 `硬编码残留` + `编辑破坏引用段`
- **效果**: 未来任何新综述项目只需修改gen_word_full.py顶部的OUT/FIG_DIR/SRC三个路径即可使用

## E002: 增量Edit破坏markdown引用段结构 — 2026-06-05
- **触发**: 3次出现重复 `## References` 段，丢失全部引用或只保留1条
- **根因**: Edit工具在长文件中查找替换时，新旧内容同时包含`## References\n\n1.`导致重复；Python分割脚本过滤掉了Abstract/Title
- **修改**:
  - `scripts/rebuild_refs.py` → 标准化引用段重建工具
  - `scripts/audit_manuscript.py` → 检测重复Reference段（重构前必跑）
- **效果**: 每次大段插入后用rebuild_refs.py重建；生成Word前audit_manuscript.py自动拦截重复段
> 与 `decisions.md` 的区别：
> - `decisions.md` — 论文主题相关决策（选刊、范围、方法）
> - `workflow-evolution.md` — 项目运行机制的修正（本文件）

---

## E001: 流程演进协议建立 — 2026-06-05

- **触发**: 用户审阅项目后发现：执行中遇到的歧义无法在事前全部预定义，需要运行中发现问题并改进流程。用户进一步明确：商讨的产出应该是项目文件的代码修改，而非仅仅是日志记录。
- **根因**: 原有 CLAUDE.md 仅有"启动确认"（瀑布式），缺少运行中歧义升级机制，更缺少"商讨→改文件→下次自动处理"的自改进闭环。
- **修改**:
  1. `CLAUDE.md` — 新增"流程演进协议"完整章节（自治边界 + 升级格式 + 商讨产出文件修改矩阵 + 教训极简命令 + 演进记录格式）
  2. `CLAUDE.md` — 命令表新增 `教训` / `lesson` 触发词
  3. `CLAUDE.md` — 会话流程新增步骤 3（歧义升级）和步骤 4（教训捕获）
  4. `memory/workflow-evolution.md` — 本文件创建
  5. `memory/MEMORY.md` — 新增本文件索引条目
- **效果**: 
  - Agent 在置信度 < 70% 或发现规则矛盾时自动暂停并升级
  - 每次商讨的产出是对 CLAUDE.md / agent-specializations.md / harness/ 等项目文件的直接修改
  - 同类歧义第二次遇到时，Agent 直接应用已修改的规则，不再需要人
  - 用户随时说 `教训：xxx` 即可触发流程缺陷的根因分析和文件修补

---

## E002: 语言自然度反模式体系 — 2026-06-05

- **触发**: 用户指出写作语言过于死板，但并非要求华丽炫技，而是希望更自然。同时用户提出一个深层问题："自然"如果有标准，是否自相矛盾？
- **根因**: 
  - 原有写作纪律仅有正面规范（"主动语态为主""避免过度被动"），没有可检测的僵硬指标
  - 审校Agent 的语言检查仅限于语法/拼写，没有自然度维度
  - 关键认识：**"自然"无法被正面规定，但"僵硬"可以被精确检测。自然 = 不僵硬 = 高方差。**
- **讨论要点**: 
  - "自然"的正面标准确实自相矛盾——规定出来的东西正是自然的反面
  - 但僵硬有明确定义：低方差——句子长度均质、过渡词重复、段落结构模板化、名词化链堆积、被动语态连续使用
  - 因此采用**反模式方法**：不定义"应该怎么写"，只定义"不应该怎么写"
  - 每个反模式都是可机械检测的（审校Agent 可以逐段扫描并标记位置）
- **修改**:
  1. `CLAUDE.md` 写作纪律 — 新增"语言自然度"小节，定义 6 个僵硬反模式 + 检测规则 + 级别（Must Fix / Nice to Have / 直接删除）
  2. `CLAUDE.md` 写作纪律 — 新增"语言自然度检查流程"（Step 6 自然度扫描 + 段落通过率统计 + 目标 ≥ 80%）
  3. `memory/agent-specializations.md` Agent 4 审校Agent 工作流 — 新增 Step 6 语言自然度扫描
  4. `memory/agent-specializations.md` Agent 4 审校Agent 输出格式 — 统计区新增"语言自然度: X/X 段落通过"
  5. `memory/agent-specializations.md` Agent 3 综述写作Agent 写作风格 — 新增"语言方差"要求和自然度反模式引用
- **效果**:
  - "自然"不复是模糊的主观感受，而是 6 个可检测、可统计、可追踪的反模式
  - 审校Agent 每次审校自动跑自然度扫描，输出段落通过率
  - 反模式可以被逐步追加（流程演进协议），每次发现新的僵硬来源就追加一条反模式
  - 反模式方法不与"自然"概念自相矛盾——它只清除病态，不规定健康应该长什么样
- **6 反模式速览**:
  1. 名词化链（≥3 名词化动作/句）
  2. 过渡词单调（连续 ≥3 段同类型过渡词）
  3. 句子长度均质（段落内无 < 12 词短句且无 > 35 词长句）
  4. 被动语态堆积（连续 ≥4 句被动）
  5. 段落结构模板化（≥3 连续段相同结构）
  6. 空洞强调词（"Interestingly"等 → 直接删除）

---

## E003: 论文类型×证据权重的二维筛选框架 — 2026-06-05

- **触发**: 用户指出文献筛选的纳入要求需要商榷——不同类型文章在综述中的功能不同，应有不同的纳入门槛和引用范围，而非一把尺子量所有论文
- **根因**: 
  - 原有 Agent 6 筛选仅使用 PICO 框架（人群、干预、对照、结局），所有论文放在同一标准下判定
  - PICO 能判断"是否相关"，但不能判断"能支撑什么"
  - 导致当前 62 篇纳入论文中：65% 为纯生信关联分析，0% 为机制实验论文，≥2 篇不应纳入（喉鳞癌、非鳞NSCLC试验）
  - 写作Agent 和审校Agent 没有论文类型概念，生信论文的关联性声明被当作因果机制使用
- **讨论要点**:
  - 机制综述的核心证据链需要实验论文（A/B/C 类）支撑，纯生信（E 类）只能提供相关性假说
  - 综述（G 类）和病例报告（I 类）不能作为主引用——综述无新数据，病例不能代表群体
  - 每种论文类型需要明确的"引用范围"标签——规定它可以支撑什么声明、不能支撑什么
  - 筛选阶段就分配引用范围，贯穿后续的写作和审校
- **修改**:
  1. `memory/agent-specializations.md` Agent 6 工作流 — 全新三轮筛选体系（Round 0 类型分类 + Round 1 PICO+类型条件 + Round 2 全文+引用范围分配+健康检查）
  2. `memory/agent-specializations.md` Agent 6 输出格式 — 新增类型分布表 + 引用范围概要 + 健康检查
  3. `CLAUDE.md` 写作纪律 — 新增"引用范围纪律": 3 条绝对禁止 + 3 条限定语 + 审校核查
  4. `memory/agent-specializations.md` Agent 3 工作流 — Step 3 类型确认 + Step 5 引用范围匹配 + 输出自查表
  5. `memory/agent-specializations.md` Agent 4 工作流 — Step 7 引用范围合规检查 + 输出统计
- **效果**:
  - 筛选不再是"相关 vs 不相关"的二元判定，而是"相关 + 能支撑什么"的二维判定
  - 每篇论文带有类型标签（A-J）和引用范围标签
  - 类型分布健康检查防止机制综述变成纯生信堆砌
  - 写作和审校环节的引用越权可以被机械检测

---

## E004: 领域知识结构层 (Module A) — 2026-06-06

- **触发**: NRDS 综述的 AI 写作不足分析识别了"沉默失明"（#3）——AI 系统性遗漏了咖啡因、维生素 A、iNO、利尿剂等关键干预。系统需要一种机制来主动发现"自己不知道什么"。
- **根因**: 原有流水线没有独立的领域知识结构。Agent 3（写作）只处理显式输入的子集，无法检查"遗漏了什么"。Agent 1（搜索）只检索用户指定的主题，不会主动构建领域全貌。
- **修改**:
  1. `knowledge/domain-ontology-template.md` → **新建** — 领域本体模板（干预清单+空白分级+紧迫性评分+交互地图+缺失报警）
  2. `harness/evidence-gap-grading.md` → **新建** — G0-G4 证据空白分级框架
  3. `harness/priority-scoring.md` → **新建** — 4 维度临床紧迫性评分标准
  4. `memory/agent-specializations.md` Agent 1 → 新增 Step 7 (领域本体构建)，门禁级，不可跳过
  5. `CLAUDE.md` → 新增 Tier 3 条目 + Gate 7 定义
  6. `memory/MEMORY.md` → 新增索引
  7. `harness/quality-gate.md` → 新增 Gate 7
- **效果**: 系统现在在检索完成后自动构建领域本体——从指南/综述中提取干预清单，对每个干预做 G0-G4 空白分级，计算临床紧迫性评分，生成缺失干预报警。沉默失明被结构性解决。

## E005: 写作前规划层 (Module D) — 2026-06-06

- **触发**: 缺陷 #4（平均主义）和 #10（时间扁平化）需要在写作之前而非之后解决。平均主义不能在审校时修复——篇幅已经写完了。
- **根因**: 原有 Agent 3 直接开始写作，没有基于领域本体的篇幅分配和证据时效规划步骤。
- **修改**:
  1. `harness/time-annotation.md` → **新建** — 证据新鲜度衰减规则（Band 0-4 + 研究类型特定衰减因子 + 加速老化因子）
  2. `memory/agent-specializations.md` Agent 3 → 新增 Steps 0a-0f（写作前规划），门禁级
  3. `CLAUDE.md` → 新增 Tier 3 条目 + Gate 8
  4. `memory/MEMORY.md` + `harness/quality-gate.md` → 新增 Gate 8
- **效果**: 写作前强制生成了 priority-weighted section allocation、gap-to-emphasis mapping、time annotation schedule 和 coverage report。LISA (G4, urgency 8.5) 自动获得 Deep 处理；HFOV (urgency 3.2) 获得 Brief 处理。

## E006: 合成推理层 (Module B) — 2026-06-06

- **触发**: 缺陷 #2（缺乏合成）、#7（优雅空洞）、#9（临床场景缺失）需要一种新的认知模式——不是写作也不是审校，而是跨文本的结构化推理。
- **根因**: 原有流水线在"写作 → 审校"之间缺少一个合成推理步骤。跨干预比较、交互假设生成、临床决策框架、论证多样性扫描——这些都需要独立的 Agent。
- **修改**:
  1. `harness/cross-intervention-matrix.md` → **新建** — 7 维度比较矩阵模板
  2. `harness/synthesis-reasoning.md` → **新建** — 全部 7 步工作流规则（含假设循环协议）
  3. `harness/clinical-decision-framework.md` → **新建** — 临床决策框架模板
  4. `memory/agent-specializations.md` → 新增 Agent 7 完整定义 + 更新协作流程图
  5. `CLAUDE.md` → 新增 `合成`/`8` 触发命令 + Gate 9 + Tier 3 + 错误模式库
  6. `memory/MEMORY.md` + `harness/quality-gate.md` → 新增 Gate 9
- **效果**: 引入假设循环（推断→定向检索→VERIFIED/HYPOTHESIS）、Pattern A 检测与转换、临床决策框架生成、时间演变标注、覆盖完整性验证。所有合成插入用 HTML comment 溯源，防黑箱。

## E007: 审校增强层 (Module C) — 2026-06-06

- **触发**: 缺陷 #5（视角单一）、#6（RR 无 NNT）、#8（Cochrane 崇拜）需要在审校时系统性地修复。
- **根因**: 原有 Agent 4 关注事实准确性、逻辑、语言流畅度——但没有专门的视角多样性、数据翻译、批判吸收检查。
- **修改**:
  1. `harness/perspective-switching.md` → **新建** — 5 种强制视角切换规则（临床/家庭/LMIC/政策/研究者）
  2. `harness/data-translation.md` → **新建** — RR→ARR/NNT 翻译协议
  3. `harness/argument-diversity-enforcement.md` → **新建** — 论证类型分布要求 + Pattern A 转换规则
  4. `harness/critical-absorption.md` → **新建** — Cochrane 5 检查批判规则
  5. `memory/agent-specializations.md` Agent 4 → 新增 Pre-Pass 1-2 + Post-Pass 3-4 + 增强统计
  6. `CLAUDE.md` → 新增 Gate 10 + Tier 3 + 错误模式库扩展
  7. `memory/MEMORY.md` + `harness/quality-gate.md` → 新增 Gate 10
- **效果**: Agent 4 现在在每个干预证据总结后插入临床/家庭/LMIC 视角；每个 RR 值翻译为 ARR/NNT；残留 Pattern A 被二次检测；每篇高引 Cochrane 综述获得批判性限定语。

---

---

## E008: Agent 4 Step 1.5 — 绝对否定声称矛盾检测 (Phase 7.6b) — 2026-06-06

- **触发**: 同行评审 #4 指出 Gibson 2015 报告了成人肺功能数据，与稿件"no adult data"的绝对声称矛盾。这不是引用错误——是声称绝对性缺乏限定。
- **根因**: 原有 Agent 4 Step 1（事实核查）验证"引用是否准确反映原文"，但未检测"声称的绝对性是否超出被引文献的实际数据范围"。当一篇文献包含声称所否认的数据时（即使数据不够具体），系统无法检测。
- **修改**:
  1. `harness/negative-claim-detection.md` → **新建** — 绝对否定声称检测规则（两步验证 A/B + 精确度分级 + 处理规则）
  2. `memory/agent-specializations.md` Agent 4 → 新增 Step 1.5 (Absolute Negative Claim Contradiction Detection)
  3. `CLAUDE.md` → 新增 Tier 3 条目 + 错误模式库
  4. `memory/MEMORY.md` → 新增索引
- **效果**: Agent 4 现在在事实核查后对每个"no data""absent""zero"声称执行两步验证——检查被引文献本身是否包含所否认的数据（验证 A），以及检查稿件所有引用中是否有文献包含相关数据（验证 B）。矛盾被标记为 MUST FIX 并给出精确限定语建议。

## E009: Agent 8 — 投稿 Agent (Phase 7.6a) — 2026-06-06

- **触发**: 同行评审 #5/#10/#11/#12 指出 HTML 审计标签残留、错别字、未完成部分、期刊不匹配。这些不是内容问题，是投稿格式化问题——需要一个新的 Agent 专门处理投稿转换。
- **根因**: 原有的 `gen_word_full.py` 直接读取源文件生成 Word——没有投稿前的清理/转化/合规检查步骤。内部审计标记（`<!-- PERSPECTIVE:P1 -->` 等）直接写入 Word。合成产物（覆盖差距报告、推理日志）没有转化为投稿文本。
- **修改**:
  1. `harness/submission-compliance.md` → **新建** — Agent 8 三阶段工作流规则（清理+转化+合规）
  2. `harness/journal-profiles.md` → **新建** — 6 本目标期刊的格式参数 + AI 披露政策
  3. `memory/agent-specializations.md` → 新增 Agent 8 完整定义（基础设施层）+ 更新协作流程图
  4. `CLAUDE.md` → 新增 `投稿`/`9` 命令 + Gate 11 + Tier 3 + 错误模式库
  5. `scripts/gen_word_full.py` → 新增 HTML comment 剥离预处理器
  6. `memory/MEMORY.md` + `harness/quality-gate.md` → 新增 Gate 11
  7. `memory/workflow-evolution.md` → 追加 E008-E009
- **效果**: 投稿前增加三阶段处理：Stage 1 剥离 HTML 标签、检测占位符和错别字；Stage 2 将覆盖差距报告转化为 Scope Limitations 段落、将合成产物转化为投稿引用；Stage 3 逐条检查期刊格式合规性。`gen_word_full.py` 在读取源文件后自动剥离所有 HTML comment。

---

*本文件在每次商讨完并修改项目文件后追加。*
