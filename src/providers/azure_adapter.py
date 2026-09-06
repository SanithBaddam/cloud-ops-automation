from collections.abc import Iterable

from models import Resource
from providers.base import CloudProvider


class AzureAdapter(CloudProvider):
    """Boundary for Azure SDK integration.

    Authentication should use managed identity or workload identity in production.
    """

    def list_resources(self) -> Iterable[Resource]:
        return []

    def apply_tags(self, resource_id: str, tags: dict[str, str]) -> None:
        raise NotImplementedError("Wire to Azure Resource Manager only behind an approval gate.")
