from langchain_core.documents import Document

from backend.retrieval.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most relevant document chunks from the vector store.
    """

    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(
        self,
        query: str,
    ) -> list[Document]:
        """
        Retrieve the top matching document chunks for the given query.
        """

        results = self.vector_store.search_with_scores(query)

        return [
            document
            for document, _ in results
        ]