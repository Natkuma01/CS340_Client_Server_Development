# import required libraries
from pymongo import MongoClient             # mongoDB driver for Python
from bson.objectid import ObjectId          # allows working with mongoDB objectId type

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password, host, port, database, collection): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username           # mongoDB username
        PASS = password        # mongoDB password
        HOST = 'localhost'         # mongoDB server host
        PORT = 27017               # default mongoDB port
        DB = 'aac'                 # database name
        COL = 'animals'            # collection name
        # 
        # 
        # Initialize mongoDB client and set database/ collection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=aac') 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
        
        # confirmation message to verify connection
        print("You are connected to MongoDB successfully .")

# ------------------- CREATE METHOD --------------------------
    def create(self, data):
        if data is not None and isinstance(data, dict): 
            self.collection.insert_one(data)          # insert document into mongoDB
            return True                               # return true when it is successful
        else: 
            raise Exception("Nothing to save, because data parameter is empty")
            return False                             # not reached if exception is raised


# ----------------- READ METHOD -----------------------------
    def read(self, lookup):
        if lookup is not None and isinstance(lookup, dict):
            cursor = self.collection.find(lookup)               # perform find query
            results = list(cursor)                              # convert cursor to list of documents
            return results
        else:
            raise Exception("Read Failed: lookup must be a dictionary.")
            return []                                          # not reached if exception is raised
        
        
# ----------------- UPDATE METHOD --------------------------
    def update(self, lookup, update_data):
        if lookup is not None and isinstance(lookup, dict):
            if update_data is not None and isinstance(update_data, dict):
                
                # use update_many() to update one or more than one matching docunments 
                result = self.collection.update_many(lookup, update_data)
                
                # return the count of modified documents
                return result.modified_count
            else:
                raise Exception("Update failed: update_data must be a dictionary.")
                                          
                
# --------------- DELETE METHOD ----------------------------
    def delete(self, lookup):
        if lookup is not None and isinstance(lookup, dict):
            
            # use delete_many() to delete all matching docunments
            result = self.collection.delete_many(lookup)
            
            # return the count of deleted docunments
            return result.deleted_count
        else:
            raise Exception("Delete failed: lookup must be a dictionary.")
            return 0