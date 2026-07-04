import streamlit as st


def render(data):

    st.header("💎 Hidden Gems")

    cols = st.columns(2)

    for i, gem in enumerate(data):

        with cols[i % 2]:

            st.container(border=True)

            st.image(
                f"https://picsum.photos/600/350?random={i}"
            )

            st.subheader(gem["name"])

            st.write(gem["why_visit"])