import numpy as np

# iteration functions. These functions will be using for the fixed point root finding problems
def g(f, x):
    epsilon = 0.0001
    gval = x - epsilon*f
    return gval
def g1(f, x):
    gval = np.abs(x - f)
    return gval
def g2(f, x):
    gval = np.abs(np.exp(-x) - f)
    return gval

# fixed point root finding method
def fixed_point(f, initialx, tol, maxiter):

    # initializing variables: x0, error and number of iterations
    error = 10.0 * tol
    x0 = initialx
    iterations = 0

    # adding print statements for the output to let the user know which iteration method is
    # being used and the iterations, root location and error.
    print("Results from g1 iteration method:")
    print("{:<25} {:<25} {:<25}".format('Iterations','Approx. Root Location','Error'))

    # Starting the while loop. If the error is greater than the tolerance and if the iterations
    # is greater than the maximum number of iterations, then the loop will continue.
    while (error > tol and iterations < maxiter):
        x1 = g1(float(eval(f)), x0) # setting x1 value using g1 iteration function, used for Task 1
        # x1 = g(float(eval(f)), x0) # used for Task 3
        error = np.abs(x1 - x0) # computing the absolute value of the error
        # printing iteration #, root approx, and error
        print("{:<25} {:<25} {:<25}".format(iterations, "{:.10f}".format(x1), "{:.10f}".format(error)))
        x0 = x1 # resetting x0
        iterations += 1 # increasing iteration
    print("Final Approximation: " + "{:.10f}".format(x1)) # final approximation

    # adding space for the outputs
    print()
    print()

    # resetting initial variables to test convergence for g2
    # the only difference from the code above is that in the following code we'll be using g2
    error = 10.0 * tol
    x0 = initialx
    iterations = 0
    print("Results from g2 iteration method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))
    while (error > tol and iterations < maxiter):
        x1 = g2(float(eval(f)), x0) # setting x1 value using g1 iteration function, used for Task 1
        # x1 = g(float(eval(f)), x0)  # used for Task 3
        error = np.abs(x1 - x0)
        print("{:<25} {:<25} {:<25}".format(iterations, "{:.10f}".format(x1), "{:.10f}".format(error)))
        x0 = x1
        iterations += 1
    print("Final Approximation: " + "{:.10f}".format(x1))

    # adding space for the outputs
    print()
    print()

def bisection(f, a, b, tol):

    # Initializing the starting variables
    x0 = a
    fa = float(eval(f))
    x0 = b
    fb = float(eval(f))
    k = (int)((np.log(tol/(b-a)))/(np.log(.5)) + 1) # this was given in the assignment and computed in class

    # note that we don't have to consider error here because it's taken into account in k
    print("Results from bisection method:")
    print("{:<25} {:<25}".format('Iterations', 'Approx. Root Location'))

    for iterations in range(1, k):
        c = .5 * (a + b)
        print("{:<25} {:<25}".format(iterations, "{:.10f}".format(c)))
        x0 = c
        if c == 0:
            print("Final Approximation: " + str(c))
            break
        fc = float(eval(f))
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("Final Approximation: " + str(c))

def newtons_method(f, x0, x1, tol, maxiter):
    x = x0
    f0 = float(eval(f))
    x = x1
    f1 = float(eval(f))
    error = 10.0 * tol
    iter = 0

    print("Results from Newtons Method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))

    while (error > tol and iter < maxiter):
        x2 = x1 - (f1 / ((f1 - f0) / (x1 - x0)))
        error = abs(x1 - x0)
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x0 = x1
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))

    print("Final Approximation: " + str(x1))

def secant_method(f, x0, x1, tol, maxiter):
    x = x0
    f0 = float(eval(f))
    x = x1
    f1 = float(eval(f))
    error = 10.0 * tol
    iter = 0

    print("Results from Secant Method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))

    while (error > tol and iter < maxiter):
        x2 = x1 - (f1 * (x1 - x0)/(f1 - f0))
        error = abs(x2 - x1)
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x0 = x1
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))

    print("Final Approximation: " + str(x1))

def bisection_newton_hybrid(f, a, b, tol, maxiter):

    error = 10.0 * tol
    iter = 0
    x0 = 0.5 * (a + b)
    x1 = b

    x = x0
    f0 = float(eval(f))
    x = x1
    f1 = float(eval(f))
    print("Results from Bisection-Newton Hybrid Method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))
    while (error > tol and iter < maxiter):
        if f1-f0 == 0 or x1 - x0 == 0:
            # cannot divide by 0. Break out of the loop is this happens
            break
        x2 = x1 - (f1 / ((f1 - f0) / (x1 - x0))) # this needs to be fixed
        newterror = abs(x1 - x0)
        if newterror > error:

            x = a
            fa = float(eval(f))
            x = b
            fb = float(eval(f))
            print("The Newton Error is greater than the general error!")
            print("Switching to Bisection method:")
            print()
            print("{:<25} {:<25}".format('Iterations', 'Approx. Root Location'))
            for i in range(1, 4):
                c = 0.5 * (a + b)
                x = c
                fc = float(eval(f))
                print("{:<25} {:<25}".format(i+iter, "{:.10f}".format(c)))
                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
            error = abs(b - a)
            iter += 4
            print("Exiting the bisection method:")
        else:
            x0 = x1
            error = newterror
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x0 = 0.5 * (a + b)
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))

    print("Final Approximation: " + str(x1))

def bisection_secant_hybrid(f, a, b, tol, maxiter):
    error = 10.0 * tol
    iter = 0
    x0 = 0.5 * (a + b)
    x1 = b

    x = x0
    f0 = float(eval(f))
    x = x1
    f1 = float(eval(f))
    print("Results from Bisection-Newton Hybrid Method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))
    while (error > tol and iter < maxiter):
        if f1-f0 == 0:
            # cannot divide by 0. Break out of the loop is this happens
            break
        x2 = x1 - (f1 * (x1 - x0)/(f1 - f0))
        secanterror = abs(x2 - x1)
        if secanterror > error:

            x = a
            fa = float(eval(f))
            x = b
            fb = float(eval(f))
            print("The Secant Error is greater than the general error!")
            print("Switching to Bisection method:")
            print()
            print("{:<25} {:<25}".format('Iterations', 'Approx. Root Location'))
            for i in range(1, 4):
                c = 0.5 * (a + b)
                x = c
                fc = float(eval(f))
                print("{:<25} {:<25}".format(i+iter, "{:.10f}".format(c)))
                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
            error = abs(b - a)
            iter+=4
            print("Exiting the bisection method:")
        else:
            x0 = x1
            error = secanterror
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x0 = x1
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))

    print("Final Approximation: " + str(x1))