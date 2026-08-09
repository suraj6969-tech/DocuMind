from backend.generation.llm import LLM
from backend.generation.prompt_builder import PromptBuilder
from backend.retrieval.retriever import Retriever
from backend.services.rag_service import RAGService


def main() -> None:
    """
    Test the complete RAG service.
    """

    retriever = Retriever()
    prompt_builder = PromptBuilder()
    llm = LLM()

    rag = RAGService(
        retriever=retriever,
        prompt_builder=prompt_builder,
        llm=llm,
    )

    response = rag.ask(
        "Who founded Nvidia?"
    )

    print("\nAnswer")
    print("=" * 60)
    print(response.answer)

    print("\nSources")
    print("=" * 60)

    for source in response.sources:
        print(source)


if __name__ == "__main__":
    main()