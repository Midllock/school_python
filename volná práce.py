""""""""" #14.11 2023
numbers = [4,5,3,7,8,2,1,6]
sum = 0
for n in numbers:
    sum += n


print ("Suma je ", sum)
print ("počet je", len(numbers))
print  ("Průměr je", sum/len(numbers)) #aritme

,

numbers = (4,5,3,7,8,2,1,6)
cnt= 0
for n in numbers:
    if n % 2 == 0:
        cnt += 1
print ("pocet =", cnt) #sudý

numbers = (4,5,3,7,8,2,1,6) 
cnt= 0
for n in numbers:
    if n % 2:
        cnt += 1
print ("pocet =", cnt) #lichý

numbers = [4,5,3,7,8,2,1,6]
for i in range (len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(numbers)

numbers = [4,5,3,7,8,2,1,6]
for i in range (len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(numbers)

n = 7
for i in range (1, 11):
    print(i, "x", n, "=", i * n)

import math
player = [2,5]
enemy = [3,3]
a = (player[0]- enemy [0])
b = (player[1]- enemy [1])
c = math.sqrt(a**2 + b**2)
print(c)
"""""""""

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
