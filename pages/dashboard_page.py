from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from keywords.action_keywords import ActionKeywords
from utilities.web_driver_singleton import WebDriverSingleton


class DashboardPage:
    def __init__(self):
        self.driver = WebDriverSingleton.get_instance()
        self.action_keywords = ActionKeywords()

    def verify_login(self, locator_type, locator_value, expected_text):
        # Wait until the element is present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator_value))
        )
        element = self.action_keywords.find_element(locator_type, locator_value)
        # Get the actual text and compare
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
        print("Login verified successfully, navigated to Dashboard.")

