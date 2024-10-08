from selenium import webdriver


class WebDriverSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if WebDriverSingleton._instance is None:
            WebDriverSingleton._instance = webdriver.Chrome()
            WebDriverSingleton._instance.maximize_window()
        return WebDriverSingleton._instance

    @staticmethod
    def quit_instance():
        if WebDriverSingleton._instance is not None:
            WebDriverSingleton._instance.quit()
            WebDriverSingleton._instance = None
