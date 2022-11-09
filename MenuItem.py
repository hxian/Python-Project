class MenuItem(object):
    def __init__(self, name, typeOfItem, price, description):
        self.name = name
        self.type = typeOfItem
        self.price = price
        self.description = description

    def getName(self):
        return self.name

    def setName(self, newName):
        if newName.isalpha() and newName != "":
            self.name = newName
        else:
            print("Invalid name")

    def getType(self):
        return self.type

    def setType(self, newType):
        if newType.isalpha() and newType != "":
            self.type = newType
        else:
            print("Invalid type")

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        if isinstance(newPrice, float):
            self.price = newPrice
        else:
            print("Invalid price")

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        if newDescription != "":
            self.description = newDescription
        else:
            print("Invalid description")

    def __str__(self):
        msg = self.name + ": " + "$" + str(self.price) + "\n\t"
        msg += self.description
        return msg

    


