# Portal submission - Transitive Record Clusterer

## Title

Transitive Record Clusterer

## Notes under 1000 chars

```text
A GenLayer IC that groups two to twelve records under a fixed sameness criterion.
Validators compare a bounded same/different vector over canonical record pairs;
union-find, transitive closure, dense canonical labels and tension reporting are
deterministic. Records are normalized, bounded, committed and integrity-checked
before judgment. Tension pairs expose records merged only through a transitive
chain, so closure does not silently hide disagreement in the direct relation.
```

## Evidence checklist

- GitHub: https://github.com/Zhekinmaksim/genlayer-transitive-record-clusterer
- Commit: pending
- Explorer contract: pending
- Deploy transaction: pending
- Offline verification: `python3 sim/check.py`, 4/4 pass on 2026-09-12
- Hosted Studio checks: pending
