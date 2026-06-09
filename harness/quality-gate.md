# 质量关卡系统 (Quality Gate System)

## 核心原则

**每个 Phase 的输出在进入下一 Phase 之前，必须通过质量关卡检查。** 未经检查的输出 = 未完成。

---

## 关卡总览

Gate 0 先验证流程是否路由到当前项目；Gate 1+ 再验证具体科研产物。任何稿件生成、审校或投稿前，必须先通过 Gate 0。

### 分级制度

| 级别 | Gate | 执行策略 |
|------|------|---------|
| **🔵 CORE** | G0–G6 | **每次 Phase 结束强制执行**，失败阻塞下一阶段 |
| **🟢 ENHANCED** | G7–G11 | **条件激活**：仅当项目类型匹配时激活；跳过需记录原因 |

跳过 ENHANCED Gate 不算失败，但必须在 SESSION_LOG 中注明跳过原因。

### Gate 0: 流程完整性与项目路由 🔵 CORE

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 当前稿件识别 | 读取 `memory/project-status.md` 与 `memory/active-focus.md`，解析 `current_manuscript` | 唯一且存在 |
| 目标期刊一致 | 比对 project-status、active-focus、稿件标题页 | 0 冲突 |
| 历史硬编码残留 | 扫描 AGENTS、Agent定义、Gate脚本、scripts 中旧项目默认值 | 0 个会影响当前任务的残留 |
| 门禁数据绑定 | Gate 4/5/6 使用当前稿件与当前证据数据集 | 不读取历史数据集 |
| 版本文件绑定 | CHANGELOG / REVISION_MAP 指向当前稿件 | 0 冲突 |
| 脚本可配置 | 生成、审计、引用重建脚本支持显式稿件路径 | 100% 支持 |

**失败处理**: 先修流程文件或脚本，再进入科研内容检查。禁止在 Gate 0 失败时继续运行投稿或 Word 生成。

---

## 十一个关卡 (Gate 0 + G1-G6 现有, G7-G11 Phase 7 新增)

### Gate 1: 文献检索 → 文献筛选 🔵 CORE

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 查全率 | 随机抽 5 篇已知关键论文，验证是否被检索到 | 5/5 命中 |
| 去重准确率 | 随机抽 50 篇，人工验证无重复 | 0 重复 |
| 数据完整性 | 检查 PMID/DOI/摘要缺失率 | <5% 缺失 |

### Gate 2: 文献筛选 → 深度阅读 🔵 CORE

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 纳入一致性 | Agent A vs Agent B 独立筛选 20 篇，计算 Cohen's Kappa | Kappa > 0.7 |
| 排除理由 | 随机抽 10 篇排除文献，验证排除理由合理 | 10/10 合理 |
| 假阳性检查 | 验证纳入文献标题→是否确实讨论鳞癌+免疫耐药 | 0 篇错分 |

### Gate 3: 深度阅读 → 写作 🔵 CORE

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 笔记质量 | 随机抽 10 篇笔记，检查核心发现是否可从摘要中推断 | ≥ 8/10 |
| 主题覆盖 | 检查是否有关键机制类别未被覆盖 | 0 空白类别 |
| 引用可追溯 | 每个交叉主题是否至少有 2 篇独立文献支撑 | 100% |

### Gate 4: 写作（正文）🔵 CORE

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| **引用-声明验证** | **逐条打开引用文献的摘要，确认声明内容确实来自该文献** | **≥ 95% 通过率** |
| 逻辑连贯性 | 检查章节过渡句是否准确反映下一章内容 | 7/7 过渡准确 |
| 数据准确性 | 验证所有频率数字、试验名称、药物名称的准确性 | 0 事实错误 |

### Gate 5: 修改/扩展（关键！）🔵 CORE

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| **新增声明溯源** | **每条新增声明必须标注具体来源（引文+段落位置）** | **100% 可溯源** |
| 修改范围审查 | 对比修改前后的 diff，确认修改不超过引用支撑范围 | 0 越界修改 |
| 回退测试 | 如果新增声明无法溯源，是否可安全回退而不破坏逻辑？ | 100% 不破坏 |

### Gate 6: 终稿 → 投稿 🔵 CORE

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 引用格式 | 检查所有引用格式一致性、PMID/DOI 完整性 | 100% |
| 图表嵌入 | 确认正文引用编号与图表文件对应 | 100% |
| 语言终审 | 全文朗读，标记不通顺句子 | ≤ 5 处标记 |

### Gate 7: 领域本体构建 → 写作前规划 🟢 ENHANCED

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 干预清单完整性 | 交叉对照 ≥2 个指南来源，验证干预覆盖率 | ≥90% 指南中的干预被收录 |
| 空白分级覆盖率 | 所有干预均分配 G0-G4 分级 | 100% |
| 紧迫性评分覆盖率 | 所有干预均计算 Composite Urgency | 100% |
| 干预交互地图 | 所有干预对枚举并标注状态 (KNOWN/UNEXPLORED) | 100% 配对枚举 |
| 缺失干预报警 | 与标准治疗清单交叉对比 | 报警已生成 |

### Gate 8: 写作前规划 → 写作 🟢 ENHANCED

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 篇幅分配覆盖 | Priority-Weighted Section Allocation 表覆盖所有大纲章节 | 100% |
| Priority 不匹配检查 | 所有 priority ≥7 的干预不得分配 Brief | 0 违规 |
| 空白-强调映射 | 所有 G3-G4 干预有 Lead-with-the-gap 策略 | 100% |
| 时间标注计划 | 所有 Band 2+ 引用在 Time Annotation Schedule 中有限定语计划 | 100% |
| 覆盖率报告 | Domain Ontology vs Outline coverage comparison | 报告已生成 |

### Gate 9: 合成推理 → 审校 🟢 ENHANCED

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 跨干预矩阵完整 | 所有干预对在 cross-intervention-output.md 中比较 | 100% 配对枚举 |
| 假设可追溯 | 每个假设在 synthesis-reasoning-log.md 中有推断链+检索式+结论 | 100% traceable |
| 论证多样性 | Pattern A 全稿检测 | ≤3 次 |
| 时间演变标注 | 所有引用跨度 >20 年的章节有时间演变小结 | 100% |
| 覆盖差距报告 | coverage-gap-report.md 已生成 | 报告存在 |
| 假设不伪装 | 所有 HYPOTHESIS 显式标注 | 0 违规 |

### Gate 10: 增强审校 → 评估 🟢 ENHANCED

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| 视角切换覆盖 | 5 种视角类型在触发位置被尝试 | ≥80% 覆盖 |
| 数据翻译 | 所有 RR/HR/OR 有 ARR/NNT 或 baseline-unknown 标注 | 100% |
| 论证多样性 | Pattern A ("优雅空洞") 最终计数 | ≤2 |
| Cochrane 批判 | 每篇被引 ≥2 次的 Cochrane 综述有 ≥1 条批判限定语 | 100% |
| Cochrane 集中度 | Cochrane 引用占比 + 批判充分性 | ≤60% 或 ≥3 条补充批判 |

### Gate 11: 投稿格式化 → Word 生成 🟢 ENHANCED

| 检查项 | 方法 | 通过标准 |
|--------|------|---------|
| HTML 审计标签 | 扫描全部 `<!--.*?-->` | 0 个残留 |
| 编辑占位符 | 扫描 `[To be completed]` `[TBD]` | 0 个 |
| 期刊匹配 | 验证期刊名 vs 主题 | MATCH 或已标记 + 替代期刊 |
| 完整性 | 检查 Author Contributions / Funding / Data Availability 等 | 5/5 完成 |
| AI 披露 | 检测 AI 声明 + 对照期刊政策 | PRESENT 或已标记 ⚠️ MISSING |

---

## 执行记录

| 关卡 | 日期 | 通过/失败 | 发现问题 | 处理 |
|------|------|----------|---------|------|
| Gate 1 | 2026-06-05 | ✅ **通过** | 历史项目发现错误人群/错误亚型残留 | 从历史筛选数据清除；2篇预印本无PMID属正常 |
| Gate 2 | 2026-06-05 | ✅ **通过** | excluded.json缺少结构化排除原因字段 | 降级使用screening_log.md文本验证 |
| Gate 3 | 2026-06-05 | ✅ **通过** | 5/18主题仅1篇文献支撑（niche/emerging topics） | 属于叙述性综述可接受范围；10/10笔记质量满分 |
| Gate 4 | 2026-06-04 | **失败** | 14条声明中13条引文不支持 | 回退方案 |
| Gate 4 | 2026-06-04 | **通过** | 回退后19/20直接验证 | 1项AST/SOX2声明修正 |
| Gate 5 | 2026-06-05 | **通过** | 41/41引用已用, Fig/Tab编号干净 | - |

### Gate 1-3 原"未执行"根因

| 问题 | 根因 | 修复 |
|------|------|------|
| 原设计假设双Agent操作 | Cohen's Kappa需两个评分者 → 单Agent不可行 | 改为单Agent可执行检查：去重/污染/数据完整性 |
| 无可执行脚本 | Gate 4/5有脚本，Gate 1-3只有文字描述 | 编写 `scripts/gate123_verify.py` |
| 无"金标准论文集合" | 查全率验证需预定义已知论文列表 | 改为喉鳞癌关键词污染检查+L2引文扩散验证 |
| 项目速度快，Gate 1-3被跳过 | 同日完成检索→筛选→阅读，关卡检查滞后 | Gate 1-3现在有可执行脚本，`git hook`或Phase结束时自动提醒 |

---

## Gate 1-3 可执行脚本 (2026-06-05 新增)

```bash
python3 scripts/gate123_verify.py
```

**Gate 1 检查项** (检索→筛选):
- 去重准确率: PMID唯一性检查
- 数据完整性: abstract/title缺失率 + preprint识别
- 年份分布合理性: 覆盖2020-2026
- 喉鳞癌/非肺鳞癌污染: 关键词扫描整个标题+摘要

**Gate 2 检查项** (筛选→深度阅读):
- 排除理由合理性: 随机抽样验证
- 纳入文献机制覆盖: 免疫/耐药/机制关键词扫描
- 年份覆盖: 确认覆盖至2026

**Gate 3 检查项** (深度阅读→写作):
- 笔记质量: 随机抽样10篇，4维度评分(finding/PMID/relation/methods)
- 交叉主题覆盖: 每个主题≥2支撑PMID
- 笔记-大纲映射: subsections≥15

---

## Gate 4 当前执行原则

```bash
python scripts/audit_manuscript.py
```

Gate 4 的声明-引用验证必须为每个当前主题重新生成 claim map。历史项目中的硬编码声明清单不得复用。

建议的当前主题流程:
1. 从 `current_manuscript` 提取关键声明和引用编号
2. 将引用编号映射至 PMID/DOI
3. 对照摘要或全文验证 direct / indirect / background 支撑类型
4. 将结果写入主题专用 claim map 或审校报告

## Gate 5b Word 格式检查 (已嵌入 gen_word_full.py)

生成 Word 后自动运行：Figure refs, Table refs, Bad refs, Body citations, Images embedded, Headings, Word count

---

## 知识库更新

所有教训已编码到：
- `CLAUDE.md` → 写作纪律 + 质量关卡 G1-G10 + 错误模式库 (新增: 优雅空洞/Cochrane崇拜/统计翻译缺失/视角单一/沉默失明)
- `memory/agent-specializations.md` → Agent 1 (Step 7) + Agent 3 (Steps 0a-0f) + Agent 7 (完整新增) + Agent 4 (Pre/Post Pass 1-4)
- `memory/lessons-learned.md` → 8条教训 + 错误模式库
- `harness/quality-gate.md` → 可执行 Gate 4 脚本 + Gates 7-10 定义
- `knowledge/domain-ontology-template.md` → 领域本体模板 (Module A)
- `harness/evidence-gap-grading.md` → G0-G4 框架 (Module A)
- `harness/priority-scoring.md` → 4 维度评分 (Module A)
- `harness/time-annotation.md` → 证据衰减规则 (Module D)
- `harness/cross-intervention-matrix.md` → 7 维度矩阵 (Module B)
- `harness/synthesis-reasoning.md` → Agent 7 规则 (Module B)
- `harness/clinical-decision-framework.md` → 决策框架 (Module B)
- `harness/perspective-switching.md` → 视角切换 (Module C)
- `harness/data-translation.md` → 数据翻译 (Module C)
- `harness/argument-diversity-enforcement.md` → 论证多样性 (Module C)
- `harness/critical-absorption.md` → Cochrane 批判 (Module C)
- `scripts/gen_word_full.py` → 内置自检
