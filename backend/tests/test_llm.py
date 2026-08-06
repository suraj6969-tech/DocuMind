from backend.generation.llm import LLM


def main():
    llm = LLM()

    answer = llm.generate(
        """
What is the capital of France?
Answer in one sentence.
"""
    )

    print(answer)


if __name__ == "__main__":
    main()