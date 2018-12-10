from istdb import ISTdb
from calculator import Calculator
from user import User

tecnico = ISTdb("ISTdb")
db = tecnico.getDB()

user = User(1, 38.736983, -9.139386)

nearestBuilding = {
    "buildingID": None,
    "distance": None
}

for campus in db:
    for space in campus.containedSpaces:
        point1 = user.getCoordinates()
        point2 = space.getCoordinates()

        distance = Calculator.findDistance(point1, point2)
        if nearestBuilding["distance"] == None or distance < nearestBuilding["distance"]:
            nearestBuilding["buildingID"] = space.getID()
            nearestBuilding["distance"] = distance

            # Nao pode estar aqui, so depois de calular todos eq se verifica
            if nearestBuilding["distance"] < space.getRadius():
                user.setBuilding(space)


print("Nearest Building ID: %d Distance %f\n" % (nearestBuilding["buildingID"], nearestBuilding["distance"]))
build = user.getBuilding()
if build:
    print("User inside building: ")
    build.__str__()
