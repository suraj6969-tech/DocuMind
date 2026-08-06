from backend.services.rag_service import RAGService


def main():
    rag = RAGService()

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