import requests
import json
from campus import Campus
from building import Building

class ImportIST:
    def __init__(self):
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
            
    def __str__(self):
        for i in self.ist:
            i.__str__()
     
