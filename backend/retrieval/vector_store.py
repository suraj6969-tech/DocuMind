from langchain_chroma import Chroma
from langchain_core.documents import Document

from backend.config import settings
from backend.embeddings.embedding_generator import EmbeddingGenerator


class VectorStore:
    """
    Handles all interactions with the Chroma vector database.
    """

    def __init__(self):
        self.embedding_generator = EmbeddingGenerator()

        self.vector_store = Chroma(
            collection_name="documind",
            embedding_function=self.embedding_generator.embeddings,
            persist_directory=str(settings.CHROMA_DIRECTORY),
        )

    def add_documents(
        self,
        documents: list[Document],
    ) -> None:
        """
        Add document chunks to ChromaDB.
        """
        self.vector_store.add_documents(documents)

    def search_with_scores(
        self,
        query: str,
    ) -> list[tuple[Document, float]]:
        """
        Retrieve document chunks together with their relevance scores.
        """
        return self.vector_store.similarity_search_with_relevance_scores(
            query=query,
            k=settings.DEFAULT_TOP_K,
        )

    def delete_document(
        self,
        document_id: str,
    ) -> None:
        """
        Delete every chunk belonging to one document.
        """

        self.vector_store.delete(
            where={
                "document_id": document_id,
            }
        )

    def delete_collection(
        self,
    ) -> None:
        """
        Delete the entire Chroma collection.
        """
        self.vector_store.delete_collection()