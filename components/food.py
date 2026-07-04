import streamlit as st


def render(data):

    st.header("🍲 Local Cuisine")

    cols = st.columns(2)

    for i, food in enumerate(data):

        with cols[i % 2]:

            st.container(border=True)

            st.image(
                f"https://picsum.photos/500/300?food={i}"
            )

            st.subheader(food["dish"])

            st.write(food["description"])