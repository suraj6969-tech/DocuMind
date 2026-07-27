from datetime import datetime

from pydantic import BaseModel, Field


class DocumentUploadResponse(BaseModel):
    """
    Response returned after a document is uploaded successfully.
    """

    success: bool = Field(..., description="Upload status")
    message: str = Field(..., description="Upload message")
    document_id: str = Field(..., description="Unique document identifier")
    original_filename: str = Field(..., description="Original uploaded filename")
    stored_filename: str = Field(..., description="Filename stored on disk")


class DocumentInfo(BaseModel):
    """
    Metadata for an uploaded document.
    """

    document_id: str
    original_filename: str
    stored_filename: str
    file_size: int
    uploaded_at: datetime


class DocumentListResponse(BaseModel):
    """
    Response containing all uploaded documents.
    """

    success: bool
    documents: list[DocumentInfo]