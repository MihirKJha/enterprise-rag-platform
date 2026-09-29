from abc import ABC, abstractmethod

from app.domain.model.document import Document


class DocumentLoader(ABC):
    """Contract for loading external knowledge sources into domain Documents."""

    @abstractmethod
    def load(self, source: str) -> list[Document]:
        """Load a source and convert it into domain Documents."""
        raise NotImplementedError
