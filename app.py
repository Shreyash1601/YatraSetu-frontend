import streamlit as st
from auth import login, logout


from api import (
    get_itinerary,
    get_hidden_gems,
    get_story,
    get_food,
    get_events,
    get_culture,
    get_summary
)

from styles import load_css

from components.hero import hero
from components.itinerary import render as itinerary_render
from components.hidden_gems import render as hidden_render
from components.story import render as story_render
from components.food import render as food_render
from components.events import render as events_render
from components.culture import render as culture_render


st.set_page_config(
    page_title="YatraSetu AI",
    page_icon="🏛️",
    layout="wide",
)

load_css()
if not login():
    st.stop()


hero()

# ---------------- Sidebar ----------------

st.sidebar.title("⚙️ Trip Planner")

st.sidebar.success(
    f"Welcome {st.session_state.user}"
)

logout()

destination = st.sidebar.text_input(
    "Destination",
    placeholder="Jaipur"
)

days = st.sidebar.slider(
    "Trip Duration",
    1,
    10,
    2
)

budget = st.sidebar.number_input(
    "Budget (₹)",
    value=5000
)

interests = st.sidebar.multiselect(
    "Interests",
    [
        "History",
        "Food",
        "Culture",
        "Adventure",
        "Photography",
        "Shopping",
        "Nature",
        "Wildlife",
    ],
    default=[
        "History",
        "Food",
    ],
)

story_place = st.sidebar.text_input(
    "Story Place",
    value=""
)

story_style = st.sidebar.selectbox(
    "Story Style",
    [
        "historian",
        "mythology",
        "child",
        "documentary",
    ],
)
summary = get_summary(
    {
        "destination": destination,
        "days": days,
        "budget": budget,
        "interests": interests
    }
)

generate = st.sidebar.button(
    "✨ Generate Journey",
    use_container_width=True,
)

# ---------------- Session State ----------------

if "results" not in st.session_state:
    st.session_state.results = None

# ---------------- API Calls ----------------

if generate:

    if destination == "":
        st.warning("Please enter a destination.")
        st.stop()

    with st.spinner("Building your AI journey..."):

        itinerary = get_itinerary(
            {
                "destination": destination,
                "days": days,
                "budget": budget,
                "interests": interests,
            }
        )

        hidden = get_hidden_gems(destination)

        food = get_food(destination)

        events = get_events(destination)

        culture = get_culture(destination)

        story = get_story(
            story_place if story_place else destination,
            story_style,
        )

        st.session_state.results = {
            "summary": summary,
            "itinerary": itinerary,
            "hidden": hidden,
            "food": food,
            "events": events,
            "culture": culture,
            "story": story,
        }

# ---------------- Results ----------------

if st.session_state.results:

    st.success("Journey Generated Successfully!")

    st.image(
        f"https://picsum.photos/1400/450?{destination}",
        use_container_width=True,
    )

    with st.container(border=True):

        st.markdown("## 🌍 AI Travel Summary")

        st.write(
            st.session_state.results["summary"]["summary"]
        )

        st.markdown(f"""
### 🌍 AI Travel Summary

> {st.session_state.results["summary"]["summary"]}
""")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "🗺️ Itinerary",
            "💎 Hidden Gems",
            "📖 Story",
            "🍲 Food",
            "🎉 Events",
            "🏛️ Culture",
        ]
    )

    with tab1:
        itinerary_render(
            st.session_state.results["itinerary"]
        )

    with tab2:
        hidden_render(
            st.session_state.results["hidden"]
        )

    with tab3:
        story_render(
            st.session_state.results["story"]
        )

    with tab4:
        food_render(
            st.session_state.results["food"]
        )

    with tab5:
        events_render(
            st.session_state.results["events"]
        )

    with tab6:
        culture_render(
            st.session_state.results["culture"]
        )

else:

    st.info(
        "👈 Fill in the trip details from the sidebar and click **Generate Journey**."
    )