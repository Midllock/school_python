#live = int(input("Kolik má životů:"))
#world = str(input("Jaký je slovo:"))
#x = str(input("Písmeno:"))
#slova = 0
y = str(input("Písmenko:"))
array= ["P","o","š","t","a"]
quit = False
def men():
    live = 10
    y = str(input("Písmenko:"))
    
    print(array)
    if y != array:
        live -= 1
        print (live)
    if live == 0:
        print("konec hry")
        print("Slovo bylo:"+ array)

while not quit:
    if y == "q":
        quit == True
    if y == "p":
        array[0]= "P"

        
print("\033c", end="") 
men()

