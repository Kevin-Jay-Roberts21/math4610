# Math 4610 Root Finding Problem: Bisection/Newton Hybrid Method

**Routine Name:**           bisection_newton_hybrid

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will iterate through a loop given a function f(x) to solve for when x = 0 (or the 
roots of f(x)). The purpose of this method is to find root given a certain interval from a to b. The function starts out 
using newtons method, but then switches to using the bisection method if the error from the Newton Method is greater than 
the error from the supposed Bisection method.

**Input:** The inputs are a function, the functions derivative, a, b, tolerance, and max iterations.

**Output:** This routine outputs the root approximation after each iteration as well as the final approximation.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      bisection_newton_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", "10.14*(2*np.exp(x*x)*x*np.cos(np.pi/x) + (np.pi*np.exp(x*x)*np.sin(np.pi/x))/(x*x))", -3, 7, 0.000001, 10)

Output from the lines above:

      Results from Bisection-Newton Hybrid Method:
      Iterations                Approx. Root Location     Error                    
      0                         2.0000000000              0.0000000000             
      Final Approximation: 2.0

The code output suggests that our final approximation is 2. Due to our inputs, we only needed one iteration to find 
the root. But, understand that different intervals and interval lengths yield increased iterations and approximations. See 
the code at the bottom of the file as I explain what's going on for this function. 

The first 6 lines of the function are for initializing variables and functions. Then we see the 2 print statements to notify
the user that the function is about to start up the while loop. The line ``while (error > tol and iter < maxiter):`` implies that we want to run the loop as long as the error is 
greater than the tolerance AND as long as the number of iterations is less than the number of the inputted maximum number 
of iterations. Then we need to check if ``fp == 0``, is this is the case then we have a singularity, and our code will break. 
Further, if this happens, we know that we've found a root! We then proceed to apply newtons method and compute the error.
After this is done, we must evaluate if Newton's Error is greater than the initial error (defined to be the bisection error).
If so, we must proceed to find the root using the bisection method. More on the bisection method and how it works can be 
found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/bisection_method.md). After running through the bisection method, we have a new x0 approximation which will be used in 
next loop along with our redefined f0 and fp. Finally, when the loop conditions are met, we break out of the loop and print
the final approximation.

**Implementation/Code:** The following is the code for bisection_newton_method()

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

**Special Note:** This method is dependent on proper initial root approximations as well as inputted functions. Without 
knowledge of the behavior of the function, a poor initial root approximation may result in confusing and/or unhelpful final
root approximations.

**Last Modified:** September/2022