num = eval(input("Enter a number between 0 and 1000: "))
sum = 0

sum += num % 10
num = num // 10

sum += num % 10
num = num // 10

sum += num % 10
num = num // 10

print("The sum of the digits is ", sum)
