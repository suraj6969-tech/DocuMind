import streamlit as st

from services.api_client import api_client


def render_chat() -> None:
    """
    Render the AI chat interface.
    """

    st.subheader("💬 Chat with Your Documents")

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    for message in st.session_state.chat_messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if message["role"] == "assistant" and message.get("sources"):

                with st.expander("📚 Sources"):

                    for source in message["sources"]:

                        st.markdown(
                            f"**{source['filename']}**"
                        )

                        st.caption(
                            f"Chunks: {', '.join(map(str, source['chunks']))}"
                        )

    question = st.chat_input(
        "Ask anything about your documents..."
    )

    if not question:
        return

    st.session_state.chat_messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = api_client.chat(question)

                answer = response["answer"]
                sources = response.get("sources", [])

                st.markdown(answer)

                if sources:

                    with st.expander("📚 Sources"):

                        for source in sources:

                            st.markdown(
                                f"**{source['filename']}**"
                            )

                            st.caption(
                                f"Chunks: {', '.join(map(str, source['chunks']))}"
                            )

                st.session_state.chat_messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources,
                    }
                )

            except Exception as e:

                error_message = "Unable to generate an answer."

                st.error(error_message)
                st.exception(e)

                st.session_state.chat_messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                    }
                )