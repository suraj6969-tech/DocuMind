from backend.generation.prompt_builder import PromptBuilder


def main():
    builder = PromptBuilder()

    prompt = builder.build_prompt(
        context="""
Nvidia was founded in 1993 by
Jensen Huang,
Chris Malachowsky,
and Curtis Priem.
""",
        question="Who founded Nvidia?",
    )

    print(prompt)


if __name__ == "__main__":
    main()