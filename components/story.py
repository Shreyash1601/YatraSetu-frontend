import streamlit as st
from image_service import get_wikipedia_image


def render(data):

    st.header("📖 AI Heritage Story")

    image = get_wikipedia_image(data["place"])

    if image:
        st.image(
            image,
            use_container_width=True
        )

    st.markdown(data["story"])