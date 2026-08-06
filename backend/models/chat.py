from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Request model for asking a question.
    """

    question: str = Field(
        ...,
        min_length=1,
        description="Question asked by the user.",
        examples=["Who founded Nvidia?"],
    )


class SourceInfo(BaseModel):
    """
    Represents one source document used to answer.
    """

    document_id: str

    filename: str

    chunks: list[int]


class ChatResponse(BaseModel):
    """
    Response returned by the RAG system.
    """

    answer: str

    sources: list[SourceInfo]