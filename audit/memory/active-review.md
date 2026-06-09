# 当前审稿任务

## 审稿进度: 未开始

| 字段 | 值 |
|------|----|
| 当前稿件 | 待用户放入 `review-pipeline/input/` |
| 目标期刊 | 待用户指定，或由 `gen-review-pack.py` 参数提供 |
| 综述类型 | 待 Agent P 从稿件中识别 |
| 当前阶段 | 等待预处理 |

## 使用方式

1. 将待审稿件放入 `review-pipeline/input/`
2. 运行结构检查：`python scripts/check-structure.py review-pipeline/input/<manuscript>.md`
3. 生成披露包：`python scripts/gen-review-pack.py review-pipeline/input/<manuscript>.md "<Target Journal>"`
4. 在 Claude Code 中说 `审稿` 或 `peer-review`

## 示例

历史 NRDS 审稿示例已移至 `audit/examples/nrds-lifecourse/active-review.md`。
