x = float(input("Enter the value of x: "))
if x > 1:
    print("x is greater than 1")
    y = 3 * x + 1
elif x == 1:
    print("x is equal to 1")
    y = x + 2
else:
    print("x is less than 1")
    y = x * 5 + 3
print("f(%.2f) = %.2f" % (x, y))
print(y)
