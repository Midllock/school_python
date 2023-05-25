import random
array = [["🥝","🥝", "🥝", "🥝","🥝"],
         ["🥝","🥝", "🥝", "🥝","🥝"], 
         ["🥝","🥝", "🥝", "🥝","🥝"], 
         ["🥝","🥝", "🥝", "🥝","🥝"],
         ["🥝","🥝", "🥝", "🥝","🥝"]]
quit = False 
x = 0
y = 0

#
generate_point = []
point_array= []
def generate_points():
    point_x = random.randint(0, 4) 
    point_y = random.randint(0, 4) 
    if array[point_x][point_y] != "🥩":
            array[point_x][point_y] = "🍔"

generate_point()

while quit == False:
    for radek in array:
        generate_point()
        array[y][x]= "🥩"
        print ("".join(radek))

    user_input = input("Zadej akci:") 
    if user_input == "q":
        quit = True #pokud se dá "q" zruší se kód

    if user_input == "w":
        if y > 0: #když se zadá "w" tak odečti -1, pokud ale je větší než 0 tak nic nedělej 
            array[y][x] = "🥝"  
            y -= 1 
    if user_input == "a":
        if x > 0:
            array [y][x] = "🥝"
            x -= 1
    
    if user_input == "d":
        if x < 4:
            array [y][x] = "🥝"
            x += 1 

    if user_input == "s":
        if y < 4:
            array [y][x] = "🥝"
            y += 1

    if array[y][x] == "🍔":
        generate_point()
    print("\033c", end="") 


    


