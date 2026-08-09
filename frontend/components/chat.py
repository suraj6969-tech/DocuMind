import streamlit as st

from services.api_client import api_client


def render_chat() -> None:
    """
    Render the AI chat interface.
    """

    st.subheader("💬 Chat with Your Documents")

    question = st.text_input(
        "Ask a question",
        placeholder="Example: Who founded Nvidia?",
    )

    if not question:
        return

    if st.button(
        "🚀 Ask AI",
        type="primary",
    ):

        with st.spinner("Thinking..."):

            try:

                response = api_client.chat(question)

                st.success("Answer")

                st.write(response["answer"])

                if response["sources"]:

                    st.markdown("---")
                    st.subheader("📚 Sources")

                    for source in response["sources"]:

                        st.markdown(
                            f"""
**{source['filename']}**

Chunks: {", ".join(map(str, source["chunks"]))}
"""
                        )

            except Exception as e:

                st.error("Unable to generate an answer.")

                st.exception(e)