# tokens e coord em cache (noutro serviço) (memcache api)
# logs em sql
# pensar em larga escala
# "messages queus" e public subscribe 
# message q mais eficiente, redireciona para vários , pouco provavel replicação de dados, ja ta feito

#edificios, bots -> base dados
# utilizador mexe, write na base dados
# quero mandar mesnagem a um utilizador, base dados

# (token) xxxxxxxxxxxxxx -> istxxxxx

# HTML5 Geolocation

class User:
    def __init__(self, newID, newLat, newLng):
        self.id = newID
        self.lat = newLat
        self.lng = newLng
        self.building = None

    def update(self, newLat, newLng):
        self.lat = newLat
        self.lng = newLng
    
    def getID(self):
        return self.id

    def getBuilding(self):
        return self.building

    def setBuilding(self, newBuilding):
        self.building = newBuilding

    def getCoordinates(self):
        return (self.lat, self.lng)
