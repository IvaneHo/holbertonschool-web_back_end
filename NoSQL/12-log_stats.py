#!/usr/bin/env python3
"""Script that prints stats about Nginx logs stored in MongoDB.

Database: logs
Collection: nginx

Output format:
<total> logs
Methods:
    method GET: <count>
    method POST: <count>
    method PUT: <count>
    method PATCH: <count>
    method DELETE: <count>
<status_count> status check
"""

from pymongo import MongoClient


def log_stats():
    """Compute and print stats for the logs.nginx collection."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total = collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        count = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")

    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()
