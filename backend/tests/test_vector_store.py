from pathlib import Path

from backend.embeddings.embedding_generator import EmbeddingGenerator
from backend.ingestion.loaders import DocumentLoader
from backend.ingestion.splitter import DocumentSplitter
from backend.retrieval.vector_store import VectorStore


def main():
    loader = DocumentLoader()

    splitter = DocumentSplitter()

    vector_store = VectorStore()

    document_path = (
        Path("backend")
        / "uploads"
        / "79a9aeb4-1ef3-42d6-9ff1-1bacc4601787.txt"
    )

    documents = loader.load_document(document_path)

    chunks = splitter.split_documents(documents)

    print(f"Loaded Documents : {len(documents)}")
    print(f"Generated Chunks : {len(chunks)}")

    print()

    print("Adding documents to ChromaDB...")

    vector_store.add_documents(chunks)

    print("Done!")

    print()

    results = vector_store.similarity_search(
        "Who founded Nvidia?"
    )

    print("=" * 60)
    print("Similarity Search Result")
    print("=" * 60)

    print("=" * 70)

    for i, doc in enumerate(results, start=1):
        print(f"\nResult {i}")
        print("-" * 70)
        print(doc.page_content[:400])


if __name__ == "__main__":
    main()