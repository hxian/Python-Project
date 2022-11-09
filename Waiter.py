from Menu import Menu
from Diner import Diner


class Waiter(object):
    def __init__(self, menuObject):
        self.menu = menuObject
        self.diners = []

    def addDiner(self, diner):
        self.diners.append(diner)

    def getNumDiners(self):
        return len(self.diners)

    def printDinerStatuses(self):
        for status in Diner.STATUSES:
            print("Diners who are", status + ":")
            for diner in self.diners:
                if diner.getStatus() == status:
                    print("Diner", diner.name, "is currently", status + ".")

    def takeOrders(self):
        for diner in self.diners:
            if diner.getStatus() == "ordering":
                for typeOfItem in Menu.MENU_ITEM_TYPES:
                    self.menu.printMenuItemsByType(typeOfItem)
                    itemNum = input(diner.name + ", " + "please select a " + typeOfItem + " menu item number.")
                    while int(itemNum) not in range(0, self.menu.getNumMenuItemsByType(typeOfItem)) or \
                            not itemNum.isdigit():
                            itemNum = input()
                    diner.addToOrder(self.menu.getMenuItem(typeOfItem, int(itemNum)))

    def ringUpDiners(self):
        for diner in self.diners:
            if diner.getStatus() == "paying":
                mealCost = diner.calculateMealCost()
                print(diner.getName(), "your meal cost $", mealCost)

    def removeDoneDiners(self):
        for diner in self.diners:
            if diner.getStatus() == "leaving":
                print("Thank you for dining with us,", diner.getName() + ". Hope to see you again soon!")

        for i in range(len(self.diners)-1, -1, -1):
            if self.diners[i].getStatus() == "leaving":
                self.diners.remove(self.diners[i])

    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.diners:
            diner.updateStatus()






