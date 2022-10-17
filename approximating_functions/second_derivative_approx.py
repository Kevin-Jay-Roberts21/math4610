import matplotlib.pyplot as plt
import numpy as np

def second_derivative_approx(f, x0, h):

    x = x0 - h
    f_left = float(eval(f))
    x = x0 + h
    f_right = float(eval(f))
    x = x0
    f_center = float(eval(f))

    second_deriv = (f_right - 2*f_center + f_left) / (h*h)

    print("Second Derivative Approximation at x0 = " + str(x0) + ":")
    print("f''(x0) = " + str(second_deriv))

    return second_deriv

def fit_data_sets(x, y):
    n = len(x) # here n = 10

    a11 = n

    a12 = x[0]
    for i in range(1, n):
        a12 = a12 + x[i]

    a21 = a12

    a22 = (x[0] * x[0])
    for i in range(1, n):
        a22 = a22 + (x[i] * x[i])

    b1 = y[0]
    for i in range(1, n):
        b1 = b1 + y[i]

    b2 = y[0] * x[0]
    for i in range(1, n):
        b2 = b2 + (x[i] * y[i])

    detA = (a11 * a22) - (a12 * a21)
    a = ((a22 * b1) - (a12 * b2)) / detA
    b = ((-a21 * b1) + (a11 * b2)) / detA

    print("The approximate coefficients for the linear fit are:")
    print("a: " + str(a))
    print("b: " + str(b))

def explicit_euler_logistic(a, b, P0, t0, f, T, n):

    # intialize variables
    h = (T - t0)/n

    P = P0
    f0 = float(eval(f))
    for i in range(1, n):
        t1 = t0 + h
        P1 = P0 + (h * f0)
        t0 = t1
        P0 = P1
        P = P0
        f0 = float(eval(f))

    print("Final Approximation: " + str(f0))
