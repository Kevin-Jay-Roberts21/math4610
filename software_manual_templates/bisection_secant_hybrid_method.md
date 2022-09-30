# Math 4610 Root Finding Problem: Bisection/Secant Hybrid Method

**Routine Name:**           bisection_secant_hybrid

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will iterate through a loop given a function f(x) to solve for when x = 0 (or the 
roots of f(x)). The purpose of this method is to find root given a certain interval from a to b. The function starts out 
using the secant method, but then switches to using the bisection method if the error from the Secant Method is greater than 
the error from the supposed Bisection method.

**Input:** The inputs are a function, the functions derivative, a, b, tolerance, and max iterations.

**Output:** This routine outputs the root approximation after each iteration as well as the final approximation.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      bisection_secant_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", -3, 7, 0.00001, 20)

Output from the lines above:

      Results from Bisection-Secant Hybrid Method:
      Iterations                Approx. Root Location     Error                    
      The Secant Error is greater than the general error!
      Switching to Bisection method:
    
      Iterations                Approx. Root Location    
      1                         2.0000000000             
      2                         -0.5000000000            
      3                         -1.7500000000            
      Exiting the bisection method:
      5                         -1.7500000000             1.2500000000             
      6                         -1.7500000000             0.0000000000             
      Final Approximation: -1.7499999999999984

The code output suggests that our final approximation is -1.749. Due to the inputs, we notice that right away we switched to 
using the bisection method and then switched back to the secant method. Further, notice our final approximation is acutally 
not even a root. This is due to our poorly estimated x0 and x1. See the Special Note for more information.

The first 8 lines of the function are for initializing variables and functions. Then we see the 2 print statements to notify
the user that the function is about to start up the while loop. The line ``while (error > tol and iter < maxiter):`` implies that we want to run the loop as long as the error is 
greater than the tolerance AND as long as the number of iterations is less than the number of the inputted maximum number 
of iterations. Then we need to check if ``f1 - f0 == 0``, is this is the case then we have a singularity, and our code will break. 
Further, if this happens, we know that we've found a root! We then proceed to apply the secant method and compute the error.
After this is done, we must evaluate if the Secant Error is greater than the initial error (defined to be the bisection error).
If so, we must proceed to find the root using the bisection method. More on the bisection method and how it works can be 
found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/bisection_method.md). After running through the bisection method, we have a new x0 approximation which will be used in 
next loop along with our redefined f0, f1, and x1. Finally, when the loop conditions are met, we break out of the loop and print
the final approximation.

**Implementation/Code:** The following is the code for bisection_secant_method()

    def bisection_secant_hybrid(f, x0, x1, tol, maxiter):
        error = 10.0 * tol
        iter = 0
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
                a = x1
                b = x2
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
                    if c == 0:
                        print("Final Approximation: " + str(c))
                        return
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
                x0 = a
                x1 = b
                iter += 4
                f0 = f1
                x = x1
                f1 = float(eval(f))
                iter += 1
                print("Exiting the bisection method:")
            else:
                iter += 1
                x0 = x1
                x1 = x2
                f0 = f1
                x = x1
                f1 = float(eval(f))
                error = secanterror
            print("{:<25} {:<25} {:<25}".format(iter, "{:.10f}".format(x1), "{:.10f}".format(error)))
    
    
        print("Final Approximation: " + str(x1))

**Special Note:** This method is dependent on proper initial root approximations as well as inputted functions. Without 
knowledge of the behavior of the function, a poor initial root approximation may result in confusing and/or unhelpful final
root approximations.

**Last Modified:** September/2022