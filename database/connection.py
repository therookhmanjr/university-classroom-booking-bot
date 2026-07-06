import os

import pyodbc
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_DATABASE')};"
            f"UID={os.getenv('DB_USERNAME')};"
            f"PWD={os.getenv('DB_PASSWORD')};"
            "TrustServerCertificate=yes;"
        )

        return connection

    except pyodbc.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise