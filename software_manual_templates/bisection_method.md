# Math 4610 Root Finding Problem: Bisection

**Routine Name:**           bisection

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will approximate a root by cutting an interval in half continuously until the root
is found. The purpose is to find a root when given any function f(x).

**Input:** The inputs needed for this routine are a function, start point a, end point b, and a tolerance.

**Output:** This routine outputs the root approximation after each iteration as well as the final approximation.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      bisection("x*np.exp(-x)", -5, 1, 0.0001)

Output from the lines above:

      Results from bisection method:
      Iterations                Approx. Root Location    
      1                         -2.0000000000            
      2                         -0.5000000000            
      3                         0.2500000000             
      4                         -0.1250000000            
      5                         0.0625000000             
      6                         -0.0312500000            
      7                         0.0156250000             
      8                         -0.0078125000            
      9                         0.0039062500             
      10                        -0.0019531250            
      11                        0.0009765625             
      12                        -0.0004882812            
      13                        0.0002441406             
      14                        -0.0001220703            
      15                        0.0000610352             
      Final Approximation: 6.103515625e-05

The code output suggests that our final approximation is very close to 0. See the code at the bottom of the file as I explain
what's going on for this function. 

The first bit of the function before the loop begins, we initialize variables: ``fa``, ``fb``, and ``k``. Then we add a 
print statement to notify the user the for loop is about to begin. The loop iterates from 1 to k. The first line is 
saying that c is the midpoint of the interval that was given. We then check to see if ``c == 0``. If it does then our interval 
is tiny and we are done! That's will be our approximation. But if it isn't, then we define a function ``fc``. We then check
if the said function, multiplied by ``fa`` is less than 0. This means we must reinitialize b and fb, if not, we must reinitialize
a and fa, then run through the loop again. Finally, we print the final approximation.

**Implementation/Code:** The following is the code for functional_iteration()

    def bisection(f, a, b, tol):

        # Initializing the starting variables
        x = a
        fa = float(eval(f))
        x = b
        fb = float(eval(f))
        k = (int)((np.log(tol/(b-a)))/(np.log(.5)) + 1) # this was given in the assignment and computed in class
    
        # note that we don't have to consider error here because it's taken into account in k
        print("Results from bisection method:")
        print("{:<25} {:<25}".format('Iterations', 'Approx. Root Location'))
    
        for iterations in range(1, k):
            c = .5 * (a + b)
            print("{:<25} {:<25}".format(iterations, "{:.10f}".format(c)))
            x = c
            if c == 0:
                print("Final Approximation: " + str(c))
                break
            fc = float(eval(f))
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
    
        print("Final Approximation: " + str(c))

**Special Note:** This method is dependent on proper initial root approximations as well as inputted functions. Without 
knowledge of the behavior of the function, a poor initial root approximation may result in confusing and/or unhelpful final
root approximations.

**Last Modified:** September/2022
