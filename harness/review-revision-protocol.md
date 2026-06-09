# Review and Revision Protocol

> Purpose: turn peer review, internal review, and journal feedback into traceable actions that can be fixed, verified, and answered without losing the current manuscript context.

---

## 1. Scope

This protocol applies to:

- internal Agent 4 review reports
- external peer review from collaborators
- journal reviewer comments and editor letters
- post-revision self-checks before Word generation or submission

It governs the process, not the manuscript content. All content edits must use `current_manuscript` resolved from `memory/project-status.md` and `memory/active-focus.md`.

---

## 2. Required Files

| File | Purpose |
|------|---------|
| `docs/review/review-action-log.json` | Structured action list for all review comments |
| `docs/review/response-to-reviewers.md` | Draft response letter mapped to action IDs |
| `manuscript/CHANGELOG.md` | Revision-round change history |
| `manuscript/REVISION_MAP.md` | Grep anchors proving each action was resolved |
| `scripts/review_revision_check.py` | Gate Revision executable check |

Historical reports may remain in `manuscript/`, but current revision work must be routed through `docs/review/review-action-log.json`.

---

## 3. Severity Taxonomy

| Severity | Meaning | Blocks submission? |
|----------|---------|-------------------|
| `critical` | Factual error, citation mismatch, unsafe clinical statement, arithmetic contradiction, or journal-blocking compliance issue | Yes |
| `must_fix` | Important scientific, structural, or methodological problem that must be corrected before the next round | Yes |
| `major` | Substantive improvement needed, but not immediately unsafe if explicitly deferred with rationale | Yes unless status is `deferred` with rationale |
| `minor` | Local clarity, style, formatting, or precision issue | No |
| `suggestion` | Optional improvement | No |
| `editorial` | Typo, grammar, punctuation, formatting | No |

Allowed statuses: `open`, `in_progress`, `resolved`, `verified`, `deferred`, `rejected`.

Rules:

- `critical` and `must_fix` actions may not remain `open`, `in_progress`, `deferred`, or `rejected` at Gate Revision.
- `major` actions may be `deferred` only if `deferral_rationale` is non-empty and the response letter explains the decision.
- Every `resolved` or `verified` action must include at least one verifier.

---

## 4. Action Schema

Each action in `docs/review/review-action-log.json` must contain:

```json
{
  "id": "RR-001",
  "source": "Agent4-R2 | external-reviewer-1 | journal-reviewer-2",
  "severity": "critical | must_fix | major | minor | suggestion | editorial",
  "status": "open | in_progress | resolved | verified | deferred | rejected",
  "location": {
    "file": "current_manuscript",
    "section": "Methods",
    "anchor": "short grep-able phrase"
  },
  "problem_type": "citation_mismatch | data_error | logic_gap | missing_context | language | formatting | compliance | other",
  "problem": "What is wrong?",
  "suggested_fix": "What should change?",
  "resolution": "What was changed, or why not?",
  "verifiers": [
    {
      "type": "grep | script | manual | literature",
      "command_or_anchor": "grep anchor or script command",
      "result": "pass | fail | pending",
      "checked_by": "Codex | Claude | human",
      "checked_at": "YYYY-MM-DD"
    }
  ],
  "response_draft": "Text for response-to-reviewers.md"
}
```

---

## 5. Workflow

1. **Intake**
   - Read the review source.
   - Resolve current context.
   - Convert every actionable comment into `docs/review/review-action-log.json`.
   - Preserve reviewer wording in `problem` or a linked source file.

2. **Normalize**
   - Assign severity and problem type.
   - Merge duplicates only when they point to the same underlying defect.
   - Split compound comments when one reviewer comment requires multiple edits.

3. **Prioritize**
   - Fix in this order: `critical` -> `must_fix` -> `major` -> `minor` -> `editorial` -> `suggestion`.
   - If a major item is deferred, record rationale before moving on.

4. **Fix**
   - Edit only `current_manuscript` or supporting current-project files.
   - Do not edit historical reports to make checks pass.
   - Do not resolve an action by changing its severity after the fact unless the rationale is recorded.

5. **Verify**
   - Add a grep anchor, script command, or manual/literature verifier for every resolved action.
   - Update `manuscript/REVISION_MAP.md`.
   - Run `python scripts/review_revision_check.py`.

6. **Respond**
   - Update `docs/review/response-to-reviewers.md`.
   - Every blocking action must have a response paragraph.
   - Rejected/deferred items must be polite, evidence-based, and explicit.

7. **Record**
   - Append the revision round to `manuscript/CHANGELOG.md`.
   - Increment the manuscript revision marker if the manuscript contains one.
   - Record model/API provenance when AI generated, triaged, or verified review actions.

---

## 6. Gate Revision

Gate Revision passes only when:

- `docs/review/review-action-log.json` exists and is valid JSON.
- Metadata `current_manuscript` matches the current project manuscript.
- Every action has required fields.
- No `critical` or `must_fix` action is unresolved.
- No unresolved `major` action lacks `deferral_rationale`.
- Every resolved/verified action has a passing verifier.
- `manuscript/CHANGELOG.md` references the current manuscript.
- `manuscript/REVISION_MAP.md` references the current manuscript and contains no current default to `jitc_submission.md`.
- `docs/review/response-to-reviewers.md` has a section for each blocking action, unless there are no blocking actions yet.

