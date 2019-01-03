class Building:
    def __init__(self, newType, newID, newName, newTopLevelSpaceID):
        self.type = newType
        self.id = newID
        self.name = newName
        self.topLevelSpaceID = newTopLevelSpaceID

    def set(self, newType, newID, newName, newTopLevelSpaceID):
        self.type = newType
        self.id = newID
        self.name = newName
        self.topLevelSpaceID = newTopLevelSpaceID

    def setCoordinates(self, newBotLat, newLeftLng, newTopLat, newRightLng):
        self.botLat = newBotLat
        self.leftLng = newLeftLng
        self.topLat = newTopLat
        self.rightLng = newRightLng


    def __str__(self):
        print("\tType: %s" %(self.type))
        print("\tID: %d" %(self.id))
        print("\tName: %s" %(self.name))
        print("\tTop Level Space ID: %d" %(self.topLevelSpaceID))
        print("\tCoordinates:")
        print("\t    -Bottom latitude: %f" %(self.botLat))
        print("\t    -Left longitude: %f" %(self.leftLng))
        print("\t    -Top latitude: %f" %(self.topLat))
        print("\t    -Right longitude: %f" %(self.rightLng))
        print("")
        