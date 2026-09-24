from dataclasses import dataclass


@dataclass
class Document:
    id: str
    content: str
    source: str
    metadata: dict[str, object]
    version: str | None = None
