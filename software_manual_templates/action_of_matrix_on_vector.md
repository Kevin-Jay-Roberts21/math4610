# Math 4610 Linear Algebra Operation: Action of a Matrix on a Vector

**Routine Name:**           action_of_matrix_on_vector

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the action of a matrix on a given vector where the dimensions of both
are correlated with each other. The purpose of creating this routine is to make linear algebra operations easier for future 
computations and necessary usages.

**Input:** The input for this function includes one matrix and one vector with correlated dimensions.

**Output:** The output of this function will be a vector.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      print("The action of matrix A on the vector u is: " + str(action_of_matrix_on_vector(A, u)))

Output from the lines above:

      The action of matrix A on the vector u is: [14, 32, 50]

The code output suggests that the action of the matrix ``A`` on ``u`` is ``[14, 32, 50]``. The function that 
produced this output can be found at the bottom of this file. Now let's get into the function itself:

In this function, the first 5 lines are checking to see whether the vector has the same number of rows as the matrix 
has columns. It's also checking to make sure that ``a`` is a matrix and not just a vector. After the checks, we 
define a ``new_vector``. A for loop is created to calculate the sum of the dot product between the first row of the matrix 
``a`` and the column of vector ``x``. When the sum is calculated, it's added to ``new_vector``. Finally, once the ``new_vector``
contains all it's new elements, it is returned.

**Implementation/Code:** The following is the code for action_of_matrix_on_vector()

```python
def action_of_matrix_on_vector(a, u):
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    if len(a) != len(u):
        return "The # of columns of the matrix must be the same number of rows of the vector."
    new_vector = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(u)):
            sum += a[i][j] * u[j]
        new_vector.append(sum)

    return new_vector
```

**Last Modified:** November/2022