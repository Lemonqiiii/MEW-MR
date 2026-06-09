# Example Active Review — NRDS Life-Course Review

This file preserves the historical example that originally lived in `audit/memory/active-review.md`. It is retained as a demonstration of the audit system's output and should not be treated as the default active review for new users.

## 审稿进度: 8/8 (100%) ✅ 全部完成

| 步骤 | 状态 | 关键结果 |
|------|:--:|------|
| R1-R6 审稿 | ✅ | 31条原始发现 |
| **V 引用验证** | **✅** | **8条抽样: 0%通过率 — 发现系统性数字偏差** |
| **M 主编综合** | ✅ | 12条合并发现 + 优先级路线图 |
| F 输出 | ⬜ | 待生成 review-actions.json |

## Agent V 关键发现 🔴

**8条关键引用Layer 2验证: 0/8 (0%) 完全匹配**

| 引用 | 偏差类型 | 严重性 |
|------|---------|:--:|
| [3] McGoldrick 2020 ACS | 4个RR全部偏离(系统向乐观方向) | **C** |
| [16] Abdel-Latif 2021 LISA | Death/BPD RR 0.77→实际0.59(36%偏差) | **C** |
| [5] Klingenberg 2017 VTV | 通气时间MD −2.36→实际−1.35(75%偏差) | **C** |
| [20] Ninan 2022 JAMA Peds | 选择性引用—忽略关键effect modification | **C** |
| [14] Doyle 2021 Early CS | Dexa亚组vs整体分析混淆 | M |
| [17] Askie 2017 Oxygen | 点估计接近但CI差异 | M |
| [21] Crowther 2019 Repeat ACS | 结局名称错误(RDS≠respiratory support) | M |
| [11] Twilhaar 2018 | SD低估(0.7-0.8 vs 0.86) | m |

## 全局评估

验证结果 + META-1(均质化) + META-2(沉默失明) = **三重缺陷组合**:
**遗漏内容 → 均质化剩余内容 → 均质化使用的数字可能不准确**

