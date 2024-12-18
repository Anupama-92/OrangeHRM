# test_cases/test_dashboard.py
import datetime
import os

import pytest
import requests
from selenium import webdriver
from config.config import Config
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.excel_util import ExcelUtil
from keywords.action_keywords import ActionKeywords
from utilities.base_class import BaseClass
from utilities.db_integration import get_user_credentials  # Import DB integration function
from utilities.api_integration import api_login  # Import the API login function
from utilities.login_helper import perform_login
from utilities.web_driver_singleton import WebDriverSingleton


@pytest.mark.usefixtures("setup")
class TestKeywordDriven(BaseClass):

    def test_login(self):
        """Test case for Keyword-Driven Framework using Excel, Database, and API validation."""
        actions = perform_login()
        dashboard = DashboardPage()
        log = self.get_logger("Test_Execution")
        try:
            # Iterate through the actions returned from perform_login for verification
            for locator_type, locator_value, expected_value in actions:
                actual_text = dashboard.verify_login(locator_type, locator_value)
                assert actual_text == expected_value, \
                    f"Test Failed: Expected '{expected_value}', but got '{actual_text}'"
                # self.capture_screenshot("Login_Success")
                log.info(
                    f"Text verification passed for '{locator_value}'. Expected and Actual text: '{expected_value}'")

            # Step 6: If the script reaches this point, it means the web login was successful.
            log.info("Web login successful.")

        except Exception as e:
            # self.capture_screenshot("Test login failure")
            log.error(f"Test case failed: {e}")
            raise e
