import random

num1 = random.randrange(0, 100)
num2 = random.randrange(0, 100)

print(num1, " + ", num2, " = ", end = "")

result = eval(input())

if((num1 + num2) == result) :
    print("The answer is correct.")
else :
    print("The answer is wrong.")
