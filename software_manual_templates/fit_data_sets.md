# Math 4610 Root Finding Problem: Secant Method

**Routine Name:**           fit_data_sets

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will fit data sets to a linear polynomial. The purpose is to experiment with linear 
regression.

**Input:** The inputs are a data array x (input values), and a data array y (the measured outputs).

**Output:** This routine outputs the approximated linear regression, given the data points.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      y = []
      for i in range(0, len(x)):
          y.append(second_derivative_approx("((x - np.pi/2) * np.tan(x))/(x*x + 65)", x[i], 0.001))
    
      fit_data_sets(x, y)

Notice how we create the x array, and then use the second derivative approximation function to approximate the y data set.
Then we put both data sets into fit_data_sets(x, y).

Ignoring the print statements that will be generated from the second_derivative_approx function, the output from the lines above
are:

      The approximate coefficients for the linear fit are:
      a: 1.7625076537953326
      b: -0.9470139831199864

The code output is a computed a and b to fit the data given, a line such that y = a(x) + b. Let's describe now, the function: 

The first line is computing an n which is going to be the number of rows of matrix A. We desire to make a linear transformation
to solve for a and b. Thus, we multiply A by it's transpose. This gets us a square matrix and the computed values ``a11``, 
``a12``, ``a21``, and ``a22`` are the elements of the matrix. Similarly, we must solve for the multiplication of the transpose of
A to the dataset y, giving us our b1 and b2 values. We now have something of the sort: Ax = b. By taking the inverse of A 
and multiplying it to both sides of the equation, we solve for b and a. Finally, we print these values.

**Implementation/Code:** The following is the code for second_derivative_approx()

    def fit_data_sets(x, y):
        n = len(x) # here n = 10
    
        a11 = n
    
        a12 = x[0]
        for i in range(1, n):
            a12 = a12 + x[i]
    
        a21 = a12
    
        a22 = (x[0] * x[0])
        for i in range(1, n):
            a22 = a22 + (x[i] * x[i])
    
        b1 = y[0]
        for i in range(1, n):
            b1 = b1 + y[i]
    
        b2 = y[0] * x[0]
        for i in range(1, n):
            b2 = b2 + (x[i] * y[i])
    
        detA = (a11 * a22) - (a12 * a21)
        a = ((a22 * b1) - (a12 * b2)) / detA
        b = ((-a21 * b1) + (a11 * b2)) / detA
    
        print("The approximate coefficients for the linear fit are:")
        print("a: " + str(a))
        print("b: " + str(b))

**Last Modified:** October/2022