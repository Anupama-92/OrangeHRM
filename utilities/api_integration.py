import requests
from config.config import Config


def api_login(username, password):
    """Perform login using API."""
    payload = {"username": username, "password": password}
    response = requests.post(Config.API_ENDPOINT, json=payload)
    print(f"API Response: {response.status_code} - {response.text}")
    return response
