# collection_to_table.py
from mongo_connector import MongoDBConnector
from sql_connector import MySQLConnector
import os
from dotenv import load_dotenv, find_dotenv

# Ensure the .env file is found and loaded
dotenv_path = find_dotenv()
if not dotenv_path:
    raise FileNotFoundError(".env file not found")

load_dotenv(dotenv_path)

def convert_collection_to_table(collection_name, skip_columns):
    mongo_conn = MongoDBConnector()
    mysql_conn = MySQLConnector()

    collection = mongo_conn.get_collection(collection_name)
    documents = collection.find()

    transferred_docs = []

    if collection.count_documents({}) > 0:
        first_doc = documents[0]
        columns = [col for col in first_doc.keys() if col not in skip_columns]
        mysql_conn.create_table(collection_name, columns)

        for doc in documents:
            doc_to_insert = {k: v for k, v in doc.items() if k not in skip_columns}
            mysql_conn.insert_data(collection_name, doc_to_insert)
            transferred_docs.append(doc_to_insert)

    mongo_conn.close_connection()
    mysql_conn.close_connection()

    return transferred_docs
