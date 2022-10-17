# Math 4610 Root Finding Problem: Secant Method

**Routine Name:**           second_derivative_approx

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will compute an approximation of a second derivative of a function. It's purpose 
is to be able to compute approximations to functions where the exact solution cannot be found.

**Input:** The inputs are a function, x0 (where the approximation is to be computed), and an initial increment h parameter.

**Output:** This routine outputs the approximation given the above inputs.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      second_derivative_approx("((x - np.pi/2) * np.tan(x))/(x*x + 65)", np.pi/4, 0.001)

Output from the lines above:

      Second Derivative Approximation at x0 = 0.7853981633974483:
      f''(x0) = 0.013849714822905534

The code output is an approximation of the second derivative of the given function ``f``. Let's delve into the code: 

The first six lines of the code are computing an approximation of ``f_left``, ``f_right`` and ``f_center``. Then we approximate 
the second derivative by using the formula: ``second_deriv = (f_right - 2*f_center + f_left) / (h*h)``. Finally, we print 
out the approximation.

**Implementation/Code:** The following is the code for second_derivative_approx()

    def second_derivative_approx(f, x0, h):

        x = x0 - h
        f_left = float(eval(f))
        x = x0 + h
        f_right = float(eval(f))
        x = x0
        f_center = float(eval(f))
    
        second_deriv = (f_right - 2*f_center + f_left) / (h*h)
    
        print("Second Derivative Approximation at x0 = " + str(x0) + ":")
        print("f''(x0) = " + str(second_deriv))
    
        return second_deriv

**Last Modified:** October/2022