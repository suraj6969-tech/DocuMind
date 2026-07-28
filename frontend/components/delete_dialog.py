import streamlit as st

from services.api_client import api_client


@st.dialog("🗑️ Delete Document")
def show_delete_dialog(
    document_id: str,
    filename: str,
) -> None:
    """
    Display a confirmation dialog before deleting a document.
    """

    st.warning(
        f"Are you sure you want to delete **{filename}**?"
    )

    st.write(
        "This action cannot be undone."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Cancel",
            use_container_width=True,
        ):
            st.rerun()

    with col2:
        if st.button(
            "Delete",
            type="primary",
            use_container_width=True,
        ):
            try:
                api_client.delete_document(document_id)

                st.success(
                    f"{filename} deleted successfully."
                )

                st.rerun()

            except Exception as e:
                st.error("Unable to delete document.")
                st.exception(e)