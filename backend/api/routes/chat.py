from fastapi import APIRouter, Depends

from backend.core.dependencies import get_rag_service
from backend.core.exceptions import RAGException
from backend.core.logging import logger
from backend.models import ChatRequest, ChatResponse
from backend.services.rag_service import RAGService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
    summary="Ask a question about uploaded documents",
)
def chat(
    request: ChatRequest,
    rag_service: RAGService = Depends(get_rag_service),
) -> ChatResponse:
    """
    Answer a user's question using Retrieval-Augmented Generation (RAG).
    """

    logger.info("Received chat request.")

    try:
        response = rag_service.ask(request.question)

        logger.info("Chat request completed successfully.")

        return response

    except RAGException as exc:
        logger.error(f"RAG error: {exc.detail}")
        raise

    except Exception:
        logger.exception("Unexpected error while processing chat request.")

        raise RAGException(
            detail="An unexpected error occurred while processing your request."
        )