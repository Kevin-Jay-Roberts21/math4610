# Homework 2

## Task 1

## Task 2


## Task 3 
This part of the assignment is inbedded inside of the functions. Instead of using verbose, I included some print statements inside the root finding functions. The following python code is a print statement to begin the list of numerical values: 

``
print("{:<25} {:<25} {:<25}".format('Iterations','Approx. Root Location','Error'))
``

Further, inside of the loop of the root finding functions, I include information from each iteration:

``
print("{:<25} {:<25} {:<25}".format(iterations, "{:.10f}".format(x1), "{:.10f}".format(error)))
``

The code line `"{:.10f}".format(x1)` will round the root approximation to the tenth decimal, and the same is done with the error variable. This will keep code cleaner as we print out iterations.

Finally, I end with the following print statement, outside of the loop, that displays the final iteration (aka the final root approximation):

``
print("Final Approximation: " + "{:.10f}".format(x1))
``

The outputted results for Newtons Method and the Hybrid Method are the following:


## Task 4


## Task 5

I have completed task 5, in that I've added you as a collaborator to my github repository and have published all of my code and notes, including this homework1.md file. My repository can be found at the following link: 

https://github.com/Kevin-Jay-Roberts21/math4610

### Appendix
Code I wrote for this assignment:

#### main.py

````
from root_finding_codes.root_finding_functions import *

# The first two calls are the fixed point functional iteration methods. My
# parameters are in order as follows (for the fixed point functions):
# 1. f function 2. initial root guess 3. tolerance 4. maximum iterations.
# the third function call is the bisection method and the parameters are
# in order as follows: 1. f function 2. end point a 3. end point b 4. tolerance.

# The reason I use x0 in the functions is because x0 is defined to be a value in
# the functions. If I used a simple x instead, then it would not be recognized because
# it's not defined. x0 is defined so we use it.

# Task 1 and 2
fixed_point("x0*np.exp(-x0)", 1.1, 0.0000001, 20)

# Task 3
# Must uncomment out the Task 3 g lines in the fixed_point function (line 32 and 53) AND
# comment out the g1() and g2() function calls in the fixed_point function (line 31 and 52)
# before uncommenting the following line:
#fixed_point("10.14 * np.exp(x0*x0) * np.cos(np.pi / x0)", 2.1, 0.0001, 1000)

# Task 4
bisection("x0*np.exp(-x0)", -100, 5, 0.0001)
bisection("10.14 * np.exp(x0*x0) * np.cos(np.pi / x0)", -2.1, 5, 0.0001)
````

#### root_finding_functions.py

```
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
    # this was given in the assignment and computed in class
    k = (int)((np.log(tol/(b-a)))/(np.log(.5)) + 1)

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

def newtons_method():
    pass

def secant_method():
    pass
```