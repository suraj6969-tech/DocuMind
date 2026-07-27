import requests


class APIClient:
    """
    Handles communication with the FastAPI backend.
    """

    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url.rstrip("/")

    def health_check(self) -> dict:
        """
        Check whether the backend API is running.
        """

        response = requests.get(
            f"{self.base_url}/api/v1/health",
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    def upload_document(self, uploaded_file) -> dict:
        """
        Upload a document to the backend.
        """

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type,
            )
        }

        response = requests.post(
            f"{self.base_url}/api/v1/documents/upload",
            files=files,
            timeout=60,
        )

        response.raise_for_status()

        return response.json()


api_client = APIClient()