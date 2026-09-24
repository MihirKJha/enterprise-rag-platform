from dataclasses import dataclass


@dataclass
class DocumentChunk:
    id: str
    document_id: str
    content: str
    position: int
    metadata: dict[str, object]
