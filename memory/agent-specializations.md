# Agent 专业化定义

本文件定义了综述写作项目中的4个领域子Agent + 2个基础设施Agent。每个子Agent有明确的触发条件、输入输出规范和prompt模板。

---

## Agent 0: 编码Agent (Infrastructure)

### 触发条件
- **手动**: 用户说"编码"、"记录进度"、"commit progress"、"更新进度"
- **自动**: 会话结束时 Stop hook 提醒（下次会话开头手动触发）

### 输入
- 当前会话的上下文（完成的工作内容）
- `features/FEATURE_LIST.md`
- `memory/project-status.md`
- `git status` / `git diff --stat`

### 工作流
1. 检查 git 变更状态
2. 读取 `features/FEATURE_LIST.md`，匹配完成的任务
3. 更新任务勾选状态
4. 更新 `memory/project-status.md` 统计数据
5. 追加 `progress/SESSION_LOG.md`
6. 如有新发现或决策，更新 `memory/key-findings.md` 或 `memory/decisions.md`
7. git commit 所有变更，使用结构化 commit message `[phase] 简短描述`

### 输出
- 表格总结本次更新内容
- 建议的下一步任务

---

## Agent 1: 文献搜索Agent

### 触发条件
用户说"搜索文献"、"find papers"、"search PubMed"、"找论文"、"检索"

### 输入
- `memory/active-focus.md` — 检索关键词和 PICO 框架
- `docs/index.md` — 了解已有文献分布
- 用户指定的检索参数（年份范围、研究类型、数据库选择）

### 工作流
1. 读取 `memory/active-focus.md` 获取检索策略
2. 构建 PubMed 检索式 (MeSH + 自由词 + 布尔运算)
3. 执行 PubMed E-utilities API 检索 (或 WebFetch PubMed)
4. 同样策略检索 Semantic Scholar / Europe PMC
5. 去重合并结果（优先 PMID 去重）
6. 按相关性/年份排序
7. 生成初筛列表 (标题 + PMID + 年份 + 期刊 + 摘要片段)
8. 更新 `docs/index.md` 文献统计数据
9. **不直接写入论文笔记** — 仅生成待筛选列表

### 输出格式
```markdown
## 检索结果: [检索主题]
- 数据库: PubMed / Semantic Scholar / Europe PMC
- 检索日期: YYYY-MM-DD
- 检索式: [完整检索式]
- 命中: N 篇 → 去重后: M 篇

### Top 20 (按相关性排序)
| # | 标题 | PMID | 年份 | 期刊 | 初筛判断 |
|---|------|------|------|------|---------|
| 1 | ... | ... | ... | ... | 纳入/排除/待定 |
```

---

## Agent 2: 论文分析Agent

### 触发条件
用户说"分析这篇"、"读论文"、"analyze paper"、"做笔记"、"take notes"

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
用户说"开始写"、"写草稿"、"draft section"、"写第X节"、"撰写"

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
用户说"审校"、"review"、"检查草稿"、"核查"、"verify"

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

## Agent 间协作流程

```
用户确定主题
    │
    ▼
文献搜索Agent ──→ 生成初筛列表
    │
    ▼
[用户手动筛选]
    │
    ▼
论文分析Agent ──→ 逐篇笔记写入 docs/papers/
    │
    ▼
综述写作Agent ──→ 输出草稿到 manuscript/draft.md
    │
    ▼
审校Agent ──→ 审校报告 → [迭代修改]
    │
    ▼
编码Agent ──→ 每个阶段结束时更新进度
```
