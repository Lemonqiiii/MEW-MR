# Medical & Biology Literature Review Project

## 项目简介
本项目旨在撰写一篇高质量的**医学与生物学英文综述论文**。项目利用 Claude Code 的上下文管理和持久化记忆系统，通过多个专业化子 Agent 协作完成从文献搜索到最终定稿的全流程。

## 项目结构

```
.
├── CLAUDE.md                # Tier 1: 会话常驻核心指引
├── docs/                    # Tier 3: 持久化知识库 (论文笔记)
│   ├── index.md             #   文献索引 (按主题/方法/年份)
│   ├── papers/              #   论文笔记 (按医学主题分类)
│   ├── methods/             #   方法论指南
│   └── glossary.md          #   医学术语表
├── memory/                  # Tier 2: 结构化记忆指针
│   ├── project-status.md    #   项目状态 (当前阶段/进度)
│   ├── active-focus.md      #   当前研究方向
│   ├── key-findings.md      #   核心发现
│   └── agent-specializations.md  # 子Agent定义
├── manuscript/              # 综述手稿
│   ├── outline.md           #   综述大纲
│   ├── draft.md             #   当前草稿
│   └── revisions/           #   历史版本
├── features/                # 任务跟踪
│   └── FEATURE_LIST.md      #   功能清单
└── progress/                # 进度记录
    ├── SESSION_LOG.md       #   会话日志
    └── MILESTONES.md        #   里程碑
```

## Agent 体系

| Agent | 职责 | 触发条件 |
|-------|------|---------|
| **文献搜索Agent** | 多数据库系统检索，去重，生成初筛列表 | "搜索文献" |
| **论文分析Agent** | 结构化提取论文信息，生成文献笔记 | "分析这篇" |
| **综述写作Agent** | 基于论文笔记撰写综述段落 | "写草稿" |
| **审校Agent** | 事实核查、逻辑审查、语言润色 | "审校" |
| **编码Agent** | 记录增量进展，更新项目状态 | 会话结束/手动触发 |

详见 `memory/agent-specializations.md`

## 工作流程

1. **确定主题** → 更新 `memory/active-focus.md`
2. **文献搜索** → 文献搜索Agent检索多数据库
3. **文献筛选** → 人工筛选 + 记录到 `docs/index.md`
4. **深度阅读** → 论文分析Agent逐篇笔记
5. **综述写作** → 综述写作Agent基于笔记撰写
6. **审校定稿** → 审校Agent核查后提交

每个阶段结束时，编码Agent自动更新项目状态。

## 技术栈
- **AI 协作**: Claude Code (DeepSeek V4 Pro 后端)
- **文献检索**: PubMed E-utilities, Semantic Scholar API, Europe PMC
- **版本控制**: Git
- **引用管理**: 待定 (Zotero / EndNote / BibTeX)

## 开始使用

1. 在 `E:\medical-review\` 打开终端
2. 启动 Claude Code (`claude`)
3. CLAUDE.md 自动加载，Agent 会引导你选择下一个任务
4. 说 "搜索文献" / "分析这篇" / "写草稿" / "审校" 触发对应 Agent

---

*项目初始化于 2026-06-04*
