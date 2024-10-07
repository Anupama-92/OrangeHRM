from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "txtUsername")
        self.password_input = (By.ID, "txtPassword")
        self.login_button = (By.ID, "btnLogin")
        self.welcome_message = (By.ID, "welcome")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_message).text