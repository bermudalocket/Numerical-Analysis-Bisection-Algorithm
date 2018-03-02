def f(x):
    return x**3 - 3*x - 2


def df(x):
    return 3*x**2 - 3


def newton(x, epsilon):
    while abs(f(x)) > epsilon:
        x = x - f(x)/df(x)
    return x


print("This algorithm will find a solution to the equation x^3 - 3x - 2 = 0 given an initial value and an epsilon.")
x = input("Initial value, x = ")
e = input("Epsilon tolerance, e = ")
print(newton(x, e))