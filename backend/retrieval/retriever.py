from langchain_core.documents import Document

from backend.config import settings
from backend.retrieval.vector_store import VectorStore


class Retriever:
    """
    Retrieves only highly relevant document chunks.
    """

    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(
    self,
    query: str,
) -> list[Document]:
        """
        Retrieve documents whose relevance score meets
        the configured threshold.
        """

        results = self.vector_store.search_with_scores(query)

        documents = []

        for document, score in results:
            if score >= settings.SCORE_THRESHOLD:
                documents.append(document)

        return documents