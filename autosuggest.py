import requests

def get_autosuggest(query):
    url = "https://suggestqueries.google.com/complete/search"
    params = {
        "client": "firefox",
        "q": query,
        "hl": "en",
        "gl": "us",
        "callback": "google.sbox.p50"
    }
    response = requests.get(url, params=params)
    suggestions = response.json()[1]
    return suggestions
