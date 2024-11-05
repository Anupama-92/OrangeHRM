import pytest
from pages.dashboard_page import DashboardPage
from utilities.base_class import BaseClass
from utilities.login_helper import perform_login
from pages.admin_page import AdminPage
from utilities.excel_util import ExcelUtil
from config.config import Config

@pytest.mark.usefixtures("setup")
class TestEmploymentStatus(BaseClass):
    def test_empstatus(self):
        # Step 1: Perform login to set up the test session
        actions = perform_login()
        log = self.get_logger("TestEmploymentStatus")
        log.info("Login performed successfully.")

        # Step 2: Load Excel data for the specific test case ID (TC02)
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
            print(
                f"Row {row} -> Action: {keyword}, LocatorType: {locator_type}, LocatorValue: {locator_value}, InputData: {value}")
            # Perform actions based on the Excel sheet's keyword-driven approach
            if keyword and locator_type and locator_value:
                if keyword.lower() == "click_admin":
                    admin_page.click_admin(locator_type, locator_value)
                elif keyword.lower() == "click_job":
                    admin_page.click_job(locator_type, locator_value)
                elif keyword.lower() == "click_employmentstatus":
                    admin_page.click_employmentstatus(locator_type, locator_value)
                elif keyword.lower() == "click_add":
                    admin_page.click_add(locator_type, locator_value)
                elif keyword.lower() == "enter_name":
                    admin_page.enter_name(locator_type, locator_value, value)
                elif keyword.lower() == "click_save":
                    admin_page.click_save(locator_type, locator_value)

        log.info("Test for Employment Status completed successfully.")