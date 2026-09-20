# Runbook: Infrastructure Drift

1. Identify the resource and changed field.
2. Determine whether the change came from an emergency action, manual administration, another automation system, or provider behavior.
3. Do not automatically overwrite security-sensitive drift without review.
4. Decide whether Git/IaC or the live environment represents the intended state.
5. Reconcile the losing side through the normal change process.
6. Record recurring drift and remove the path that permits uncontrolled mutation.

Security-related changes such as public access, IAM policy, or network ACL modifications require explicit review.
