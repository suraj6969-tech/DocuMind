import streamlit as st

from services.api_client import api_client


def render_upload() -> None:
    """
    Render the document upload component.
    """

    st.subheader("📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "txt", "docx"],
    )

    if uploaded_file is None:
        return

    st.write(f"**Selected File:** {uploaded_file.name}")
    st.write(f"**Size:** {uploaded_file.size / 1024:.2f} KB")

    if st.button(
        "⬆️ Upload Document",
        type="primary",
    ):

        with st.spinner("Uploading document..."):

            try:
                response = api_client.upload_document(uploaded_file)

                st.success(response["message"])

                st.success(
                    f"Document ID: {response['document_id']}"
                )

                st.info(
                    f"Original File: {response['original_filename']}"
                )

                st.info(
                    f"Stored File: {response['stored_filename']}"
                )

            except Exception as e:
                st.error("Document upload failed.")
                st.exception(e)