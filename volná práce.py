""""""""" #14.11 2023
numbers = [4,5,3,7,8,2,1,6]
sum = 0
for n in numbers:
    sum += n


print ("Suma je ", sum)
print ("počet je", len(numbers))
print  ("Průměr je", sum/len(numbers)) #aritme

--------------------------------------------

numbers = (4,5,3,7,8,2,1,6)
cnt= 0
for n in numbers:
    if n % 2 == 0:
        cnt += 1
print ("pocet =", cnt) #sudý
--------------------------------------------
numbers = (4,5,3,7,8,2,1,6) 
cnt= 0
for n in numbers:
    if n % 2:
        cnt += 1
print ("pocet =", cnt) #lichý
--------------------------------------------
numbers = [4,5,3,7,8,2,1,6]
for i in range (len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(numbers)
--------------------------------------------
n = 7
for i in range (1, 11):
    print(i, "x", n, "=", i * n)
--------------------------------------------
import math
player = [2,5]
enemy = [3,3]
a = (player[0]- enemy [0])
b = (player[1]- enemy [1])
c = math.sqrt(a**2 + b**2)
print(c)
--------------------------------------------
znamky = [[3, 1], [3, 2], [3, 1], [10, 3], [4, 4]]

celkova_vaha = 0
vazeny_prumer_citatel = 0

for znamka in znamky:
    celkova_vaha += znamka[0]
    vazeny_prumer_citatel += znamka[0] * znamka[1] 

vazeny_prumer = vazeny_prumer_citatel / celkova_vaha

nevažený_průměr = sum(znamka[1] for znamka in znamky) /len(znamky)

rozdil = vazeny_prumer - nevažený_průměr

print(f"Celkový vážený průměr: {vazeny_prumer}")
print(f"Celkový nevážený průměr: {nevažený_průměr}")
print(f"Rozdíl mezi průměry: {rozdil}")
import random
--------------------------------------------
w, h, mines = 8, 2, 2

field = [[0 for y in range(h)]for y in range(w)]


#put mine
rx = random.randint(0,w - 1)
ry = random.randint(0, h -1)
--------------------------------------------
for y in range(h):
    for x in range(w):
        print(field[x][0], end="")
    print()
def list_swap(list,old_num, new_num):

    for x in range(len(list)):
        if list[x] == old_num:
            list[x] = new_num
    return(list)

print(list_swap([2,5,8,6,2,4,7,2], 5,0))
--------------------------------------------
name = input("Jméno:")
if name[-1] == "k":
    print("True")
else:
    print("False")

def card_hide(card):
    return 12* "*" + card[12:]

print(card_hide("1565411565415321"))
--------------------------------------------
x = float(input("Váha:"))
y = float(input("Výška:"))

z = x / (y / 100 * 2) 
if z < 18.4:
    print("Velká podváha")
elif z < 19.9:
    print("Podváha")
elif z < 24.9:
    print("Normální")
elif z < 29.9:
    print ("Nadváha")
elif z < 34.9:
    print ("Obezita 1. stupeň")
elif z < 39.9:
    print ("Obezita 2. stupeň")
elif z > 39.9:
    print ("obezita 3. stupně")

print(z)
-------------------------------------------- #19.12
def zahada(x):
    return x//2

a = zahada(8)
b = zahada(6)
print(a+b)
------
def test(x,y,z):
    print(y)

test(1,2,3)

i = 1
    while i <= h * 2:
        print("A"*i)
        i += 2

        def triangl_1(h):
    for i in range(1, h + 1):
        print(" "*(h-i), "A"* (i*2 -1))

triangl_1 (40)
--------------------------------------------
def triangl_1(h):
    for i in range(1, h + 1):
        print(" "*(2*((h-i))), "000 "* (i*2 -1))
triangl_1 (8)
--------------------------------------------
import math

def o(r):

    print(round(2*math.pi*r, 0))
    r += 1
    print(round(2*math.pi*r, 0))
    return 
print(o(6378e3))
--------------------------------------------
def money(days, initial_money): #počítání peněz
    den = 0 
    while den < days:
        print(den ,initial_money, "Kč")
        den += 1
        initial_money = initial_money * 2
    
    return den ,initial_money

print( money(29, 0.01), "kč")
--------------------------------------------
def najdi_pocet_lidi_a_koni(celkovy_pocet_hlav, celkovy_pocet_nohou):
    lidi = 0

    while True:
        koni = celkovy_pocet_hlav - lidi
        pocet_nohou = 2 * lidi + 4 * koni

        if pocet_nohou == celkovy_pocet_nohou:
            return lidi, koni

        lidi += 1

# Zadání
celkovy_pocet_hlav = 22
celkovy_pocet_nohou = 72

# Hledání řešení
pocet_lidi, pocet_koni = najdi_pocet_lidi_a_koni(celkovy_pocet_hlav, celkovy_pocet_nohou)
pocet_nohou = pocet_lidi*2 + pocet_koni*4
# Výsledky
print(f"Počet lidí: {pocet_lidi}")
print(f"Počet koní: {pocet_koni}")
print(f"Počet nohou: {pocet_nohou}")
--------------------------------------------
import math #pithágorova věta
player = [2,5]
enemy = [3,3]
a = (player[0]- enemy [0])
b = (player[1]- enemy [1])
c = math.sqrt(a**2 + b**2)
print(c) 
--------------------------------------------
"""""""""