class Campus:
    def __init__(self, newType, newID, newName):
        self.type = newType
        self.id = newID
        self.name = newName
        self.containedSpaces = []
    
    def set(self, newType, newID, newName):
        self.type = newType
        self.id = newID
        self.name = newName

    def addContainedSpace(self, building):
        self.containedSpaces.append(building)

    def __str__(self):
        print("Type: %s" %(self.type))
        print("ID: %d" %(self.id))
        print("Name: %s" %(self.name))
        
        if self.containedSpaces:
            print("Contained spaces:")
            for s in self.containedSpaces:
                s.__str__()
       

    