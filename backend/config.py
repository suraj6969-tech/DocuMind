from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """
    Central application configuration.

    Every configuration value used anywhere in the backend
    should be defined here and loaded from the .env file.
    """

    # ==========================
    # Application
    # ==========================
    APP_NAME: str = "DocuMind AI"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "Enterprise Document Intelligence Platform powered by FastAPI."
    )
    DEBUG: bool = True

    # ==========================
    # API
    # ==========================
    API_PREFIX: str = "/api/v1"

    # ==========================
    # OpenAI
    # ==========================
    OPENAI_API_KEY: str = ""

    # ==========================
    # Cohere
    # ==========================
    COHERE_API_KEY: str = ""

    # ==========================
    # Models
    # ==========================
    LLM_MODEL: str = "gpt-4o"
    EMBEDDING_MODEL: str = "text-embedding-3-small"

    # ==========================
    # Storage
    # ==========================
    UPLOAD_DIRECTORY: Path = BASE_DIR / "uploads"
    CHROMA_DIRECTORY: Path = BASE_DIR / "vector_store"

    # ==========================
    # Retrieval
    # ==========================
    DEFAULT_TOP_K: int = 5

    SCORE_THRESHOLD: float = 0.55

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.

    Using lru_cache ensures the configuration
    is loaded only once during application startup.
    """
    return Settings()


settings = get_settings()