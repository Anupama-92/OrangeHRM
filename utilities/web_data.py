# get_web_data.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_web_data(driver):
    web_data = []
    # Wait until the table is visible
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "orangehrm-container")))
    driver.execute_script("arguments[0].scrollIntoView();", table)

    # XPath for retrieving the table rows
    row_xpath = "//div[@class='oxd-table-body']//div[@role='row']"


    # XPath for retrieving the specific columns
    username_xpath = ".//div[@role='cell'][2]"
    user_role_xpath = ".//div[@role='cell'][3]"
    employee_name_xpath = ".//div[@role='cell'][4]"
    status_xpath = ".//div[@role='cell'][5]"
    # Find all rows within the table
    rows = table.find_elements(By.XPATH, row_xpath)

    # Iterate over each row and extract data
    for row in rows:
        try:
            username = row.find_element(By.XPATH, username_xpath).text
            user_role = row.find_element(By.XPATH, user_role_xpath).text
            employee_name = row.find_element(By.XPATH, employee_name_xpath).text
            status = row.find_element(By.XPATH, status_xpath).text
            # Append the extracted data to the list
            web_data.append({
                "Username": username,
                "User Role": user_role,
                "Employee Name": employee_name,
                "Status": status
            })

            print(f"Username: {username}, User Role: {user_role}, Employee Name: {employee_name}, Status: {status}")
        except Exception as e:
            print(f"Error processing row: {e}")

    return web_data


def get_nationality_web_data(driver):
    nationality_web_data = []
    # Wait until the table is visible
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "orangehrm-container")))
    driver.execute_script("arguments[0].scrollIntoView();", table)

    # XPath for retrieving the table rows
    row_xpath = "//div[@class='oxd-table-body']//div[@role='row']"

    # XPath for retrieving the specific columns
    nationality_xpath = ".//div[@role='cell'][2]"
    # Find all rows within the table
    rows = table.find_elements(By.XPATH, row_xpath)

    # Iterate over each row and extract data
    for row in rows:
        try:
            nationality = row.find_element(By.XPATH, nationality_xpath).text
            # Append the extracted data to the list
            nationality_web_data.append({
                "Nationality": nationality
            })

            print(f"Nationality: {nationality}")
        except Exception as e:
            print(f"Error processing row: {e}")

    return nationality_web_data
