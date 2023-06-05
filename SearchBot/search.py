import requests
from config import SERP_API_KEY

def search_google(search_query):
    search_url = f"https://serpapi.com/search?q={search_query}&api_key={SERP_API_KEY}"
    response = requests.get(search_url)
    response_json = response.json()
    search_results = response_json.get("organic_results", [])
    return search_results