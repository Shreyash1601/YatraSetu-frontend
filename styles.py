import streamlit as st


def load_css():

    st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{

    font-family:'Poppins',sans-serif;

}


/* =========================
BACKGROUND
========================= */

.stApp{

    background:linear-gradient(
        135deg,
        #F6F9FC,
        #EDF4FF
    );

}


/* =========================
MAIN CONTAINER
========================= */

.block-container{

    padding-top:2rem;
    padding-bottom:2rem;

}


/* =========================
HERO
========================= */

.hero{

    background:linear-gradient(
        135deg,
        #0F172A,
        #2563EB
    );

    color:white;

    padding:40px;

    border-radius:22px;

    text-align:center;

    margin-bottom:30px;

    box-shadow:0 10px 30px rgba(37,99,235,.20);

}


/* =========================
LOGIN LEFT PANEL
========================= */

[data-testid="column"]:first-child{

    background:white;

    padding:35px;

    border-radius:22px;

    box-shadow:0 12px 30px rgba(0,0,0,.08);

}


/* =========================
LOGIN RIGHT PANEL
========================= */

[data-testid="column"]:last-child{

    background:linear-gradient(
        135deg,
        #F5F9FF,
        #E4F1FF
    );

    border-radius:22px;

    padding:35px;

    box-shadow:0 12px 30px rgba(0,0,0,.08);

}


/* =========================
TEXT INPUT
========================= */

.stTextInput input{

    border-radius:12px;

    height:52px;

    border:1px solid #CBD5E1;

}


/* =========================
BUTTON
========================= */

.stButton>button{

    width:100%;

    height:55px;

    border-radius:12px;

    border:none;

    background:#2563EB;

    color:white;

    font-size:18px;

    font-weight:600;

    transition:0.3s;

}

.stButton>button:hover{

    background:#1D4ED8;

    transform:translateY(-2px);

}


/* =========================
SUCCESS BOXES
========================= */

[data-testid="stAlert"]{

    border-radius:14px;

}


/* =========================
INFO BOX
========================= */

[data-testid="stInfo"]{

    border-radius:16px;

}


/* =========================
SIDEBAR
========================= */

section[data-testid="stSidebar"]{

    background:#FFFFFF;

}


/* =========================
TABS
========================= */

button[data-baseweb="tab"]{

    font-size:16px;

    font-weight:600;

}


/* =========================
IMAGES
========================= */

img{

    border-radius:18px;

}


/* =========================
SCROLLBAR
========================= */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#2563EB;

    border-radius:20px;

}


/* =========================
HIDE STREAMLIT
========================= */

#MainMenu{

    visibility:hidden;

}

footer{

    visibility:hidden;

}

header{

    visibility:hidden;

}

</style>

""", unsafe_allow_html=True)