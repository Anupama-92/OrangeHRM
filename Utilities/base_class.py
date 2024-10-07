# utilities/base_class.py
import os
import datetime
from Config.Config import Config

class BaseClass:
    def capture_screenshot(self, screenshot_name):
        """Capture screenshot and save to a specified directory."""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(Config.SCREENSHOTS_PATH, f"{screenshot_name}_{current_time}.png")
        self.driver.save_screenshot(screenshot_path)
