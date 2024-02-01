import random
import time

count = 0

start = time.time()
for i in range(10):
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)

    print(num1, " + ", num2, " = ", end = "")

    result = eval(input())

    if((num1 + num2) == result) :
        count += 1
end = time.time()

print("You got ", count, " correct from 10 in ", round((end - start) / 1000, 3), "s")
