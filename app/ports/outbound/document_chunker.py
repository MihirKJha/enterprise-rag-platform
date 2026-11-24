from abc import ABC, abstractmethod

from app.domain.model.document import Document
from app.domain.model.document_chunk import DocumentChunk


class DocumentChunker(ABC):
    """Contract for splitting domain Documents into retrievable DocumentChunks."""

    @abstractmethod
    def split(self, document: Document) -> list[DocumentChunk]:
        """Split a document into smaller, retrievable chunks."""
        raise NotImplementedError
