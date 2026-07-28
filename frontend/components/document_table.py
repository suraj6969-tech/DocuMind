from datetime import datetime

import streamlit as st

from components.delete_dialog import show_delete_dialog
from services.api_client import api_client


def render_document_table() -> None:
    """
    Display all uploaded documents with delete functionality.
    """

    st.subheader("📂 Uploaded Documents")

    try:
        response = api_client.get_documents()

        documents = response["documents"]

        if not documents:
            st.info("No documents have been uploaded yet.")
            return

        for document in documents:
            col1, col2, col3, col4 = st.columns([4, 2, 3, 1])

            with col1:
                st.write(f"**{document['original_filename']}**")

            with col2:
                st.write(f"{document['file_size'] / 1024:.2f} KB")

            with col3:
                uploaded_at = datetime.fromisoformat(
                    document["uploaded_at"]
                )

                st.write(
                    uploaded_at.strftime("%d-%m-%Y %H:%M")
                )

            with col4:
                if st.button(
                    "🗑️",
                    key=f"delete_{document['document_id']}",
                    help="Delete document",
                ):
                    show_delete_dialog(
                        document_id=document["document_id"],
                        filename=document["original_filename"],
                    )

            st.divider()

    except Exception as e:
        st.error("Unable to load documents.")
        st.exception(e)