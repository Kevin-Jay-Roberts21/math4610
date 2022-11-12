# Math 4610 Linear Algebra Operation: L1 Norm of a Vector

**Routine Name:**           L1_norm_of_vector

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the sum of absolute vector values of a given vector. The purpose
of creating this routine is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes a single vector.

**Output:** The output of this function will be a list (vector).

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      print("The L1 norm of u is: " + str(L1_norm_of_vector(u)))

Output from the lines above:

      The L1 norm of u is: 6

The code output suggests that the vector ``[1, 2, 3]`` has an L1 norm of ``6``. The function that produced this
output can be found at the bottom of this file. Now let's get into the function itself:

For this routine we do not need to perform any length checks for the inputted vector. Firstly we define a sum that we must 
return ``sum_of_abs_elements``. Then we must start the loop that iterates for however large the inputted vector ``x``
is. For each iteration, we increase the sum by the absolute value of each of the vector ``x``'s elements. Finally, we return
this sum and this is the L1 norm of a vector.

**Implementation/Code:** The following is the code for L1_norm_of_vector()

```python
def L1_norm_of_vector(x):

    sum_of_abs_elements = 0
    for i in range(0, len(x)):
        sum_of_abs_elements += (np.abs(x[i]))

    return sum_of_abs_elements
```

**Last Modified:** November/2022