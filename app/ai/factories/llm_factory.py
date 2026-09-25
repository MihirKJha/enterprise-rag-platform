"""
AI provider factory.

Creates the configured language-model provider without exposing
provider-specific implementation details to the application layer.
"""

import logging

from app.adapters.providers.llm.local_provider import LocalLLMProvider
from app.adapters.providers.llm.watsonx_provider import WatsonxLLMProvider
from app.config import AI_PROVIDER
from app.ports.outbound.llm_provider import LLMProvider

logger = logging.getLogger(__name__)


def create_llm_provider() -> LLMProvider:
    """
    Create the configured LLM provider.

    Returns:
        Configured LLM provider instance.

    Raises:
        RuntimeError: If the configured provider is unsupported.
    """
    if AI_PROVIDER == "local":
        logger.info("Using Local LLM provider")
        return LocalLLMProvider()

    if AI_PROVIDER == "watsonx":
        logger.info("Using Watsonx LLM provider")
        return WatsonxLLMProvider()

    raise RuntimeError(f"Unsupported AI provider: '{AI_PROVIDER}'.")
