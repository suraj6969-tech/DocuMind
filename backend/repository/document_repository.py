from sqlalchemy.orm import Session

from backend.db.models import Document


class DocumentRepository:
    """
    Handles all database operations related to documents.
    """

    def __init__(self, db: Session):
        self.db = db

    def create_document(
        self,
        document_id: str,
        original_filename: str,
        stored_filename: str,
        file_size: int,
    ) -> Document:
        """
        Save document metadata to the database.
        """

        document = Document(
            document_id=document_id,
            original_filename=original_filename,
            stored_filename=stored_filename,
            file_size=file_size,
        )

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def get_all_documents(self) -> list[Document]:
        """
        Return every uploaded document.
        """

        return (
            self.db.query(Document)
            .order_by(Document.uploaded_at.desc())
            .all()
        )

    def get_document_by_id(
        self,
        document_id: str,
    ) -> Document | None:
        """
        Return a document by its ID.
        """

        return (
            self.db.query(Document)
            .filter(Document.document_id == document_id)
            .first()
        )


    def delete_document(
        self,
        document: Document,
    ) -> None:
        """
        Delete a document from the database.
        """

        self.db.delete(document)
        self.db.commit()