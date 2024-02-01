num = eval(input("Enter a four-digit integer: "))

print(num // 1000)

num %= 1000

print(num // 100)

num %= 100

print(num // 10)

num %= 10

print(num)
