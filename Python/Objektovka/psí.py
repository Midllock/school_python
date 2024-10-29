class Dog:

    def __init__(self):
        pass
        
    def bark(self):
        print("I generealy bark because I´m a general dog.")

    def eat(self):
        print("I generealy eat because I'am a general dog.")

    def run(self):
        print("I generealy run because I'am a general dog.")

class Bulldog(Dog):

    def bark(self):
        super().bark()
        print("Woof Woof, You´re dead hooman. Woof!!!")
    
    def eat(self):
        super().eat()
        print("I eat meat.")
    
    def run(self):
        super().run()
        print("I´m run fast.")

d = Dog()
d.bark()
d.eat()

d = Bulldog()
d.bark()
d.eat()