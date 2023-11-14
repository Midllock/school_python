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
"""""""""

import math
player = [2,5]
enemy = [3,3]
a = (player[0]- enemy [0])
b = (player[1]- enemy [1])
c = math.sqrt(a**2 + b**2)
print(c)