x, y, z = eval(input("Enter three integers: "))

m = min(x, y, z)

if(m == x):
    if y >= z:
        print(m, " ", z, " ", y)
    else:
        print(m, " ", y, " ", z)
elif (m == y):
    if x >= z:
        print(m, " ", z, " ", x)
    else:
        print(m, " ", x, " ", z)
elif (m == z):
    if x >= y:
        print(m, " ", y, " ", x)
    else:
        print(m, " ", x, " ", y)
    
