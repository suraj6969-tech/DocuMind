from backend.generation.llm import LLM
from backend.generation.prompt_builder import PromptBuilder
from backend.retrieval.retriever import Retriever
from backend.services.rag_service import RAGService


def get_retriever() -> Retriever:
    """
    Dependency provider for the Retriever.
    """
    return Retriever()


def get_prompt_builder() -> PromptBuilder:
    """
    Dependency provider for the Prompt Builder.
    """
    return PromptBuilder()


def get_llm() -> LLM:
    """
    Dependency provider for the Language Model.
    """
    return LLM()


def get_rag_service() -> RAGService:
    """
    Dependency provider for the RAG service.
    """

    return RAGService(
        retriever=get_retriever(),
        prompt_builder=get_prompt_builder(),
        llm=get_llm(),
    )