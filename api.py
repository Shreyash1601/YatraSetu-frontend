import requests

BASE_URL = "https://yatrasetu-backend.onrender.com"



def get_summary(data):

    return call_api(
        "summary",
        data
    )


def call_api(endpoint: str, payload: dict):

    response = requests.post(
        f"{BASE_URL}/{endpoint}/",
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    return response.json()


def get_itinerary(data):
    return call_api("itinerary", data)


def get_hidden_gems(destination):
    return call_api(
        "hidden-gems",
        {
            "destination": destination
        }
    )


def get_story(place, style):
    return call_api(
        "story",
        {
            "place": place,
            "style": style
        }
    )


def get_food(destination):
    return call_api(
        "food",
        {
            "destination": destination
        }
    )


def get_events(destination):
    return call_api(
        "events",
        {
            "destination": destination
        }
    )


def get_culture(destination):
    return call_api(
        "culture",
        {
            "destination": destination
        }
    )