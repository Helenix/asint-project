import requests
import json
import pickle
from campus import Campus
from building import Building
from building_coordinates import BuildingCoordinates

class ISTdb:
    def __init__(self, name):
        self.name = name

        try:
            f = open('dump_' + name, 'rb')
            self.ist  = pickle.load(f)
            f.close()

        except IOError:
            self.ist = []

            url = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces/"
            response = requests.get(url)
            istCampus = response.json()

            buildingsInfo = BuildingCoordinates()

            for c in istCampus:
                newUrl = url + c["id"]
                response = requests.get(newUrl)
                
                campus = response.json()
                cType = campus["type"]
                cID = int(campus["id"])
                cName = campus["name"]
                cContainedSpaces = campus["containedSpaces"]

                campusObj = Campus(cType, cID, cName)

                for space in cContainedSpaces:
                    info = buildingsInfo.getInfo(campus["id"], space["id"])

                    if info:
                        sType = space["type"]
                        sID = int(space["id"])
                        sName = space["name"]
                        sTopLevelSpace = space["topLevelSpace"]
                        sLat = info["lat"]
                        sLng = info["lng"]
                        sRadius = info["radius"]
                        buildingObj = Building(sType, sID, sName, sTopLevelSpace, sLat, sLng, sRadius)
                        
                        campusObj.addContainedSpace(buildingObj)

                self.ist.append(campusObj)

            f = open('dump_' + self.name, 'wb')
            pickle.dump(self.ist, f)
            f.close()

    def getDB(self):
            return self.ist
            
    def __str__(self):
        for i in self.ist:
            i.__str__()
     
