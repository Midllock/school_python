import math

# Definice poloměru
polomer =int(input("Zadejte poloměr: "))

# Výpočet obvodu kruhu
obvod = 2 * math.pi * polomer
print("Obvod kruhu je:", obvod, "cm")

# Výpočet obsahu kruhu
obsah = math.pi * polomer ** 2
print("Obsah kruhu je:", obsah, "cm^2")