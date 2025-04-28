from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, USER, PASS) -> None:
        # Connection Variables
        #
        # Hard coded to utilize AAC database and connection
        # variables for Jeff Fulfer's instance in Apporto
        #
        # Class CS-340 - 03/27/2025
        #
        USER = urllib.parse.quote_plus(USER)
        PASS = urllib.parse.quote_plus(PASS)
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32014
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection using variables above
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    # Create method
    #
    # Method accepts dict parameter to insert into defined collection above
    #
    def create(self, data: dict) -> bool:
        if data is not None:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save because data parameter is empty")
            return False
            
    # Read Method
    #
    # Method accepts single item dict parameter to perform query within
    # collection defined above and returns list object
    #
    def read(self, queryParams: dict) -> list:
        results = self.collection.find(queryParams)
        return list(results)
    
    # Update Method
    #
    # Method parameters requires two dict data items with the first parameter used 
    # to query existing records and the second a set of key/value pairs that 
    # should be updated in the existing records
    #
    def update(self, queryParams: dict, updatedFields: dict) -> int:
        updateParams = {"$set": updatedFields}
        result = self.collection.update_many(queryParams, updateParams)
        return result.modified_count
    
    # Delete Method
    #
    # Method expects a single dict item parameter that will be used to query
    # for and delete any matching records
    #
    def delete(self, queryParams: dict) -> int:
        result = self.collection.delete_many(queryParams)
        return result.deleted_count
