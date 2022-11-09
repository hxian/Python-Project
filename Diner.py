from MenuItem import MenuItem

class Diner(object):
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    def __init__(self, dinerName):
        self.name = dinerName
        self.order = []
        self.status = 0

    def getName(self):
        return self.name

    def setName(self, newName):
        if newName.isalpha() and newName != "":
            self.name = newName
        else:
            print("Invalid name")

    def getOrder(self):
        return self.order

    def setOrder(self, newOrder):
        if isinstance(newOrder, list):
            self.order = newOrder
        else:
            print("Invalid order list")

    def getStatus(self):
        return Diner.STATUSES[self.status]

    def setStatus(self, newStatus):
        if isinstance(newStatus, int) and newStatus in range(5):
            self.status = newStatus
        else:
            print("Invalid new status")

    def updateStatus(self):
        self.status += 1

    def addToOrder(self, item):
        self.order.append(item)

    def printOrder(self):
        print(self.name, "ordered:")
        for item in self.order:
            print("-", item)

    def calculateMealCost(self):
        mealCost = 0
        for item in self.order:
            mealCost += item.getPrice()
        return mealCost

    def __str__(self):
        msg = "Diner " + self.name + " is currently " + Diner.STATUSES[self.status] + "."
        return msg