# test_cases/test_keyword_driven.py
import pytest
from selenium import webdriver
from Config.Config import Config
from Utilities.excel_util import ExcelUtil
from Keywords.action_keywords import ActionKeywords
from Utilities.base_class import BaseClass

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
        action_keywords = ActionKeywords(self.driver)

        # Loop through each row in the Excel sheet
        for row in range(2, row_count + 1):
            keyword = excel_util.get_cell_value(row, 1)
            locator_type = excel_util.get_cell_value(row, 2)
            locator_value = excel_util.get_cell_value(row, 3)
            input_data = excel_util.get_cell_value(row, 4)

            # Execute each action keyword read from Excel
            if keyword.lower() == "open_browser":
                action_keywords.open_browser(input_data)
            elif keyword.lower() == "enter_username":
                action_keywords.enter_username(locator_type, locator_value, input_data)
            elif keyword.lower() == "enter_password":
                action_keywords.enter_password(locator_type, locator_value, input_data)
            elif keyword.lower() == "click_login":
                action_keywords.click_login(locator_type, locator_value)
            elif keyword.lower() == "verify_login":
                action_keywords.verify_login(locator_type, locator_value, input_data)
