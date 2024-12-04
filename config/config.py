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
    USERS_GETURL = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users"
    HEADERS = {
        "Authorization": f"Bearer def502001f64fdfdc63165f8f62269dba1e133d0727e6ef8c84b9ce32ca18ee0a9f05f7f63f3704af82ed481dcf76956ea382fabf8b66a5668e94d190071d6d1d2e1eed28ac86645eb6d4b0900efcf6e5da9e9dfd87527a2b2da77019089b3be8a2cc8a8f9ff073f8a64933cc54967ce440462c01142766f071771d19fcd37015cb6de198df5be6ed000fd6ef1408f32641769d8746d3539cd52c8b53c3ea442fafafce0",
        "Content-Type": "application/json"
    }



