class Point:
    x = 0
    y = 2

A = Point()
Point.x = 5
B = Point()
print(Point.x, A.x, B.x)
C = Point()
Point.x = 57
print(Point.x, B.x, C.x)