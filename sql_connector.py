# sql_connector.py
import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv

# Ensure the .env file is found and loaded
dotenv_path = find_dotenv()
if not dotenv_path:
    raise FileNotFoundError(".env file not found")

load_dotenv(dotenv_path)

class MySQLConnector:
    def __init__(self):
        # Fetch environment variables
        host = os.getenv("SQL_HOST")
        user = os.getenv("SQL_USER")
        password = os.getenv("SQL_PASSWORD")
        db = os.getenv("SQL_DATABASE")

        # Print the variables to debug
        print(f"SQL_HOST: {host}")
        print(f"SQL_USER: {user}")
        print(f"SQL_PASSWORD: {password}")
        print(f"SQL_DATABASE: {db}")

        # Ensure all required environment variables are present
        if not all([host, user, db]):
            raise ValueError("One or more required environment variables are missing")

        # Establish connection considering an empty password
        self.connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password if password else '',  # Handle empty password
            db=db
        )
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        columns_def = ", ".join([f"{col} TEXT" for col in columns])
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            {columns_def}
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_data(self, table_name, data):
        columns = ", ".join(data.keys())
        values = ", ".join(["%s"] * len(data))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(insert_query, list(data.values()))
        self.connection.commit()
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
