s, gr = eval(input("Enter the subtotal and a gratuity rate: "))

g = (gr * 0.01) * s

print("The gratuity is ", round(g, 2), " and the total is ", round(g + s, 2))
