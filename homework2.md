# Homework 2

## Task 1

To begin this task I called the newton method in the ``main.py`` file: 

``newtons_method("x*np.exp(-x)", "-x*np.exp(-x) + np.exp(-x)", -3, 0.000001, 10)``

The method takes 5 parameters starting from left to right: a function f, f's derivative, an inital approximation, tolerance, 
and max iterations. The function was created in my root_finding_functions.py file:

```
def newtons_method(f, fprime, x0, tol, maxiter):
    x = x0
    f0 = float(eval(f))
    fp = float(eval(fprime))
    error = 10.0 * tol
    iter = 0

    print("Results from Newtons Method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))

    while (error > tol and iter < maxiter):
        x1 = x0 - (f0 / fp)
        error = abs(x1 - x0)
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x0 = x1
        x = x0
        f0 = float(eval(f))
        fp = float(eval(fprime))

    print("Final Approximation: " + str(x1))
```

The output from this code is: 

```
Results from Newtons Method:
Iterations                Approx. Root Location     Error                    
0                         -2.2500000000             0.7500000000             
1                         -1.5576923077             0.6923076923             
2                         -0.9486697513             0.6090225564             
3                         -0.4618403382             0.4868294131             
4                         -0.1459095720             0.3159307663             
5                         -0.0185787812             0.1273307908             
6                         -0.0003388752             0.0182399060             
7                         -0.0000001148             0.0003387604             
8                         -0.0000000000             0.0000001148             
Final Approximation: -1.3178467639212633e-14
```

To conclude, I've found that this method is dependent on proper initial root approximations as well as inputted functions. Without 
knowledge of the behavior of the function, a poor initial root approximation may result in confusing and/or unhelpful final
root approximations.

See Software Manual [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/newtons_method.md) to get a more in-depth description of the method.

See code function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/root_finding_codes/root_finding_functions.py)

See function call in the main function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py)

## Task 2

To begin this task I called the secant method in the ``main.py`` file: 

``secant_method("x*np.exp(-x)", -5, -1, 0.000001, 10)``

The method takes 5 parameters starting from left to right: a function f, an x0 approximation, an x1 approximation, tolerance, 
and max iterations. The function was created in my root_finding_functions.py file:

```
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
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x2), "{:.10f}".format(error)))
        iter += 1
        x0 = x1
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))

    print("Final Approximation: " + str(x2))
```

The output from this code: 

```
Results from Secant Method:
Iterations                Approx. Root Location     Error                    
0                         -0.9852936175             0.0147063825             
1                         -0.4944602834             0.4908333341             
2                         -0.2768316201             0.2176286633             
3                         -0.0985055100             0.1783261101             
4                         -0.0229093895             0.0755961204             
5                         -0.0021265887             0.0207828009             
6                         -0.0000481148             0.0020784739             
7                         -0.0000001022             0.0000480126             
8                         -0.0000000000             0.0000001022             
Final Approximation: -4.91766058164191e-12
```

To conclude we can see that the secant method will iterate through a loop given a function f(x) to solve for when x = 0 (or the 
roots of f(x)). The purpose of this method is to find root given a certain x0 and x1 as opposed to one value. We can see 
that the final approximation from the above output is very close to 0.

See Software Manual [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/secant_method.md) to get a more in-depth description of the method.

See code function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/root_finding_codes/root_finding_functions.py)

See function call in the main function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py)

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

The outputted results for Newtons Method and the Hybrid Method were the following:

```
Results from Newtons Method:
Iterations                Approx. Root Location     Error                    
0                         -2.2500000000             0.7500000000             
1                         -1.5576923077             0.6923076923             
2                         -0.9486697513             0.6090225564             
3                         -0.4618403382             0.4868294131             
4                         -0.1459095720             0.3159307663             
5                         -0.0185787812             0.1273307908             
6                         -0.0003388752             0.0182399060             
7                         -0.0000001148             0.0003387604             
8                         -0.0000000000             0.0000001148             
Final Approximation: -1.3178467639212633e-14
```
```
Results from Secant Method:
Iterations                Approx. Root Location     Error                    
0                         -0.9852936175             0.0147063825             
1                         -0.4944602834             0.4908333341             
2                         -0.2768316201             0.2176286633             
3                         -0.0985055100             0.1783261101             
4                         -0.0229093895             0.0755961204             
5                         -0.0021265887             0.0207828009             
6                         -0.0000481148             0.0020784739             
7                         -0.0000001022             0.0000480126             
8                         -0.0000000000             0.0000001022             
Final Approximation: -4.91766058164191e-12
```

## Task 4

To begin this task I called the bisection newton hybrid method in the ``main.py`` file: 

``bisection_newton_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", "10.14*(2*np.exp(x*x)*x*np.cos(np.pi/x) + (np.pi*np.exp(x*x)*np.sin(np.pi/x))/(x*x))", 1, 7, 0.000001, 10)``

The method takes 6 parameters starting from left to right: a function f, f's derivative, end point a, end point b, tolerance, 
and max iterations. Notice that I tested my code on the endpoints [1, 7] instead of [-3, 7] just to see the method work a 
harder on a different interval. The function was created in my root_finding_functions.py file: 

```
def bisection_newton_hybrid(f, fprime, a, b, tol, maxiter):

    error = 10.0 * tol
    iter = 0
    x0 = 0.5 * (a + b)
    x = x0
    f0 = float(eval(f))
    fp = float(eval(fprime))

    print("Results from Bisection-Newton Hybrid Method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))
    while (error > tol and iter < maxiter):
        if fp == 0:
            # cannot divide by 0. Break out of the loop is this happens
            break
        x1 = x0 - (f0 / fp)
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
            x0 = c
            iter += 4
            print("Exiting the bisection method:")
        else:
            x0 = x1
            error = newterror
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x = x0
        f0 = float(eval(f))
        fp = float(eval(fprime))

    print("Final Approximation: " + str(x1))
```

The output from the code above yields the following: 

```
Results from Bisection-Newton Hybrid Method:
Iterations                Approx. Root Location     Error                    
The Newton Error is greater than the general error!
Switching to Bisection method:

Iterations                Approx. Root Location    
1                         4.0000000000             
2                         2.5000000000             
3                         1.7500000000             
4                         2.1250000000             
Exiting the bisection method:
4                         3.8779944663              0.3750000000             
5                         2.0399513166              0.0850486834             
6                         2.0050014557              0.0349498609             
7                         2.0000862919              0.0049151638             
8                         2.0000000261              0.0000862658             
9                         2.0000000000              0.0000000261             
Final Approximation: 2.000000000000002
```

We can see from the output that if our approximations of x0 is 1 and x1 is 7, then we quit to the bisection method right
away and then revert back to the newton method to get a final approximation of 2. Again, note that the method is dependent 
on proper initial root approximations as well as inputted functions. Without knowledge of the behavior of the function, 
a poor initial root approximation may result in confusing and/or unhelpful final root approximations.

See Software Manual [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/bisection_newton_hybrid_method.md) to get a more in-depth description of the method.

See code function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/root_finding_codes/root_finding_functions.py)

See function call in the main function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py)

## Task 5

To begin this task I called the bisection secant hybrid method in the ``main.py`` file: 

``bisection_secant_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", 1.2, 1.7, 0.00001, 20)``

The method takes 5 parameters starting from left to right: a function f, an x0 approximation, an x1 approximation, tolerance, 
and max iterations. The function was created in my root_finding_functions.py file:

```
def bisection_secant_hybrid(f, a, b, tol, maxiter):
    error = 10.0 * tol
    iter = 0
    x0 = 0.5 * (a + b)
    x1 = b
    x = x0
    f0 = float(eval(f))
    x = x1
    f1 = float(eval(f))

    print("Results from Bisection-Secant Hybrid Method:")
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
                print("{:<25} {:<25}".format(i + iter, "{:.10f}".format(c)))
                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
            error = abs(b - a)
            x0 = c
            iter += 4
            print("Exiting the bisection method:")
        else:
            x0 = x1
            error = secanterror
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        #x0 = x1
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))

    print("Final Approximation: " + str(x1))
```

The output from this code is the following: 

```
Results from Bisection-Secant Hybrid Method:
Iterations                Approx. Root Location     Error                    
The Secant Error is greater than the general error!
Switching to Bisection method:

Iterations                Approx. Root Location    
1                         0.7298275539             
2                         0.2447413308             
3                         0.4872844423             
4                         0.6085559981             
Exiting the bisection method:
5                         0.6085559981              0.1212715558             
6                         0.6223099959              0.0137539978             
The Secant Error is greater than the general error!
Switching to Bisection method:

Iterations                Approx. Root Location    
7                         0.6454296652             
8                         0.6569894998             
9                         0.6627694172             
10                        0.6656593758             
Exiting the bisection method:
11                        0.6685493345              0.0028899587             
12                        0.6684308907              0.0001184437             
The Secant Error is greater than the general error!
Switching to Bisection method:

Iterations                Approx. Root Location    
13                        0.6675484646             
14                        0.6671072516             
15                        0.6668866451             
16                        0.6667763418             
Exiting the bisection method:
17                        0.6666660385              0.0001103033             
18                        0.6666660778              0.0000000393             
Final Approximation: 0.666666077801113
```

We can see from the output that the code quite often switches from the bisection method the secant method until finally 
we get a final approximation of about 0.666. Again, note that the method is dependent 
on proper initial root approximations as well as inputted functions. Without knowledge of the behavior of the function, 
a poor initial root approximation may result in confusing and/or unhelpful final root approximations.

See Software Manual [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/bisection_secant_hybrid_method.md) to get a more in-depth description of the method.

See code function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/root_finding_codes/root_finding_functions.py)

See function call in the main function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py)

### Appendix
Code can be found in my repository: 

All code I wrote for this assignment:

root_finding_functions.py

````
def newtons_method(f, fprime, x0, tol, maxiter):
    x = x0
    f0 = float(eval(f))
    fp = float(eval(fprime))
    error = 10.0 * tol
    iter = 0

    print("Results from Newtons Method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))

    while (error > tol and iter < maxiter):
        x1 = x0 - (f0 / fp)
        error = abs(x1 - x0)
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x0 = x1
        x = x0
        f0 = float(eval(f))
        fp = float(eval(fprime))

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
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x2), "{:.10f}".format(error)))
        iter += 1
        x0 = x1
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))

    print("Final Approximation: " + str(x2))

def bisection_newton_hybrid(f, fprime, a, b, tol, maxiter):

    error = 10.0 * tol
    iter = 0
    x0 = 0.5 * (a + b)
    x = x0
    f0 = float(eval(f))
    fp = float(eval(fprime))

    print("Results from Bisection-Newton Hybrid Method:")
    print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))
    while (error > tol and iter < maxiter):
        if fp == 0:
            # cannot divide by 0. Break out of the loop is this happens
            break
        x1 = x0 - (f0 / fp)
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
            x0 = c
            iter += 4
            print("Exiting the bisection method:")
        else:
            x0 = x1
            error = newterror
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x = x0
        f0 = float(eval(f))
        fp = float(eval(fprime))

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

    print("Results from Bisection-Secant Hybrid Method:")
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
                print("{:<25} {:<25}".format(i + iter, "{:.10f}".format(c)))
                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
            error = abs(b - a)
            x0 = c
            iter += 4
            print("Exiting the bisection method:")
        else:
            x0 = x1
            error = secanterror
        print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        #x0 = x1
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))

    print("Final Approximation: " + str(x1))
````

main.py

````
# Task 1
newtons_method("x*np.exp(-x)", "-x*np.exp(-x) + np.exp(-x)", -3, 0.000001, 10)

# Task 2
# Notes: (only works when both x0 < x1 and both are negative and close to each other)
secant_method("x*np.exp(-x)", -5, -1, 0.000001, 10)

# Task 4
# passing in f, fprime, a, b, tol, and maxiter (interval (-2, 7) doesn't work for some reason)
bisection_newton_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", "10.14*(2*np.exp(x*x)*x*np.cos(np.pi/x) + (np.pi*np.exp(x*x)*np.sin(np.pi/x))/(x*x))", -3, 7, 0.000001, 10)


# Task 5
# passing in f, a, b, tol, maxiter
bisection_secant_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", -3, 7, 0.00001, 20)
````