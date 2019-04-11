import numpy as np


def f0(x):
    return x * x - 2


def dichotomie(f, a, b, prec):
    if f(a) < 0 < f(b):
        print("L'intérvalle est bon")

    for n in range(0, 200):
        m = 0.5 * (a + b)

        if f(m) < 0:
            a = m
        else:
            b = m

        print(a, b)

        dd = abs(b - a)
        if dd < prec:
            print("Itération atteint la précision ", n)
            break


dichotomie(f0, 0, 2, 1.e-4)

