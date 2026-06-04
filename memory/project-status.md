# 项目状态

```yaml
---
phase: initialization           # init | literature-search | screening | deep-reading | writing | revision
progress_pct: 0
current_section: null
target_journal: null             # 待定
papers_collected: 0
papers_screened: 0
papers_read_in_depth: 0
papers_included: 0
words_written: 0
last_session_id: null
last_update: 2026-06-04
---
```

## 当前状态说明
- **阶段**: 初始化 — 已完成基础设施搭建，准备进入文献搜索阶段
- **下一步**: 确定综述的具体主题方向，写入 `active-focus.md`，然后开始 Phase 2 文献搜索
- **阻碍**: 需要用户明确综述主题（具体疾病/机制/方法学方向）

## 阶段流转规则
1. `init` → 用户确认综述主题后 → `literature-search`
2. `literature-search` → 完成检索去重 → `screening`
3. `screening` → PRISMA流程图完成 → `deep-reading`
4. `deep-reading` → 核心论点提取完成 → `writing`
5. `writing` → 初稿完成 → `revision`
6. `revision` → 投稿 → 项目归档
