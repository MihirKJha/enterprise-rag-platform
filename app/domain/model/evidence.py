from dataclasses import dataclass


@dataclass
class Evidence:
    content: str
    document_id: str
    source: str
    metadata: dict[str, object]
    retrieval_score: float | None = None
