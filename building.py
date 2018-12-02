class Building:
    def __init__(self, newType, newID, newName, newTopLevelSpace):
        self.type = newType
        self.id = newID
        self.name = newName
        self.topLevelSpace = newTopLevelSpace
        #lista ou dicionario indexados por ID?
        self.containedSpaces = []

    def set(self, newType, newID, newName, newTopLevelSpace):
        self.type = type
        self.id = newID
        self.name = newName
        self.topLevelSpace = newTopLevelSpace

    def addContainedSpace(self, space):
        #falta verificar valores
        self.containedSpaces.append(space)

    def removeContainedSpace(self, space):
        self.containedSpaces.remove(space)

    def __str__(self):
        print("\ttype: %s\n\tID: %d\n\tname: %s\n\ttopLevel: %s\n"%(self.type, self.id, self.name, self.topLevelSpace))
        