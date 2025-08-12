#!/usr/bin/env python3
"""Module for updating the topics of a school document in MongoDB."""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document by the school's name.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
