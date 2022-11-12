# Math 4610 Linear Algebra Operation: Dot Product of Two Vectors

**Routine Name:**           dot_product

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the dot product of two given vectors. The purpose of creating this routine 
is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes two vectors of the same length.

**Output:** The output of this function will be a single number.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      v = [4, 5, 6]
      print("The dot product of u and v is: " + str(dot_product(u, v)))

Output from the lines above:

      The dot product of u and v is: 32

The code output suggests that the vector ``[1, 2, 3]`` dotted with the vector ``[4, 5, 6]`` is ``32``. The function that 
produced this output can be found at the bottom of this file. Now let's get into the function itself:

We must make an initial check to ensure that the two inputted vectors have the same dimensions. After this check, ``sum``
is defined and will be what we return. Then we start a loop that iterates for however long the given vector lengths are. 
in the loop, for each of iteration, we increase the sum by the multiplication of an element in ``x`` and ``y``. Finally, we 
return the sum. This sum is the dot product of the two vectors.

**Implementation/Code:** The following is the code for dot_product()

```python
def dot_product(x, y):
    if len(x) != len(y):
        return "Vectors must be the same length."
    sum = 0
    for i in range(0, len(x)):
        sum += (x[i]*y[i])

    return sum
```

**Last Modified:** November/2022