import streamlit as st


def render(data):

    st.header("📖 Story Mode")

    st.markdown(data["story"])