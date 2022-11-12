# Math 4610 Linear Algebra Operation: Vector Addition

**Routine Name:**           vector_addition

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform vector addition between two vectors of appropriate dimensions. The purpose
of creating this routine is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes two lists (vectors) u and v.

**Output:** The output of this function will be a list (vector) that is the result of the two inputted vectors being added.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      v = [4, 5, 6]
      print("The addition of vector u and v is: " + str(vector_addition(u, v)))

Output from the lines above:

      The addition of vector u and v is: [5, 7, 9]

The code output suggests that the two vectors (u and v) added together are ``[5, 7, 9]``. The function that produced this
output can be found at the bottom of this file. Now let's get into the function itself:

In the first line we need to check if the vectors being added are the same length. We cannot perform any operation if otherwise.
Then we define a new, empty vector which will be the resulting vector we return. Then we start a loop the spans the length
of the vectors inputted. For every iteration we need to add an elements to the ``new_vector`` that is an element of the vector
``x`` added with an element of the vector ``y``. Finally, we return the new vector.

**Implementation/Code:** The following is the code for vector_addition()

```python
def vector_addition(x, y):
        if len(x) != len(y):
            return "Vectors must be the same length."
        new_vector = []
        for i in range(0, len(x)):
            new_vector.append(x[i] + y[i])
    
        return new_vector
```

**Last Modified:** November/2022