import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from models import Resource
from tag_compliance import remediation_plan

def test_noncompliant_resource_is_not_mutated_automatically():
    resource = Resource("vm-001", "virtual_machine", {"owner": "platform"})
    plan = remediation_plan(resource)
    assert plan["compliant"] is False
    assert plan["action"] == "request_metadata"
    assert plan["missing_tags"] == ["cost_center", "environment"]
