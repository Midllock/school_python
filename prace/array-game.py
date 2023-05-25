import random
#Určení velikosti hracího pole
x = 5
y = 5

c= 0
v = 0
#Určení pozice hráče
position_y = 0
position_x = 0

#pozice místa 
position_c = 4
position_v = 3

#Funkce pro naplnění hracího pole
def fill_field(x, y, position_x, position_y):
    field = []
    while y > 0:
        row = []
        columns = x
        while columns > 0:
            row.append("o")
            columns -= 1
        field.append(row)
        y -= 1
        if y == 0:
            field[position_y][position_x] = "X"
    return field

def fill_fieldd(x, y, position_c, position_v):
    fieldd = []
    while v > 0:
        row = []
        columns = c
        while columns > 0:
            row.append("o")
            columns -= 1
        fieldd.append(row)
        v -= 1
        if v == 0:
            fieldd[position_c][position_v] = "y"
    return fieldd


#Funkce pro výpis hracího pole
def print_field(field, rows):
    n = 0
    while n < rows:
        print("".join(field[n]))
        n += 1

#Naplnění a výpis hracího pole
field = fill_field(x, y, position_x, position_y)
print_field(field, y)

fieldd = fill_fieldd(x, y, position_c, position_v)
print_fieldd(fieldd, v)

#Herní smyčka
while True:
    user_input = input("zadej akci: ")
    # if user_input == "q": 
    #     break
    # elif user_input == "d":
    #     field[position_y][position_x] = "o"
    #     field[position_y][position_x+1] = "X"
    #     position_x = position_x+1
    # elif user_input == "a":
    #     field[position_y][position_x] = "o"
    #     field[position_y][position_x-1] = "X"
    #     position_x = position_x-1
    # elif user_input == "w":
    #     field[position_y][position_x] = "o"
    #     field[position_y-1][position_x] = "X"
    #     position_y = position_y-1
    # elif user_input == "s":
    #     field[position_y][position_x] = "o"
    #     field[position_y+1][position_x] = "X"
    #     position_y = position_y+1
    # else:
    #     print("Zadej správný vstup")
    match user_input:
        case "q":
            break
        case "d":
            field[position_y][position_x] = "o"
            field[position_y][position_x+1] = "X"
            position_x = position_x+1
        case "a":
            field[position_y][position_x] = "o"
            field[position_y][position_x-1] = "X"
            position_x = position_x-1
        case "w":
            field[position_y][position_x] = "o"
            field[position_y-1][position_x] = "X"
            position_y = position_y-1
        case "s":
            field[position_y][position_x] = "o"
            field[position_y+1][position_x] = "X"
            position_y = position_y+1
        case _:
            print("Zadej správný vstup")
            continue
    print_field(field, y)
