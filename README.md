# Cloud Operations Automation

Python automation patterns for safe day-2 cloud operations: inventory normalization, tag compliance, bounded remediation decisions, and auditable execution.

## Capabilities
- Validate required cloud resource metadata
- Produce deterministic remediation plans
- Separate detection from mutation
- Unit-test operational policy
- Run quality checks in GitHub Actions

The policy layer is cloud-provider-neutral so Azure and AWS adapters can be added without rewriting operational rules.

## Safety model
Operational automation follows **detect -> decide -> approve -> execute**. High-impact actions should use least privilege, explicit gates, and recorded outcomes.
