#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client['web_logs']
    collection = db['nginx_logs']
    request_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f'{collection.count_documents({})} requests logged')
    print('Request Methods:')
    for method in request_methods:
        print(f'\t{method}:',
              collection.count_documents({'method': method}))
    status_checks = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{status_checks} status checks')
