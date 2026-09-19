# Cluster - consensus on partition

A GenLayer Intelligent Contract that groups records into "these are the same"
clusters under a textual criterion. The consensus object is a partition of
unknown group count, compared by canonical labeling.

## Consensus mechanism

Validators agree on a per-pair same/different relation. Stage C closes that
relation transitively with union-find and labels clusters canonically by their
smallest member index, so two validators that find the same grouping never
disagree over label ids. This is unlike a fixed-length output: the number of
clusters is not known in advance, and the object compared is the canonical
partition.

Only the pairwise same/different vector and the records hash reach consensus,
via `prompt_comparative`. The closure and labeling are deterministic.

## Design decisions made explicit

- Transitive closure is authoritative: A~B and B~C put A, B, C in one cluster
  even without a direct A~C judgment. Pairs merged only through the chain are
  exposed in `tension_pairs` so a reader can see and audit the chain rather than
  it being hidden.
- Canonical labeling by smallest member index is mandatory, or identical
  partitions with different ids fail consensus for no real reason.

## Outcomes

- CLUSTERED: a label per record, plus tension pairs.
- UNDETERMINED: judgment did not converge or records changed after submission.

## API

- `open_clustering(id, sameness_criterion)` -> criterion hash
- `submit_records(id, records)` - 2 to 12 records, committed and hashed
- `cluster(id)` - permissionless
- `get_outcome(id)` -> 0 pending, 1 clustered, 2 undetermined
- `get_labels(id)` -> cluster id per record, empty unless CLUSTERED

## Test plan (run in hosted Studio)

1. Two clear duplicates and one distinct -> two clusters, correct labels.
2. All distinct -> each record its own cluster.
3. All the same -> one cluster.
4. Transitive chain (A~B, B~C, A and C not obviously alike) -> one cluster, the
   A-C pair listed in tension_pairs.
5. Injection in a record -> judged on merit or consensus fails.
6. Records changed after submit -> revert or records-changed UNDETERMINED.
7. Re-cluster after settlement -> revert.

## Notes

SDK compatibility and deployment were verified in hosted Studio. Union-find
closure and canonical labeling are deterministic and checked off-chain; only
the pairwise judgment is non-deterministic.

## Deployment

- GitHub: https://github.com/Zhekinmaksim/genlayer-transitive-record-clusterer
- Studio contract: https://explorer-studio.genlayer.com/address/0x74214E2a395c62D401e2d14CDE3b1cc89CdE5653
- Deploy transaction: https://explorer-studio.genlayer.com/tx/0xca527a11519f3f533eeae4caec9fac195e4a389b511c3c4ef113c658018b4a1a
- Deployed source commit: `88cbc4ec914ea9bfed59523120f12aaf609e9a63`
