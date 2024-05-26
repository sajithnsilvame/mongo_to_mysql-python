# test_connection.py
import os
from dotenv import load_dotenv, find_dotenv

# Ensure the .env file is found and loaded
dotenv_path = find_dotenv()
if not dotenv_path:
    raise FileNotFoundError(".env file not found")

load_dotenv(dotenv_path)

def test_connection():
    # Print the environment variables to debug
    host = os.getenv("SQL_HOST")
    user = os.getenv("SQL_USER")
    password = os.getenv("SQL_PASSWORD")
    db = os.getenv("SQL_DATABASE")

    print(f"SQL_HOST: {host}")
    print(f"SQL_USER: {user}")
    print(f"SQL_PASSWORD: {password}")  # Ensure this is not empty
    print(f"SQL_DATABASE: {db}")

    # Initialize MySQLConnector after verifying the variables
    from sql_connector import MySQLConnector

    try:
        mysql_conn = MySQLConnector()
        print("Connection successful!")
        mysql_conn.close_connection()
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
