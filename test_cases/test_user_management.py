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
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        web_data = get_web_data(self.driver)

        # Assert that API and web data match
        assert api_data == web_data, "API data does not match web data"

