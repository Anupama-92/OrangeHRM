import time

import pytest
from pages.dashboard_page import DashboardPage
from utilities.api_integration import get_api_data, create_nationality
from utilities.base_class import BaseClass
from utilities.login_helper import perform_login
from pages.admin_page import AdminPage
from utilities.excel_util import ExcelUtil
from config.config import Config
from utilities.web_data import get_web_data, get_nationality_web_data


@pytest.mark.usefixtures("setup")
class TestNationality(BaseClass):
    def test_nationality(self):
        actions = perform_login()
        log = self.get_logger("TestUserManagement")
        log.info("Login performed successfully.")
        nationality_name = "Automation123Test"
        api_data = create_nationality(nationality_name)
        print(api_data)
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

            # Perform actions based on the Excel sheet's keyword-driven approach
            if keyword and locator_type and locator_value:
                if keyword.lower() == "click_admin":
                    admin_page.click_admin(locator_type, locator_value)
                elif keyword.lower() == "click_nationalities":
                    admin_page.click_nationalities(locator_type, locator_value)
        time.sleep(3)
        web_data = get_nationality_web_data(self.driver)
        print(f"api_data: {api_data}")
        print(f"web_data: {web_data}")
        # Step 4: Validate API nationality exists in web data
        assert any(
            nationality["Nationality"] == api_data["name"] for nationality in web_data
        ), f"Nationality {api_data['name']} from API response does not exist in web data."

