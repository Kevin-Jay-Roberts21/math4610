# Math 4610 Linear Algebra Operation: Cross Product of Two Vectors

**Routine Name:**           cross_product

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the cross product of two given 3x1 vectors. The purpose of creating this routine 
is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes two vectors of the same length.

**Output:** The output of this function will be a 3x1 vector.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      v = [4, 5, 6]
      print("The cross product of u and v is: " + str(cross_product(u, v)))

Output from the lines above:

      The cross product of u and v is: [-3, 6, -3]

The code output suggests that the cross product between ``u`` and ``v`` is ``[-3, 6, -3]``. The function that 
produced this output can be found at the bottom of this file. Now let's get into the function itself:

In this function, the first 4 lines are checking to see whether the two vectors are the same length and if they are 3x1 
in dimensions. If either of these conditions are not met then we cannot take the cross product. After the checks, we 
define a ``new_vector``. Then we add the 3 elements to this vector. All of which are determinants of sub-elements of the 
vectors ``x`` and ``y``. Finally, we return ``new_vector``, which is the corresponding cross product of ``x`` and ``y``.

**Implementation/Code:** The following is the code for cross_product()

```python
def cross_product(x, y):
    if len(x) != 3 or len(y) != 3:
        return "Vectors for triple product must have length of 3."
    if len(x) != len(y):
        return "Vectors must be the same length."
    new_vector = []

    new_vector.append(x[1]*y[2] - x[2]*y[1])
    new_vector.append(-(x[0]*y[2] - x[2]*y[0]))
    new_vector.append(x[0]*y[1] - x[1]*y[0])

    return new_vector
```

**Last Modified:** November/2022