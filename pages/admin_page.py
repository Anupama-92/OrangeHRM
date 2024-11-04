from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from keywords.action_keywords import ActionKeywords
from utilities.web_driver_singleton import WebDriverSingleton


class AdminPage:
    def __init__(self):
        self.driver = WebDriverSingleton.get_instance()
        self.action_keywords = ActionKeywords()

    def click_admin(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        element = self.action_keywords.find_element(locator_type, locator_value)
        element.click()

    def click_job(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, 10)
        element = self.action_keywords.find_element(locator_type, locator_value)
        element.click()

    def click_add(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, 10)
        element = self.action_keywords.find_element(locator_type, locator_value)
        element.click()

    def enter_name(self, locator_type, locator_value, input_data):
        wait = WebDriverWait(self.driver, 10)
        element = self.action_keywords.find_element(locator_type, locator_value)
        element.send_keys(input_data)

    def click_save(self, locator_type, locator_value):
        element = self.action_keywords.find_element(locator_type, locator_value)
        element.click()