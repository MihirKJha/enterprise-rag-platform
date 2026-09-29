from dataclasses import dataclass

from app.domain.value_objects.document_id import DocumentId


@dataclass
class Document:
    id: DocumentId
    content: str
    metadata: dict[str, object]
