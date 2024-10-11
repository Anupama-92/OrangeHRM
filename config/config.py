import os


class Config:
    REPORT_PATH = "D:\\Personal\\OrangeHRM\\reports"
    SCREENSHOTS_PATH = os.path.join('screenshots')
    LOGFILE_PATH = os.path.abspath("logs")
    BASE_URL = "https://opensource-demo.orangehrmlive.com/"
    DB_HOST = "192.168.0.30"
    DB_USER = "User11"
    DB_PASSWORD = "CDev011@gfh"
    DB_NAME = "Anupama"
    API_ENDPOINT = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/validate"
    EXCEL_PATH = os.path.abspath("test_data/test_data.xlsx")  # Excel file path for data-driven testing


