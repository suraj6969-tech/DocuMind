from langchain_core.documents import Document

from backend.generation.llm import LLM
from backend.generation.prompt_builder import PromptBuilder
from backend.models import ChatResponse, SourceInfo
from backend.retrieval.retriever import Retriever


class RAGService:
    """
    Coordinates the complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(
        self,
        retriever: Retriever,
        prompt_builder: PromptBuilder,
        llm: LLM,
    ):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm

    def ask(
        self,
        question: str,
    ) -> ChatResponse:
        """
        Answer a question using the uploaded documents.
        """

        documents = self.retriever.retrieve(question)

        if not documents:
            return ChatResponse(
                answer="I don't know based on the uploaded documents.",
                sources=[],
            )

        context = self._build_context(documents)

        prompt = self.prompt_builder.build_prompt(
            context=context,
            question=question,
        )

        answer = self.llm.generate(prompt)

        sources = self._build_sources(documents)

        return ChatResponse(
            answer=answer,
            sources=sources,
        )

    def _build_context(
        self,
        documents: list[Document],
    ) -> str:
        """
        Combine retrieved chunks into one context string.
        """

        return "\n\n".join(
            document.page_content
            for document in documents
        )

    def _build_sources(
        self,
        documents: list[Document],
    ) -> list[SourceInfo]:
        """
        Group retrieved chunks by source document.
        """

        grouped: dict[str, dict] = {}

        for document in documents:

            metadata = document.metadata

            document_id = metadata["document_id"]

            if document_id not in grouped:
                grouped[document_id] = {
                    "filename": metadata["original_filename"],
                    "chunks": [],
                }

            grouped[document_id]["chunks"].append(
                metadata["chunk_index"]
            )

        return [
            SourceInfo(
                document_id=document_id,
                filename=data["filename"],
                chunks=sorted(data["chunks"]),
            )
            for document_id, data in grouped.items()
        ]