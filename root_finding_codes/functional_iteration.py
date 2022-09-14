import numpy as np

# def g(x):
#     gval = x - (x*np.exp(-x))
#     return gval

def functional_iteration(g, x00, x11):

    x0 = x00
    x1 = x11
    for k in range(1, 10):
        x1 = float(eval(g))
        x0 = x1

    print(x1, g)

def bisection():
    pass

def newtons_method():
    pass

def secant_method():
    pass
