# keywords/action_keywords.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from utilities.web_driver_singleton import WebDriverSingleton


class ActionKeywords:
    def __init__(self):
        self.driver = WebDriverSingleton.get_instance()

    def find_element(self, locator_type, locator_value):
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


