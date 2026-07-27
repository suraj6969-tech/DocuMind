from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.db.base import Base


class Document(Base):
    """
    Database model representing an uploaded document.
    """

    __tablename__ = "documents"

    document_id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    original_filename: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    stored_filename: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    file_size: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )