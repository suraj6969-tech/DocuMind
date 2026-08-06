from pathlib import Path
from uuid import uuid4

from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    Response,
    UploadFile,
)
from sqlalchemy.orm import Session
from backend.retrieval.vector_store import VectorStore

from backend.config import settings
from backend.db.database import get_db
from backend.models import (
    DocumentInfo,
    DocumentListResponse,
    DocumentUploadResponse,
)
from backend.repository import DocumentRepository
from backend.services.ingestion_service import IngestionService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

settings.UPLOAD_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".docx",
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    summary="Upload a document",
)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Upload a document, save metadata,
    and automatically index it into ChromaDB.
    """

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type.",
        )

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 10 MB.",
        )

    document_id = str(uuid4())

    stored_filename = f"{document_id}{extension}"

    file_path = settings.UPLOAD_DIRECTORY / stored_filename

    with open(file_path, "wb") as f:
        f.write(content)

    repository = DocumentRepository(db)

    repository.create_document(
        document_id=document_id,
        original_filename=file.filename,
        stored_filename=stored_filename,
        file_size=len(content),
    )

    ingestion_service = IngestionService()

    try:
        ingestion_service.ingest(
            file_path=file_path,
            document_id=document_id,
            original_filename=file.filename,
            stored_filename=stored_filename,
        )

    except Exception as exc:

        if file_path.exists():
            file_path.unlink()

        document = repository.get_document_by_id(document_id)

        if document:
            repository.delete_document(document)

        raise HTTPException(
            status_code=500,
            detail=f"Document indexing failed: {str(exc)}",
        )

    return DocumentUploadResponse(
        success=True,
        message="Document uploaded and indexed successfully.",
        document_id=document_id,
        original_filename=file.filename,
        stored_filename=stored_filename,
    )


@router.get(
    "",
    response_model=DocumentListResponse,
    summary="Get all uploaded documents",
)
def get_documents(
    db: Session = Depends(get_db),
):
    """
    Return all uploaded documents.
    """

    repository = DocumentRepository(db)

    documents = repository.get_all_documents()

    return DocumentListResponse(
        success=True,
        documents=[
            DocumentInfo(
                document_id=document.document_id,
                original_filename=document.original_filename,
                stored_filename=document.stored_filename,
                file_size=document.file_size,
                uploaded_at=document.uploaded_at,
            )
            for document in documents
        ],
    )


@router.delete(
    "/{document_id}",
    status_code=204,
    summary="Delete a document",
)
def delete_document(
    document_id: str,
    db: Session = Depends(get_db),
):
    """
    Delete a document and its metadata.
    """

    repository = DocumentRepository(db)

    document = repository.get_document_by_id(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found.",
        )

    file_path = settings.UPLOAD_DIRECTORY / document.stored_filename

    if file_path.exists():
        file_path.unlink()

    vector_store = VectorStore()

    vector_store.delete_document(document.document_id)

    repository.delete_document(document)

    return Response(status_code=204)