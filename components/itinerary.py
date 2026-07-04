import streamlit as st


def render(data):

    st.header("🗺️ Personalized Itinerary")

    st.subheader(data["title"])

    for day in data["days"]:

        st.markdown(f"## 📅 Day {day['day']}")

        for activity in day["activities"]:

            with st.container(border=True):

                st.markdown(
                    f"""
### 🕒 {activity['time']}

### 📍 {activity['title']}

{activity['description']}
"""
                )