import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from keywords.action_keywords import ActionKeywords
from utilities.web_driver_singleton import WebDriverSingleton
from behave import given, when, then


class LoginPage:
    def __init__(self, db_credentials=None):
        """
        Initialize ActionKeywords class with WebDriver instance and optional database credentials.

        :param driver: WebDriver instance
        :param db_credentials: Optional dictionary containing username and password from the database.
        """
        self.driver = WebDriverSingleton.get_instance()
        self.action_keywords = ActionKeywords()
        self.db_username = db_credentials['username'] if db_credentials else None
        self.db_password = db_credentials['password'] if db_credentials else None
        time.sleep(3)

    @given("I am on the login page")
    def open_browser(self, url):
        print(f"Opening browser with URL: {url}")
        self.driver.get(url)
        time.sleep(3)

    @when("I enter the username")
    def enter_username(self, locator_type, locator_value, input_data):
        # If input_data is empty, use username from database
        input_value = input_data if input_data else self.db_username
        print(f"Entering username: {input_value}")
        element = self.action_keywords.find_element(locator_type, locator_value)
        element.send_keys(input_value)

    @when("I enter the password")
    def enter_password(self, locator_type, locator_value, input_data):
        # If input_data is empty, use password from database
        input_value = input_data if input_data else self.db_password
        print(f"Entering password: {input_value}")
        element = self.action_keywords.find_element(locator_type, locator_value)
        element.send_keys(input_value)

    @then("I should see the dashboard")
    def click_login(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        element = self.action_keywords.find_element(locator_type, locator_value)
        element.click()
        time.sleep(3)
        print("Success")


