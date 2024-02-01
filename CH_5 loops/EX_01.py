import sys

n = eval(input("Enter an integer, the input ends if it is 0: "))
if(n == 0):
    print("You didn't enter any number")
    sys.exit()
np = 0
nv =0
s = 0
count = 0

while(n != 0):
    if(n >= 0):
        np += 1
    else:
        nv += 1
    count += 1
    s += n
    n = eval(input("Enter an integer, the input ends if it is 0: "))

print("The number of positives is ", np)
print("The number of negatives is ", nv)
print("The total is ", s)
print("The average is ", s / count)
