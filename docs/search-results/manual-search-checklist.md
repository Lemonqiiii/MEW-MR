# VPN 手动检索清单

> **使用说明**: 搜索Agent 在完成 Tier 1 自动检索后，生成此清单。您需要在一次 VPN 连接中按清单逐个数据库执行检索并导出结果。完成后说"全文已就绪"或"检索结果已就绪"，Agent 会自动导入和处理。

---

## 当前检索任务

**检索主题**: [待搜索Agent 生成后填入]

**检索日期**: [YYYY-MM-DD]

**预计总耗时**: [搜索Agent 估算]

---

## 操作顺序

建议按以下顺序执行，每个数据库导出完成后将文件放入 `docs/search-results/`：

---

### 1. Embase (via Ovid)

- [ ] 连接医学院 VPN
- [ ] 打开 Ovid Embase: [URL]
- [ ] 选择 "Advanced Search"
- [ ] 逐行粘贴以下检索式并执行:

```
[Agent 预编译的 Ovid 检索式]
```

- [ ] 应用筛选条件: [年份/语言/文献类型]
- [ ] 点击 "Export" → 选择格式: **RIS**
- [ ] 选择导出范围: **All Results**
- [ ] 导出字段选择: Citation + Abstract + Keywords
- [ ] 保存文件到: `E:\medical-review\docs\search-results\embase-export.ris`
- [ ] **实际命中数**: ________ (请填入，Agent 用于对比预期)

---

### 2. Cochrane Library

> 仅在综述涉及 RCT/临床试验时激活

- [ ] 打开 Cochrane Library: https://www.cochranelibrary.com/
- [ ] 选择 "Advanced Search"
- [ ] 粘贴检索式:

```
[Agent 预编译的 Cochrane 检索式]
```

- [ ] 切换到 "Trials" 标签页 (CENTRAL)
- [ ] 点击 "Export Selected" → 选择格式: **RIS**
- [ ] 保存文件到: `E:\medical-review\docs\search-results\cochrane-export.ris`
- [ ] **实际命中数**: ________
- [ ] (可选) 切换到 "Cochrane Reviews" 标签页 → 重复导出

---

### 3. CNKI (中国知网)

> 仅在综述涉及中国人群/中医药/亚洲流行病学时激活

- [ ] 打开 CNKI: https://www.cnki.net/
- [ ] 选择 "专业检索"
- [ ] 粘贴检索式:

```
[Agent 预编译的 CNKI 专业检索式]
```

- [ ] 点击检索
- [ ] 筛选: [年份/语言/文献类型]
- [ ] 全选 → 导出 → 选择格式: **EndNote** (或 RIS)
- [ ] 保存文件到: `E:\medical-review\docs\search-results\cnki-export.txt` 或 `.ris`
- [ ] **实际命中数**: ________

---

### 4. 万方数据

> 仅在综述涉及中国人群/中医药/亚洲流行病学时激活

- [ ] 打开万方: https://www.wanfangdata.com.cn/
- [ ] 选择 "高级检索"
- [ ] 粘贴检索式:

```
[Agent 预编译的万方检索式]
```

- [ ] 点击检索 → 全选 → 导出
- [ ] 保存文件到: `E:\medical-review\docs\search-results\wanfang-export.ris`
- [ ] **实际命中数**: ________

---

### 5. SinoMed (中国生物医学文献数据库)

> 仅在综述涉及中医药/中西医结合时激活

- [ ] 打开 SinoMed: [URL]
- [ ] 粘贴检索式 → 导出
- [ ] 保存文件到: `E:\medical-review\docs\search-results\sinomed-export.txt`
- [ ] **实际命中数**: ________

---

## 完成后

- [ ] 所有文件已放入 `docs/search-results/`
- [ ] 实际命中数已填入各节
- [ ] 关闭不需要的 VPN 连接
- [ ] 在 Claude Code 中说: **"检索结果已就绪"**

---

## 注意事项

1. **不要修改检索式**：Agent 已根据各数据库语法优化过检索式，手动修改可能导致与自动检索的 PubMed/S2/EPMC 检索式不同构，影响后续合并去重。
2. **导出全部结果**：不筛选、不摘要查看——筛选交给筛选Agent 在统一去重后做，减少人为偏差。
3. **如果某数据库检索结果为 0**：不要重新搜索，直接填入 0，Agent 会验证检索式并排查原因。
4. **如果某个数据库暂时无法访问**：标注 ⚠️ 跳过，Agent 会在评估报告中记录为数据库覆盖缺口。

---

*本清单由文献搜索Agent 在每次检索任务前自动生成。*
*最后更新: 2026-06-04*
