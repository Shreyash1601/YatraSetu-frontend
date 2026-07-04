import streamlit as st
from image_service import get_wikipedia_image


def render(data):

    st.header("💎 Hidden Gems")

    cols = st.columns(2)

    for i, gem in enumerate(data):

        with cols[i % 2]:

            with st.container(border=True):

                image = get_wikipedia_image(gem["name"])

                if image:
                    st.image(
                        image,
                        use_container_width=True
                    )

                st.subheader(gem["name"])

                st.write(gem["why_visit"])