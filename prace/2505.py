import random

array = [["❌", "❌", "❌", "❌", "❌"],
         ["❌", "❌", "❌", "❌", "❌"],
         ["❌", "❌", "❌", "❌", "❌"],
         ["❌", "❌", "❌", "❌", "❌"],
         ["❌", "❌", "❌", "❌", "❌"]]

miny = int(input("Kolik min: "))
quit_game = False

x = 0
y = 0
mina_x = 0
mina_y = 0
generate_point = []

mina_x = random.choice([0, 4])  # Náhodně vybere buď první nebo poslední pozici na ose x
mina_y = random.randint(1, 3)  # Náhodně vybere hodnotu mezi 1 a 3 pro osu y

math_logic = [
    [+1, +0],
    [-1, +0],
    [+0, -1],
    [+0, +1],
    [+1, +1],
    [-1, -1],
    [+1, -1],
    [-1, +1],
]


def generate_min():
    global mina_x, mina_y
    array[mina_x][mina_y] = "💣"

    while miny > 0:
        new_mina_x = random.randint(0, 4)
        new_mina_y = random.randint(0, 4)
        if array[new_mina_x][new_mina_y] == "❌" and (new_mina_x != x or new_mina_y != y):
            array[new_mina_x][new_mina_y] = "💣"
            miny -= 1

            for mine in math_logic:
                if array[new_mina_x + mine[0]][new_mina_y + mine[1]] == '❌':
                    array[new_mina_x + mine[0]][new_mina_y + mine[1]] = "🟨"
                elif array[new_mina_x + mine[0]][new_mina_y + mine[1]] == '🟨':
                    array[new_mina_x + mine[0]][new_mina_y + mine[1]] = "🟥"


generate_min()
while not quit_game:
    for radek in array:
        array[y][x] = "⭕"
        print("".join(radek))
    user_input = input("Zadej akci: ")
    if user_input == "q":
        quit_game = True
    elif user_input == "w" and y > 0:
        array[y][x] = "❌"
        y -= 1
    elif user_input == "a" and x > 0:
        array[y][x] = "❌"
        x -= 1
    elif user_input == "d" and x < 4:
        array[y][x] = "❌"
        x += 1
    elif user_input == "s" and y < 4:
        array[y][x] = "❌"
        y += 1
    if array[y][x] == "💣":
        print("Vybuchl jsi na mině!")
        break

    print("\033c", end="") 

