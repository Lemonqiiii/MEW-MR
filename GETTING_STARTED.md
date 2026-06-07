# Getting Started

Welcome. This guide takes you from zero to a working AI-assisted medical review pipeline in under 10 minutes. Every command can be copy-pasted. Expected output is shown so you know things are working.

## What Is This?

Two tools that work together:

| Tool | Does | You'd otherwise spend |
|------|------|----------------------|
| **framework/** | Searches PubMed, screens papers, drafts and formats your review manuscript | 2-3 weeks of manual work |
| **audit/** | Reviews your manuscript through 6 independent expert perspectives, verifies every citation against PubMed | Another week of proofreading you'd still get wrong |

You don't need to use both. Start with the framework — it produces a manuscript on its own. The audit catches what the framework missed.

## Step 0: What You Need

**Hard requirements:**
- Python 3.10 or newer → `python3 --version`
- Git → `git --version`
- Claude Code → install if needed:

```bash
npm install -g @anthropic-ai/claude-code
```

## Step 1: Download

```bash
git clone https://github.com/Lemonqiiii/MEW-MR.git
cd MEW-MR
```

You should see two directories: `framework/` and `audit/`.

## Step 2: Install Dependencies

```bash
cd framework
pip install -r scripts/requirements.txt
```

Expected output: four packages install (or "already satisfied" if you had them).

The audit project needs no dependencies — it uses only Python's standard library.

## Step 3: Verify Everything Works

```bash
python3 scripts/smoke_test.py
```

This runs 34 checks in ~3 seconds. You should see all green checkmarks:

```
Medical Review Framework — Smoke Test
============================================================
── 1. Python Environment ──
  ✅  Python 3.14.5

── 2. Dependencies ──
  ✅  yaml
  ✅  docx
  ✅  requests
  ✅  PIL

── 3. Required Files ──
  ✅  config.yaml
  ✅  state.json
  ...

RESULTS
  Passed:  34/36
  🎉  All checks passed!
```

If you see any red ❌, fix those before continuing. The error message tells you exactly what's wrong and how to fix it.

## Step 4: Try the Demo (5 minutes)

We've included a pre-configured demo topic so you can see the full pipeline immediately:

```bash
cp config.demo.yaml config.yaml
claude
```

When Claude Code starts, it will show the current project phase ("planning") and available actions. Say:

```
1
```

This triggers the Literature Search agent. It will:
1. Assess your topic and plan the search strategy
2. Search PubMed, Semantic Scholar, and Europe PMC
3. Deduplicate results
4. Build a domain ontology of key concepts

The agent will show you what it's doing at each step. When it finishes, it runs quality gates to verify the search was thorough.

**What if WebFetch is blocked?** (Common on corporate/university networks.) The agent will detect this and fall back to WebSearch or Semantic Scholar API. If both are blocked, it will tell you and suggest alternatives. This is a known limitation — not a bug in your setup.

After Agent 1 finishes, try the next steps at your own pace:

| Say | What happens |
|-----|-------------|
| `2` | Screen papers — classify, apply inclusion/exclusion criteria |
| `3` | Analyze — structured note-taking for included papers |
| `4` | Write — generate a formatted Word document |

You can stop at any point. Your progress is saved in `state.json`.

## Step 5: Try the Audit (3 minutes)

The audit project includes a demo manuscript with intentionally seeded issues. See what the review catches:

```bash
cd ../audit
```

### Quick structural check

```bash
python3 scripts/check-structure.py review-pipeline/input/DEMO-MANUSCRIPT.md
```

This tells you word count, section structure, reference count.

### Citation verification

```bash
python3 scripts/verify-citations.py review-pipeline/input/DEMO-MANUSCRIPT.md
```

You'll see 4 real PMIDs verified ✅, and 1 fake PMID (99999999) flagged. This demonstrates what happens when a citation can't be verified.

### Full 6-dimension review

```bash
claude
```

Say `审稿` (or `peer-review`). Six independent reviewer agents will analyze the manuscript in parallel:
- R1: Methodology quality
- R2: Clinical reasoning
- R3: Logic & argument structure
- R4: Statistics & data interpretation
- R5: Literature coverage
- R6: Narrative & structure

They produce a structured report with severity ratings (Critical / Major / Minor). The editor agent then cross-references all findings to identify convergence — problems that multiple reviewers independently discovered from different angles.

## Step 6: Start Your Own Project

Ready to write your own review?

### 6a. Configure your topic

Edit `framework/config.yaml`:

```yaml
project:
  topic: "Your Specific Review Topic Here"
  domain: "oncology, immunotherapy"       # comma-separated keywords
  review_type: "narrative"                # or "systematic"
  target_journal: "Target Journal Name"
  language: "en"
```

That's the minimum. See `config.example.yaml` for every available option.

### 6b. Start the pipeline

```bash
cd ../framework
claude
```

Say `1` to begin. The pipeline is:

```
1 (Search) → 2 (Screen) → 3 (Analyze) → 4 (Write) → 8 (Synthesis) → 5 (Review) → 9 (Submit)
```

Each agent runs quality gates before and after. A gate failure means "fix this before continuing" — not "something is broken." Read the gate output, fix the issue, and continue.

### 6c. Get an external review

After Agent 4 (Write) produces a manuscript in `framework/manuscript/submission.md`:

```bash
cp framework/manuscript/submission.md audit/review-pipeline/input/
cd audit
claude
# Say "审稿"
```

Apply the feedback from `review-pipeline/output/review-actions.json`, then re-audit.

## What Your Project Will Look Like

```
framework/
├── config.yaml           ← Your topic configuration
├── state.json            ← Auto-updated progress (phase, %, metrics)
├── manuscript/
│   ├── submission.md     ← Your manuscript (the source of truth)
│   ├── output.docx       ← Generated Word document
│   └── figures/          ← Auto-generated charts
├── data/                 ← Search results, screening data
└── docs/papers/          ← Structured notes on each paper
```

## Troubleshooting

| You see | What it means | What to do |
|---------|---------------|------------|
| `ModuleNotFoundError: No module named 'yaml'` | Dependencies not installed | `pip install -r scripts/requirements.txt` |
| All 11 gates show FAIL | No data yet. **This is normal.** | Run Agent 1 first. Gates check for artifacts that don't exist until agents create them. |
| `FileNotFoundError: manuscript/submission.md` | No manuscript yet | Complete Agents 1→2→3 first, or create a placeholder file |
| `UnicodeEncodeError: 'gbk' codec...` | Windows terminal encoding | Run with `python3 -X utf8 script.py` or use Windows Terminal (not cmd.exe) |
| WebFetch blocked | Network security policy | Agent 1 will try fallback methods. If all fail, manually download PubMed results. |
| `claude: command not found` | Claude Code not installed | `npm install -g @anthropic-ai/claude-code` |
| Agent asks for API key / login | Claude Code needs auth | Follow the Claude Code setup instructions — it's separate from this project |

## Where to Go Next

| Want to | Read |
|---------|------|
| Understand why this exists | `framework/WHY.md` |
| See every config option | `framework/docs/CONFIG.md` |
| Understand each agent | `framework/claude/agents/` |
| Learn the audit system | `audit/WHY.md` |
| See the full workflow | `framework/docs/WORKFLOW.md` |

---

If something doesn't work and the troubleshooting table doesn't help, open an issue on GitHub.
