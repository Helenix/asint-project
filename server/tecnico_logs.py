import pymongo
from logs_validador import LogsValidator

class TecnicoLogs():
    def __init__(self, collection):
        self.logs_collection = collection
        self.validator = LogsValidator()

    def addLog(self, logDict):
        if self.validator.checkLog(logDict):
            self.logs_collection.insert_one(logDict)
            return True
        return False

    def getLogs(self, user_id):
        pass
        