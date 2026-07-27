from fastapi import FastAPI

from backend.api.router import api_router
from backend.config import settings
from backend.db import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    debug=settings.DEBUG,
)

# =====================================================
# API Routes
# =====================================================

app.include_router(
    api_router,
    prefix=settings.API_PREFIX,
)


# =====================================================
# Root Endpoint
# =====================================================

@app.get(
    "/",
    tags=["Root"],
    summary="Root Endpoint",
)
async def root():
    """
    Root endpoint of the application.
    """

    return {
        "success": True,
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs",
    }