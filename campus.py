class Campus:
    def __init__(self, type, id, name):
        self.type = type
        self.id = id
        self.name = name
        #lista ou dicionario indexados por ID?
        self.containedSpaces = []
    
    def set(self, type, id, name):
        self.type = type
        self.id = id
        self.name = name

    def addContainedSpace(self, space):
        #falta verificar valores
        self.containedSpaces.append(space)

    def removeContainedSpace(self, space):
        self.containedSpaces.remove(space)
    