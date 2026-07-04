import streamlit as st
from image_service import get_wikipedia_image


def render(data):

    st.header("🍲 Local Cuisine")

    cols = st.columns(2)

    for i, food in enumerate(data):

        with cols[i % 2]:

            with st.container(border=True):

                image = get_wikipedia_image(food["dish"])

                if image:
                    st.image(
                        image,
                        use_container_width=True
                    )

                st.subheader(food["dish"])

                st.write(food["description"])