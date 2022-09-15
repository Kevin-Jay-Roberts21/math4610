import numpy as np

# iteration functions. These functions will be using for the fixed point root finding problems
def g1(f, x):
    gval = x - f
    return gval
def g2(f, x):
    gval = x + f
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
        x1 = g1(float(eval(f)), x0) # setting x1 value using g1 iteration function
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
        x1 = g2(float(eval(f)), x0)
        error = np.abs(x1 - x0)
        print("{:<25} {:<25} {:<25}".format(iterations, "{:.10f}".format(x1), "{:.10f}".format(error)))
        x0 = x1
        iterations += 1
    print("Final Approximation: " + "{:.10f}".format(x1))

    # adding space for the outputs
    print()
    print()

def bisection(f, endpointA, endpointB, tol):
    pass

def newtons_method():
    pass

def secant_method():
    pass


