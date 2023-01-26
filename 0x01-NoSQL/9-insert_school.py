#!/usr/bin/env python3
"""Using MongoDB with Python and PyMongo"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    ret = mongo_collection.insert_one(kwargs)
    return ret.inserted_id
