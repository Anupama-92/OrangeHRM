# utilities/base_class.py
import inspect
import logging
import os
import datetime

import pytest

from config.config import Config
from utilities.web_driver_singleton import WebDriverSingleton


class BaseClass:

    def get_logger(self, logfile_name):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Create a logger object
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(os.path.join(Config.LOGFILE_PATH,f"{logfile_name}_{current_time}.log"))
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler Object
        logger.setLevel(logging.DEBUG)
        return logger




    def capture_screenshot(self, screenshot_name):
        """Capture screenshot and save to a specified directory."""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(Config.SCREENSHOTS_PATH, f"{screenshot_name}_{current_time}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

    # @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    # def pytest_runtest_makereport(self, item, call):
    #     """
    #     Extends the PyTest Plugin to take and embed screenshot in HTML report, whenever a test fails.
    #     """
    #     pytest_html = item.config.pluginmanager.getplugin('html')
    #     outcome = yield
    #     report = outcome.get_result()
    #     extra = getattr(report, 'extra', [])
    #
    #     if report.when == 'call' or report.when == "setup":
    #         xfail = hasattr(report, 'wasxfail')
    #         if (report.skipped and xfail) or (report.failed and not xfail):
    #             # Use the class method to capture a screenshot
    #             screenshot_name = report.nodeid.replace("::", "_")
    #             self.capture_screenshot(screenshot_name)
    #             screenshot_file = f"{screenshot_name}.png"
    #             if screenshot_file:
    #                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
    #                        'onclick="window.open(this.src)" align="right"/></div>' % screenshot_file
    #                 extra.append(pytest_html.extras.html(html))
    #         report.extra = extra
