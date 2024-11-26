import time

import pytest
from pages.dashboard_page import DashboardPage
from utilities.api_integration import get_api_data
from utilities.base_class import BaseClass
from utilities.login_helper import perform_login
from pages.admin_page import AdminPage
from utilities.excel_util import ExcelUtil
from config.config import Config
from utilities.web_data import get_web_data


@pytest.mark.usefixtures("setup")
class TestUserManagement(BaseClass):
    def test_user_management(self):
        actions = perform_login()
        log = self.get_logger("TestUserManagement")
        log.info("Login performed successfully.")
        api_data = get_api_data()
        # Navigate to the User Management page to get the web data
        excel_util = ExcelUtil(Config.EXCEL_PATH)
        row_count = excel_util.get_row_count()

        admin_page = AdminPage()
        keywords = []
        # Step 3: Execute actions based on Excel instructions for TC02
        for row in range(2, row_count + 1):  # Start from the second row to skip headers
            test_case_id = excel_util.get_cell_value(row, 1)
            keyword = excel_util.get_cell_value(row, 2)
            locator_type = excel_util.get_cell_value(row, 3)
            locator_value = excel_util.get_cell_value(row, 4)
            value = excel_util.get_cell_value(row, 5)

            # Print each cell value to ensure data is being read properly
            # print(
                #f"Row {row} -> Action: {keyword}, LocatorType: {locator_type}, LocatorValue: {locator_value}, InputData: {value}")
            # Perform actions based on the Excel sheet's keyword-driven approach
            if keyword and locator_type and locator_value:
                if keyword.lower() == "click_admin":
                    admin_page.click_admin(locator_type, locator_value)
        time.sleep(3)
        #self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        web_data = get_web_data(self.driver)
        print(f"api_data: {api_data}")
        print(f"web_data: {web_data}")
        # Assert that API and web data match
        assert api_data == web_data, "API data does not match web data"

