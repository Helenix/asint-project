from tecnico_buildings import TecnicoBuildings
import pickle

tecnico = TecnicoBuildings("ist")
tecnico.showBuildings()

#serialized_data = tecnico.getTecnico()
#original_data = pickle.loads(serialized_data)

#original_data['Alameda'].__str__()
