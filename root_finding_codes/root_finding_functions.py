import numpy as np

def g1(f, x):
    gval = x - f
    return gval
def g2(f, x):
    gval = x + f
    return gval

def fixed_point(f, initialx, tol, maxiter):

    error = 10.0 * tol
    x0 = initialx
    iterations = 0
    print("Results from g1 iteration method:")
    while (error > tol and iterations < maxiter):
        x1 = g1(float(eval(f)), x0)
        error = np.abs(x1 - x0)
        print(x1)
        x0 = x1
        iterations += 1
    print(x1, g1(float(eval(f)), x1))

    # resetting initial variables to test convergence for g2
    error = 10.0 * tol
    x0 = initialx
    iterations = 0
    print("Results from g2 iteration method:")
    while (error > tol and iterations < maxiter):
        x1 = g2(float(eval(f)), x0)
        error = np.abs(x1 - x0)
        print(x1)
        x0 = x1
        iterations += 1
    print(x1, g2(float(eval(f)), x1))

def bisection(f, endpointA, endpointB, tol):
    pass

def newtons_method():
    pass

def secant_method():
    pass


