# keywords/action_keywords.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ActionKeywords:

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, url):
        self.driver.get(url)
        time.sleep(3)

    def enter_username(self, locator_type, locator_value, input_data):
        element = self._find_element(locator_type, locator_value)
        element.send_keys(input_data)

    def enter_password(self, locator_type, locator_value, input_data):
        element = self._find_element(locator_type, locator_value)
        element.send_keys(input_data)

    def click_login(self, locator_type, locator_value):
        element = self._find_element(locator_type, locator_value)
        element.click()

    def verify_login(self, locator_type, locator_value, expected_text):
        element = self._find_element(locator_type, locator_value)
        assert element.text == expected_text, f"Expected {expected_text} but got {element.text}"

    def _find_element(self, locator_type, locator_value):
        """Helper method to find element based on locator type."""
        if locator_type.lower() == "id":
            return self.driver.find_element(By.ID, locator_value)
        elif locator_type.lower() == "name":
            return self.driver.find_element(By.NAME, locator_value)
        elif locator_type.lower() == "xpath":
            return self.driver.find_element(By.XPATH, locator_value)
        # Add more locator strategies as needed.


    # def verify_login(self):
    #     dashboard = DashboardPage(self.driver)
    #     assert "Welcome" in dashboard.get_welcome_message(), "Login verification failed!"
