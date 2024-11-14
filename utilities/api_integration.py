import requests
from config.config import Config


def api_login(username, password):
    """Perform login using API."""
    payload = {"username": username, "password": password}
    response = requests.post(Config.API_ENDPOINT, json=payload)
    print(f"API Response: {response.status_code} - {response.text}")
    return response


def get_api_data():
    """Fetch user data from API and return it in a structured format."""
    # Assuming the API login has already been handled, if not, handle login and get session or token if required.
    response = requests.get(f"{Config.API_ENDPOINT}/admin/users")
    if response.status_code == 200:
        api_data = []
        data = response.json().get("data", [])
        for user in data:
            api_data.append({
                "Username": user["userName"],
                "User Role": user["userRole"]["displayName"],
                "Employee Name": f"{user['employee']['firstName']} {user['employee']['lastName']}",
                "Status": "Enabled" if user["status"] else "Disabled"
            })
        return api_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
