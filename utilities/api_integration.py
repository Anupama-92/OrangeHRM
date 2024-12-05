import requests
from config.config import Config
import random
import string


def api_login(username, password):
    """Perform login using API."""
    payload = {"username": username, "password": password}
    response = requests.post(Config.API_ENDPOINT, json=payload)
    print(f"API Response: {response.status_code} - {response.text}")
    return response


def get_api_data():
    """Fetch user data from API and return it in a structured format."""
    # Assuming the API login has already been handled, if not, handle login and get session or token if required.
    url = Config.USERS_GETURL
    headers = Config.HEADERS
    response = requests.get(url, headers=headers)
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


def generate_random_name():
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return f"{random_suffix}"


def create_nationality():
    name = generate_random_name()
    print(f"Generated Random Nationality Name: {name}")
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/nationalities"
    headers = {
        "Authorization": f"Bearer def502001f64fdfdc63165f8f62269dba1e133d0727e6ef8c84b9ce32ca18ee0a9f05f7f63f3704af82ed481dcf76956ea382fabf8b66a5668e94d190071d6d1d2e1eed28ac86645eb6d4b0900efcf6e5da9e9dfd87527a2b2da77019089b3be8a2cc8a8f9ff073f8a64933cc54967ce440462c01142766f071771d19fcd37015cb6de198df5be6ed000fd6ef1408f32641769d8746d3539cd52c8b53c3ea442fafafce0",
        "Content-Type": "application/json"
    }
    payload = {
        "name": name,
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            response_data = response.json()
            nationality_data = response_data.get("data", {})
            nationality_id = nationality_data.get("id")
            nationality_name = nationality_data.get("name")
            return {"id": nationality_id, "name": nationality_name}
        except KeyError as e:
            return {"error": f"Unexpected response structure: {e}"}
    else:
        return {"error": response.text}





