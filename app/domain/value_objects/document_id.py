from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentId:
    """Value object representing the stable identity of a domain document."""

    value: str
