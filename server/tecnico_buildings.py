import requests
import json
import pickle
from campus import Campus
from building import Building
from buildings_info import BuildingsInfo

'''import pymongo

client = pymongo.MongoClient("mongodb+srv://asint:asint@asint-3tsob.gcp.mongodb.net/test?retryWrites=true")

db = client["Test"]
collections = db["Campus"]
collections.insert_one({
    "name": "alameda"
})'''



class TecnicoBuildings:
    def __init__(self, name):
        self.name = name

        try:
            f = open('dump_' + name, 'rb')
            self.tecnico  = pickle.load(f)
            f.close()

        except IOError:
            self.tecnico = {}

            url = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces/"
            response = requests.get(url)
            campus = response.json()

            info = BuildingsInfo()

            for c in campus:
                if info.getCampus(c['id']):
                    newUrl = url + c['id']
                    response = requests.get(newUrl)
                    campusInfo = response.json()
                                        
                    campusObj = Campus(c['type'], int(c['id']), c['name'])

                    buildings = campusInfo['containedSpaces']
                    
                    for b in buildings:
                        b_info = info.getBuilding(b['id'])

                        if b_info:
                            buildingObj = Building(b['type'], int(b['id']), b['name'], int(c['id']))
                            buildingObj.setCoordinates(float(b_info['botLat']), float(b_info['leftLng']), float(b_info['topLat']), float(b_info['rightLng']))
                            campusObj.addContainedSpace(buildingObj)

                    self.tecnico[c['name']] = campusObj

            f = open('dump_' + self.name, 'wb')
            pickle.dump(self.tecnico, f)
            f.close()
           

    def showBuildings(self):
        for campus_name, campus_obj in self.tecnico.items():
            campus_obj.__str__()