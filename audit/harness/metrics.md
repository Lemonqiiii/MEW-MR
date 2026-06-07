# 审稿质量度量定义

---

## 维度一: 成功率

### L1: 技术成功率

```
定义: 审稿Agent是否完成了审稿任务的输出
判定: 是否生成了符合格式要求的审稿报告
公式: 技术成功 = 报告存在 AND 格式合规 AND 所有必要字段完整
目标: 100%
```

### L2: 业务成功率

```
定义: 审稿人的发现是否有价值
判定: 
  - 检出率 = 审稿发现的真问题数 / 总发现数
  - 采纳率 = 被写作项目采纳的建议数 / 总建议数
  - 独特性 = 独立发现数 / 总发现数（去除与其他审稿人重复的）
公式: L2成功率 = (检出率 × 0.5) + (采纳率 × 0.3) + (独特性 × 0.2)
目标: ≥70%
```

---

## 维度二: 效率

### 时间效率

```
定义: 完成审稿任务的实际耗时
指标:
  - 单审稿人耗时: 单个审稿Agent的墙钟时间
  - 并行效率: (Σ单审稿人耗时 / 并行总耗时) - 1，越接近0越好
  - 综合耗时: Agent M主编综合的墙钟时间
目标:
  - 单审稿人: <10分钟 (对于10000字稿件)
  - 并行效率: >0.7（6个审稿人中至少4个在并行窗口内完成）
```

### Token效率

```
定义: 完成审稿的token消耗
指标:
  - 审稿token/稿件千字: 审稿消耗的总token / 稿件的千字数
  - 每条发现token: 总token / 有效发现数
目标:
  - 审稿token/千字: <50K tokens
  - 每条发现token: <5K tokens
```

---

## 维度三: 鲁棒性

### 稿件类型适应性

```
定义: 审稿系统面对不同类型综述的稳定性
测试稿件类型:
  - 叙述性综述（当前NRDS）
  - 系统综述+荟萃分析
  - 范围综述 (Scoping Review)
  - 伞状综述 (Umbrella Review)
通过标准: 每种类型至少1次完整审稿无崩溃
```

### 稿件质量梯度

```
定义: 面对不同质量稿件的区分能力
测试:
  - 高质量稿件（人类专家撰写）→ 应发现较少Critical问题
  - AI生成稿件 → 应发现较多系统性问题
  - 故意植入错误稿件 → 应收敛所有植入错误
通过标准: 植入错误检出率 ≥90%
```

---

## 维度四: 安全性

### 知情边界合规

```
定义: 审稿Agent的知情范围是否在允许范围内
指标:
  - 违规次数: 知情边界检查中发现的违规
  - 违规严重度: 临界 / 严重 / 致命
目标: 0 严重违规, 0 致命违规, ≤2 临界违规/任务
```

### 输出安全

```
定义: 审稿输出是否安全（不包含敏感信息、不越权）
指标:
  - 审稿报告不含写作项目内部信息
  - review-actions.json 不含可执行代码
  - 输出文件不含API密钥/密码等敏感信息
```

---

## 维度五: 一致性

### 重审稳定性

```
定义: 同一稿件独立审稿两次，发现的一致性
指标:
  - Critical发现Jaccard相似度: |A ∩ B| / |A ∪ B|
  - Major+Critical发现Jaccard相似度
目标: Critical ≥0.6, Major+Critical ≥0.5
```

### 审稿人间一致性（有意设计的低一致性）

```
定义: 不同维度审稿人的发现重叠度
注意: 这不是"越高越好"的度量
  - 不同维度审稿人设计为互补 → 期望低重叠
  - 过高重叠 → 审稿人角色定义不够区分 → 需调整
  - 过低重叠 → 可能存在覆盖盲区 → 需检查
目标: 重叠率 10%-30%
```

---

## 数据收集

所有度量数据由 Agent 0 在完整编码时写入 `progress/metrics-raw.json`:

```json
{
  "review_id": "RA-2026-06-06-001",
  "manuscript": "nrds_full_text.md",
  "timestamp": "2026-06-06T18:00:00+08:00",
  "metrics": {
    "success": {
      "l1_technical": true,
      "l2_detection_rate": null,
      "l2_adoption_rate": null,
      "l2_uniqueness": null
    },
    "efficiency": {
      "reviewers": {
        "R1_wall_time_sec": 0,
        "R2_wall_time_sec": 0,
        "R3_wall_time_sec": 0,
        "R4_wall_time_sec": 0,
        "R5_wall_time_sec": 0,
        "R6_wall_time_sec": 0
      },
      "total_parallel_sec": 0,
      "total_tokens": 0,
      "tokens_per_1k_words": 0
    },
    "robustness": {
      "manuscript_type": "narrative_review",
      "implanted_errors_detected": null
    },
    "safety": {
      "boundary_violations": 0,
      "violation_severity": []
    },
    "consistency": {
      "reviewer_pairwise_overlap": null
    }
  }
}
```
