from pathlib import Path


class PromptBuilder:
    """
    Builds prompts for the LLM using external prompt templates.
    """

    def __init__(self):
        prompt_path = (
            Path(__file__).resolve().parent.parent
            / "prompts"
            / "qa_prompt.txt"
        )

        self.template = prompt_path.read_text(encoding="utf-8")

    def build_prompt(
        self,
        context: str,
        question: str,
    ) -> str:
        """
        Build the final prompt for the LLM.
        """

        prompt = self.template.replace(
            "{context}",
            context,
        )

        prompt = prompt.replace(
            "{question}",
            question,
        )

        return prompt