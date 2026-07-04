import streamlit as st


def render(data):

    st.header("🎉 Events")

    for event in data:

        with st.expander(event["event"]):

            st.write(event["description"])