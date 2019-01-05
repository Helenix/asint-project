import requests
import json
import pickle
import pymongo
from buildings_info import BuildingsInfo

class TecnicoBuildings:
    def __init__(self, db_name):
        client = pymongo.MongoClient("mongodb+srv://asint:asint@asint-3tsob.gcp.mongodb.net/test?retryWrites=true")
        self.db = client[db_name]
        dbs = client.list_database_names()

        
        if db_name in dbs:
            print("Database '%s' exists, loading it..." % (db_name))
            
            campus_collection = self.db['campus']

        else:
            print("There is no database named '%s', creating it... " % (db_name))

            campus_collection = self.db['campus']

            url = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces/"
            response = requests.get(url)
            campus = response.json()

            info = BuildingsInfo()

            for c in campus:
                if info.getCampus(c['id']):
                    newUrl = url + c['id']
                    response = requests.get(newUrl)
                    campusInfo = response.json()
                                        
                    campusDict = {
                        'type': c['type'],
                        'id': int(c['id']),
                        'name': c['name'],
                        'containedSpaces': []
                    }

                    buildings = campusInfo['containedSpaces']
                    
                    for b in buildings:
                        b_info = info.getBuilding(b['id'])

                        if b_info:
                            buildingDict = {
                                'type': b['type'],
                                'id': int(b['id']),
                                'name': b['name'],
                                'topLevelSpaceId': int(c['id']),
                                'botLat': float(b_info['botLat']),
                                'leftLng': float(b_info['leftLng']),
                                'topLat': float(b_info['topLat']),
                                'rightLng': float(b_info['rightLng'])
                            }

                            campusDict['containedSpaces'].append(buildingDict)
            
                    campus_collection.insert_one(campusDict)

    def addCampus(self, newType, newID, newName):
        campus_collection = self.db['campus']
        campusDict = {
            'type': newType,
            'id': newID,
            'name': newName,
            'containedSpaces': []
        }
       
        campus_collection.insert_one(campusDict)

    def addBuilding(self, newType, newID, newName, newTopLevelSpaceID, newBotLat, newLeftLng, newTopLat, newRightLng):
        campus_collection = self.db['campus']
        buildingDict = {
            'type': newType,
            'id': newID,
            'name': newName,
            'topLevelSpaceId': newTopLevelSpaceID,
            'botLat': newBotLat,
            'leftLng': newLeftLng,
            'topLat': newTopLat,
            'rightLng': newRightLng
        }
        
        campus_collection.update_one({'id': newTopLevelSpaceID},{'$push': {'containedSpaces': buildingDict}})
