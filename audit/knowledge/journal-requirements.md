# 目标期刊审稿标准

> 记录不同目标期刊的审稿标准和格式要求。供 Agent P 配置审稿上下文使用。

---

## Pediatric Research (Springer Nature)

### 基本信息
- **出版商**: Springer Nature
- **IF**: ~3
- **类型**: 综合儿科研究期刊
- **接受综述类型**: 叙述性综述、系统综述、迷你综述

### 综述要求
- 非结构化摘要（叙述性综述）
- 正文结构: Introduction → Main body (作者自定义标题) → Discussion → Conclusion
- 引用格式: 顺序编号 (Vancouver style)
- 字数限制: 视类型而定，一般叙述性综述 ~4000-8000 words
- 图表: 鼓励使用

### 审稿标准
- 时效性: 主题是否前沿且与期刊范围相关？
- 全面性: 是否平衡地覆盖了该领域的关键文献？
- 深刻性: 是否有超出文献总结的洞察？
- 临床相关性: 对儿科临床实践的意义？

---

## JITC (Journal for ImmunoTherapy of Cancer, BMJ)

### 基本信息
- **出版商**: BMJ
- **IF**: ~10
- **类型**: 免疫治疗专科期刊

### 综述要求
- 结构化摘要
- 系统综述需PRISMA
- Vancouver引用格式

---

## 待补充
- 随着审稿项目使用的期刊增加，在本文件中追加

---

## 审稿配置模板

当用户说 `设置 <期刊名>` 时，Agent P加载对应期刊的审稿标准作为审稿上下文的一部分：

```json
{
  "journal": "Pediatric Research",
  "review_type": "narrative_review",
  "word_limit": 8000,
  "citation_style": "vancouver",
  "requires_prisma": false,
  "key_criteria": ["timeliness", "comprehensiveness", "insight", "clinical_relevance"]
}
```
