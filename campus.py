class Campus:
    def __init__(self, newType, newID, newName):
        self.type = newType
        self.id = newID
        self.name = newName
        #lista ou dicionario indexados por ID?
        self.containedSpaces = []
    
    def set(self, newType, newID, newName):
        self.type = newType
        self.id = newID
        self.name = newName

    def addContainedSpace(self, space):
        #falta verificar valores
        self.containedSpaces.append(space)

    def removeContainedSpace(self, space):
        self.containedSpaces.remove(space)
    
    def __str__(self):
        print("type: %s\nID: %d\nname: %s" % (self.type, self.id, self.name))
        
        print("containedSpaces:\n")
        for s in self.containedSpaces:
            s.__str__()

    