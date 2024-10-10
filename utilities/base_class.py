# utilities/base_class.py
import inspect
import logging
import os
import datetime
from config.config import Config


class BaseClass:
    def capture_screenshot(self, screenshot_name):
        """Capture screenshot and save to a specified directory."""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(Config.SCREENSHOTS_PATH, f"{screenshot_name}_{current_time}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

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
