from tecnico_buildings import TecnicoBuildings
from db_connector import DB_Conector
import pickle

db = DB_Conector('asint')
db.addBuilding({
    'type': 'CAMPUS', 
    'id':8, 
    'name': 'novoo',
    'topLevelSpaceId': 2,
    'botLat': 0,
    'leftLng': 1,
    'topLat': 2,
    'rightLng': 0
    })

'''db.addCampus({
    'type': 'CAMPUS', 
    'id':10, 
    'name': 'novo2',
    'containedSpaces': []
    })'''

#db.deleteSpace(2)
#tecnico.addCampus('CAMPUS', 1, 'Novo Campus')
#tecnico.addBuilding('BUILDING', 2, 'Novo Building', 1, 0, 0, 0, 0)

