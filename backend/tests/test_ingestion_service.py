from pathlib import Path

from backend.services.ingestion_service import IngestionService


def main():
    ingestion_service = IngestionService()

    document_path = (
        Path("backend")
        / "uploads"
        / "79a9aeb4-1ef3-42d6-9ff1-1bacc4601787.txt"
    )

    print("Starting ingestion...")

    ingestion_service.ingest(
    file_path=document_path,
    document_id="test-document-id",
    original_filename="Nvidia.txt",
    stored_filename="79a9aeb4-1ef3-42d6-9ff1-1bacc4601787.txt",
)

    print("Document indexed successfully!")


if __name__ == "__main__":
    main()