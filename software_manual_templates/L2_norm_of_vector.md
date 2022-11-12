# Math 4610 Linear Algebra Operation: L2 Norm of a Vector

**Routine Name:**           L2_norm_of_vector

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the L2 norm of a given vector, more specifically, the distance of the
vector from the origin of the vector space. The purpose of creating this routine is to make linear algebra operations easier 
for future computations and necessary usages.

**Input:** The input for this function includes a single vector.

**Output:** The output of this function will be a list (vector).

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      print("The L2 norm of u is: " + str(L2_norm_of_vector(u)))

Output from the lines above:

      The L2 norm of u is: 3.7416573867739413

The code output suggests that the vector ``[1, 2, 3]`` has an L2 norm of ``3.74``. The function that produced this
output can be found at the bottom of this file. Now let's get into the function itself:

For this routine we do not need to perform any length checks for the inputted vector. Firstly we define a sum that we must 
return ``sum_of_squared_elements``. Then we must start the loop that iterates for however large the inputted vector ``x``
is. For each iteration, we increase the sum by the square of each of the vector ``x``'s elements. Then we take the square 
root of the sum and define it as ``norm``. Finally, we return ``norm``. This the L2 norm of the vector ``x``.

**Implementation/Code:** The following is the code for L2_norm_of_vector()

```python
def L2_norm_of_vector(x):

    sum_of_squared_elements = 0
    for i in range(0, len(x)):
        sum_of_squared_elements += (x[i]*x[i])

    norm = np.sqrt(sum_of_squared_elements)

    return norm
```

**Last Modified:** November/2022