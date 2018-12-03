class User:
    def __init__(self, newID, newLat, newLong):
        self.id = newID
        self.lat = newLat
        self.long = newLong

    def update(self, newLat, newLong):
        self.lat = newLat
        self.long = newLong
    
    def getID(self):
        return self.id

    def getCoordinates(self):
        return (self.lat, self.long)
