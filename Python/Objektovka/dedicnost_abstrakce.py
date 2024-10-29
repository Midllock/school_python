from abc import ABC, abstractmethod

class Polygon(ABC):
    #abstraktní třída pro mnohoúhelník
    @abstractmethod
    def numsides(self):
        #abstraktní metoda pro počet stran mnohoúhelníka
        pass

class Triangle(Polygon):

    def numsides(self):
        print("I have 3 sides")
class Pentagon (Polygon):
    def numsides(self):
        print("I have 5 sides")


class Octagon (Polygon):
    def numsides(self):
        print("I have 8 sides")

t = Triangle()
t.numsides()

t = Pentagon()
t.numsides()

t = Octagon()
t.numsides()