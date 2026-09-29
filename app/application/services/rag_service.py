from app.ports.inbound.rag_use_case import RAGUseCase
from app.domain.model.rag_request import RAGRequest
from app.domain.model.rag_response import RAGResponse


class RAGService(RAGUseCase):
    """Application service implementing the inbound RAG use-case contract."""

    def execute(self, request: RAGRequest) -> RAGResponse:
    # application orchestration
