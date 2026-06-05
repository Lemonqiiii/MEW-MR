# Tier 2 手动检索清单 — NRDS 全生命周期综述

> **生成日期**: 2026-06-05
> **说明**: 以下数据库需通过医学院 VPN 手动检索。每个数据库的检索式已预编译，可直接粘贴使用。
> **完成后**: 将导出文件放入 `docs/search-results/`，然后对 Agent 说"检索结果已就绪"

---

## 数据库 1: Embase (via Ovid) — 高优先级 ⭐

**理由**: 综述涉及皮质类固醇、表面活性物质等药物/生物制剂。Embase 在药理学文献和欧洲期刊的覆盖显著优于 PubMed。

### 检索式 (Ovid 语法)

```
1. exp respiratory distress syndrome/ or exp hyaline membrane disease/
2. (neonatal adj2 (RDS or respiratory distress)).ti,ab,kw.
3. NRDS.ti,ab,kw.
4. 1 or 2 or 3

5. exp artificial ventilation/ or exp positive end expiratory pressure/ or exp continuous positive airway pressure/
6. (mechanical ventilation or non-invasive ventilation or NIV or CPAP or NIPPV or bubble CPAP).ti,ab,kw.
7. exp corticosteroid/ or exp dexamethasone/ or exp betamethasone/ or exp hydrocortisone/
8. (dexamethasone or betamethasone or hydrocortisone or postnatal steroid* or antenatal steroid*).ti,ab,kw.
9. exp lung surfactant/
10. (surfactant or beractant or poractant or calfactant or LISA or MIST or INSURE).ti,ab,kw.
11. exp oxygen therapy/
12. (oxygen therap* or oxygen target* or high-frequency ventilation or HFOV or volume-targeted ventilation).ti,ab,kw.
13. 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12

14. exp long term care/ or exp follow up/ or exp treatment outcome/
15. (long-term outcome* or long term outcome* or follow-up or follow up).ti,ab,kw.
16. exp lung function test/ or exp forced expiratory volume/
17. (pulmonary function or lung function or FEV1 or spirometry or asthma or wheez* or respiratory morbidity).ti,ab,kw.
18. exp child development/ or exp cognitive development/ or exp developmental disorder/
19. (neurodevelopment* or cognitive or cerebral palsy or behavioral or IQ or school performance or academic achievement).ti,ab,kw.
20. exp quality of life/
21. (quality of life or HRQOL or functional outcome* or life course or developmental origin*).ti,ab,kw.
22. 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21

23. 4 and 13 and 22
24. limit 23 to (english language and yr="1990-2026")
25. limit 24 to (article or review or "conference abstract")
```

### 操作步骤
1. 连接医学院 VPN
2. 访问 [Ovid Embase](https://ovidsp.ovid.com/)
3. 选择 "Advanced Search"
4. 逐行粘贴检索式（或一次性粘贴全部）
5. 导出: **RIS 格式** → 全字段 → 命名为 `embase-export.ris`
6. 放入: `E:/medical-review/docs/search-results/embase-export.ris`

**预计耗时**: 15-20 分钟

---

## 数据库 2: Cochrane Library (CENTRAL + CDSR) — 建议 ⭐

**理由**: 综述涉及 RCT（通气策略试验、激素试验、表面活性物质试验）。CENTRAL 包含 PubMed/Embase 中未索引的试验报告。

### 检索式 (Cochrane Library 语法)

```
#1 MeSH descriptor: [Respiratory Distress Syndrome, Newborn] explode all trees
#2 (neonatal NEXT "respiratory distress" OR NRDS OR "hyaline membrane disease"):ti,ab,kw
#3 #1 OR #2

#4 MeSH descriptor: [Respiration, Artificial] explode all trees
#5 MeSH descriptor: [Continuous Positive Airway Pressure] this term only
#6 (mechanical NEXT ventilation OR "non invasive ventilation" OR NIV OR CPAP OR NIPPV):ti,ab,kw
#7 MeSH descriptor: [Adrenal Cortex Hormones] explode all trees
#8 (dexamethasone OR betamethasone OR hydrocortisone OR postnatal NEXT steroid* OR antenatal NEXT steroid*):ti,ab,kw
#9 MeSH descriptor: [Pulmonary Surfactants] explode all trees
#10 (surfactant OR beractant OR poractant OR LISA OR MIST OR INSURE):ti,ab,kw
#11 MeSH descriptor: [Oxygen Inhalation Therapy] this term only
#12 (oxygen NEXT therap* OR "high frequency ventilation" OR HFOV OR "volume targeted ventilation"):ti,ab,kw
#13 #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12

#14 MeSH descriptor: [Follow-Up Studies] explode all trees
#15 (long-term NEXT outcome* OR "follow up" OR "follow-up"):ti,ab,kw
#16 (pulmonary NEXT function OR lung NEXT function OR FEV1 OR asthma OR wheez* OR "respiratory morbidity"):ti,ab,kw
#17 MeSH descriptor: [Child Development] explode all trees
#18 (neurodevelopment* OR cognitive OR "cerebral palsy" OR behavioral OR IQ OR "school performance"):ti,ab,kw
#19 MeSH descriptor: [Quality of Life] this term only
#20 ("quality of life" OR HRQOL OR functional NEXT outcome* OR "life course" OR developmental NEXT origin*):ti,ab,kw
#21 #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20

#22 #3 AND #13 AND #21
#23 #22 with Cochrane Library publication date Between Jan 1990 and Jun 2026, in Trials (CENTRAL) and Cochrane Reviews (CDSR)
```

### 操作步骤
1. 访问 [Cochrane Library Advanced Search](https://www.cochranelibrary.com/advanced-search)
2. 切换到 "Search Manager" 标签
3. 逐行粘贴 → 点击 "Run Search"
4. 导出: 选择所有结果 → Export Selected → **RIS format**
5. 命名为 `cochrane-export.ris`
6. 放入: `E:/medical-review/docs/search-results/cochrane-export.ris`

**预计耗时**: 10-15 分钟

---

## 数据库 3: ClinicalTrials.gov — 可选

**理由**: 发表偏倚检测 — 检查是否有已完成但未发表的 NRDS 干预长期随访试验。

### 检索式
```
Condition: "Respiratory Distress Syndrome, Newborn" OR NRDS OR "neonatal respiratory distress"
Intervention: mechanical ventilation OR corticosteroid OR surfactant OR CPAP
Other terms: long-term OR follow-up OR neurodevelopment OR pulmonary function
Status: Completed, Terminated, Active not recruiting
```

### 操作步骤
1. 访问 [ClinicalTrials.gov Advanced Search](https://clinicaltrials.gov/search/advanced)
2. 填写上述字段
3. 导出: CSV 格式
4. 命名为 `clinicaltrials-export.csv`
5. 放入: `E:/medical-review/docs/search-results/clinicaltrials-export.csv`

**预计耗时**: 5-10 分钟

---

## ⚠️ 注意事项

1. **CNKI + 万方**: 本次未激活——NRDS 综述不以中国人群/中医药为主要焦点
2. **检索式测试**: 建议粘贴前先在搜索框中测试检索式第一行，确认数据库正常响应
3. **文件命名**: 严格按照上述命名规则，Agent 才能自动识别和解析
4. **完成后**: 对本会话说 `检索结果已就绪` 或 `Tier 2 done`
