from collections.abc import Iterable

from models import Resource
from providers.base import CloudProvider


class AwsAdapter(CloudProvider):
    """Boundary for boto3 integration.

    Production execution should assume a narrowly scoped IAM role rather than use static keys.
    """

    def list_resources(self) -> Iterable[Resource]:
        return []

    def apply_tags(self, resource_id: str, tags: dict[str, str]) -> None:
        raise NotImplementedError("Wire to AWS tagging APIs only behind an approval gate.")
