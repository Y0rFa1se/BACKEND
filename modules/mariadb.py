import pymysql
import os

async def get_db_connection(db_name: str):
    connection = pymysql.connect(
        host = os.getenv("MARIADB_HOST"),
        user = os.getenv("MARIADB_USER"),
        password = os.getenv("MARIADB_PASSWORD"),
        database = os.getenv("MARIADB_DATABASE"),
        cursorclass = pymysql.cursors.DictCursor
    )

    connection.select_db(db_name)

    return connection

async def is_password_right(username: str, password: str):
    conn = await get_db_connection("web")
    c = conn.cursor()

    c.execute(f"SELECT password FROM users WHERE username = '{username}'")
    result = c.fetchone()

    conn.close()

    if result is None:
        return False
    
    return result["password"] == password

async def get_users():
    conn = await get_db_connection("web")
    c = conn.cursor()

    c.execute(f"SELECT username FROM users")
    result = c.fetchall()

    conn.close()

    return result

async def get_user_permission(username: str):
    conn = await get_db_connection("web")
    c = conn.cursor()

    c.execute(f"SELECT permission FROM users WHERE username = '{username}'")
    result = c.fetchone()

    conn.close()

    return result["permission"]

async def get_stock_tickers():
    conn = await get_db_connection("stock_prices")
    c = conn.cursor()

    c.execute("SELECT TABLE_NAME, TABLE_ROWS FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'stock_prices'")
    result = c.fetchall()

    conn.close()

    return result

async def get_stock_prices(ticker: str):
    conn = await get_db_connection("stock_prices")
    c = conn.cursor()

    if not ticker.endswith("_prices"):
        ticker += "_prices"

    c.execute(f"SELECT * FROM {ticker}")
    result = c.fetchall()

    conn.close()

    return result