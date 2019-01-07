import pymongo

class TecnicoUsers():
    def __init__(self, collection):
        self.users_collection = collection