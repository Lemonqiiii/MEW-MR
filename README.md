# MEW-MR — Medical Evidence Writing & Meta-Review Framework

AI-assisted framework for systematic narrative reviews, built on Claude Code with multi-agent orchestration.

## Quick Start

```bash
git clone git@github.com:Lemonqiiii/MEW-MR.git
cd MEW-MR
# Start Claude Code — CLAUDE.md auto-loads
claude
```

On first use, create `memory/project-status.md` and `memory/active-focus.md` to define your review topic and PICO.

## Project Structure

```
.
├── CLAUDE.md                  # Auto-loaded: core rules, command shortcuts, Gate overview
├── AGENTS.md                  # Canonical detailed rules (loaded on demand)
├── README.md
├── .gitignore
│
├── memory/                    # Project state & agent definitions
│   ├── MEMORY.md              #   Memory index
│   └── agent-specializations.md  # Agent 0-5 definitions
│
├── harness/                   # Quality assurance protocols
│   ├── quality-gate.md        #   Gate 0-11 checklist
│   ├── review-revision-protocol.md  # Review → fix → verify → respond workflow
│   ├── search-screening-protocol.md # Literature search & screening standards
│   ├── safety-policy.md       #   Access control & security
│   ├── metrics.md             #   Five-dimension evaluation framework
│   └── ...                    #   ~20 additional protocol files
│
├── scripts/                   # Automation scripts
│   ├── gen_word_full.py       #   Markdown → Word generator
│   ├── audit_manuscript.py    #   Manuscript integrity checker
│   ├── gate_search_check.py   #   Gate Search validator
│   ├── gate_screening_check.py #  Gate Screening validator
│   ├── review_revision_check.py # Gate Revision validator
│   ├── process_integrity_check.py  # Gate 0: project routing check
│   ├── cross_reference_check.py    # Cross-file consistency validator
│   ├── rebuild_refs.py        #   Reference list rebuilder
│   ├── run_harness_checks.py  #   One-click harness check runner
│   └── ...
│
├── docs/                      # Reference knowledge
│   ├── methods/               #   Systematic review, meta-analysis, statistics guides
│   └── glossary.md            #   Medical terminology
│
├── knowledge/                 # Domain knowledge templates
│   └── domain-ontology-template.md  # Intervention inventory + evidence gap grading
│
└── features/
    └── FEATURE_LIST.md        # Task tracking
```

## Agent System

| Agent | Trigger | Responsibility |
|-------|---------|---------------|
| Agent 1 | `搜索` | Literature search + screening |
| Agent 2 | `分析` | Deep paper analysis |
| Agent 3 | `写作` | Writing + synthesis reasoning |
| Agent 4 | `审校` | Review (fact-check, logic, naturalness, citation scope) |
| Agent 5 | `评估` | Quality assessment |
| Agent 0 | `编码` | Progress encoding + safety audit + Git |

## Quality Gates

| Tier | Gates | Policy |
|------|-------|--------|
| CORE | G0–G6 | Enforced every phase — blocks next phase on failure |
| ENHANCED | G7–G11 | Conditional — activate per project type |

## Review Protocol

Six-stage workflow: Intake → Normalize → Prioritize → Fix → Verify → Respond

See `harness/review-revision-protocol.md` for the full protocol with severity taxonomy, JSON action schema, and Gate Revision rules.

## License

MIT
