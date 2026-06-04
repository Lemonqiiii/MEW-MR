# Harness Engineering — Agent 质量保证框架

## 概述

Harness Engineering 是本项目的质量保证与可观测性层，对 Agent 执行质量进行五个维度的系统性度量和提升：

| 维度 | 核心问题 | 判定方式 |
|------|---------|---------|
| **成功率** | Agent 是否完成了任务？ | L1 技术成功（自动化）+ L2 业务成功（审校Agent判定） |
| **效率** | 完成任务的代价多大？ | 编码Agent自动收集：墙钟时间、工具调用次数、token消耗 |
| **鲁棒性** | 环境抖动/输入扰动时能否正常运行？ | 定期批量跑对抗性测试用例 |
| **安全性** | 是否发生了越权操作？ | 编码Agent被动审计 + 评估Agent复核 |
| **一致性** | 同一任务多次运行，结果是否稳定？ | 每 Phase 重跑基准任务 + 行为路径diff + 语义diff |

## 架构

```
编码Agent (数据收集)              评估Agent (质量判断)
    │                                  │
    ├─ progress/metrics-raw.json ──→   ├─ L2 成功率判定（调用审校Agent）
    ├─ git diff                         ├─ 一致性语义对比
    ├─ 工具调用序列                      ├─ 鲁棒性测试执行
    └─ 安全审计                          └─ 生成 harness/reports/phase-N-report.md
```

## 文件说明

| 文件 | 内容 |
|------|------|
| `metrics.md` | 五维度度量定义、计算公式、判定标准 |
| `eval-log.md` | 结构化评估日志模板（评估Agent写入） |
| `test-scenarios.md` | 鲁棒性对抗测试场景库（L1-L5） |
| `safety-policy.md` | 安全策略与越权检测规则 |
| `consistency-benchmarks.md` | 一致性基准任务定义 |
| `reports/` | 各 Phase 评估报告存档 |

## 执行节奏

| 活动 | 频率 | 执行者 |
|------|------|--------|
| 效率数据收集 | 每次任务 | 编码Agent |
| 安全审计 | 每次任务 | 编码Agent |
| L2 成功率判定 | 每次任务 | 评估Agent（调用审校Agent） |
| 一致性测试 | 每 Phase 结束 | 评估Agent |
| 鲁棒性测试 | 每 Phase 结束 | 评估Agent |
| 综合评估报告 | 每 Phase 结束 | 评估Agent |
