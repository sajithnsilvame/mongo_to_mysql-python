# mongo_to_mysql.py
import argparse
from mongo_connector import MongoDBConnector
from collection_to_table import convert_collection_to_table
import os
from dotenv import load_dotenv, find_dotenv

# Ensure the .env file is found and loaded
dotenv_path = find_dotenv()
if not dotenv_path:
    raise FileNotFoundError(".env file not found")

load_dotenv(dotenv_path)

def main():
    parser = argparse.ArgumentParser(description='Transfer data from MongoDB to MySQL.')
    parser.add_argument('--collection', type=str, help='Specify the collection name to transfer data from MongoDB to MySQL.')
    parser.add_argument('--skip', type=str, help='Comma-separated list of columns to skip.')
    args = parser.parse_args()

    skip_columns = args.skip.split(',') if args.skip else []

    mongo_conn = MongoDBConnector()
    collections = [args.collection] if args.collection else mongo_conn.get_all_collections()
    
    all_transferred_data = {}

    for collection_name in collections:
        transferred_docs = convert_collection_to_table(collection_name, skip_columns)
        all_transferred_data[collection_name] = transferred_docs

    mongo_conn.close_connection()
    
    print_transfer_success_message(all_transferred_data)

def print_transfer_success_message(all_transferred_data):
    print("\n============================")
    print("+                           +")	
    print("+ data transfer successful! +")
    print("+                           +")
    print("============================\n")
    print("Transferred data list:\n")
    
    for collection_name, documents in all_transferred_data.items():
        print(f"- {collection_name}")
        for doc in documents:
            print(f"  {doc}")

if __name__ == "__main__":
    main()
