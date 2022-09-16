# Homework 1

The coding modules I used are displayed at the bottom of this file in the appendix. I have created a python file called root_finding_functions.py where all of the root finding methods are stored and I've added a main.py file which is what I used to import the root funcing functions and test them with various initial approximations. See the appendix at the bottom of this file, or view my github repository to see the code I wrote for this assignment.

## Task 1

To start this task, I called the fixed point function in the ``main.py`` file:

```
fixed_point("x0*np.exp(-x0)", 1.1, 0.0000001, 20)
```

The parameters, from left to right are as follows: function, x0 approximation, tolerance, and maximum iterations. Now, I used the following code find the fixed points, given the initial variables: 

```
import numpy as np

# iteration functions. These functions will be using for the fixed point root finding problems
def g1(f, x):
    gval = np.abs(x - f)
    return gval
def g2(f, x):
    gval = np.abs(np.exp(-x) - f)
    return gval

# fixed point root finding function
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
```

The beginning of my code is the g1 and g2 functions. I have found, that for the given function, g1 will work and it will always converge to 0. However, I needed to add an absolute value: ``np.abs(x - f)``. This will account for negative inputs. 

The initial g2 function (``x + f``), I've found, will never converge. I tried modifying it to get convergence by changing it to the following: ``np.abs(np.exp(-x) - f)``. This gives an odd type of behavior, it doesn't converge to 0, but it alternates between 0 and 1, getting closer and closer to 1 and 0. The output looks like the following: 
```
Results from g2 iteration method:
Iterations                Approx. Root Location     Error                    
0                         0.0332871084              1.0667128916             
1                         0.9350634956              0.9017763872             
2                         0.0254915351              0.9095719605             
3                         0.9499807015              0.9244891663             
4                         0.0193448880              0.9306358134             
5                         0.9618667638              0.9425218758             
6                         0.0145737138              0.9472930500             
7                         0.9711691080              0.9565953942             
8                         0.0109165321              0.9602525759             
9                         0.9783448275              0.9674282954             
10                        0.0081408900              0.9702039375             
11                        0.9838172723              0.9756763823             
12                        0.0060504171              0.9777668553             
13                        0.9879539298              0.9819035127             
14                        0.0044852066              0.9834687232             
15                        0.9910597024              0.9865744958             
16                        0.0033184877              0.9877412147             
17                        0.9933795188              0.9900610310             
18                        0.0024517169              0.9909278019             
19                        0.9951055728              0.9926538559
Final Approximation: 0.9951055728
```

This isn't a solution, but just a test and something to explore more in the future.

The function itself, ``fixed_point()``, is very well documented and can be understood by reading the comments next to each line of code. I run two loops in the function because I wanted to text the g1 function as well as the g2 function separately.

## Task 2 
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

## Task 3

To begin, I called the ``fixed_point()`` function in the ``main.py`` file: 

``fixed_point("10.14 * np.exp(x0*x0) * np.cos(np.pi / x0)", 2.1, 0.0001, 1000)``

All that I did for this task was redefine a ``g()`` function to be the following (using an epsilon):

```
def g(f, x):
    epsilon = 0.0001
    gval = x - epsilon*f
    return gval
```

Then I modified the ``fixed_point()`` function slightly to call the ``g()`` function instead of the ``g1()`` or ``g2()`` functions. This seems to converge the correct values but only very very slowly. To conclude, it seems as though when it comes to root finding problems, these functional iteration methods are not necessarily the most efficient way to go.

## Task 4

To start this task, I called the bisection function twice in the ``main.py`` file with two different inputted functions:

``bisection("x0*np.exp(-x0)", -100, 5, 0.0001)``

``bisection("10.14 * np.exp(x0*x0) * np.cos(np.pi / x0)", -2.1, 5, 0.0001)``

These parameters include the function, the endpoint (a and b) and the tolerance. Also, I've included ``x0`` into the inputted function, and it'll be used later on as we plug in values. Now let's get into the bisection function itself: 

````
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
````

As you can see the first 8 lines of code is just initialization. The reason I set x0 equal to ``a`` and then defined ``fa`` was because when we do a ``float(eval(f))``, it only recognizes the ``x0`` variable, thus we have to set our ``x0 = a``, then define ``fa``. The same is done for ``fb``. Furthemore, we define ``k`` and will use it to account for the number of iterations we go through. 

The next few lines are print statements and then we begin the for loop from 1 to k. in the loops we need to define a ``c`` which will be our midpoint value. Then we add a print statement to let the user know where we're at. After this we want to evaluate ``f`` at ``c`` but we MUST make sure ``c`` is not equal to 0 because we cannot divide by 0 in our second bisection function call. After this, we continue with more if statments.

In the next if statement, we want to check if ``f`` evaluated at ``a`` multiplied by ``f`` evaluated at ``c`` is greater than 0. If it is, then we reset ``b`` and ``fb`` and if not, we reset ``a`` and ``fa``.

This method will always work because it's just cutting the interval in half and will get ever closer to the root. However, this method may take many many iterations, thus it can be seen as a brute force solution.

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

````
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

def newtons_method():
    pass

def secant_method():
    pass
````