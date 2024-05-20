#!/usr/bin/env python3
"""
function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
    mongo_collection (pymongo.collection.Collection): The collection to insert into.
    **kwargs: The key-value pairs to insert as the document.

    Returns:
    The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id