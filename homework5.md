# Homework 5 
Kevin Roberts
## Task 1 

To begin this task, I called the function in my ``main.py`` file under Homework 5: 

```
a = 0.2
b = 0.0005
P0 = 10.0
first_implicit = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)
a = 0.01
b = 0.0005
P0 = 10.0
second_implicit = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
a = 2.0
b = 0.0005
P0 = 10.0
third_implicit = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)
```

From the code above, we can see that I run the implicit euler function 3 times for each different condition of ``a``. The
inputs in the euler function are alpha a, beta b, initial condition P0, and initial t0 0, the logistic equation, a final 
time step T, and a number of intervals n. The corresponding printed output to the code is the following: 

```
Final Approximation: 0.12240034679439304
Final Approximation: 0.0004275008197252017
Final Approximation: 0.24597994992655003
```

Note that this is simply just what the implicit euler method prints. The method actually returns two lists: one list is 
the approximations, and the second list is the corresponding t values to those approximations. To view the graphs, we have
to do a little more in the ``main.py`` file where we call access the xvals and tvals and plot them using matplotlib: 

```
plt.plot(first_implicit[1], first_implicit[0])
plt.show()
plt.plot(second_implicit[1], second_implicit[0])
plt.show()
plt.plot(third_implicit[1], third_implicit[0])
plt.show()
```

The corresponding outputted graphs are the following: 

For ``a = 0.2``:

![alt text](homework5_images/implicit_1.png)

For ``a = 0.01``:

![alt text](homework5_images/implicit_2.png)

For ``a = 2.0``:

![alt text](homework5_images/implicit_3.png)

Finally, the code the implicit euler method is below. I initialize a time step h, tvals, xvals and the initial f0 value.
Then I proceed to use the newtons approximation method to approximate P0. Notice that I only use this once before I start
the loop because the can just use our previous P1 as our next P0 in the loop. I also had to rename variables from ``x``'s 
``P``'s and vice versa accordingly so that I could actually use the newton approximation method. The assignment said to 
use the library I created in c code. However, I decided writing the implicit method in python would be more simple and I 
can just call the newtons method here in my python code. The following method returns the approximated xvals at the corresponding
tvals. These values are then used and plotted in the ``main.py`` file.

```
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
```

## Task 2 

For this task, I derived the function on paper to find the exact solution. My work can be found below: 

![alt text](homework5_images/derivation_of_logistic_equation.png)

After I found my exact solution, I tested it on various values. The code I used to call the function for the exact solution
is the following (which can be found in my ``main.py`` file in github): 

```
a = 0.2
b = 0.0005
P0 = 10.0
exact = exact_logistic(a, b, P0, 0, "(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", 50, 100)
print("The exact value at " + str(exact[1][2]) + " is " + str(exact[0][2]))
print("The exact value at " + str(exact[1][5]) + " is " + str(exact[0][5]))
print("The exact value at " + str(exact[1][10]) + " is " + str(exact[0][10]))
```

The corresponding output is the following: 

```
The exact value at 1.0 is 12.146794237924682
The exact value at 2.5 is 16.22408990157865
The exact value at 5.0 is 26.063219378365762
```

The following is the function I wrote to compute the exact solution for the logistic equation:

```
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
```

I created the exact function to also return a set of xvals that correspond to each of the tvals. Thus, when I called the 
exact solution in the ``main.py`` file, I can grab a certain t value and it's corresponding exact value at the t value.

## Task 3 

For this task, a lot more is happening in the ``main.py`` file. This is what I did in the ``main.py`` file: 

```
a = 0.2
b = 0.0005
P0 = 10.0
implicit1 = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)
explicit1 = explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)
exact1 = exact_logistic(a, b, P0, 0, "(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", 50, 100)
a = 0.01
b = 0.0005
P0 = 10.0
implicit2 = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
explicit2 = explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
exact2 = exact_logistic(a, b, P0, 0, "(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", 600, 100)
a = 2.0
b = 0.0005
P0 = 10.0
implicit3 = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)
explicit3 = explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)
exact3 = exact_logistic(a, b, P0, 0, "(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", 8, 100)

# now we must create a plot with all 3 graphs
# use label='first plot', to label
plt.plot(implicit1[1], implicit1[0], label='Implicit')
plt.plot(explicit1[1], explicit1[0], label='Explicit')
plt.plot(exact1[1], exact1[0], label='Exact')
plt.legend()
plt.show()
plt.plot(implicit2[1], implicit2[0], label='Implicit')
plt.plot(explicit2[1], explicit2[0], label='Explicit')
plt.plot(exact2[1], exact2[0], label='Exact')
plt.legend()
plt.show()
plt.plot(implicit3[1], implicit3[0], label='Implicit')
plt.plot(explicit3[1], explicit3[0], label='Explicit')
plt.plot(exact3[1], exact3[0], label='Exact')
plt.legend()
plt.show()
```

The methods exact_logistic(), implicit_euler_logistic(), and explicit_euler_logistic() can all be found in the code appendix. 
As well as the newtons_method() function. The first 18 lines of the code above are used to create x approximations for their 
corresponding t values for the implicit, explicit and exact solutions. Once I obtain all this information, the next lines 
of code include graphing using matplotlib. The graphs I got are the following: 

For ``a = 0.2``:

![alt text](homework5_images/combination_1.png)

For ``a = 0.01``:

![alt text](homework5_images/combination_2.png)

For ``a = 2.0``:

![alt text](homework5_images/combination_3.png)

Looking at how close the implicit approximation, and the explicit approximation are to the exact solution is most interesting.

## Task 4 

For this task I had computed 5 different n values: n = 2, 4, 8, 16, and 32. know that we didn't have to compute for n = 32
however, I wanted to see what would happen if we included more partitions. In my ``main.py`` file I ran the following code: 

```
# for n = 2
partitions = [0, np.pi/4]
a = partitions[0]
b = partitions[1]
trapezoidal_rule("np.exp(-x*x)", a, b, len(partitions), partitions)
# for n = 4
partitions = [0, np.pi/12, 2*np.pi/12, 3*np.pi/12]
a = partitions[0]
b = partitions[3]
trapezoidal_rule("np.exp(-x*x)", a, b, len(partitions), partitions)
# for n = 8
partitions = [0, np.pi/28, 2*np.pi/28, 3*np.pi/28, 4*np.pi/28, 5*np.pi/28, 6*np.pi/28,  7*np.pi/28]
a = partitions[0]
b = partitions[7]
trapezoidal_rule("np.exp(-x*x)", a, b, len(partitions), partitions)
# for n = 16
partitions = [0, np.pi/60, 2*np.pi/60, 3*np.pi/60, 4*np.pi/60, 5*np.pi/60, 6*np.pi/60, 7*np.pi/60, 8*np.pi/60, 9*np.pi/60, 10*np.pi/60, 11*np.pi/60, 12*np.pi/60, 13*np.pi/60, 14*np.pi/60, 15*np.pi/60]
a = partitions[0]
b = partitions[15]
trapezoidal_rule("np.exp(-x*x)", a, b, len(partitions), partitions)
# for n = 32
partitions = [0, 1*np.pi/124, 2*np.pi/124, 3*np.pi/124, 4*np.pi/124, 5*np.pi/124, 6*np.pi/124, 7*np.pi/124, 8*np.pi/124, 9*np.pi/124, 10*np.pi/124, 11*np.pi/124, 12*np.pi/124, 13*np.pi/124, 14*np.pi/124, 15*np.pi/124, 16*np.pi/124, 17*np.pi/124, 18*np.pi/124, 19*np.pi/124, 20*np.pi/124, 21*np.pi/124, 22*np.pi/124, 23*np.pi/124, 24*np.pi/124, 25*np.pi/124, 26*np.pi/124, 27*np.pi/124, 28*np.pi/124, 29*np.pi/124, 30*np.pi/124, 31*np.pi/124]
a = partitions[0]
b = partitions[31]
trapezoidal_rule("np.exp(-x*x)", a, b, len(partitions), partitions)
```

Notice that the defined trapezoidal_rule() function takes a function f, end point a, end point b, number of partitions, 
and the partitions list. The following output I got is: 

```
The final approximation is: 0.30230789881265957for n = 2
The final approximation is: 0.20255813899533687for n = 4
The final approximation is: 0.24080472695354477for n = 8
The final approximation is: 0.27167754998156457for n = 16
The final approximation is: 0.28938806389213895for n = 32
```

The trapezoidal function is the following: 

```
def trapezoidal_rule(f, a, b, n, p):
    dx = (b - a)/n
    x = b
    fxn = float(eval(f))
    x = a
    fx0 = float(eval(f))
    sum = 0.5 * (fx0 + fxn)
    for i in range(1, n-2):

        fxi = p[i]
        sum = sum + fxi
    sum = sum * dx
    print("The final approximation is: " + str(sum) + "for n = " + str(n))
    return sum
```

Notice that in the code I had to include the partition list to be able to evaluate f and certain x values. From the output, 
we cannot seem to get an exact value to which the sequence is converging to. But from the ``n = 32`` case, we can see that
the sequence will possibly converge to 30.

## Task 5 



## Code Appendix

Functions used: 

```
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
```

```
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
```

```
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
```

```
def newtons_method(f, fprime, x0, tol, maxiter):
    x = x0
    f0 = float(eval(f))
    fp = float(eval(fprime))
    error = 10.0 * tol
    iter = 0

    # print("Results from Newtons Method:")
    # print("{:<25} {:<25} {:<25}".format('Iterations', 'Approx. Root Location', 'Error'))

    while (error > tol and iter < maxiter):
        if (fp == 0):
            print("Quitting because we found division by 0")
            return x0
        x1 = x0 - (f0 / fp)
        error = abs(x1 - x0)
        # print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
        iter += 1
        x0 = x1
        x = x0
        f0 = float(eval(f))
        fp = float(eval(fprime))

    return x1

    print("Final Approximation: " + str(x1))
```

