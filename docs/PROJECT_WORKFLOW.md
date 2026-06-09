# MEW-MR 全流程说明

MEW-MR 是一个“双系统医学综述生产线”：

```text
framework/  负责写综述
audit/      负责独立审稿
```

它的核心目标不是让 AI 一次性写出一篇综述，而是把医学综述拆成多个阶段，每个阶段由专门的 Agent 或脚本处理，并用质量门禁阻止低质量结果继续往下流。

---

## 1. 总体架构

项目根目录下最重要的是两个子项目：

```text
MEW-MR/
├── framework/   # 写作系统：检索、筛选、分析、写作、合成、投稿
├── audit/       # 审稿系统：多维度独立审稿、引用验证、主编综合
├── docs/        # 跨平台/非 Claude 使用说明和总流程文档
├── README.md
└── GETTING_STARTED.md
```

两个系统相互独立，但可以闭环协作：

```text
framework 写出 manuscript/submission.md
        ↓
复制到 audit/review-pipeline/input/
        ↓
audit 生成 review-actions.json
        ↓
framework 导入 review-actions.json
        ↓
逐项修稿，再次审稿
```

这样做的原因是“写审分离”：写作系统容易有自己的盲区，审稿系统只看稿件和披露包，更像外部审稿人。

---

## 2. framework：综述写作系统

`framework/` 是从选题到投稿的写作流水线。

入口文件：

```text
framework/CLAUDE.md
framework/config.yaml
framework/state.json
```

`config.yaml` 管项目设置，例如：

```yaml
project:
  topic: "Your Review Topic Here"
  domain: "your research domain keywords"
  review_type: "narrative"
  target_journal: "Target Journal Name"
  language: "en"
```

`state.json` 管当前进度，例如：

```json
{
  "project": {
    "phase": "planning",
    "progress_pct": 0
  },
  "metrics": {
    "papers_collected": 0,
    "papers_screened": 0,
    "words_written": 0
  }
}
```

简单说：

```text
config.yaml = 我要做什么
state.json  = 我做到哪了
```

---

## 3. framework 主流程

主流程：

```text
Planning
→ Literature Search
→ Screening
→ Deep Reading
→ Writing
→ Synthesis
→ Review
→ Submission
```

对应 Claude 命令：

```text
1 搜索
2 筛选
3 分析
4 写作
8 合成
5 审校
9 投稿
6 编码
7 评估
```

### 3.1 Planning：配置选题

用户先配置：

```text
framework/config.yaml
```

需要填写：

- 综述主题
- 领域关键词
- 综述类型：`narrative` / `systematic` / `meta-analysis`
- 目标期刊
- 稿件语言
- 数据路径
- 投稿格式参数

如果只是试用，可以复制 demo：

```bash
cp config.demo.yaml config.yaml
```

Windows PowerShell：

```powershell
Copy-Item config.demo.yaml config.yaml
```

### 3.2 Literature Search：文献检索

触发：

```text
1
search
搜索
```

对应：

```text
framework/claude/agents/1-search.md
```

这个 Agent 会：

- 根据 PICO 判断需要哪些数据库
- 自动检索 PubMed / Europe PMC / Semantic Scholar
- 必要时生成 Embase / Cochrane / CNKI 等手动检索清单
- 去重
- 做五层全面性验证
- 生成领域本体

常见输出：

```text
framework/data/
framework/docs/search-results/
framework/knowledge/domain-ontology.md
```

目标是防止：

- 只搜 PubMed 导致漏文献
- 检索式不可复现
- 忘记记录数据库、日期、结果数量
- 遗漏临床重要干预

### 3.3 Screening：文献筛选

触发：

```text
2
screen
筛选
```

对应：

```text
framework/claude/agents/6-screening.md
```

筛选分三轮：

```text
Round 0: 论文类型分类
Round 1: 标题/摘要筛选
Round 2: 全文筛选 + 引用范围分配
```

它会给论文分类型，并判断每篇论文能支撑什么：

```text
能否支撑机制声明？
能否支撑临床声明？
能否作为主引用？
是否只能做背景？
是否 abstract-only？
```

常见输出：

```text
data/screening_final_included.json
data/screening_excluded.json
docs/search-results/
```

目标是防止“引用越权”：例如用综述当主证据、用病例报告支撑普遍结论、用纯生信论文写因果机制。

### 3.4 Deep Reading：论文分析

触发：

```text
3
analyze
分析
```

对应：

```text
framework/claude/agents/2-analysis.md
```

它会对纳入论文做结构化笔记，使用模板：

```text
framework/templates/paper-note.md
```

每篇笔记通常记录：

- PMID / DOI
- 研究设计
- 人群
- 干预或暴露
- 结局
- 主要发现
- 局限性
- 与本综述的关系
- 能支持哪些类型的声明

输出进入：

```text
framework/docs/papers/
```

这一步的目标是让写作时不要直接从模型记忆写，而是从可追溯笔记写。

### 3.5 Writing：综述写作

触发：

```text
4
write
写作
```

对应：

```text
framework/claude/agents/3-writing.md
```

写作前会做规划：

```text
priority-weighted section allocation
gap-to-emphasis mapping
time annotation
figure/table plan
citation scope check
```

稿件唯一源文件是：

```text
framework/manuscript/submission.md
```

Word 输出由脚本生成：

```text
framework/scripts/gen_word.py
```

输出：

```text
framework/manuscript/output.docx
```

重要纪律：

```text
先改 markdown 源文件，再生成 Word。
不要直接改 Word 当源文件。
```

`gen_word.py` 会从 `config.yaml` 读取：

- markdown 源文件路径
- figures 目录
- Word 输出路径
- 目标期刊
- review_type
- 字体、字号、页边距等

### 3.6 Synthesis：合成推理

触发：

```text
8
synthesis
合成
```

对应：

```text
framework/claude/agents/7-synthesis.md
```

它不是简单润色，而是做跨章节推理：

- 跨干预比较矩阵
- 干预交互分析
- 假设生成
- 临床决策框架
- 论证多样性扫描
- 时间演变标注
- 覆盖缺口报告

相关模板：

```text
framework/templates/cross-intervention-matrix.md
framework/templates/clinical-decision-framework.md
framework/templates/evidence-gap-grading.md
framework/templates/time-annotation.md
```

目标是防止综述变成“每章各讲各的”，而是形成真正的综合判断。

### 3.7 Review：内部审校

触发：

```text
5
review
审校
```

对应：

```text
framework/claude/agents/4-review.md
```

审校包括：

- 事实核查
- 引用是否支持声明
- 绝对否定声称检查
- 语言自然度扫描
- RR/OR/HR 是否翻译成 ARR/NNT
- Cochrane 是否被过度崇拜
- 是否有重复论证模板
- 是否存在当前 PICO 错配

相关规则：

```text
framework/claude/disciplines/
framework/claude/prompts/
```

例如：

```text
language-naturalness.md
citation-scope.md
negative-claim-detection.md
critical-absorption.md
data-translation.md
```

### 3.8 Submission：投稿准备

触发：

```text
9
submit
投稿
```

对应：

```text
framework/claude/agents/8-submission.md
```

它检查：

- HTML 审计标记是否残留
- `[TBD]` / `[To be completed]` 是否残留
- 目标期刊是否匹配
- Author Contributions 是否完整
- Funding / Data Availability / Competing Interests 是否完整
- AI disclosure 是否需要
- 引用格式是否合规
- Word 文件是否能生成

目标是让内部草稿变成投稿可用版本。

### 3.9 Coder：编码与保存进度

触发：

```text
6
commit
编码
```

对应：

```text
framework/claude/agents/0-coder.md
```

它负责：

- 更新 `state.json`
- 更新进度
- 更新 metrics
- 安全审计
- git commit

轻量模式：

```text
快记
quick
```

用于每 2-3 个子任务后保存状态。

### 3.10 Evaluation：评估

触发：

```text
7
evaluate
评估
```

对应：

```text
framework/claude/agents/5-evaluation.md
```

评估维度包括：

- 成功率
- 效率
- 鲁棒性
- 安全性
- 一致性

这部分让项目不只是“能跑”，还要长期观察 Agent 是否稳定。

---

## 4. framework 质量门禁

门禁定义在：

```text
framework/claude/gates/gates.md
```

执行脚本：

```text
framework/scripts/verify_gates.py
```

典型命令：

```bash
python3 scripts/verify_gates.py --gate 4
python3 scripts/verify_gates.py --all
python3 scripts/verify_gates.py --check-prereq 3
python3 scripts/verify_gates.py --check-output 3
```

11 个 gate：

```text
Gate 1  检索质量
Gate 2  筛选质量
Gate 3  笔记/深度阅读质量
Gate 4  引用-声明验证
Gate 5  稿件结构与格式完整性
Gate 6  引用范围合规
Gate 7  领域本体完整性
Gate 8  写作前规划完整性
Gate 9  合成推理质量
Gate 10 增强审校质量
Gate 11 投稿就绪
```

门禁的意义是：

```text
失败不是项目坏了，而是告诉你不能继续往下走。
```

---

## 5. audit：独立审稿系统

`audit/` 是第二个子项目。它不是写作系统的一部分，而是独立审稿人。

入口文件：

```text
audit/CLAUDE.md
audit/memory/active-review.md
audit/memory/project-status.md
audit/memory/agent-specializations.md
```

输入目录：

```text
audit/review-pipeline/input/
```

输出目录：

```text
audit/review-pipeline/output/
```

上下文目录：

```text
audit/review-pipeline/context/
```

---

## 6. audit 主流程

完整审稿流程：

```text
稿件输入
→ Agent P 预处理
→ 6 个审稿人并行审稿
→ Agent G 关卡复查
→ Agent V 引用验证
→ Agent M 主编综合
→ Agent F 输出格式化
→ review-actions.json
```

触发命令：

```text
审稿
review
peer-review
```

也可以单独触发某个维度：

```text
审稿 方法学
审稿 临床
审稿 统计
审稿 结构
```

### 6.1 Agent P：预处理

它读取稿件，生成 disclosure packet：

```bash
python scripts/gen-review-pack.py review-pipeline/input/DEMO-MANUSCRIPT.md "Demo Journal"
```

输出：

```text
review-pipeline/context/disclosure-packet.json
```

披露包只包含允许审稿人知道的信息，例如：

- 标题
- 字数
- 章节数
- 引用数
- 目标期刊
- 综述类型
- PICO
- 检索策略描述

它刻意不包含写作项目内部决策，保证“有限知情”。

### 6.2 R1-R6：六维度审稿

六个审稿人：

```text
R1 方法学
R2 临床
R3 逻辑与论证
R4 统计/数据
R5 文献覆盖
R6 结构与叙事
```

每个审稿人独立工作，不互相通信。

它们检查不同问题：

- 方法学是否自洽
- 临床推理是否充分
- 论证链是否完整
- 数据解读是否准确
- 是否遗漏关键文献
- 章节结构是否合理

### 6.3 Agent G：关卡复查

它检查每个审稿人的输出质量：

- 是否覆盖该维度
- 是否有具体位置
- 是否有原文引用
- 是否有可执行建议
- 是否越界评价
- 是否和其他审稿人矛盾

### 6.4 Agent V：引用验证

这是客观事实检查层。

脚本：

```bash
python scripts/verify-citations.py review-pipeline/input/DEMO-MANUSCRIPT.md
```

它会验证 PMID 是否存在。demo 中故意放了 fake PMID：

```text
PMID:99999999
```

会正确输出：

```text
Verified: 4, Failed: 1, Total: 5
```

### 6.5 Agent M：主编综合

它把六个审稿人的意见合并，做：

- 去重
- 严重性重新校准
- 收敛分析
- 优先级排序
- 总体审稿意见

关键思想是“交叉收敛”：如果多个审稿人从不同角度发现同一个问题，那通常是深层结构缺陷。

### 6.6 Agent F：输出格式化

最终输出：

```text
review-pipeline/output/review-report.md
review-pipeline/output/review-actions.json
```

`review-actions.json` 是机器可解析的审稿意见，用于回流到 `framework`。

---

## 7. 写审闭环

写审之间的桥接脚本：

```text
framework/scripts/import_review_actions.py
```

用法：

```bash
cd framework
python3 scripts/import_review_actions.py ../audit/review-pipeline/output/review-actions.json
```

Windows：

```powershell
python scripts/import_review_actions.py ..\audit\review-pipeline\output\review-actions.json
```

它会生成：

```text
framework/manuscript/review-actions-import.md
```

里面是按严重性排序的修回清单。

重要的是：它不会自动改稿件。这是有意设计的，因为医学稿件修回必须由作者或 Agent 在证据核查后逐项处理，而不是让脚本直接改正文。

schema 在：

```text
audit/schemas/review-actions.schema.json
```

这样 audit 和 framework 之间有了明确 contract。

---

## 8. 典型使用路径

从零开始，用 framework 写稿：

```bash
git clone ...
cd MEW-MR/framework
pip install -r scripts/requirements.txt
python3 scripts/smoke_test.py
cp config.demo.yaml config.yaml
claude
```

然后在 Claude 里：

```text
1  → 搜索
2  → 筛选
3  → 分析
4  → 写作
8  → 合成
5  → 审校
9  → 投稿
```

写完后：

```bash
cp framework/manuscript/submission.md audit/review-pipeline/input/
cd audit
python3 scripts/check-structure.py review-pipeline/input/submission.md
python3 scripts/gen-review-pack.py review-pipeline/input/submission.md "Target Journal"
claude
```

在 audit 里：

```text
审稿
```

得到：

```text
review-actions.json
```

再回 framework：

```bash
cd framework
python3 scripts/import_review_actions.py ../audit/review-pipeline/output/review-actions.json
```

然后按清单修稿，再重新审稿。

---

## 9. 脚本层功能

不使用 Claude Code 时，仍可运行部分脚本。

framework：

```text
scripts/smoke_test.py
scripts/verify_gates.py
scripts/gen_word.py
scripts/audit_manuscript.py
scripts/import_review_actions.py
```

audit：

```text
scripts/check-structure.py
scripts/gen-review-pack.py
scripts/verify-citations.py
```

但没有 LLM 时，项目不能自动完成：

- 文献筛选判断
- 论文深度分析
- 综述写作
- 合成推理
- 多维审稿

这些仍需要 Claude Code 或其他 LLM coding agent 读取 prompt 文件执行。

---

## 10. 当前模板状态

目前 MEW-MR 更像一个干净模板，而不是某个具体综述项目。

framework 当前：

```text
phase: planning
topic: Your Review Topic Here
progress: 0%
```

audit 当前：

```text
等待用户放入 review-pipeline/input/ 稿件
```

历史 NRDS 审稿示例在：

```text
audit/examples/nrds-lifecourse/active-review.md
```

它不作为默认当前任务。

---

## 11. 设计价值

这个项目最重要的设计价值有三点。

第一，写作流程可追踪。  
不是让 AI 直接写，而是从检索、筛选、笔记、写作、合成到投稿逐层推进。

第二，审稿系统独立。  
audit 不共享 framework 的内部思路，因此更容易发现写作系统自己的盲区。

第三，门禁阻断低质量推进。  
每个阶段都有 gate。失败时不是继续糊过去，而是回到对应阶段修。

一句话总结：

```text
MEW-MR 是一个用于医学综述的 AI 协作生产框架：
framework 负责系统化写作，
audit 负责独立多维审稿，
二者通过结构化审稿意见形成“写作 → 审稿 → 修回 → 再审稿”的闭环。
```

