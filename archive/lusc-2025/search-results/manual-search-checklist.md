# VPN 手动检索清单

> **使用说明**: 搜索Agent 在完成 Tier 1 自动检索后，生成此清单。您需要在一次 VPN 连接中按清单逐个数据库执行检索并导出结果。完成后说"全文已就绪"或"检索结果已就绪"，Agent 会自动导入和处理。

---

## 当前检索任务

**检索主题**: Mechanisms of Immunotherapy Resistance in Squamous Cell Carcinoma of NSCLC

**检索日期**: 2026-06-05（预编译） / 待用户VPN执行

**预计总耗时**: ~30分钟（Embase 15min + Cochrane 10min + 导出 5min）

**PICO对应**:
- P: NSCLC squamous cell carcinoma patients
- I: Immune checkpoint inhibitors (anti-PD-1, anti-PD-L1, anti-CTLA-4)
- O: Resistance mechanisms (primary + acquired)

---

## 操作顺序

建议按以下顺序执行，每个数据库导出完成后将文件放入 `docs/search-results/`：

---

### 1. Embase (via Ovid) — 高优先级 🔴

**激活理由**: 综述涉及药物/生物制剂（ICIs: pembrolizumab, nivolumab, atezolizumab, durvalumab, ipilimumab, cemiplimab），Embase 是药理学文献金标准，覆盖 2,900+ PubMed 未索引期刊。

- [ ] 连接医学院 VPN
- [ ] 打开 Ovid Embase: https://ovidsp.ovid.com/
- [ ] 选择数据库: **Embase** (1974 to present)
- [ ] 选择 "Advanced Search"
- [ ] 逐行粘贴以下检索式并执行:

```
1. exp lung non small cell cancer/                                  (Emtree term: NSCLC)
2. (NSCLC or "non small cell lung" or "non-small cell lung").ti,ab,kw.
3. 1 or 2
4. exp lung squamous cell carcinoma/                                (Emtree term: LUSC)
5. (squamous cell carcinoma or squamous or LUSC or LSCC).ti,ab,kw.
6. 4 or 5
7. exp immunotherapy/
8. exp immune checkpoint inhibitor/
9. exp programmed death 1 receptor/ or exp programmed death 1 ligand 1/
10. exp cytotoxic T lymphocyte antigen 4/
11. (immunotherap* or "immune checkpoint" or ICI or ICIs).ti,ab,kw.
12. (anti-PD-1 or anti-PD-L1 or anti-CTLA-4).ti,ab,kw.
13. (pembrolizumab or nivolumab or atezolizumab or durvalumab or ipilimumab or cemiplimab).ti,ab,kw.
14. 7 or 8 or 9 or 10 or 11 or 12 or 13
15. exp drug resistance/
16. exp cancer resistance/
17. (resistan* or refractory or "immune evasion" or "non-response" or nonresponse).ti,ab,kw.
18. 15 or 16 or 17
19. 3 and 6 and 14 and 18
20. limit 19 to (yr="2020-2026" and english and (article or review))
```

- [ ] 执行行 1-19，查看命中数：________
- [ ] 执行行 20（加筛选），查看命中数：________
- [ ] 点击 "Export" → 选择格式: **RIS**
- [ ] 选择导出范围: **All Results** (筛选后)
- [ ] 导出字段选择: Citation + Abstract + Keywords + Emtree Terms
- [ ] 保存文件到: `E:\medical-review\docs\search-results\embase-export.ris`
- [ ] **实际命中数**: ________ (请填入，Agent 用于对比预期)

**预期命中**: 约 200-800 篇（Embase 通常较 PubMed 多 20-40% 独特记录）

---

### 2. Cochrane Library — 中优先级 🟡

**激活理由**: 综述涉及 RCT/临床试验（KEYNOTE-407, CheckMate-017/227, IMpower-131, EMPOWER-Lung 1, Lung-MAP S1400F/I, TROPION-Lung10），Cochrane CENTRAL 包含 PubMed/Embase 中未索引的试验报告。

- [ ] 打开 Cochrane Library: https://www.cochranelibrary.com/
- [ ] 选择 "Advanced Search"
- [ ] 在 "Search Manager" 标签页粘贴以下检索式:

```
#1 MeSH descriptor: [Carcinoma, Non-Small-Cell Lung] explode all trees
#2 (NSCLC or "non small cell lung" or "non-small cell lung"):ti,ab,kw
#3 #1 or #2
#4 MeSH descriptor: [Carcinoma, Squamous Cell] explode all trees
#5 (squamous or LUSC or LSCC):ti,ab,kw
#6 #4 or #5
#7 MeSH descriptor: [Immunotherapy] explode all trees
#8 MeSH descriptor: [Immune Checkpoint Inhibitors] explode all trees
#9 (immunotherap* or "immune checkpoint" or ICI or ICIs):ti,ab,kw
#10 (anti-PD-1 or anti-PD-L1 or anti-CTLA-4):ti,ab,kw
#11 (pembrolizumab or nivolumab or atezolizumab or durvalumab or ipilimumab):ti,ab,kw
#12 #7 or #8 or #9 or #10 or #11
#13 MeSH descriptor: [Drug Resistance, Neoplasm] explode all trees
#14 (resistan* or refractory or "immune evasion"):ti,ab,kw
#15 #13 or #14
#16 #3 and #6 and #12 and #15
#17 #16 with Cochrane Library publication date from Jan 2020 to Jun 2026
```

- [ ] 点击 "Run Search"
- [ ] 切换到 "Trials" 标签页 (CENTRAL) → 查看命中数：________
- [ ] 点击 "Export Selected" → 选择格式: **RIS**
- [ ] 保存文件到: `E:\medical-review\docs\search-results\cochrane-export.ris`
- [ ] **CENTRAL 命中数**: ________
- [ ] (可选) 切换到 "Cochrane Reviews" 标签页 → 查看命中数：________
- [ ] (可选) 导出 Cochrane Reviews → `cochrane-reviews-export.ris`

**预期命中**: CENTRAL ~50-150 篇试验记录；Cochrane Reviews ~5-15 篇相关系统综述

---

### 3. CNKI (中国知网) — 本综述不激活 ⚪

> 综述不涉及中国人群/中医药/亚洲流行病学 → 跳过

### 4. 万方数据 — 本综述不激活 ⚪

> 同上 → 跳过

### 5. SinoMed — 本综述不激活 ⚪

> 同上 → 跳过

---

## 完成后

- [ ] 所有文件已放入 `docs/search-results/`
- [ ] 实际命中数已填入各节
- [ ] 关闭不需要的 VPN 连接
- [ ] 在 Claude Code 中说: **"检索结果已就绪"**

---

## ⚠️ 如果 VPN 不可用

如果 VPN 不可用（当前状态），执行以下兜底措施：
1. `docs/search-results/` 下创建 `tier2_unavailable.md` 标记
2. 运行 Layer 3 金标准交叉验证（检查 PubMed 对已知 Embase 文献的覆盖度）
3. 在稿件 Methods 中声明: "Searches were limited to PubMed/MEDLINE (via Europe PMC) and Semantic Scholar. Embase and Cochrane CENTRAL were not searched due to institutional access constraints, which may result in incomplete coverage of pharmacology and clinical trial literature."
4. 评估Agent 标记此数据库覆盖缺口为 ⚠️

---

## 注意事项

1. **不要修改检索式**：以上检索式已按各数据库语法优化（PubMed MeSH→Emtree映射，Cochrane MeSH适配），手动修改可能导致不同构。
2. **导出全部结果**：不筛选、不摘要查看——筛选交给筛选Agent。
3. **如果某数据库检索结果为 0**：检查VPN连接和数据库选择是否正确，Agent 会验证检索式。
4. **如果某个数据库暂时无法访问**：标注 ⚠️ 跳过，Agent 会在评估报告中记录。

---

*本清单由文献搜索Agent 预编译。Embase检索式含 MeSH→Emtree 术语映射。*
*预编译日期: 2026-06-05*
*状态: ⚠️ VPN不可用 — 待用户获取机构访问权限后执行*
