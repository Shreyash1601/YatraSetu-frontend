import streamlit as st


def hero():

    st.markdown(
        """
<div class="hero">

<h1>🏛️ YatraSetu AI</h1>

<h4>
Discover India's Hidden Stories with AI
</h4>

<p>
Generate personalized itineraries, hidden gems,
cultural experiences and immersive stories.
</p>

</div>
""",
        unsafe_allow_html=True,
    )