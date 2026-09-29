from abc import ABC, abstractmethod

from app.domain.model.evidence import Evidence


class Retriever(ABC):
    """Contract for retrieving relevant evidence for a user query."""

    @abstractmethod
    def retrieve(self, query: str, top_k: int = 5) -> list[Evidence]:
        """Retrieve relevant evidence for the supplied query."""
        raise NotImplementedError
