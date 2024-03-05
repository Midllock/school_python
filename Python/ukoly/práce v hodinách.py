"""""""""
import math

# Definice poloměru
polomer =int(input("Zadejte poloměr: "))

# Výpočet obvodu kruhu
obvod = 2 * math.pi * polomer
print("Obvod kruhu je:", obvod, "cm")

# Výpočet obsahu kruhu
obsah = math.pi * polomer ** 2
print("Obsah kruhu je:", obsah, "cm^2")

-----------------------------------
kone= int(input("Zadejte počet koní: "))
clovek = int(input("Zadejte počet lidi: "))
ovci= int(input("Zadejte počet ovci: "))
nohy = 0

print ("Dohromady mají", clovek*2 +ovci*4 + kone*4, "nohou")

def kalkulacka():
    cislo1 = float(input("Zadej prvni cislo: "))
    cislo2 = float(input("Zadej druhe cislo: "))
    
    operace = input("Zadej operaci (+, -, *, /): ")
    
    if operace == '+':
        vysledek = cislo1 + cislo2
    elif operace == '-':
        vysledek = cislo1 - cislo2
    elif operace == '*':
        vysledek = cislo1 * cislo2
    elif operace == '/':
        if cislo2 != 0:
            vysledek = cislo1 / cislo2
        else:
            vysledek = "Nelze dělit nulou"
    else:
        vysledek = "Neplatná operace"
    
    print("Výsledek:", vysledek)

kalkulacka()
"""""""""
with open("mess.txt", "r") as file:
    text = file.read()
print(text)