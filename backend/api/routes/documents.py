from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models import DocumentUploadResponse
from backend.repository import DocumentRepository

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

UPLOAD_DIRECTORY = Path("backend/uploads")
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)

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
    Upload a document and save its metadata.
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

    file_path = UPLOAD_DIRECTORY / stored_filename

    with open(file_path, "wb") as f:
        f.write(content)

    repository = DocumentRepository(db)

    repository.create_document(
        document_id=document_id,
        original_filename=file.filename,
        stored_filename=stored_filename,
        file_size=len(content),
    )

    return DocumentUploadResponse(
        success=True,
        message="Document uploaded successfully.",
        document_id=document_id,
        original_filename=file.filename,
        stored_filename=stored_filename,
    )