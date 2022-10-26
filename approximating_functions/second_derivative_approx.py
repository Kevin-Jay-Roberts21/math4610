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

    plt.plot(tvals, xvals)
    plt.show()

    print("Final Approximation: " + str(f0))

def implicit_euler_logistic(a, b, P0, t0, f, T, n):

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

    plt.plot(tvals, xvals)
    plt.show()

    print("Final Approximation: " + str(f0))

def exact_logistic(P, P_initial, alpha, beta, time):
    a = alpha
    b = beta
    t = time
    P0 = P_initial
    P_final = float(eval(P))
    print("Exact Solution to Logistic Equation: " + str(P_final))
    return P_final

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
