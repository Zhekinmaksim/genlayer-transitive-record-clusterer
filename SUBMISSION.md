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
- Deployed source commit: `88cbc4ec914ea9bfed59523120f12aaf609e9a63`
- Explorer contract: https://explorer-studio.genlayer.com/address/0x74214E2a395c62D401e2d14CDE3b1cc89CdE5653
- Deploy transaction: https://explorer-studio.genlayer.com/tx/0xca527a11519f3f533eeae4caec9fac195e4a389b511c3c4ef113c658018b4a1a
- Offline verification: `python3 sim/check.py`, 4/4 pass on 2026-09-19
- Hosted Studio checks: Normal (Full Consensus) deployment finalized; GenVM
  result SUCCESS, consensus Accepted, and Explorer source matches `contract.py`.
