import math

class Kruznice:
    def __init__(self, r):
        self.r = r

    def ma_obvod(self):
        return 2 * math.pi * self.r

    def ma_obsah(self):
        return math.pi * self.r ** 2

    def __str__(self):
        obvod = self.ma_obvod()
        obsah = self.ma_obsah()
        return f"Kružnice o poloměru {self.r} má obvod {obvod} a obsah {obsah}."

r = float(input("Zadejte poloměr kružnice: "))
k = Kruznice(r)
print(k)