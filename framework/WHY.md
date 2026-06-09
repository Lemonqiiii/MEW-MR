# Why Medical Review Framework?

## The Problem

Writing a high-quality medical review is hard. Really hard.

You spend weeks searching PubMed, screening hundreds of abstracts, taking notes on dozens of papers, synthesizing evidence across interventions, checking every citation, and wrestling with Word formatting — only to discover after submission that you missed 3 key papers, cited an outdated Cochrane version, and never checked whether your RR of 0.77 actually makes clinical sense as an ARR.

**The worst part?** Most of these mistakes are systematic, not random. They happen because a single human brain can't simultaneously track: literature coverage, citation accuracy, statistical translation, argument diversity, domain ontology, narrative structure, and formatting compliance. Something always slips through.

## What This Framework Does

This is an **AI-assisted framework with 11 agent definition files**: 9 pipeline agents plus standalone peer-review and systematic-review modes. The core pipeline agents each focus on one thing and do it systematically:

| Agent | What it does | What you'd do without it |
|-------|-------------|--------------------------|
| **Search** | Multi-database retrieval, dedup, domain ontology | Manually search 3+ databases, export, deduplicate in EndNote |
| **Screen** | A-J paper type classification, inclusion/exclusion with recorded reasons | Read 500 titles/abstracts, track decisions in a spreadsheet |
| **Analyze** | Structured note-taking with evidence grading (G0-G4) | Write paper notes, forget which claims came from which paper |
| **Write** | Draft sections from notes, generate formatted Word (.docx) | Type everything from scratch, manually format |
| **Synthesis** | Cross-intervention matrix, hypothesis generation, gap analysis | Stare at 5 intervention chapters wondering what connects them |
| **Review** | Fact-check claims against sources, scan for 6 language anti-patterns, verify citation scope | Proofread 50 times, still miss things |
| **Submit** | Format compliance, author checklist, disclosure statements | Spend 2 hours on journal-specific formatting |

**And the real innovation: 11 automated quality gates.**

Every agent must pass a gate before the next one starts. Gates are **executable Python scripts**, not honor-system checklists. If Gate 4 (Citation Verification) fails, you can't proceed to Synthesis. No exceptions.

```
Gate 1  → Search quality (dedup rate, data completeness, year distribution)
Gate 2  → Screening quality (exclusion reasoning, type distribution)
Gate 3  → Analysis quality (note completeness, evidence grading)
Gate 4  → Citation verification (cross-check claims vs sources)
Gate 5  → Format integrity (sections, placeholders, orphans)
Gate 6  → Citation scope (type-based citation count rules)
Gate 7  → Domain ontology (coverage completeness)
Gate 8  → Pre-writing planning (narrative arc, figure plan)
Gate 9  → Synthesis quality (cross-intervention matrix, argument diversity)
Gate 10 → Enhanced review (perspective switching, naturalness scan)
Gate 11 → Submission readiness (cleanliness, compliance)
```

## What You Can Do With It

### Write a narrative review
Pick a topic, edit `config.yaml`, say `1`. The pipeline handles everything from literature search to submission-ready Word document. Works for any biomedical topic — neonatology, oncology, immunology, epidemiology.

### Write a systematic review with PRISMA compliance
Set `review_type: "systematic"` in config. The pipeline switches to dual-screening, RoB assessment, GRADE evidence profiles, and PRISMA 2020 checklist generation.

### Peer-review your own manuscript before submission
The built-in peer review agent reads your manuscript as an external reviewer would — catching citation inaccuracies, argument gaps, and structure problems before journal reviewers do.

### Domain-adapt for any field
The framework ships with generic defaults. Add your domain keywords and mechanism categories in `config.yaml`, and the screening/analysis agents automatically adapt. Domain-specific templates can be added without changing the core pipeline.

## Why It's Better Than the Alternative

### vs. Doing it manually
- **Time**: 2-3 weeks → 3-6 hours of guided AI collaboration
- **Errors**: Systematic blind spots → 11 gates catch them before they reach the manuscript
- **Consistency**: Variable attention → Every paper gets the same structured treatment

### vs. Asking ChatGPT to "write a review"
- **Hallucinations**: ChatGPT invents citations with plausible-sounding DOIs. This framework verifies every PMID against PubMed.
- **Shallow synthesis**: ChatGPT writes generic summaries. This framework builds cross-intervention matrices and grades evidence gaps (G0-G4).
- **No quality control**: ChatGPT output is whatever the model decided. This framework has 11 gates, each with pass/fail criteria and actionable error messages.

### vs. Other AI review tools
- **Not a black box**: Every agent's reasoning is recorded. You can audit every decision.
- **Not a one-shot**: The pipeline is iterative. Gates fail, you fix, gates pass, you proceed.
- **Not locked to one provider**: The agent definitions are plain markdown. Use Claude Code, or adapt to any LLM with tool-use capability.

## Who Should Use This

- **Researchers** writing a review for journal submission — get from idea to submission-ready manuscript with systematic quality control
- **Lab groups** maintaining living reviews — the structured pipeline makes updates predictable: re-run search, re-screen, re-synthesize
- **Clinicians** who need an evidence synthesis but don't have weeks to write — answer a PICO question in an afternoon
- **Students** learning how to write reviews — the gate system teaches what "good" looks like by catching mistakes

## Getting Started (60 seconds)

```bash
pip install -r scripts/requirements.txt
# Edit config.yaml — set your topic
claude
# Say "1" to begin search
```

See [QUICKSTART.md](QUICKSTART.md) for the full 5-minute walkthrough.
