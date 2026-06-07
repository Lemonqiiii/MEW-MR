# Citation Discipline

## Iron Rule
- Every claim must be supported by at least one cited paper's **abstract** (full text is better)
- **NEVER** extract knowledge from training data and attach it to unrelated citations
- Before expanding a paragraph, verify the claim-citation pairing

## Citation Scope Rules

Each paper receives a **scope label** during screening (see Agent 6 citation scope matrix).
Writing and review must respect these labels:

### Absolute Prohibitions
- ❌ Use type G (narrative review) as **primary citation** for any claim — reviews do not produce new data; cite the original paper
- ❌ Use type I (case report) to **solely support** a general claim — single cases ≠ population evidence
- ❌ Use type E (pure bioinformatics) to support a **causal mechanism claim** — correlation ≠ causation; use types A/B/C/D

### Requires Qualifier
- ⚠️ Claims supported by type E → must use "is associated with" / "correlates with" (not "causes" / "drives")
- ⚠️ Type D alone supporting mechanism claims → must add "clinical evidence suggests" / "translational data indicate"
- ⚠️ Type G as auxiliary citation → mark as "(reviewed in [N])", not as primary reference number

### Review-Time Verification
Agent 4 must verify during Step 7 (citation scope compliance check):
- Mechanism claim primary citations come from types A/B/C
- No type G used as primary citation
- No type I solely supporting a general claim
- No type E used for causal mechanism claims

## Citation Parsing Rules
All reference-counting scripts must handle three formats: `[N]`, `[N,M]`, `[N-M]`
