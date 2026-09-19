# Test plan - Transitive Record Clusterer

## Offline checks

1. Two duplicates and one distinct record produce labels `[0, 0, 1]`.
2. All-different records produce one cluster per record.
3. All-same records produce one cluster.
4. A transitive A-B, B-C chain merges all three and records A-C as tension.
5. Two to twelve records are accepted; empty, duplicate, and overlong records
   revert before judgment.
6. Recomputed stored-record hash must equal the commitment before clustering.
7. A second `cluster` call after settlement reverts.

## Hosted Studio checks

Deploy the exact GitHub revision and repeat the duplicate/distinct and
transitive-chain cases. Record the canonical labels, tension pairs, deploy hash,
and smoke transaction hashes. LLM convergence remains a live-only check.
