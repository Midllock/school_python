# Toto je mini hra která se ovládá wasd + q. Tato minihraje je založená na tom aby jsi dosáhl 100 bodů (skore). Po tom se hra ukončí. 
import random

array = [["🥝","🥝", "🥝", "🥝","🥝"],
         ["🥝","🥝", "🥝", "🥝","🥝"], 
         ["🥝","🥝", "🥝", "🥝","🥝"], 
         ["🥝","🥝", "🥝", "🥝","🥝"],
         ["🥝","🥝", "🥝", "🥝","🥝"]]

quit = False 
x = 0
y = 0
burger_x = random.randint(0, 4)
burger_y = random.randint(0, 4)

while burger_x == x and burger_y == y:
    burger_x = random.randint(0, 4)
    burger_y = random.randint(0, 4)

array[burger_x][burger_y] = "🍔"
score = 0
Button =0
def generate_burger():
    global burger_x, burger_y
    array[burger_x][burger_y] = "🥝"
    while True:
        new_burger_x = random.randint(0, 4)
        new_burger_y = random.randint(0, 4)
        if array[new_burger_x][new_burger_y] == "🥝" and (new_burger_x, new_burger_y != x, y) and array[new_burger_x][new_burger_y] != "🍔":
            array[new_burger_x][new_burger_y] = "🍔"
            burger_x, burger_y = new_burger_x, new_burger_y
            break

while not quit:
    for radek in array:
        array[y][x] = "🥩"
        print("".join(radek))
    print(f"Přesunutí: {Button} ")
    print(f"Score: {score}")
    user_input = input("Zadej akci:")
    if user_input == "q":
        quit = True
    elif user_input == "w" and y > 0:
        Button += 1
        array[y][x] = "🥝"
        y -= 1
    elif user_input == "a" and x > 0:
        Button += 1
        array[y][x] = "🥝"
        x -= 1
    elif user_input == "d" and x < 4:
        Button += 1
        array[y][x] = "🥝"
        x += 1
    elif user_input == "s" and y < 4:
        Button += 1
        array[y][x] = "🥝"
        y += 1
    if Button == 11 and score == 0:
        print("Zemřel jsem na hlad ty študente!")
        break
    elif Button == 21 and score == 1:
        print("Zemřel jsem na hlad ty študente!")
        break
    elif Button == 31 and score == 2:
        print("Zemřel jsem na hlad ty študente!")
        break
    elif Button == 41 and score == 3:
        print("Zemřel jsem na hlad ty študente!")
        break
    elif Button == 51 and score == 4:
        print("Zemřel jsem na hlad ty študente!")
        break
    if array[y][x] == "🍔":
        score += 1
        generate_burger()
        if score == 101:
            break

    print("\033c", end="")
