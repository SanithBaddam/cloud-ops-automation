from models import Resource

REQUIRED_TAGS = {"owner", "environment", "cost_center"}

def missing_tags(resource: Resource) -> set[str]:
    return REQUIRED_TAGS - set(resource.tags)

def remediation_plan(resource: Resource) -> dict:
    missing = sorted(missing_tags(resource))
    return {
        "resource_id": resource.resource_id,
        "compliant": not missing,
        "missing_tags": missing,
        "action": "none" if not missing else "request_metadata",
    }
