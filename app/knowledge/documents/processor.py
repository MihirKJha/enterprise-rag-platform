import re

from app.domain.model.document import Document


class DocumentProcessor:
    """Prepares loaded documents for chunking through basic normalization and validation."""

    def process(self, document: Document) -> Document:
        """Normalize document content and validate that usable content exists."""

        content = document.content.replace("\r\n", "\n").replace("\r", "\n")
        content = re.sub(r"\n{3,}", "\n\n", content)
        content = content.strip()

        if not content:
            raise ValueError(f"Document {document.id.value} contains no usable text.")

        return Document(
            id=document.id,
            content=content,
            metadata=dict(document.metadata),
        )
