import requests
import json
import pymongo
from buildings_info import BuildingsInfo

class TecnicoBuildings:
    def __init__(self, collection, initialize):
        self.campus_collection = collection
        
        if initialize:
            print("No collection named 'campus, creating it...")

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
            
                    self.campus_collection.insert_one(campusDict)

    def addCampus(self, newType, newID, newName):
        #campus_collection = self.db['campus']
        campusDict = {
            'type': newType,
            'id': newID,
            'name': newName,
            'containedSpaces': []
        }
       
        self.campus_collection.insert_one(campusDict)

    def addBuilding(self, newType, newID, newName, newTopLevelSpaceID, newBotLat, newLeftLng, newTopLat, newRightLng):
        #campus_collection = self.db['campus']
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
        
        self.campus_collection.update_one({'id': newTopLevelSpaceID},{'$push': {'containedSpaces': buildingDict}})
