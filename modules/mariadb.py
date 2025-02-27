import pymysql
import os

async def get_db_connection(db_name: str):
    connection = pymysql.connect(
        host = os.getenv("HOST"),
        user = "root",
        password = os.getenv("MARIADB_PASSWORD"),
        database = "mysql",
        cursorclass = pymysql.cursors.DictCursor
    )

    connection.select_db(db_name)

    return connection

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