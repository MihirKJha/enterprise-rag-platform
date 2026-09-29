from enum import Enum


class RetrievalStrategy(str, Enum):
    """Defines the retrieval strategy selected by the RAG architecture."""

    SEMANTIC = "semantic"
    SPARSE = "sparse"
    HYBRID = "hybrid"
