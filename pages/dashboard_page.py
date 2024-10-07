from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.ID, "welcome")

    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_message).text