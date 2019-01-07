import pymongo

class TecnicoLogs():
    def __init__(self, collection):
        self.logs_collection = collection