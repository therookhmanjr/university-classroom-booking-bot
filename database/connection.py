import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        return pyodbc.connect(
            f"DRIVER = {{ODBC DRIVER 18 for SQL Server}};"
            f"SERVER = {os.getenv('DB_SERVER')};"
            f"DATABASE = {os.getenv('DB_DATABASE')};"
            f"UID = {os.getenv('DB_USERNAME')};"
            f"PWD = {os.getenv('DB_PASSWORD')};"
            "TrustServerCertificate=yes"
        )
    except pyodbc.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise