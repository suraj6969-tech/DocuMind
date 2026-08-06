from backend.retrieval.retriever import Retriever


def main():
    retriever = Retriever()

    query = "Who founded Nvidia?"

    documents = retriever.retrieve(query)

    print("=" * 70)
    print(f"Query: {query}")
    print("=" * 70)

    print(f"\nRelevant Documents Found: {len(documents)}\n")

    if not documents:
        print("No documents satisfied the score threshold.")
        return

    for index, document in enumerate(documents, start=1):
        print(f"Result {index}")
        print("-" * 70)
        print(document.page_content[:500])
        print()


if __name__ == "__main__":
    main()