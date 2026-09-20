from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Drift:
    resource_id: str
    field: str
    desired: Any
    actual: Any

def detect_drift(resource_id: str, desired: dict, actual: dict) -> list[Drift]:
    keys = set(desired) | set(actual)
    return [
        Drift(resource_id, key, desired.get(key), actual.get(key))
        for key in sorted(keys)
        if desired.get(key) != actual.get(key)
    ]

def classify(drift: Drift) -> str:
    if drift.field in {"network_acl", "public_access", "iam_policy"}:
        return "security_review"
    return "reconcile_review"
