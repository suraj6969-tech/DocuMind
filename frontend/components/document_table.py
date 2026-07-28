import streamlit as st

from services.api_client import api_client


def render_document_table() -> None:
    """
    Display all uploaded documents.
    """

    st.subheader("📂 Uploaded Documents")

    try:
        response = api_client.get_documents()

        documents = response["documents"]

        if not documents:
            st.info("No documents have been uploaded yet.")
            return

        table_data = []

        for document in documents:
            table_data.append(
                {
                    "Filename": document["original_filename"],
                    "Size (KB)": round(document["file_size"] / 1024, 2),
                    "Uploaded At": document["uploaded_at"],
                }
            )

        st.dataframe(
            table_data,
            use_container_width=True,
            hide_index=True,
        )

    except Exception as e:
        st.error("Unable to load documents.")
        st.exception(e)