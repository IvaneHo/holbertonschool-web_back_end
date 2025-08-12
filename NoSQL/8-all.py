#!/usr/bin/env python3
"""Module for listing all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection object.

    Returns:
        list: A list of documents in the collection.
              Returns an empty list if the collection is empty.
    """
    return list(mongo_collection.find())
