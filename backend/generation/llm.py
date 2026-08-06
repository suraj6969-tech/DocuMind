from openai import OpenAI

from backend.config import settings
from backend.core.exceptions import LLMException


class LLM:
    """
    Wrapper around the OpenAI Chat Completions API.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

        self.model = settings.LLM_MODEL

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate an answer from the LLM.
        """

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=0,
            )

            return response.choices[0].message.content.strip()

        except Exception as exc:
            raise LLMException() from exc