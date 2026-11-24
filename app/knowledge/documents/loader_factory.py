from app.adapters.frameworks.langchain.document_loader import LangChainDocumentLoader
from app.adapters.frameworks.llamaindex.document_loader import LlamaIndexDocumentLoader
from app.config import RAG_FRAMEWORK
from app.ports.outbound.document_loader import DocumentLoader


class DocumentLoaderFactory:
    """Creates the document loader adapter selected by the configured RAG framework."""

    @staticmethod
    def create() -> DocumentLoader:
        """Create the configured framework-specific document loader."""

        framework = RAG_FRAMEWORK.lower()

        if framework == "langchain":
            return LangChainDocumentLoader()

        if framework == "llamaindex":
            return LlamaIndexDocumentLoader()

        raise ValueError(f"Unsupported RAG framework: {framework}")
