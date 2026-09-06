# Runbook: Credential or Secret Expiry

## Detection
Alert before expiry with enough lead time for ownership and rotation. Include owner, environment, dependent service, and expiry timestamp.

## Response
1. Confirm whether the credential is actively used.
2. Identify all consumers before rotation.
3. Create a new version rather than overwriting when the platform supports versioning.
4. Update consumers through their normal deployment path.
5. Validate authentication and error rates.
6. Revoke the old credential only after all consumers are confirmed healthy.

Prefer managed identity, workload identity, or IAM roles over long-lived secrets whenever possible.
