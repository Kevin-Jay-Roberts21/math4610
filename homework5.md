# Homework 5 
Kevin Roberts
## Task 1 



## Task 2 

For this task, I derived the function to find the exact solution. My work can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/homework5_images/CamScanner%2010-24-2022%2019.43.pdf).

After I found my exact solution, I tested it on various values. The code I used to call the function for the exact solution
is the following (which can be found in my ``main.py`` file in github): 

```
a = 0.2
b = 0.0005
P0 = 10.0
exact_logistic("(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", P0, a, b, 2)
exact_logistic("(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", P0, a, b, 5)
exact_logistic("(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", P0, a, b, 10)
```

The corresponding output is the following: 

```
Exact Solution to Logistic Equation: 14.737045897841911
Exact Solution to Logistic Equation: 26.063219378365762
Exact Solution to Logistic Equation: 63.71378700331849
```

The following is the function I wrote to compute the exact solution for the logistic equation:

```
def exact_logistic(P, P_initial, alpha, beta, time):
    a = alpha
    b = beta
    t = time
    P0 = P_initial
    P_final = float(eval(P))
    print("Exact Solution to Logistic Equation: " + str(P_final))
    return P_final
```

All I do in the above function is set variables to be the inputted values and then evaluate the solution. This function 
will be used to compare with the explicit and implicit methods in the next task.

## Task 3 



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



