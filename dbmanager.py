"""
manage the data in the mongodb
"""
from pymongo import MongoClient
from tornado.log import logging
import config

class DbManager():
    """
    use pymongo to implement CRUD
    """
    client = MongoClient(config.options.mongodb_host)
    database = client.get_database(config.options.database_name)
    col = database.get_collection(config.options.collection_name)

    @classmethod
    def insert(cls, person_id, name, phone):
        """
        Insert a single document.
        """
        return cls.col.insert_one({'id': person_id, "name": name, "phone": phone})

    @classmethod
    def find_one(cls):
        """
        Get a single document from database
        """
        return cls.col.find_one()

    @classmethod
    def find(cls, *args):
        """
        Query the database
        """
        return cls.col.find(args[0])

    @classmethod
    def update(cls, *args):
        """
        Update a document in the current collection
        """
        return cls.col.find_one_and_replace(args[0], args[1])

    @classmethod
    def delete_one(cls, *args):
        """
        Delete the first finded document of the collection
        """
        logging.debug(args[0])
        return cls.col.find_one_and_delete(args[0])

    @classmethod
    def count(cls):
        """
        Return the count of the collection
        """
        pass

