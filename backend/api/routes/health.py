from fastapi import APIRouter

from backend.config import settings
from backend.models.health import HealthResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    response_model=HealthResponse,
    summary="Health Check",
    description="Returns the current health status of the DocuMind API.",
)
async def health_check() -> HealthResponse:
    """
    Health check endpoint.

    This endpoint is used to verify that the backend
    is running correctly.
    """

    return HealthResponse(
        success=True,
        message="DocuMind API is running successfully.",
        app_name=settings.APP_NAME,
        version=settings.APP_VERSION,
    )