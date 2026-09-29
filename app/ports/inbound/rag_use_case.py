from abc import ABC, abstractmethod

from app.domain.model.rag_request import RAGRequest
from app.domain.model.rag_response import RAGResponse


class RAGUseCase(ABC):
    """Inbound application contract for executing a RAG use case."""

    @abstractmethod
    def execute(self, request: RAGRequest) -> RAGResponse:
        """Execute the RAG use case for the supplied request."""
        raise NotImplementedError
