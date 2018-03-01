def g(x):
    return x**(-1) - 2**x


def bisection(f, a, b, epsilon):
    global m
    assert not f(a)*f(b) > 0

    epsilon = 10**(-1*epsilon)

    while b - a >= epsilon:
        m = (a+b)/2

        if f(a) == 0:
            return a
        if f(b) == 0:
            return b
        if f(m) == 0:
            return m

        if f(a)*f(m) > 0:
            a = m
        else:
            b = m

        if b - a < epsilon:
            return a
    return m


print("This algorithm will use the bisection method to find the solutions of x^(-1) - 2^(x) = 0 on the interval (0,1].")
print(bisection(g, 0.000001, 1, 3))
