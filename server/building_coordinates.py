class BuildingCoordinates:
    def __init__(self):
        self.info = {}
        # Campus Tecnológico e Nuclear
        self.info["2448131392438"] = None
        # Campus Tagus
        self.info["2448131360898"] = None
         # Campus Alameada
        self.info["2448131360897"] = {}

        # Buildings in Alameda
        # Central
        self.info["2448131360897"]["2448131361060"] = {
            "lat": 38.736743,
            "lng": -9.139372,  
            "radius": 40 
        }
        # Torre Norte
        self.info["2448131360897"]["2448131361091"] = {
            "lat": 38.737582, 
            "lng": -9.138586,  
            "radius": 30 
        }

        # Torre Sul
        self.info["2448131360897"]["2448131361074"] = {
            "lat": 38.736000, 
            "lng": -9.138432,  
            "radius": 30 
        }

        # Civil
        self.info["2448131360897"]["2448131361042"] = {
            "lat": 38.737409,  
            "lng": -9.140284,  
            "radius": 50 
        }

        # Pavilhão de matemática
        self.info["2448131360897"]["2448131361119"] = {
            "lat": 38.735556,   
            "lng": -9.139992, 
            "radius": 20
        }

        # Complexo interdisciplinar
        self.info["2448131360897"]["2448131361035"] = {
            "lat": 38.736072,   
            "lng": -9.140174,  
            "radius": 20
        }

        # Pavilhão de mecanica III
        self.info["2448131360897"]["2448131361155"] = {
            "lat": 38.737377, 
            "lng": -9.137021,  
            "radius": 20
        }

        # Pavilhão informatica I
        self.info["2448131360897"]["2448131361133"] = {
            "lat": 38.737846, 
            "lng": -9.137653,  
            "radius": 20
        }
        
        # Associação de Estudantes
        self.info["2448131360897"]["2448131384238"] = {
            "lat": 38.736369,  
            "lng": -9.137113,  
            "radius": 20
        }
    
    def getInfo(self, campusID, buildingID):
        try:
            return self.info[campusID][buildingID]
        except:
            return None
        
    