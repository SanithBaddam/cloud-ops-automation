# Cloud Operations Architecture

```mermaid
flowchart LR
    Schedulers[Scheduler / Event] --> Collector[Inventory Collector]
    Collector --> Policy[Policy Engine]
    Policy --> Plan[Remediation Plan]
    Plan --> Gate[Approval Gate]
    Gate --> Executor[Cloud Executor]
    Executor --> Audit[Audit Log]
    Executor --> Azure[Azure]
    Executor --> AWS[AWS]
```

The policy layer is intentionally separated from provider adapters so the same operational rule can be tested once and executed consistently across clouds.

High-impact actions should require explicit approval, least-privilege credentials, idempotent execution, and structured audit output.
