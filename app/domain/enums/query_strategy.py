from enum import Enum


class QueryStrategy(str, Enum):
    """Defines the strategy for querying the knowledge base."""

    ORIGINAL = "original"
    REWRITE = "rewrite"
    MULTI_QUERY = "multi_query"
