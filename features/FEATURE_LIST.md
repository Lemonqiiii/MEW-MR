# 功能清单

> **使用说明**: 编码Agent每次会话结束时根据进展更新本文件。优先完成当前 Phase 内的所有任务再进入下一 Phase。

---

## Phase 1: 项目初始化

- [x] 1.1 确定综述主题和 PICO 框架（更新 `memory/active-focus.md`）
- [ ] 1.2 确定目标期刊
- [x] 1.3 确定综述类型（叙述性 / 系统综述 / 荟萃分析）

---

## Phase 2: 文献搜索

- [x] 2.1 数据库需求评估（Step 0 门禁）
- [x] 2.2 PubMed / EPMC 检索
- [x] 2.3 Semantic Scholar 补充检索（限流，EPMC 1,009篇已足够）
- [x] 2.4 Europe PMC 补充检索
- [x] 2.5 Tier 2 数据库（ClinicalTrials.gov ✅ + EPMC 补充填补 Embase/Cochrane 盲区；浏览器交互数据库无法自动化）
- [x] 2.6 去重并生成初筛列表

---

## Phase 3: 文献筛选

- [x] 3.1 Round 0: 论文类型分类（A-J）
- [x] 3.2 Round 1: 标题/摘要筛选（PICO + 类型条件）
- [ ] 3.3 全文获取
- [x] 3.4 Round 2: 全文筛选 + 引用范围分配 + 健康检查
- [ ] 3.5 PRISMA 流程图

---

## Phase 4: 深度阅读与笔记

- [x] 4.1 Batch 1 核心文献批量笔记 (528 P1)
- [x] 4.2 Batch 2 重要文献简记 (47 P2)
- [x] 4.3 剩余文献索引 (15 P3)
- [x] 4.4 提取交叉主题和核心论点（→ `memory/key-findings.md`）
- [ ] 4.5 构建证据表

---

## Phase 5: 写作

- [x] 5.1 确定综述大纲（`manuscript/outline.md`）
- [x] 5.2 撰写 Introduction
- [x] 5.3 撰写 Methods（叙述性综述 — 见 Introduction 末段检索方法描述）
- [x] 5.4-5.N 撰写各主题章节 (Sections 2-8)
- [x] 5.N+1 撰写 Discussion/Conclusions (Sections 9-11)
- [x] 5.N+2 撰写 Abstract + Key Messages
- [ ] 5.N+3 生成图表 (无图表 — 纯文本综述)
- [x] 5.N+4 初稿完成 → 进入内审

---

## Phase 6: 修改与定稿

- [x] 6.1 第一轮内部审校（Agent 4: 0 空强调词, 0 Gate6 违规, 92% 自然度）
- [x] 6.2 第二轮语言润色（审校中完成）
- [x] 6.3 引用核查（Gate 4/5/6 — 35/35 引用匹配, 0 违规）
- [ ] 6.4 格式化参考文献（目标期刊格式 — 待定期刊）
- [x] 6.5 最终定稿，提交前检查清单 (gen_word_full.py 通过)

---

## 图例
- `[ ]` 待完成
- `[x]` 已完成
- `[~]` 进行中

*最后更新: 2026-06-05*
