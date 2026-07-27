import streamlit as st

from services.api_client import api_client


def render_sidebar() -> None:
    """
    Render the application sidebar.
    """

    with st.sidebar:
        st.header("⚙️ Dashboard")

        st.markdown("---")

        st.subheader("Backend Status")

        try:
            health = api_client.health_check()

            st.success("Connected")

            st.write(f"**Application:** {health['app_name']}")
            st.write(f"**Version:** {health['version']}")

        except Exception:
            st.error("Backend Offline")

        st.markdown("---")

        st.subheader("Project")

        st.write("📚 DocuMind AI")
        st.write("FastAPI + Streamlit")
        st.write("RAG Document Intelligence")

        st.markdown("---")

        st.info(
            "More options such as document management, chat history, and "
            "evaluation will appear here in later milestones."
        )