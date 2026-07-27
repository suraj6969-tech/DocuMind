import streamlit as st


def render_header() -> None:
    """
    Render the main application header.
    """

    st.set_page_config(
        page_title="DocuMind AI",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("📚 DocuMind AI")

    st.caption(
        "Enterprise Document Intelligence Platform powered by FastAPI and Streamlit."
    )

    st.divider()