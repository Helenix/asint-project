from tecnico_buildings import TecnicoBuildings
from db_connector import DB_Conector
import pickle
from pymemcache.client import base
import requests

url = "http://127.0.0.1:5000/api"
headers = {
    'Authorization':'Basic ' + 'token_test'
}

response = requests.get(url, headers = headers)

print(response.json())

'''db = DB_Conector('asint')

client = base.Client(('localhost',11211))

client.set('admin', '12345')

result_bytes = client.get('admin')
result_original = result_bytes.decode('utf-8')

print(result_original)

client.set('admin', '6789')

result_bytes = client.get('admin')
result_original = result_bytes.decode('utf-8')

print(result_original)

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

db.addCampus({
    'type': 'CAMPUS', 
    'id': 10, 
    'name': 'novo2',
    'containedSpaces': []
    })'''

#db.deleteSpace(2)

