# utilities/login_helper.py


from utilities.db_integration import get_user_credentials
from utilities.api_integration import api_login
from config.config import Config
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.excel_util import ExcelUtil


def perform_login():
    # Step 1: Fetch credentials from the database
    credentials = get_user_credentials()
    if not credentials:
        raise ValueError("No active credentials found in the database.")

    username, password = credentials['username'], credentials['password']
    print(f"Fetched username and password from DB: {username}, {password}")

    # Step 2: Perform API login to verify the credentials
    api_response = api_login(username, password)

    # Assert that the API returned a 200 OK response, indicating a successful login
    assert api_response.status_code == 200, f"API login failed. Expected 200, but got {api_response.status_code}"
    print("API login successful with 200 OK response.")

    # Step 3: Write these credentials to the Excel file before running the test
    excel_util = ExcelUtil(Config.EXCEL_PATH)
    print(f"Excel file path: {Config.EXCEL_PATH}")

    # Assuming the Excel file has specific cells for username and password (e.g., row 2, column 5 for username and row 3, column 5 for password)
    username_cell = (3, 5)  # Update this as per your Excel file structure
    password_cell = (4, 5)  # Update this as per your Excel file structure

    # Write the fetched username and password to the specified cells
    excel_util.write_cell_value(username_cell[0], username_cell[1], username)
    excel_util.write_cell_value(password_cell[0], password_cell[1], password)
    print(f"Excel updated with username: '{username}' and password: '{password}'.")

    # Step 4: Read Excel data to perform keyword-driven testing using Selenium
    row_count = excel_util.get_row_count()
    print(f"Total rows in Excel: {row_count}")

    login = LoginPage(db_credentials=credentials)
    actions = []  # To hold actions and locators for verification
    for row in range(2, row_count + 1):  # Start from the second row assuming the first row is the header
        action = excel_util.get_cell_value(row, 2)
        locator_type = excel_util.get_cell_value(row, 3)
        locator_value = excel_util.get_cell_value(row, 4)
        value = excel_util.get_cell_value(row, 5)  # This should now use the updated value from DB

        # Print each cell value to ensure data is being read properly
        print(
            f"Row {row} -> Action: {action}, LocatorType: {locator_type}, LocatorValue: {locator_value}, InputData: {value}")

        # Step 5: Perform actions based on the Excel sheet's keyword-driven approach
        if action and locator_type and locator_value:
            if action.lower() == "open_browser":
                login.open_browser(locator_value)  # Pass URL directly from Excel
            elif action.lower() == "enter_username":
                login.enter_username(locator_type, locator_value, username)  # Use fetched username
            elif action.lower() == "enter_password":
                login.enter_password(locator_type, locator_value, password)  # Use fetched password
            elif action.lower() == "click_login":
                login.click_login(locator_type, locator_value)
            elif action.lower() == "verify_login":
                actions.append((locator_type, locator_value, value))

    print("Login actions completed.")
    return actions  # Return the list of actions for verification
