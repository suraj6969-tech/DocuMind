from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """
    Response model for the health check endpoint.
    """

    success: bool = Field(
        ...,
        description="Indicates whether the API is healthy."
    )

    message: str = Field(
        ...,
        description="Human-readable health status."
    )

    app_name: str = Field(
        ...,
        description="Application name."
    )

    version: str = Field(
        ...,
        description="Current application version."
    )