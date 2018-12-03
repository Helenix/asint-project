import requests
import json
import pickle
from campus import Campus
from building import Building

# falta coordenadas
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
                    sType = space["type"]
                    sID = int(space["id"])
                    sName =space["name"]
                    sTopLevelSpace = space["topLevelSpace"]
                    buildingObj = Building(sType, sID, sName, sTopLevelSpace)
                    campusObj.addContainedSpace(buildingObj)

                self.ist.append(campusObj)

            f = open('dump_' + self.name, 'wb')
            pickle.dump(self.ist, f)
            f.close()
            
    def __str__(self):
        for i in self.ist:
            i.__str__()
     
