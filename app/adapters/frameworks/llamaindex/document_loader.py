from pathlib import Path

from app.domain.value_objects.document_id import DocumentId
from llama_index.core import SimpleDirectoryReader

from app.domain.model.document import Document
from app.ports.outbound.document_loader import DocumentLoader


class LlamaIndexDocumentLoader(DocumentLoader):
    """Loads documents through LlamaIndex and converts them into domain Documents."""

    def load(self, source: str) -> list[Document]:
        """Load documents from the supplied source using LlamaIndex."""

        path = Path(source)

        reader = SimpleDirectoryReader(
            input_dir=str(path),
            recursive=True,
        )

        framework_documents = reader.load_data()

        return [
            Document(
                id=DocumentId(str(index)),
                content=document.text,
                metadata=document.metadata,
            )
            for index, document in enumerate(framework_documents)
        ]
