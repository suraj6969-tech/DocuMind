from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from backend.config import settings


class EmbeddingGenerator:
    """
    Generates embeddings for LangChain Documents.
    """

    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model=settings.EMBEDDING_MODEL,
            api_key=settings.OPENAI_API_KEY,
        )

    def embed_documents(
        self,
        documents: list[Document],
    ) -> list[list[float]]:
        """
        Generate embeddings for every document chunk.
        """

        texts = [
            document.page_content
            for document in documents
        ]

        return self.embeddings.embed_documents(texts)