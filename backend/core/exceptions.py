from fastapi import HTTPException, status


class RAGException(HTTPException):
    """
    Base exception for RAG-related errors.
    """

    def __init__(
        self,
        detail: str = "Unable to generate an answer.",
    ):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class RetrievalException(RAGException):
    """
    Raised when document retrieval fails.
    """

    def __init__(self):
        super().__init__(
            detail="Unable to retrieve relevant documents.",
        )


class LLMException(RAGException):
    """
    Raised when the language model fails.
    """

    def __init__(self):
        super().__init__(
            detail="Unable to generate an answer. Please try again later.",
        )