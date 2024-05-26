# mongo_connector.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

# Ensure the .env file is found and loaded
dotenv_path = find_dotenv()
if not dotenv_path:
    raise FileNotFoundError(".env file not found")

load_dotenv(dotenv_path)

class MongoDBConnector:
    def __init__(self, uri=None, db_name=None):
        uri = uri or os.getenv("MONGO_URI")
        db_name = db_name or os.getenv("MONGO_DATABASE")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_all_collections(self):
        return self.db.list_collection_names()

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        self.client.close()
