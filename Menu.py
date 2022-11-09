from MenuItem import MenuItem


class Menu(object):
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    def __init__(self, fileName):
        self.menuItemDictionary = {}
        fileIn = open(fileName, "r")
        for line in fileIn:
            line = line.strip()
            lineList = line.split(",")
            item = MenuItem(lineList[0], lineList[1], float(lineList[2]), lineList[3])
            if lineList[1] in self.menuItemDictionary:
                self.menuItemDictionary[lineList[1]].append(item)
            else:
                self.menuItemDictionary[lineList[1]] = [item]
        fileIn.close()

    def getMenuItem(self, typeOfItem, index):
        if typeOfItem.capitalize() in Menu.MENU_ITEM_TYPES and str(index).isdigit():
            return self.menuItemDictionary[typeOfItem][index]
        else:
            print("Invalid type or index")

    def printMenuItemsByType(self, typeOfItem):
        num = 0
        print("-----", typeOfItem.upper(), "-----")
        for item in self.menuItemDictionary[typeOfItem]:
            print(str(num) + ") ", item)
            num += 1

    def getNumMenuItemsByType(self, typeOfItem):
        return len(self.menuItemDictionary[typeOfItem])

