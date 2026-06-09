# Revision Workflow

Use this when an audit run produces `review-actions.json`.

## 1. Import Review Actions

From `framework/`:

```bash
python3 scripts/import_review_actions.py ../audit/review-pipeline/output/review-actions.json
```

Windows PowerShell:

```powershell
python scripts/import_review_actions.py ..\audit\review-pipeline\output\review-actions.json
```

The script validates the minimum schema and writes a human-readable checklist to:

```text
manuscript/review-actions-import.md
```

It does not modify the manuscript.

## 2. Fix in Priority Order

Recommended order:

1. `critical`
2. `major`
3. `minor`
4. `suggestion`

For each action, record:

- what changed
- where it changed
- how it was verified
- whether the action was accepted, rejected, or deferred

## 3. Re-run Checks

After edits:

```bash
python3 scripts/audit_manuscript.py
python3 scripts/verify_gates.py --gate 4
python3 scripts/verify_gates.py --gate 5
```

Then re-run the audit project if you need independent confirmation.
