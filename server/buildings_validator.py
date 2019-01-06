class BuildingsValidator:
    def __init__(self):
        pass
    
    def checkCampus(self, campusDict, documents):
        keys = list(campusDict.keys())
        args_list = ['type', 'id', 'name', 'containedSpaces']

        for value in args_list:
            if value in keys:
                pass
            else: 
                return False

        for campus in documents:
            if campusDict['id'] == campus['id']:
                return False
            elif campusDict['name'] == campus['name']:
                return False
            else:
                for containedSpace in campus['containedSpaces']:
                    if campusDict['id'] == containedSpace['id']:
                        return False
                    elif campusDict['name'] == containedSpace['name']:
                        return False
        return True

    def checkBuilding(self, buildingDict, documents):
        keys = list(buildingDict.keys())
        args_list = ['type', 'id', 'name', 'topLevelSpaceId', 'botLat', 'leftLng', 'topLat', 'rightLng']

        for value in args_list:
            if value in keys:
                pass
            else: 
                return False

        for campus in documents:
            if buildingDict['topLevelSpaceId'] != campus['id']:
                return False
            if buildingDict['id'] == campus['id']:
                return False
            elif buildingDict['name'] == campus['name']:
                return False
            else:
                for containedSpace in campus['containedSpaces']:
                    if buildingDict['id'] == containedSpace['id']:
                        return False
                    elif buildingDict['name'] == containedSpace['name']:
                        return False
                    elif (buildingDict['botLat'] == containedSpace['botLat'] and 
                            buildingDict['leftLng'] == containedSpace['leftLng'] and 
                            buildingDict['topLat'] == containedSpace['topLat'] and 
                            buildingDict['rightLng'] == containedSpace['rightLng']):
                        return False
                    elif(abs(buildingDict['botLat']) > 90 or
                            abs(buildingDict['leftLng']) > 180 or
                            abs(buildingDict['topLat']) > 90 or
                            abs(buildingDict['rightLng']) > 180):
                        return False 
        return True