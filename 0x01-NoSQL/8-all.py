#!/usr/bin/env python3
"""Using MongoDB with Python and PyMongo"""


def list_all(mongo_collection):
    """Lists all documents in a collection
    Args: 
        mongo_collection(pymongo collection object)
    Return: 
        All documents inside the collection
        Else an empty list
    """
    doc = mongo_collection.find()
    return doc
