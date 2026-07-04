import streamlit as st


def load_css():
    st.markdown("""
    <style>

    .stApp{
        background:#F8FAFC;
    }

    .hero{
        background:linear-gradient(135deg,#0F172A,#1E3A8A);
        padding:35px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    }

    .stButton>button{
        width:100%;
        height:50px;
        border-radius:12px;
        background:#2563EB;
        color:white;
        font-weight:bold;
    }

    </style>
    """, unsafe_allow_html=True)