import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return x * x


def monte_carlo_simple(f, a, b, n):
    longueur = b - a    # longueur entre les bornes min et max
    aires = 0
    i = 0
    while i < n:
        nb = np.random.random_sample()  # une valeur aléatoire entre [0,1)
        xi = longueur * nb + a          # une valeur x(i) aléatoire entre [a, b)
        fxi = f(xi)                     # la valeur f(x)/y de la fonction pour le xi
        si = longueur * fxi             # la surface de ce rectangle
        aires += si
        i += 1

    # la surface de l'intégrale est la moyen des surfaces des rectangles calculé aléatoirement
    integral = aires / float(n)
    return integral


def monte_carlo_cercle(f, a, b, n):
    compt = 0
    i = 0
    while i < n:
        xi = np.random.random_integers(a, b)     # une valeur aléatoire entre [a, b)
        yi = np.random.random_integers(a, b)     # une valeur aléatoire entre [a, b)
        if (xi * xi) + (yi * yi) < b:
            compt += 1
        i += 1
    cercle = compt / float(n)
    return cercle


a, b = 0, 2
for n in [10, 100, 1000, 10000, 100000]:
    print(n, ": ", monte_carlo_simple(f1, a, b, n))
    print(n, ": ", monte_carlo_cercle(f1, 0, 1, n))

