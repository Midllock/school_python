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
----------------------------- #otevření souborů
# Otevření souboru 
message.txtwith open("message.txt", "r") as file:
    plaintext = file.read()
    
# Caesarova šifra
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():  
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.isnumeric():
            result += chr((ord(char) - 48 + shift) % 10 + 48)
        else:            
            result += char    
    return result

ciphertext = caesar_cipher(plaintext, 3)

# Uložení zašifrované zprávy do souboru message_.txtwith 
open("message_.txt", "w") as file:
    file.write(ciphertext)
----------------#otevření souboru json, a přečtení
import json
with open("grid.json", "r") as file:
    grid = json.load(file)

print(grid)
------------------

"""""""""

