import pymssql
from Config.Config import Config


def get_user_credentials():
    """Fetch user credentials from the SQL Server database."""
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
