# Automation Safety Model

1. **Detect** — collect state without mutation.
2. **Decide** — evaluate deterministic policy.
3. **Approve** — require an explicit gate for destructive/high-impact actions.
4. **Execute** — use least privilege and record the result.

Stopping compute, rotating credentials, deleting snapshots, or changing network rules should never be inferred from a single weak signal.
