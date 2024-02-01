m = eval(input("Enter the number of minutes: "))

y = m / 525600;
d = (m % 525600) / 1440;

print(m, " minutes is approximately ", int(y), " years and ", int(d), " days")
