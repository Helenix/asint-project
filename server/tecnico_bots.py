from bots_validator import BotsValidator

import pymongo

class TecnicoBots():
    def __init__(self, collection):
        self.bots_collection = collection
        self.validator = BotsValidator() 

    def addBot(self, botDict):
        if self.validator.checkBot(botDict):
            results = self.bots_collection.count_documents({'$or': [{'acc_name': botDict['acc_name']},{'acc_building_id': botDict['acc_building_id']}]})
        
            if results == 0:
                self.bots_collection.insert(botDict)
                return True
            return False
        else:
            return False

    def deleteBot(self, botID):
        pass