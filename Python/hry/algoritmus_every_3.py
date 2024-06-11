y = 0
for i in range(0,800, 10):
    if i == 0 and not i == 800:
        y = y-1
        continue
    y = y + 1
    print(y)
    print(i,end=" ")