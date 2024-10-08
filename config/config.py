import os


class Config:
    SCREENSHOTS_PATH = os.path.abspath("screenshots")
    BASE_URL = "https://opensource-demo.orangehrmlive.com/"
    USERNAME = "Admin"
    PASSWORD = "admin123"
    DB_HOST = "192.168.0.30"
    DB_USER = "User11"
    DB_PASSWORD = "CDev011@gfh"
    DB_NAME = "Anupama"
    API_ENDPOINT = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/validate"
    EXCEL_PATH = os.path.abspath("test_data/test_data.xlsx")  # Excel file path for data-driven testing
