class BuildingsValidator:
    def __init__(self):
        pass
    
    def checkCampus(self, campusDict, documents):
        for campus in documents:
            if campusDict['id'] == campus['id']:
                print('ID already in use!')
                return False
            elif campusDict['name'] == campus['name']:
                print('Name already in use!')
                return False
            else:
                for containedSpace in campus['containedSpaces']:
                    if campusDict['id'] == containedSpace['id']:
                        print('ID already in use!')
                        return False
                    elif campusDict['name'] == containedSpace['name']:
                        print('Name already in use!')
                        return False
        return True

    def checkBuilding(self, buildingDict, documents):
        for campus in documents:
            if buildingDict['id'] == campus['id']:
                print('ID already in use!')
                return False
            elif buildingDict['name'] == campus['name']:
                print('Name already in use!')
                return
            else:
                for containedSpace in campus['containedSpaces']:
                    if buildingDict['id'] == containedSpace['id']:
                        print('ID already in use!')
                        return False
                    elif buildingDict['name'] == containedSpace['name']:
                        print('Name already in use!')
                        return False
                    elif (buildingDict['botLat'] == containedSpace['botLat'] and 
                            buildingDict['leftLng'] == containedSpace['leftLng'] and 
                            buildingDict['topLat'] == containedSpace['topLat'] and 
                            buildingDict['rightLng'] == containedSpace['rightLng']):
                        print('Latitudes and longitudes already in use!')
                        return False
        return True