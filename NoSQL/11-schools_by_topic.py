#!/usr/bin/env python3
"""Module for finding schools by a specific topic in MongoDB."""


def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of matching school documents.
    """
    return list(mongo_collection.find({"topics": topic}))
