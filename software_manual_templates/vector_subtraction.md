# Math 4610 Linear Algebra Operation: Vector Subtraction

**Routine Name:**           vector_subtraction

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform vector subtraction between two vectors of appropriate dimensions. The purpose
of creating this routine is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes two lists (vectors) u and v.

**Output:** The output of this function will be a list (vector) that is the result of the two inputted vectors being subtracted.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      v = [4, 5, 6]
      print("The difference of vector u and v is: " + str(vector_subtraction(u, v)))

Output from the lines above:

      The difference of vector u and v is: [-3, -3, -3]

The code output suggests that the two vectors (u and v) subtracted together are ``[-3, -3, -3]``. The function that produced this
output can be found at the bottom of this file. Now let's get into the function itself:

In the first line we need to check if the vectors being subtracted are the same length. We cannot perform any operation if otherwise.
Then we define a new, empty vector which will be the resulting vector we return. Then we start a loop the spans the length
of the vectors inputted. For every iteration we need to subtract an elements to the ``new_vector`` that is an element of the vector
``x`` added with an element of the vector ``y``. Finally, we return the new vector.

**Implementation/Code:** The following is the code for vector_subtraction()

```python
def vector_subtraction(x, y):
    if len(x) != len(y):
        return "Vectors must be the same length."
    new_vector = []
    for i in range(0, len(x)):
        new_vector.append(x[i] - y[i])

    return new_vector
```

**Last Modified:** November/2022