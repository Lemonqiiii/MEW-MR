# 文献知识库索引

## 使用说明
1. Agent 在需要文献背景时，**首先读取本索引文件**
2. 根据主题/方法/年份定位到 `docs/papers/[topic]/` 目录
3. 每篇论文笔记遵循 `docs/papers/template.md` 模板
4. 新笔记按照主题存入对应的子目录

---

## 按主题分类

### 肿瘤学 (oncology/)
- 肿瘤免疫微环境
- 免疫检查点抑制剂
- CAR-T 细胞治疗
- 靶向治疗耐药机制
- 肿瘤异质性

### 免疫学 (immunology/)
- 固有免疫与适应性免疫
- T细胞耗竭与记忆
- 细胞因子与炎症
- 自身免疫病机制
- 感染免疫

### 神经科学 (neuroscience/)
- 神经退行性疾病
- 突触可塑性
- 胶质细胞功能
- 血脑屏障
- 神经免疫交互

### 遗传学 (genetics/)
- CRISPR/Cas9 基因编辑
- 表观遗传调控
- GWAS 与多基因风险评分
- 单细胞基因组学
- 线粒体遗传

### 药理学 (pharmacology/)
- 药物代谢动力学
- 抗体药物偶联物 (ADC)
- 纳米药物递送
- 老药新用 (Drug repurposing)
- 临床试验设计

### 细胞生物学 (cell-biology/)
- 细胞凋亡与自噬
- 细胞衰老
- 干细胞与再生
- 细胞信号转导

### 生理学 (physiology/)
- 代谢调控
- 昼夜节律
- 微生物组-宿主互作
- 运动生理

### 流行病学 (epidemiology/)
- 传染病建模
- 慢性病风险因素
- 环境暴露组学
- 全球疾病负担

---

## 按方法学分类

| 方法 | 说明 |
|------|------|
| 系统综述 (Systematic Review) | 按 PRISMA 指南的系统文献综述 |
| 荟萃分析 (Meta-analysis) | 定量合并效应量 |
| RCT (随机对照试验) | 金标准临床试验设计 |
| 队列研究 (Cohort Study) | 前瞻性或回顾性队列 |
| 病例对照研究 (Case-Control) | 回顾性病例对照 |
| 孟德尔随机化 (Mendelian Randomization) | 因果推断工具 |
| 单细胞测序 (scRNA-seq) | 单细胞组学分析 |
| 空间转录组学 (Spatial Transcriptomics) | 空间分辨的基因表达 |

---

## 按年份分层

| 层级 | 年份范围 | 说明 |
|------|---------|------|
| 最新 | 2024-2026 | 当前最新文献，重点关注 |
| 近期 | 2020-2023 | 近年重要进展 |
| 中期 | 2015-2019 | 奠定当前方向的关键工作 |
| 经典 | 2010及以前 | 领域奠基性文献 |

---

## 文献统计
- 已收集: 4,106 篇 (2026-06-04检索)
- 已筛选: 432 → 62 → **40 篇** (最终纳入)
- 已深度阅读并笔记: 30 篇
- 已纳入综述引用: 37 篇 (3篇已排除: 喉鳞癌1+非鳞NSCLC 2)
- 初稿完成: 8,546 词, 41 引文, 7 章节 + 摘要 + 图表

## 当前综述: NSCLC鳞癌免疫治疗耐药机制

### PRISMA 流程
```
检索获得 (n=4,106)
    ↓ 去重 + 排除勘误/病例报告
初筛候选 (n=432)
    ↓ 标题/摘要筛选
全文候选 (n=62)
    ↓ 全文评估 + 机制覆盖分析
最终纳入 (n=40)
```

### 机制覆盖度
| 机制类别 | 覆盖论文数 |
|------|------|
| Tumor-Intrinsic Resistance | 27 |
| Genomic & Transcriptomic Determinants | 28 |
| Cytokine & Metabolic Immune Modulation | 33 |
| Immunosuppressive Cell Populations | 16 |
| Immune Checkpoint Pathways | 14 |
| T Cell Exhaustion & Dysfunction | 6 |
| Combination Strategies | 6 |
| Acquired Resistance Mechanisms | 5 |
| Antigen Presentation | 4 |

### 数据文件
| 文件 | 内容 |
|------|------|
| `data/pubmed_merged_all.json` | 全量检索 (4,106篇) |
| `data/screening_final_40.json` | 最终纳入 (40篇) |
| `docs/papers/lusc_ici_resistance/` | 论文笔记目录 (62篇) |

### 项目状态: 初稿完成 🎉

7 章节, 8,546词, 41 引文, 4 图, 4 表
详见 `manuscript/complete_draft.md`

### 下一步
→ 用户最终审阅 → 目标期刊选定 → 格式化参考文献 → 投稿

*最后更新: 2026-06-04*
