# Math 4610 Root Finding Problem: Secant Method

**Routine Name:**           explicit_euler_logistic

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** To conduct an approximate solution of the initial value problem of the logistic equation using
the explicit euler method. Th purpose is to approximate the solution using derivatives without actually calculating the
solution.

**Input:** The inputs are alpha a, beta b, P0 (initial condition), an initial time t0, the logistic equation f, a final time T, and n.

**Output:** This routine outputs the approximation of the logistic equation at the finaly time step T. It also outputs the
graph of the logistic equation.

**Usage/Example:**

The function will be called with inputs (specified above) like the following:

      a = 0.2
      b = 0.0005
      P0 = 10.0
      explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)

Output from the lines above give a final approximation at T and a graph of the function:

      Final Approximation: 0.13607479095833241
      [graph](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/approximating_functions/second_derivative_approx.py)

I've computed the same for different alpha and beta values as well:

Input:

Output:
      Final Approximation: 0.00045465986240039724
      [graph](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/approximating_functions/second_derivative_approx.py)
      Final Approximation: 0.2940624089205812
      [graph](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/approximating_functions/second_derivative_approx.py)


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