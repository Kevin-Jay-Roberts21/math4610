import math

import matplotlib.pyplot as plt
import sys
import time
import os.path
sys.path.insert(0, "./math4610")
from root_finding_codes.root_finding_functions import *


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

    # initialize variables
    tvals = []
    xvals = []

    h = (T - t0)/n
    P = P0

    tvals.append(t0)
    xvals.append(P0)

    f0 = float(eval(f))
    for i in range(1, n):
        t1 = t0 + h
        P1 = P0 + (h * f0)
        tvals.append(t1)
        xvals.append(P0)
        t0 = t1
        P0 = P1
        P = P0
        f0 = float(eval(f))

    print("Final Approximation: " + str(f0))
    return [xvals, tvals]

def implicit_euler_logistic(a, b, P0, t0, f, T, n):

    # initialize variables
    tvals = []
    xvals = []

    h = (T - t0) / n

    P = P0
    f0 = float(eval(f))

    f = f.replace("P", "x")
    f = f.replace("a", str(a))
    f = f.replace("b", str(b))
    f_prime = "1" + " - " + str(h) + "*" + str(a) + " + 2" + "*" + str(b) + "*" + str(h) + "*x"
    f_P0 = "x" + " - " + str(h) + " * (" + f + ")" + " - " + str(P0)
    Pbar = newtons_method(f_P0, f_prime, h, 0.0001, 10)

    f = f.replace("x", "P")
    f = f.replace(str(a), "a")
    f = f.replace(str(b), "b")

    tvals.append(t0)
    xvals.append(P0)

    for i in range(1, n):
        t1 = t0 + h
        P1 = Pbar + (h * f0)
        tvals.append(t1)
        xvals.append(Pbar)
        t0 = t1
        Pbar = P1
        P = Pbar
        f0 = float(eval(f))

    print("Final Approximation: " + str(f0))
    return [xvals, tvals]

def exact_logistic(a, b, P0, t0, f, T, n):
    # initialize variables
    tvals = []
    xvals = []

    h = (T - t0) / n

    t = 0
    f0 = float(eval(f))

    tvals.append(t0)
    xvals.append(P0)

    xi = 0
    for i in range(1, n):
        t1 = t0 + h
        xi = xi + h
        t = t1
        f0 = float(eval(f))
        tvals.append(t1)
        xvals.append(f0)
        t0 = t1

    return [xvals, tvals]

def trapezoidal_rule(f, a, b, n):
    dx = (b - a)/n
    x = b
    fxn = float(eval(f))
    x = a
    fx0 = float(eval(f))
    sum = 0.5 * (fx0 + fxn)
    xk = 0
    for k in range(1, n):
        xk = xk + (b - a) / n
        x = xk
        fxk = float(eval(f))
        sum = sum + fxk
    sum = sum * dx
    print("The final approximation is: " + str(sum) + "for n = " + str(n))
    return sum

def simpsons_rule(f, a, b, n):
    dx = (a + b)/n
    x = b
    fxn = float(eval(f))
    x = a
    fx0 = float(eval(f))
    sum = fx0 + fxn
    xk = 0
    for k in range(1, n-2, 2):
        xk = xk + (b-a)/n
        x = xk
        fxk = float(eval(f))
        sum = sum + (4.0 * fxk)
    xk = 0
    for i in range(2, n-2, 2):
        xk = xk + (b - a)/n
        x = xk
        fxk = float(eval(f))
        sum = sum + (2.0 * fxk)
    sum = (sum * dx)/3.0
    print("The final approximation is: " + str(sum) + "for n = " + str(n))
    return sum

def my_simpsons_rule(f, a, b, n):
    if (n % 2) != 0:
        return "n must be an even number for Simpson's Rule."

    start = time.time()
    h = 2 * ((b - a)/n)
    sum = 0
    x0 = (b-a)/n
    for i in range(0, int(n/2)):
        x = x0
        fx0 = float(eval(f))
        x1 = x0 + (b-a)/n
        x = x1
        fx1 = float(eval(f))
        x2 = x1 + (b-a)/n
        x = x2
        fx2 = float(eval(f))
        sum += (fx0 + 4*fx1 + fx2)*(h/3)
        x0 = x2
    end = time.time()

    totaltime = end-start
    print("The time it took to generate pi was: " + str(totaltime))
    return 3 * sum

def approximate_e(n):

    sum = 0
    start = time.time()
    for i in range(0, n):
        sum += 1/(math.factorial(i))

    end = time.time()
    totaltime = end - start
    print("The time it took to generate e was: " + str(totaltime))
    return sum



