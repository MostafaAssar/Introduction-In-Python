import math

x, y = eval(input("Enter a point with two coordinates: "))

if (math.sqrt((x ** 2) + (y ** 2))) <= 10:
    print("Point (", x, ", ", y, ") is in the circle")
else:
    print("Point (", x, ", ", y, ") is not in the circle")
