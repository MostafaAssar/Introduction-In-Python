print("Miles       Kilometers")
for i in range(1, 11):
    if i % 10 != 0:
        print(i, "         ", round(i * 1.609, 2))
    else :
        print(i, "        ", round(i * 1.609, 2))
    
