from pathlib import Path

from backend.embeddings.embedding_generator import EmbeddingGenerator
from backend.ingestion.loaders import DocumentLoader
from backend.ingestion.splitter import DocumentSplitter

def main():
    loader = DocumentLoader()

    splitter = DocumentSplitter()

    embedder = EmbeddingGenerator()

    document_path = (
        Path("backend")
        / "uploads"
        / "79a9aeb4-1ef3-42d6-9ff1-1bacc4601787.txt"
    )

    documents = loader.load_document(document_path)

    chunks = splitter.split_documents(documents)

    vectors = embedder.embed_documents(chunks)

    print("=" * 60)
    print("Embedding Test")
    print("=" * 60)

    print(f"Original Documents : {len(documents)}")
    print(f"Chunks Created     : {len(chunks)}")
    print(f"Vectors Created    : {len(vectors)}")

    print()

    print(f"Embedding Dimension : {len(vectors[0])}")

    print()

    print("First 10 Values:")
    print(vectors[0][:10])


if __name__ == "__main__":
    main()