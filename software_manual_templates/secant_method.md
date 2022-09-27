# Math 4610 Root Finding Problem: Secant Method

**Routine Name:**           secant_method

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will iterate through a loop given a function f(x) to solve for when x = 0 (or the 
roots of f(x)). The purpose of this method is to find root given a certain x0 and x1 as opposed to one value.

**Input:** The inputs are a function, x0, x1, tolerance, and max iterations.

**Output:** This routine outputs the root approximation after each iteration as well as the final approximation.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      secant_method("x*np.exp(-x)", -5, -1, 0.000001, 10)

Output from the lines above:

      Results from Secant Method:
      Iterations                Approx. Root Location     Error                    
      0                         -1.0000000000             0.0147063825             
      1                         -0.9852936175             0.4908333341             
      2                         -0.4944602834             0.2176286633             
      3                         -0.2768316201             0.1783261101             
      4                         -0.0985055100             0.0755961204             
      5                         -0.0229093895             0.0207828009             
      6                         -0.0021265887             0.0020784739             
      7                         -0.0000481148             0.0000480126             
      8                         -0.0000001022             0.0000001022             
      Final Approximation: -4.91766058164191e-12

The code output suggests that our final approximation is very close to 0. See the code at the bottom of the file as I explain
what's going on for this function. 

The first 4 lines of the code are for initializing variables. We want to define ``f0``, ``f1``, ``error``, and ``tol``. 
The next few lines are the informative print statements and then we being the while loop. The line ``while (error > tol and iter < maxiter):`` implies that we want to run the loop as long as the error is 
greater than the tolerance AND as long as the number of iterations is less than the number of the inputted maximum number 
of iterations. Then we define an ``x2`` using the secant method. This is going to be root approximation. Our error will 
be the absolute value of ``x2`` minus ``x1``. Then we print our approximation. Finally, we need to reinitialize the variables
and run the loop again until one of the loops conditions is met.

**Implementation/Code:** The following is the code for newtons_method()

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

**Special Note:** This method is dependent on proper initial root approximations as well as inputted functions. Without 
knowledge of the behavior of the function, a poor initial root approximation may result in confusing and/or unhelpful final
root approximations.

**Last Modified:** September/2022
