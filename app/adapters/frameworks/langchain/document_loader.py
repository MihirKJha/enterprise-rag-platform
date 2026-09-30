from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader

from app.domain.model.document import Document
from app.domain.value_objects.document_id import DocumentId
from app.ports.outbound.document_loader import DocumentLoader


class LangChainDocumentLoader(DocumentLoader):
    """Loads documents through LangChain and converts them into domain Documents."""

    def load(self, source: str) -> list[Document]:
        """Load documents from the supplied source using LangChain."""

        path = Path(source)

        loader = DirectoryLoader(
            str(path),
            recursive=True,
        )

        framework_documents = loader.load()

        return [
            Document(
                id=DocumentId(str(index)),
                content=document.page_content,
                metadata=document.metadata,
            )
            for index, document in enumerate(framework_documents)
        ]
