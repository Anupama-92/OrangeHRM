# keywords/action_keywords.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class ActionKeywords:

    def __init__(self, driver):
        self.driver = driver
        time.sleep(3)

    def open_browser(self, url):
        print(f"Opening browser with URL: {url}")
        self.driver.get(url)
        time.sleep(3)

    def enter_username(self, locator_type, locator_value, input_data):
        element = self._find_element(locator_type, locator_value)
        element.send_keys(input_data)

    def enter_password(self, locator_type, locator_value, input_data):
        element = self._find_element(locator_type, locator_value)
        element.send_keys(input_data)

    def click_login(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        element = self._find_element(locator_type, locator_value)
        element.click()
        time.sleep(3)
        print("Success")

    def verify_login(self, locator_type, locator_value, expected_text):
        element = self._find_element(locator_type, locator_value)
        # Get the actual text and compare
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
        print("Login verified successfully, navigated to Dashboard.")

    def _find_element(self, locator_type, locator_value):
        """Helper method to find element based on locator type."""
        if locator_type.lower() == "id":
            return self.driver.find_element(By.ID, locator_value)
        elif locator_type.lower() == "name":
            return self.driver.find_element(By.NAME, locator_value)
        elif locator_type.lower() == "xpath":
            return self.driver.find_element(By.XPATH, locator_value)
        elif locator_type == "css":
            return self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_type == "link_text":
            return self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type == "class_name":
            return self.driver.find_element(By.CLASS_NAME, locator_value)
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")

        # Add more locator strategies as needed.


    # def verify_login(self):
    #     dashboard = DashboardPage(self.driver)
    #     assert "Welcome" in dashboard.get_welcome_message(), "Login verification failed!"
