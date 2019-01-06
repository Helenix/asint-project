import pymongo
from tecnico_buildings import TecnicoBuildings

class DB_Conector:
    def __init__(self, db_name):
        client = pymongo.MongoClient("mongodb+srv://asint:asint@asint-3tsob.gcp.mongodb.net/test?retryWrites=true")
        db = client[db_name]
        dbs = client.list_database_names()
      
        if db_name in dbs:
            print("Database '%s' exists, loading it..." % (db_name))
        else:
            print("There is no database named '%s', creating it... " % (db_name))  
        
        if 'campus' in db.collection_names():
            self.buildings_db = TecnicoBuildings(db['campus'], False)
        else:
            self.buildings_db = TecnicoBuildings(db['campus'], True)
        #self.user_db = TecnicoUsers()
        #self.logs_db = TecnicoLogs()

    def addCampus(self, campusDict):
        return self.buildings_db.addCampus(campusDict)

    def addBuilding(self, buildingDict):
        return self.buildings_db.addBuilding(buildingDict)
    
    def deleteSpace(self, spaceId):
        return self.buildings_db.deleteSpace(spaceId)
    