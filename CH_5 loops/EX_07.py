import math

print("Degree      Sin       Cos")
for i in range(0, 361, 10):
    if i == 0:
        print(i, "         ", round(math.sin(i), 4), "     ", round(math.cos(i), 4))
    else:
        print(i, "       ", round(math.sin(i), 4), "  ", round(math.cos(i), 4))
