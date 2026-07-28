from pathlib import Path

from langchain_community.document_loaders import (
    Docx2txtLoader,
    PyPDFLoader,
    TextLoader,
)
from langchain_core.documents import Document


class DocumentLoader:
    """
    Loads supported documents from disk.
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".txt",
        ".docx",
    }

    def load_document(
        self,
        file_path: str | Path,
    ) -> list[Document]:
        """
        Load a document using the appropriate LangChain loader.
        """

        file_path = Path(file_path)

        extension = file_path.suffix.lower()

        if extension == ".pdf":
            loader = PyPDFLoader(str(file_path))

        elif extension == ".txt":
            loader = TextLoader(
                str(file_path),
                encoding="utf-8",
            )

        elif extension == ".docx":
            loader = Docx2txtLoader(str(file_path))

        else:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return loader.load()