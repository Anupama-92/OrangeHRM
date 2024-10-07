# strategies/login_strategy.py
from keywords.action_keywords import ActionKeywords
from utilities.api_integration import api_login
from utilities.db_integration import get_user_credentials

class LoginStrategy:
    def __init__(self, driver=None):
        self.driver = driver

    def perform_ui_login(self, username, password):
        keywords = ActionKeywords(self.driver)
        keywords.enter_username(username)
        keywords.enter_password(password)
        keywords.click_login()

    def perform_api_login(self, username, password):
        response = api_login(username, password)
        return response.status_code == 200

    def perform_db_login(self):
        # Fetch credentials from DB
        credentials = get_user_credentials()
        return credentials['username'], credentials['password']
