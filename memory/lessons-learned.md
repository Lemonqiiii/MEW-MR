---
name: lessons-learned
description: Systemic failures and fixes from the 2026-06-04 LUSC review project — used to harden future agent behavior
metadata:
  type: project
---

# 项目教训与系统改进 (2026-06-04)

## 核心教训

### 1. 单源真理 (Single Source of Truth)
**问题**: 维护了两套 Word 生成脚本 (`gen_english_word.py` 含硬编码文本, `gen_word_full.py` 解析 markdown)，修改不同步导致引用丢失。
**规则**: 
- 所有内容修改必须写入唯一源文件 `manuscript/jitc_submission.md`
- Word 文档通过解析脚本自动生成，脚本只负责格式化，不包含内容
- 任何修改先在源文件完成 → 再运行生成器 → 再验证

### 2. 引用验证必须在写作前
**问题**: Agent 在扩展段落时从训练数据中提取知识（如具体药名 alpelisib/CB-839），贴在无关引用上，导致 13/14 扩展声明无引文支撑。
**规则**:
- 任何新增声明必须有至少一篇引用文献的摘要直接支撑
- 禁止从训练数据补充细节到不相关的引用上
- 引用-声明配对验证是 Gate 4 的硬性要求，必须在合并前通过

### 3. 图表编号必须是系统级约束
**问题**: 删减图表后手动重编号，正文引用、图片内标题、Word 标题三处不一致。反复出现 Figure 2/3/4 残留。
**规则**:
- 图表编号必须在源文件中全局唯一且自洽
- 删除图表 = 删除所有引用 + 重新编号 + 更新图表内嵌标题
- 自检脚本必须同时检查：正文引用编号、图片文件名对应、Word Caption 文字

### 4. 自检必须覆盖格式渲染
**问题**: 只检查文本内容（引用编号），忽略了 Word 文档的标题格式（小标题挤在一起）。
**规则**:
- 自检必须验证：段落分隔（不应合并）、标题层级的段前段后间距、图片清晰度
- 每次生成后自动运行：引用编号、正文引用完整性、图片嵌入数、标题格式

### 5. 范围引用必须解析
**问题**: 评测脚本只解析 `[N]` 和 `[N,M]`，不解析 `[N-M]` 范围引用，导致 refs 9-10 被误报为未使用。
**规则**:
- 所有引用解析必须处理：`[N]`, `[N,M]`, `[N-M]` 三种格式
- 范围展开后验证：文本引用集合 == 列表引用集合

### 6. 喉鳞癌论文必须过滤
**问题**: 检索结果中包含 "LSCC" 缩写，在喉鳞癌 (laryngeal) 和肺鳞癌 (lung) 之间混淆。PMID 42111396 被错误纳入。
**规则**:
- 筛选时必须显式检查 "laryngeal", "head and neck", "oral", "esophageal", "cutaneous", "cervical" 等非肺鳞癌标志
- 即使论文在纳入列表中，引用前必须验证其为肺鳞癌相关

### 7. 非鳞 NSCLC 论文不能用于 LUSC 论点
**问题**: TROPION-Lung10 (PMID 41669261) 明确针对 non-squamous NSCLC，却用于支撑 LUSC 的 TIGIT 阻断策略。
**规则**:
- 引用非鳞试验时必须加限定语
- 理想情况下，LUSC 特异性论点应引用 LUSC 特异性文献

### 8. 扩展内容 = 新引用验证
**问题**: 用户提出修改建议后，Agent 扩展了 3.5/5.4/Ch6，但新增声明无引文支撑，被迫回退。
**规则**:
- 任何扩展段落必须先将新增声明与引用文献逐一配对验证
- 未通过验证的声明一律删除，不留"可能对"的内容

---

### 9. 编码Agent触发机制缺失
**问题**: 编码Agent定义完善（4 Parts），但在整个项目周期中几乎从未被触发执行。导致 SESSION_LOG 空白、MILESTONES 未更新、metrics-raw.json 全是null、Git只有4次提交。项目关闭后无法有效恢复。
**根因**: (a) 完全依赖用户手动触发，用户不知道/忘记了命令；(b) settings.local.json 中未配置 Stop hook 提醒；(c) 4 Parts工作流过重，执行心理成本高；(d) 项目节奏太快（一日全流程），编码被忽略。
**规则**:
- 编码Agent拆分为轻量模式（`快记`，每2-3任务）和完整模式（`编码`，每Phase结束）
- CLAUDE.md 必须有自愈启动逻辑：交叉验证 CLAUDE.md ↔ project-status.md 的一致性
- settings.local.json 必须配置 Stop hook 提醒
- Phase结束时Agent必须主动展示检查清单（编码/Gate/Git/MILESTONES）
- 每2-3个子任务后Agent应主动建议"快记"

### 10. 搜索Agent分支决策点被跳过
**问题**: 搜索Agent的设计工作流包含 Step 0（数据库需求评估）和 Step 2（生成 Tier 2 预编译检索清单），但在实际执行中，这两个分支决策点被完全跳过。尽管激活决策表明确指出本综述涉及药物/生物制剂→应激活 Embase，涉及临床试验→应激活 Cochrane CENTRAL，但：
- `manual-search-checklist.md` 保留了模板占位符（"[Agent 预编译的 Ovid 检索式]"等4处）
- 用户从未被提示"请连接医学院VPN执行Tier 2检索"
- "如果 VPN 不可用"的兜底流程（Layer 3 金标准验证 + Methods 局限性声明）未被触发
- 稿件完全没有 Methods/Limitations 段落（至今才补充）
**根因**: (a) 项目节奏过快（一日全流程），搜索Agent 直接从 Step 1 (Tier 1 检索) 跳到了 Step 3 (合并去重)，Step 0 和 Step 2 被隐式跳过；(b) Agent 工作流中的"分支决策点"缺少强制卡点——Step 0 应该是一个必须返回明确结果的步骤，而不是可选项；(c) "VPN 不可用"被当作隐性前提而非显式决策记录下来。
**规则**:
- 搜索Agent 的 Step 0（数据库需求评估）必须产生明确输出：一张"应激活/已激活/未激活原因"表
- 即使 Tier 2 全部不激活，也必须走完 Step 0 → Step 2 → 兜底流程，不可跳过
- "VPN 不可用"不是默默接受的状态，必须触发兜底流程：预编译检索式 + Layer 3 验证 + 稿件 Limitations 声明
- 稿件必须包含 Methods/Limitations 段落（即使是叙述性综述），声明检索范围和局限性
- 预编译检索式应始终生成并保存（即使不立即执行），供未来补充检索使用

---

## 编码到 Agent 系统的改进

这些教训已编码到以下文件：
- `CLAUDE.md` → 新增 "写作纪律"、"自检要求"、"启动自愈逻辑"、"编码Agent双模式"、"Phase结束检查清单" 章节
- `memory/agent-specializations.md` → Agent 0拆分为轻量/完整双模式；Agent 3/4/5 v2 改进版
- `memory/lessons-learned.md` → 新增第9条教训（编码Agent触发缺失）
- `harness/quality-gate.md` → 更新 Gate 4/5 的具体检查项和脚本
- `scripts/gen_word_full.py` → 内置自检函数，每次生成自动运行
- `.claude/settings.local.json` → 新增 Stop hook 提醒
- `progress/SESSION_LOG.md` → 补写全部缺失会话记录
- `progress/MILESTONES.md` → 更新全部已完成里程碑
