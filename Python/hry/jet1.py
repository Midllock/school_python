# Toto je mini hra která se ovládá wasd + q. Tato minihraje je založená na tom aby jsi dosáhl 100 bodů (skore). Po tom se hra ukončí. 
import random

array = [["🥝","🥝", "🥝", "🥝","🥝","🥝","🥝", "🥝", "🥝","🥝"],
         ["🥝","🥝", "🥝", "🥝","🥝","🥝","🥝", "🥝", "🥝","🥝"], 
         ["🥝","🥝", "🥝", "🥝","🥝","🥝","🥝", "🥝", "🥝","🥝"], 
         ["🥝","🥝", "🥝", "🥝","🥝","🥝","🥝", "🥝", "🥝","🥝"],
         ["🥝","🥝", "🥝", "🥝","🥝","🥝","🥝", "🥝", "🥝","🥝"]]

quit = False 
x = 0
y = 0
burger_x = random.randint(0, 9)
burger_y = random.randint(0, 9)
while burger_x == x and burger_y == y:
    burger_x = random.randint(0, 9)
    burger_y = random.randint(0, 9)
array[burger_x][burger_y] = "🍔"
score = 0

def generate_burger():
    global burger_x, burger_y
    array[burger_x][burger_y] = "🥝"
    while True:
        new_burger_x = random.randint(0, 9)
        new_burger_y = random.randint(0, 9)
        if array[new_burger_x][new_burger_y] == "🥝" and (new_burger_x != x or new_burger_y != y):
            array[new_burger_x][new_burger_y] = "🍔"
            burger_x, burger_y = new_burger_x, new_burger_y
            break

while not quit:
    for radek in array:
        array[y][x] = "🥩"
        print("".join(radek))
    print(f"Skore: {score}")
    user_input = input("Zadej akci:")
    
    if user_input == "q":
        quit = True
    elif user_input == "w" and y > 0:
        array[y][x] = "🥝"
        y -= 1
    elif user_input == "a" and x > 0:
        array[y][x] = "🥝"
        x -= 1
    elif user_input == "d" and x < 9:
        array[y][x] = "🥝"
        x += 1
    elif user_input == "s" and y < 9:
        array[y][x] = "🥝"
        y += 1

    if array[y][x] == "🍔":
        score += 1
        generate_burger()
        if score == 101:
            break

    print("\033c", end="")
