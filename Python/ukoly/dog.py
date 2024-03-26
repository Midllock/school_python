class Dog:
    def __init__(self, name):
        self.name = name
        print(f"Vytváříme objekt psa s jménem {self.name}") 

    def bark(self):
        print(f"{self.name} štěká!")
