class Building:
    def __init__(self, newType, newID, newName, newTopLevelSpace, newLat, newLng, newRadius):
        self.type = newType
        self.id = newID
        self.name = newName
        self.topLevelSpace = newTopLevelSpace
        #lista ou dicionario indexados por ID?
        self.containedSpaces = []
        
        self.lat = newLat
        self.lng = newLng
        self.radius = newRadius
        

    def set(self, newType, newID, newName, newTopLevelSpace):
        self.type = type
        self.id = newID
        self.name = newName
        self.topLevelSpace = newTopLevelSpace

    def setCoordinates(self, newLat, newLng):
        self.lat = newLat
        self.lng = newLng
    
    def getCoordinates(self):
        return (self.lat ,self.lng)

    def getID(self):
        return self.id

    def setRadius(self, newRadius):
        self.radius = newRadius

    def getRadius(self):
        return self.radius

    def addContainedSpace(self, space):
        #falta verificar valores
        self.containedSpaces.append(space)

    def removeContainedSpace(self, space):
        self.containedSpaces.remove(space)

    def __str__(self):
        print("\tType: %s\n\tID: %d\n\tName: %s" % (self.type, self.id, self.name))
        print("\tCoordinates: %f, %f" % (self.lat, self.lng))
        print("\tRadius: %d" % (self.radius))
        print("\tTop level space: %s\n" % (self.topLevelSpace))