import streamlit as st
from pathlib import Path

# ------------------------------
# Dummy Users
# ------------------------------

USERS = {
    "judge1": {
        "password": "Yatra@123",
        "name": "Hackathon Judge"
    },
    "demo": {
        "password": "Demo@123",
        "name": "Demo User"
    },
    "admin": {
        "password": "Admin@123",
        "name": "Administrator"
    }
}


# ------------------------------
# Login
# ------------------------------

def login():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    left, right = st.columns([2, 3], gap="large")

    # ==========================================
    # LEFT PANEL
    # ==========================================

    with left:

        st.markdown("<div style='margin-top:60px'></div>", unsafe_allow_html=True)

        st.title("🏛️ YatraSetu AI")

        st.subheader("AI Powered Cultural Travel Companion")

        st.write(
            "Discover India's hidden treasures with the power of **Google Gemini AI**."
        )

        st.divider()

        username = st.text_input(
            "Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        login_clicked = st.button(
            "🚀 Login",
            use_container_width=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.info(
            """
### Demo Credentials

**Username:** `judge1`

**Password:** `Yatra@123`
"""
        )

    # ==========================================
    # RIGHT PANEL
    # ==========================================

    with right:

        st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)

        logo_path = Path(__file__).parent / "assets" / "logo.png"

        if logo_path.exists():

            _, center, _ = st.columns([1, 2, 1])

            with center:
                st.image(str(logo_path), width=420)

        st.markdown(
            """
<div style="text-align:center;">

<h1 style="margin-bottom:8px;">
Experience India Beyond Tourism
</h1>

<h3 style="color:#475569;">
AI Powered Cultural Travel Companion
</h3>

</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        features = [
            "🗺️ Personalized AI Itineraries",
            "🏛️ Heritage Storytelling",
            "💎 Hidden Gems Discovery",
            "🍲 Authentic Local Cuisine",
            "🎉 Cultural Events",
            "🤖 Powered by Google Gemini"
        ]

        for feature in features:

            st.markdown(
                f"""
<div style="
background:#F8FAFC;
padding:14px;
margin-bottom:10px;
border-radius:12px;
border-left:5px solid #2563EB;
font-size:17px;
">

{feature}

</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.info(
            """
### 🌍 Why YatraSetu?

• Discover unexplored destinations

• Experience authentic Indian culture

• AI-generated heritage storytelling

• Explore authentic cuisine & festivals

• Promote responsible tourism
"""
        )

    # ==========================================
    # LOGIN VALIDATION
    # ==========================================

    if login_clicked:

        username = username.strip()

        if username == "" or password == "":
            st.warning("Please enter username and password.")
            return False

        if (
            username in USERS
            and USERS[username]["password"] == password
        ):

            st.session_state.authenticated = True
            st.session_state.user = USERS[username]["name"]

            st.toast("Welcome to YatraSetu AI! 🎉")

            st.rerun()

        else:

            st.error("❌ Invalid username or password.")

    return False


# ------------------------------
# Logout
# ------------------------------

def logout():

    if st.sidebar.button("🚪 Logout"):

        st.session_state.clear()

        st.rerun()