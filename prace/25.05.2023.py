import random 
array = [["❌", "❌", "❌","❌","❌"],
         ["❌", "❌", "❌","❌","❌"],
         ["❌", "❌", "❌","❌","❌"],
         ["❌", "❌", "❌","❌","❌"],
         ["❌", "❌", "❌","❌","❌"]]
miny = int(input("Kolik min: "))
quit = False 

x = 0 
y = 0
mina_x = 0
mina_y = 0
generate_point = []
bomb_x = random.randint(0, 4)
bomb_y = random.randint(0, 4)

def generate_min ():
    global mina_x, mina_y
    array[mina_x][mina_y] = "💣"
    while True:
        new_mina_x = random.randint(0, 4)
        new_mina_y = random.randint(0, 4)
        if array[new_mina_x][new_mina_y] == "❌" and (new_mina_x, new_mina_y != x, y):
           array[new_mina_x][new_mina_y] = "💣"
           mina_x, mina_y = new_mina_x, new_mina_y
           break
    
generate_min ()
while not quit:
    for radek in array:
        array[y][x] = "⭕"
        print("".join(radek))
    user_input = input("Zadej akci:")
    if user_input == "q":
        quit = True
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
        break



    print("\033c", end="") 

