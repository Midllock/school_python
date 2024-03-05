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

#Tohle vypočítá obsah a obejm kruhu

kone= int(input("Zadejte počet koní: ")) #Zjistí počet koní
clovek = int(input("Zadejte počet lidi: "))#Zjistí počet lidí
ovci= int(input("Zadejte počet ovci: "))#Zjistí počet ovci
nohy = 0

print ("Dohromady mají", clovek*2 +ovci*4 + kone*4, "nohou")
#Toto nám vypíše končný počet nohou všech dohromady

kone= int(input("Zadejte počet koní: "))
clovek = int(input("Zadejte počet lidi: "))
ovci= int(input("Zadejte počet ovci: "))
nohy = 0

print ("Dohromady mají", clovek*2 +ovci*4 + kone*4, "nohou")
""""""""" 
def kalkulacka(): #tento kód je základní kalkulačka
    cislo1 = float(input("Zadej prvni cislo: "))
    cislo2 = float(input("Zadej druhe cislo: "))
    #zadání čísel
    
    operace = input("Zadej operaci (+, -, *, /): ")
    #zadání operace

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

print(kalkulacka())