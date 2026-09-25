"""
Embedding provider factory.

Creates the configured embedding provider without exposing
provider-specific implementation details to the application layer.
"""

import logging

from app.adapters.providers.embeddings.local_embedding import LocalEmbeddingProvider
from app.adapters.providers.embeddings.watsonx_embedding import WatsonxEmbeddingProvider
from app.config import EMBEDDING_PROVIDER
from app.ports.outbound.embedding_provider import EmbeddingProvider

logger = logging.getLogger(__name__)


def create_embedding_provider() -> EmbeddingProvider:
    """
    Create the configured embedding provider.

    Returns:
        Configured embedding provider instance.

    Raises:
        RuntimeError: If the configured provider is unsupported.
    """
    if EMBEDDING_PROVIDER == "local":
        logger.info("Using Local Embedding provider")
        return LocalEmbeddingProvider()

    if EMBEDDING_PROVIDER == "watsonx":
        logger.info("Using Watsonx Embedding provider")
        return WatsonxEmbeddingProvider()

    raise RuntimeError(f"Unsupported embedding provider: '{EMBEDDING_PROVIDER}'.")
