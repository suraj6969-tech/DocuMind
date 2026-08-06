from backend.generation.llm import LLM
from backend.generation.prompt_builder import PromptBuilder
from backend.retrieval.retriever import Retriever


class RAGService:
    """
    Coordinates the complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = LLM()

    def ask(
        self,
        question: str,
    ) -> dict:
        """
        Answer a question using the uploaded documents.
        """

        documents = self.retriever.retrieve(question)

        if not documents:
            return {
                "answer": "I don't know based on the uploaded documents.",
                "sources": [],
            }

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt = self.prompt_builder.build_prompt(
            context=context,
            question=question,
        )

        answer = self.llm.generate(prompt)

        sources = []

        for document in documents:

            metadata = document.metadata

            sources.append(
                {
                    "document_id": metadata.get("document_id"),
                    "filename": metadata.get("original_filename"),
                    "chunk_index": metadata.get("chunk_index"),
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }