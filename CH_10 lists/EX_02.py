li = []

print("Enter 5 numbers: ")
for i in range(5):
    li.append(eval(input()))

for i in range(len(li)-1, -1, -1):
    print(li[i], end = " ")
