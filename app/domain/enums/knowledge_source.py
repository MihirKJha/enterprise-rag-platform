from enum import Enum


class KnowledgeSource(str, Enum):
    """Defines the source of the knowledge used in the RAG system."""

    YOUTUBE = "youtube"
