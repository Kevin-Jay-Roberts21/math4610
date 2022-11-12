# Math 4610 Linear Algebra Operation: L Infinity Norm of a Vector

**Routine Name:**           Linf_norm_of_vector

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the L Infinity norm of a given vector, more specifically, the largest 
element contained in a given vector. The purpose of creating this routine is to make linear algebra operations easier 
for future computations and necessary usages.

**Input:** The input for this function includes a single vector.

**Output:** The output of this function will be a list (vector).

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      print("The L_infinity norm of u is: " + str(Linf_norm_of_vector(u)))

Output from the lines above:

      The L_infinity norm of u is: 3

The code output suggests that the vector ``[1, 2, 3]`` has an L infinity norm of ``3``. The function that produced this
output can be found at the bottom of this file. Now let's get into the function itself:

For this routine we do not need to perform any length checks for the inputted vector. Firstly we define a max that we must 
return ``max``, initially, we just set it to the first element of the given vector ``x``. Then we must start the loop that 
iterates for however large the inputted vector ``x``is minus 1. For each iteration, we check to see if the next element in
``x`` is larger than the previous. If it is, then we redefine the max value. Finally, we return the max. This is the L 
infinity norm of a given vector.

**Implementation/Code:** The following is the code for Linf_norm_of_vector()

```python
def Linf_norm_of_vector(x):

    max = x[0]
    for i in range(1, len(x)):
        if x[i] > max:
            max = x[i]

    return max
```

**Last Modified:** November/2022