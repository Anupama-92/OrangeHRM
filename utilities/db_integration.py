import openpyxl
import pymssql
from config.config import Config
from utilities.excel_util import  ExcelUtil


def get_user_credentials():
    """
    Fetch user credentials from the SQL Server database.
    Returns:
        dict: A dictionary containing username and password.
    """
    conn = pymssql.connect(
        server=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )
    cursor = conn.cursor(as_dict=True)
    cursor.execute("SELECT username, password FROM UserCredentials WHERE active=1")
    result = cursor.fetchone()  # Fetch only the first active user
    conn.close()
    return result


def update_excel_with_db_credentials(excel_path, username_cell, password_cell, credentials):
    """
    Update the specified Excel cells with username and password fetched from the database.

    Parameters:
    - excel_path: Path to the Excel file.
    - username_cell: Tuple specifying (row, column) for the username.
    - password_cell: Tuple specifying (row, column) for the password.
    - credentials: Dictionary containing 'username' and 'password'.
    """
    excel_util = ExcelUtil(excel_path)
    excel_util.write_cell_value(username_cell[3], username_cell[5], credentials['username'])
    excel_util.write_cell_value(password_cell[4], password_cell[5], credentials['password'])
    print(f"Excel file '{excel_path}' updated with username and password from the database.")
