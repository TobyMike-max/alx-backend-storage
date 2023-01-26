#!/usr/bin/env python3
"""Using MongoDB with Python and PyMongo"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on name"""
    mongo_collection.update(
      {"name": name},
      {$set: {"topics": topics}},
      {multi: true}
    )
