#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
    mongo_collection (pymongo.collection.Collection): The collection to query.
    topic (str): The topic to search for.

    Returns:
    List of documents that match the topic.
    """
    return list(mongo_collection.find({"topics": topic}))