# Math 4610 Root Finding Problem: Bisection

**Routine Name:**           fixed_point

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will approximate a root of a function by subtracting an approximation by a given 
previous approximation. There are two functions incorporated into finding the root, a ``g1`` function and a ``g2`` function.
The purpose of these functions are to approximate a root.

**Input:** The inputs needed for this routine are a function, a root approximation, tolerance, and a max number of iterations.

**Output:** This routine outputs the root approximation after each iteration as well as the final approximation.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      fixed_point("x*np.exp(-x)", 1.1, 0.0000001, 20)

Output from the lines above:

      Results from g1 iteration method:
      Iterations                Approx. Root Location     Error                    
      0                         0.7338418079              0.3661581921             
      1                         0.3815528729              0.3522889350             
      2                         0.1210284632              0.2605244098             
      3                         0.0137961869              0.1072322762             
      4                         0.0001890278              0.0136071591             
      5                         0.0000000357              0.0001889921             
      6                         0.0000000000              0.0000000357             
      Final Approximation: 0.0000000000
      
      
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

The code output suggests that our final approximation from the g1 function is 0 and from the g2 function it's about 1. This 
suggests that certain approximating methods may work better or worse for certain given functions.

For the first part of the function before we start the while loop, we define our error, the initial x0 approximation, and 
we declare the initial number of iterations. Then we add a few print statements to let the user know what's happening inside
the function. Then we begin the while loop and will run the loop for as long as our error is greater than our tolerance 
and as long as the number of iterations does not exceed the max number of iterations. Inside the loop we let ``x = x0`` 
and define our x1 approximation. This approximation is a result from the ``g1`` method, where we take the absolute value 
of the difference of f (evaluated at x0) by x0. Then we evaluate the error, and reset x0 to be x1. Further, once we break 
out of the loop, we perform the same fixed point approximation in another while loop, only we use the g2 function to approximate
the root.

**Implementation/Code:** The following is the code for fixed_point()

    def g1(f, x):
        gval = np.abs(x - f)
        return gval
    def g2(f, x):
        gval = np.abs(np.exp(-x) - f)
        return gval

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
            x = x0
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
            x = x0
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

**Special Note:** This method is dependent on proper initial root approximations as well as inputted functions. Without 
knowledge of the behavior of the function, a poor initial root approximation may result in confusing and/or unhelpful final
root approximations.

**Last Modified:** September/2022

