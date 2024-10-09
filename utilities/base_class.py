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

    def get_logger(self,logfile_name):
        # Create a timestamped log file path
        current_time2 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logfile_path = os.path.join(Config.LOGFILE_PATH, f"{logfile_name}_{current_time2}.log")

        # Create a logger object using the function name
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # Check if the logger already has handlers to avoid duplicates
        if not logger.hasHandlers():
            file_handler = logging.FileHandler(logfile_path)
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)

        return logger
