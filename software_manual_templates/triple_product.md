# Math 4610 Linear Algebra Operation: Triple Product of Three Vectors

**Routine Name:**           triple_product

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the triple product of 3 given 3x1 vectors. The purpose of creating this routine 
is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes 3 vectors of length 3x1.

**Output:** The output of this function will be a number.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      v = [4, 5, 6]
      w = [7, 8, 9]
      print("The triple product of u, v and w is: " + str(triple_product(u, v, w)))

Output from the lines above:

      The triple product of u, v and w is: 0

The code output suggests that the triple product between ``u``, ``v`` and ``w`` is ``0``. The function that 
produced this output can be found at the bottom of this file. Now let's get into the function itself:

In this function, the first 4 lines are checking to see whether the two vectors are the same length and if they are 3x1 
in dimensions. If either of these conditions are not met then we cannot take the triple product. After the checks, we 
define a ``sum``. Then we add the 3 values to this sum. All of which are determinants of sub-elements of the 
vectors ``y`` and ``z``, multiplied by the elements in ``x``. Finally, we return ``sum``, which is the corresponding triple 
product of ``x``, ``y`` and ``z``.

**Implementation/Code:** The following is the code for triple_product()

```python
def triple_product(x, y, z):
    if len(x) != 3 or len(y) != 3:
        return "Vectors for cross product must have length of 3."
    if len(x) != len(y):
        return "Vectors must be the same length."

    sum = 0

    sum += x[0]*(y[1]*z[2] - y[2]*z[1])
    sum += x[1]*(-(y[0]*z[2] - y[2]*z[0]))
    sum += x[2]*(y[0]*z[1] - y[1]*z[0])

    return sum
```

**Last Modified:** November/2022