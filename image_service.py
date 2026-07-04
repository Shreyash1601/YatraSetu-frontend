import requests


def get_wikipedia_image(query: str):

    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"

        response = requests.get(url)

        data = response.json()

        if "thumbnail" in data:
            return data["thumbnail"]["source"]

    except Exception:
        pass

    return None