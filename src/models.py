from dataclasses import dataclass

@dataclass(frozen=True)
class Resource:
    resource_id: str
    resource_type: str
    tags: dict[str, str]
