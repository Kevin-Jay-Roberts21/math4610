# Math 4610 Root Finding Problem: Newtons Method

**Routine Name:**           newtons_method

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will iterate through a loop given a function f(x) to solve for when x = 0 (or the 
roots of f(x)). The purpose of creating this as opposed to other methods is because it's accurate, but may take more time. 
We like to use this method when we assume there is more than one solution.

**Input:** The inputs are a function, the function's derivative, an initial guess, tolerance, and max iterations.

**Output:** This routine outputs the root approximation after each iteration as well as the final approximation.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      newtons_method("x*np.exp(-x)", "-x*np.exp(-x) + np.exp(-x)", -3, 0.000001, 10)

Output from the lines above:

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

The code output suggests that our final approximation is very close to 0. See the code at the bottom of the file as I explain
what's going on for this function. 

The first 5 lines I initialize variables ``f0``, ``fp``, ``error``, ``iter``. Then I make a print statement to start off 
loop. The line ``while (error > tol and iter < maxiter):`` implies that we want to run the loop as long as the error is 
greater than the tolerance AND as long as the number of iterations is less than the number of the inputted maximum number 
of iterations. Next, we approximate ``x1`` by using newtons method. After which we calculate the error, and make a print
statement to inform the user where the program is at. Then we reinitialize all the variables and run through the loop again. 
Finally, when the loop finishes, we print the final approximation.

**Implementation/Code:** The following is the code for newtons_method()

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

**Special Note:** This method is dependent on proper initial root approximations as well as inputted functions. Without 
knowledge of the behavior of the function, a poor initial root approximation may result in confusing and/or unhelpful final
root approximations.

**Last Modified:** September/2022
