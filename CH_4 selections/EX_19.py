x, y ,z = eval(input("Enter three edges: "))

if((x + y) < z) or ((x + z) < y) or ((z + y) < x):
    print("The input is invalid")
else:
    print("The perimeter is ", x + y + z)
