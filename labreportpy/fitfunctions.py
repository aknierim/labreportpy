# A collection of functions for fitting of data
import numpy as np


def lin_fit(x, a, b):
    return a * x + b


def exp_fit(x, a, b, c):
    return a * np.exp(-b * x) + c


def gauss_fit(x, a, b, c):
    return a * np.exp(-((x - b) ** 2) / (2 * c**2))


def gauss_fit2(x, a, b, c, d, e, f):
    return a * np.exp(-((x - b) ** 2) / (2 * c**2)) + d * np.exp(
        -((x - e) ** 2) / (2 * f**2)
    )


def poly2(x, a, b, c):
    return a * x**2 + b * x + c


def poly3(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d


def poly4(x, a, b, c, d, e):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e


def poly5(x, a, b, c, d, e, f):
    return a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f


def weibull(x, a, b, c):
    return a * b * x ** (b - 1) * np.exp(-a * x**b)
