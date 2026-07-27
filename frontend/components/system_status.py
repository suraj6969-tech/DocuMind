import streamlit as st

from services.api_client import api_client


def render_system_status() -> None:
    """
    Render backend status information.
    """

    st.subheader("📊 System Status")

    try:
        health = api_client.health_check()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label="Backend",
                value="Online",
            )

        with col2:
            st.metric(
                label="Application",
                value=health["app_name"],
            )

        with col3:
            st.metric(
                label="Version",
                value=health["version"],
            )

        st.success(
            "Frontend and backend are connected successfully."
        )

    except Exception as e:
        st.error("Unable to connect to the FastAPI backend.")
        st.exception(e)