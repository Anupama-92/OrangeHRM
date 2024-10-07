# test_cases/test_keyword_driven.py
from datetime import time

import pytest
from selenium import webdriver
from config.config import Config
from utilities.excel_util import ExcelUtil
from keywords.action_keywords import ActionKeywords
from utilities.base_class import BaseClass

@pytest.fixture(scope="class")
def setup(request):
    """Setup method to initialize WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestKeywordDriven(BaseClass):

    def test_login(self):
        """Test case for Keyword-Driven Framework using Excel."""
        excel_util = ExcelUtil(Config.EXCEL_PATH)
        row_count = excel_util.get_row_count()

        # Print the number of rows to verify data loading
        print(f"Total rows in Excel: {row_count}")

        action_keywords = ActionKeywords(self.driver)

        for row in range(2, row_count + 1):
            action = excel_util.get_cell_value(row, 1)
            locator_type = excel_util.get_cell_value(row, 2)
            locator_value = excel_util.get_cell_value(row, 3)
            value = excel_util.get_cell_value(row, 4)

            # Print each cell value to ensure data is being read properly
            print(
                f"Row {row} -> Action: {action}, LocatorType: {locator_type}, LocatorValue: {locator_value}, InputData: {value}")

            # Proceed only if the action and locator are correctly read
            if action and locator_type and locator_value:
                if action.lower() == "open_browser":
                    action_keywords.open_browser(value)  # Pass URL directly from Excel
                elif action.lower() == "enter_username":
                    action_keywords.enter_username(locator_type, locator_value, value)
                elif action.lower() == "enter_password":
                    action_keywords.enter_password(locator_type, locator_value, value)
                elif action.lower() == "click_login":
                    action_keywords.click_login(locator_type, locator_value)
                elif action.lower() == "verify_login":
                    action_keywords.verify_login(locator_type, locator_value, value)
                    self.capture_screenshot("Login_Success")
