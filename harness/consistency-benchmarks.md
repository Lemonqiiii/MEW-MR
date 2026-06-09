# 一致性基准测试

> 每 Phase 结束时由评估Agent 执行。每个基准跑 2 次，对比行为路径和语义输出。
> 基准任务在项目推进中持续积累——Phase N 的真实任务如果表现稳定，可提升为基准。

---

## 基准选择原则

1. **输入明确** — 不依赖含糊的人类判断
2. **可重复** — 不依赖外部状态（不假设某篇论文还在不在）
3. **有独立答案** — 存在客观标准可以对照（如已知的 PMID 列表）
4. **覆盖核心能力** — 每个基准测试一个不同的 Agent 核心能力

---

## 当前基准集 (Phase 1 — 初始化)

### Bench-001: PubMed 精确检索 — 文献搜索Agent

```
任务: "在 PubMed 中搜索 2024 年发表的、标题中包含 'PD-L1' 和 'resistance' 的综述文章"
期望:
  - 行为: WebFetch → pubmed.ncbi.nlm.nih.gov（或 E-utilities API）
  - 结果: 返回的论文列表应包含已知文献 PMID: 38200123（如该数据变化，以实际检索为准）
  - 一致性要求: 两次检索的 PMID 列表 Jaccard ≥ 80%
```

### Bench-002: 论文元数据提取 — 论文分析Agent

```
任务: "获取 PMID 38200123 的详细信息（标题、第一作者、期刊、年份、摘要前 200 字）"
期望:
  - 行为: WebFetch → pubmed 或 Semantic Scholar API
  - 结果: 标题、作者、期刊、年份必须与数据库记录一致（精确匹配）
  - 一致性要求: 两次提取完全一致
```

### Bench-003: 术语定义查找 — 通用Agent

```
任务: "在 docs/glossary.md 中查找 'ITT' 的全称和中文翻译"
期望:
  - 行为: Read → E:\medical-review\docs\glossary.md
  - 结果: Intention-to-Treat / 意向性分析
  - 一致性要求: 两次输出完全相同
```

### Bench-004: 简单统计解释 — 通用Agent

```
任务: "解释 I² 统计量为 75% 在荟萃分析中意味着什么"
期望:
  - 行为: 可能 Read → docs/methods/statistical-methods.md 或直接回答
  - 结果: 应提及"高异质性"和通常的阈值划分（<25%低, 50%中, >75%高）
  - 一致性要求: 核心判断（高异质性）一致，措辞可不同
```

### Bench-005: 功能清单读取 — 通用Agent

```
任务: "当前项目的下一个待完成任务是什么？"
期望:
  - 行为: Read → features/FEATURE_LIST.md
  - 结果: 返回当前最高优先级未勾选任务；如旧 Phase 与当前 project-status 冲突，应说明冲突
  - 一致性要求: 两次返回相同的任务项
```

### Bench-006: Gate 0 当前稿件路由 — 基础设施Agent

```
任务: "检查当前项目是否仍有会影响当前任务的旧项目硬编码"
期望:
  - 行为: 运行或等价执行 `python scripts/process_integrity_check.py`
  - 结果: 报告 current_manuscript，并区分 blocking / warning / historical info
  - 一致性要求: 两次 blocking 计数一致
```

### Bench-007: Harness 架构完整性 — 评估Agent

```
任务: "检查 harness 架构是否齐全"
期望:
  - 行为: 运行或等价执行 `python scripts/harness_architecture_check.py`
  - 结果: 按 context/search_screening/quality/evaluation/safety/submission/evolution 分层报告
  - 一致性要求: 两次 missing/schema issue 计数一致
```

### Bench-008: VPN 全文处理 — 搜索Agent

```
任务: "某篇纳入文献需要 VPN 才能查看全文，应该怎么记录？"
期望:
  - 行为: 读取 harness/search-screening-protocol.md
  - 结果: 标记 Tier 2，写入 fulltext-access-log.csv，并加入 vpn-download-checklist.md
  - 一致性要求: 两次都不得允许该文献作为核心声明唯一证据
```

---

## 执行记录格式

评估Agent 在 `harness/reports/consistency-phase-N.md` 记录：

```markdown
## 一致性测试报告 — Phase N — YYYY-MM-DD

### Bench-001: PubMed 精确检索

| 指标 | Run 1 | Run 2 | 差异 |
|------|-------|-------|------|
| 工具调用序列 | WebFetch→Read→Write | WebFetch→Read→Write | 一致 ✅ |
| 序列编辑距离 | — | 0 | ✅ |
| 返回 PMID 数量 | 12 | 14 | - |
| PMID Jaccard | — | — | 0.77 ⚠️ |
| 关键路径完整性 | 全部 | 全部 | ✅ |

**判定**: ⚠️ 部分一致 — 行为一致，但结果 Jaccard 低于 80% 阈值

### 汇总

| 基准 | 行为一致 | 结果一致 | 综合 |
|------|---------|---------|------|
| Bench-001 | ✅ | ⚠️ | ⚠️ |
| Bench-002 | ✅ | ✅ | ✅ |
| Bench-003 | ✅ | ✅ | ✅ |
| Bench-004 | ✅ | ✅ | ✅ |
| Bench-005 | ✅ | ✅ | ✅ |

通过率: 4/5 完全一致, 1/5 部分一致
```

---

## 基准维护规则

1. **新增**: 每个 Phase 结束时，从本 Phase 完成的任务中挑选 1-2 个加入基准集
2. **退役**: 连续 3 个 Phase 100% 一致的基准改为每 2 Phase 跑一次
3. **失效**: 如果基准依赖的外部数据发生变化（如 PMID 被撤稿），标记为失效并替换
4. **上限**: 基准总数控制在 10 个以内，超出时限退役通过率最高且最简单的
