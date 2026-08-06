from pathlib import Path

from backend.ingestion.loaders import DocumentLoader
from backend.ingestion.splitter import DocumentSplitter
from backend.retrieval.vector_store import VectorStore


class IngestionService:
    """
    Orchestrates the complete document ingestion pipeline.
    """

    def __init__(self):
        self.loader = DocumentLoader()
        self.splitter = DocumentSplitter()
        self.vector_store = VectorStore()

    def ingest(
        self,
        file_path: Path,
        document_id: str,
        original_filename: str,
        stored_filename: str,
    ) -> None:
        """
        Load, split, enrich metadata, and index a document.
        """

        # Load document
        documents = self.loader.load_document(file_path)

        # Split into chunks
        chunks = self.splitter.split_documents(documents)

        # Enrich metadata
        for index, chunk in enumerate(chunks):
            chunk.metadata["document_id"] = document_id
            chunk.metadata["original_filename"] = original_filename
            chunk.metadata["stored_filename"] = stored_filename
            chunk.metadata["chunk_index"] = index
            chunk.metadata["chunk_id"] = f"{document_id}_{index}"

                # Store in ChromaDB
        self.vector_store.add_documents(chunks)