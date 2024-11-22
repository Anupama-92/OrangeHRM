# get_web_data.py
from selenium.webdriver.common.by import By


def get_web_data(driver):
    web_data = []
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        if columns:
            web_data.append({
                "Username": columns[1].text,
                "User Role": columns[2].text,
                "Employee Name": columns[3].text,
                "Status": columns[4].text
            })

    return web_data
