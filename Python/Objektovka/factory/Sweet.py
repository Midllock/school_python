class Sweet:
    pass

class Pralines(Sweet):
    def __init__(self, type_of):
        self.__kind_of = "Pralines"
        self.__type_of = type_of

    def getTypeOf(self):
        return self.__type_of
    
    def getKindOf(self):
        return self.__kind_of
    
class Truffles(Sweet):
    def __init__(self, type_of):
        self.__kind_of = "Truffles"
        self.__type_of = type_of

    def getTypeOf(self):
        return self.__type_of
    
    def getKindOf(self):
        return self.__kind_of
    
class Chocolate(Sweet):
    def __init__(self, type_of):
        self.__kind_of = "Chocolate"
        self.__type_of = type_of

    def getTypeOf(self):
        return self.__type_of
    
    def getKindOf(self):
        return self.__kind_of

class Factory:
    def __init__(self):
        self.__sweets = []

    def showProducts(self):
        print(f"{self.__sweets}")

    def showDetails(self):
        for s in self.__sweets:
            print(f"{s.getKindOf()} {s.getTypeOf()}")

    def make (self, kind_of, type_of, amount=1):
        if kind_of == "Pralines":
            for i in range(0, amount):
                self.__sweets.append(Pralines(type_of))
        elif kind_of == "Truffles":
            for i in range(0, amount):
                self.__sweets.append(Truffles(type_of))
        elif kind_of == "Chocolate":
            for i in range(0, amount):
                self.__sweets.append(Chocolate(type_of))

sweets=Factory()
sweets.make("Pralines", "chocolate", 3)
sweets.make("Truffles", "nougat")
sweets.make("Chocolate", "salted caramel", 6)
rum = Pralines("rum")
sweets.showProducts()
sweets.showDetails()
print(rum)