import streamlit as st

from components.header import render_header
from components.sidebar import render_sidebar
from components.system_status import render_system_status
from components.upload import render_upload
from components.document_table import render_document_table
from components.chat import render_chat


def main() -> None:
    """
    Main Streamlit application.
    """

    # Configure page and render header
    render_header()

    # Sidebar
    render_sidebar()

    # Dashboard
    st.subheader("🏠 Dashboard")

    st.write(
        "Welcome to **DocuMind AI**, an enterprise-grade document intelligence "
        "platform built with FastAPI and Streamlit."
    )

    st.markdown("---")

    # Backend Status
    render_system_status()

    st.markdown("---")

    # Upload Section
    render_upload()

    st.markdown("---")

    render_document_table()

    st.markdown("---")

    render_chat()
    

if __name__ == "__main__":
    main()