# numpy operations using arrays
import numpy as np

a = np.array([[1, 2], [4, 5]])
b = np.array([[1, 2], [4, 5]])

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Dot product")
    print("6. Exponentiation")
    print("7. Logarithm")
    print("8. Natural logarithm")
    print("9. Exit")

    n = int(input("Enter the option number: "))

    if n == 1:
        c = np.add(a, b)
        print("Sum:\n", c)
    elif n == 2:
        d = np.subtract(a, b)
        print("Difference:\n", d)
    elif n == 3:
        e = np.multiply(a, b)
        print("Product:\n", e)
    elif n == 4:
        f = np.divide(a, b)
        print("Quotient:\n", f)
    elif n == 5:
        g = np.dot(a, b)
        print("Dot product:\n", g)
    elif n == 6:
        h, i = np.exp(a), np.exp(b)
        print("Exponentiation for array a:\n", h)
        print("Exponentiation for array b:\n", i)
    elif n == 7:
        l, m = np.log(a), np.log(b)
        print("Logarithm for array a:\n", l)
        print("Logarithm for array b:\n", m)
    elif n == 8:
        x, y = np.log10(a), np.log10(b)
        print("Natural logarithm (base 10) for array a:\n", x)
        print("Natural logarithm (base 10) for array b:\n", y)
    elif n == 9:
        print("Exiting the program.")
        break
    else:
        print("No such option exists, please enter a valid option.\n")

    print("\n")  # Add space between operations
