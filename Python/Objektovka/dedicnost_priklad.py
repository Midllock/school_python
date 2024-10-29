from abc import ABC, abstractmethod

class Animal(ABC):
    #abstraktní třída pro mnohoúhelník
    @abstractmethod
    def whoami(self):
        #abstraktní metoda pro počet stran mnohoúhelníka
        pass

class Giraffe (Animal):
    def whoami(self):
        print("I am a giraffe")

    def Giraffe(self):
        super().whoami()
        print("I am a giraffe")
    

g=Giraffe()
g.whoami()

