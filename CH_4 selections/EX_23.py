x, y = eval(input("Enter a point with two coordinates: "))

if(abs(x) > 10 / 2) or (abs(y) > 5 / 2):
    print("Point (", x, ", ", y, ") is not in the rectangle")
else:
    print("Point (", x, ", ", y, ") is in the rectangle")
