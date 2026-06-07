# Why Medical Review Audit?

## The Problem with Peer Review

Peer review is the foundation of scientific quality control — and it's breaking.

**One reviewer catches methodological flaws but misses statistical errors. Another flags missing literature but doesn't check whether the numbers are correct. A third suggests narrative improvements but can't assess clinical relevance.** Each reviewer works in isolation, their findings never cross-referenced. The editor must reconcile three contradictory reports into a coherent decision.

Meanwhile, systematic errors sail through:
- Citation numbers that don't match their sources (our verification found a **0% match rate** on one manuscript)
- Missing interventions that every reviewer assumed someone else would catch
- Template writing patterns that look complete but homogenize evidence of vastly different quality
- Statistical claims (RR, CI) without clinical translation (ARR, NNT)

**The root cause?** Human reviewers each bring one perspective. No single reviewer can be simultaneously strong in methodology, clinical reasoning, logic, statistics, literature coverage, and narrative structure.

## What This System Does

This is a **6-dimension parallel review system** — six specialized reviewer agents, plus citation verification, plus editor synthesis — that find what individual reviewers miss by cross-referencing findings.

```
Manuscript → 6 parallel reviews → Citation verification → Editor synthesis → Structured report
```

### The 6 Reviewers

| Reviewer | Focus | Example finding |
|----------|-------|-----------------|
| **R1: Methodology** | Study design, bias risk, evidence grading, review type consistency | "Claims 'narrative review' but uses 'systematic search' terminology — methods identity crisis" |
| **R2: Clinical** | Clinical reasoning depth, intervention knowledge, practice applicability | "Caffeine therapy — the most common NICU respiratory drug — is entirely absent from the manuscript" |
| **R3: Logic & Argument** | Argument diversity, reasoning chain completeness, claim-evidence matching | "Same Pattern A template repeated 5 times across chapters with no variation" |
| **R4: Statistics & Data** | Effect size interpretation, RR→ARR/NNT translation, P-value accuracy | "92% of reported effect sizes lack absolute risk translation — 30+ RRs, only 1 ARR" |
| **R5: Literature Coverage** | Citation completeness, key paper omission, citation bias, disciplinary blind spots | "49% of references are Cochrane reviews — missing the original RCTs beneath them" |
| **R6: Structure & Narrative** | Logical flow, section weighting, narrative arc, reader experience | "The chapter with 30 years of data = the chapter with zero data = 900 words each" |

### Two-Layer Citation Verification

**Layer 1** checks that every cited PMID/DOI actually exists (API verification against PubMed).  
**Layer 2** spot-checks key claims by opening the cited paper and comparing the numbers. Our test run found a 0% match rate on 8 sampled citations — effect sizes and confidence intervals systematically deviated from their sources.

### Editor Synthesis & Convergence Analysis

The real innovation: **cross-reviewer convergence detection.** When 5 out of 6 reviewers independently discover the same problem from different angles, that's not 5 separate findings — it's one **deep structural defect** with 5 lines of converging evidence.

Example from a real review:
```
🔴 Five-way convergence: Evidence homogenization
  R1: Evidence grades used interchangeably
  R2: Gaps of different natures collapsed into "no long-term data"
  R3: Identical argument template repeated mechanically
  R5: Cochrane dependency makes all interventions look equally outdated
  R6: Equal chapter weighting regardless of evidence volume
→ Editor synthesis: "The manuscript lacks the ability to make qualitative distinctions"
```

This is the kind of insight no single human reviewer can produce — because no single reviewer sees all five dimensions at once.

## What You Can Do With It

### Peer-review a manuscript before journal submission
Run your own manuscript through the system before sending it to a journal. Find and fix the problems before external reviewers do. Our test run on a real manuscript found 31 issues — 7 critical — that the authors' own self-review had missed.

### Audit a preprint or published paper
Want to critically evaluate a paper in your field? Feed it in, get a structured 6-dimension assessment. Useful for journal clubs, systematic review screening, or just building your critical appraisal skills.

### Power a review pipeline
Pair this with the [Medical Review Framework](https://github.com/...) — the framework writes, this audits. Write → Audit → Revise → Re-audit. Each cycle catches problems the previous one missed.

### Train reviewers
The 6-dimension structure is an excellent teaching tool. Each reviewer's output shows what "good" looks like for that dimension. The convergence analysis teaches how different perspectives illuminate the same underlying problem.

## Why Write-Review Separation Matters

Most AI writing tools have a **self-review problem**: the same system that wrote the text is asked to review it. It shares the same knowledge boundaries, the same blind spots, the same assumptions. It can't see what it can't see.

This system operates under **limited knowledge boundary** — it sees only the manuscript and a disclosure packet. It doesn't know which papers were considered and rejected. It doesn't know the authors' reasoning. This is deliberate: it mimics what an external reviewer actually sees.

```
Writing project          Audit project
     │                        │
     │  manuscript + packet   │
     ├──────────────────────→ │  (only these files)
     │                        │
     │                        ├─ R1 methodology
     │                        ├─ R2 clinical
     │                        ├─ R3 logic
     │                        ├─ R4 statistics
     │                        ├─ R5 literature
     │                        ├─ R6 structure
     │                        ├─ V citation verification
     │                        └─ M editor synthesis
     │                        │
     │  review-actions.json   │
     │ ←──────────────────────┤  (machine-parseable)
     │                        │
     │  fix → re-audit        │
```

## Getting Started

```bash
# Place a manuscript in review-pipeline/input/
cp your-manuscript.md review-pipeline/input/

# Quick structural check
python3 scripts/check-structure.py review-pipeline/input/your-manuscript.md

# Generate disclosure packet (for the reviewers)
python3 scripts/gen-review-pack.py review-pipeline/input/your-manuscript.md

# Verify all citations against PubMed
python3 scripts/verify-citations.py review-pipeline/input/your-manuscript.md

# Full review (via Claude Code)
claude
# Say "审稿" or "peer-review" to start the 6-dimension pipeline
```

**Requirements**: Python 3.10+. All scripts use standard library only — no pip install needed.

See [README.md](README.md) for the full architecture and command reference.
