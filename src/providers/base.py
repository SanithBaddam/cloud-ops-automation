from abc import ABC, abstractmethod
from typing import Iterable

from models import Resource


class CloudProvider(ABC):
    @abstractmethod
    def list_resources(self) -> Iterable[Resource]:
        raise NotImplementedError

    @abstractmethod
    def apply_tags(self, resource_id: str, tags: dict[str, str]) -> None:
        raise NotImplementedError
