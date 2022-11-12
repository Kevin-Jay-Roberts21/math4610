# Math 4610 Linear Algebra Operation: Sum of Two Matrices

**Routine Name:**           sum_of_matrices

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the summation of two given matrices with equal dimensions. The purpose 
of creating this routine is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes two multidimensional lists (matrices) with equal dimensions.

**Output:** The output of this function will be a multidimensional list (a matrix).

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
      print("The sum of matrices A and B is: " + str(sum_of_matrices(A, B)))

Output from the lines above:

      The sum of matrices A and B is: [[11, 13, 15], [17, 19, 21], [23, 25, 27]]

The code output suggests that the addition of the matrix ``A`` and ``B`` is ``[[11, 13, 15], [17, 19, 21], [23, 25, 27]]``. 
The function that produced this output can be found at the bottom of this file. Now let's get into the function itself:

The first 6 lines of code in the function are checks to make sure that ``a`` and ``b`` are actually multidimensional lists
(matrices). The next 5 lines of code in the function are checks to make sure that the number of rows, and the number of columns
are the same between ``a`` and ``b``. The next line of code defines a new matrix. Then I start a loop where I go through 
every row of ``a``. Then I define a ``new_row`` because we'll need to add this to the ``new_matrix``. Then I create another
loop that iterates through the number of columns that matrix ``a`` has. In this iteration, I add the summation of the elements
in ``a`` and in ``b`` and add them to the ``new_row``. After which I add the ``new_row`` to the ``new_matrix``. Finally, 
I return the new matrix which is the resulting matrix for when matrix ``a`` is added to matrix ``b``.

**Implementation/Code:** The following is the code for sum_of_matrices()

```python
def sum_of_matrices(a, b):
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    for i in range(0, len(b)):
        if type(b[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    if len(a) != len(b):
        return "Matrices must have the same number of rows."
    for i in range(0, len(a)):
        if len(a[i]) != len(b[i]):
            return "Matrices must have the same number of columns."

    new_matrix = []

    for i in range(0, len(a)):
        new_row = []
        for j in range(0, len(a[i])):
            new_row.append(a[i][j] + b[i][j])
        new_matrix.append(new_row)

    return new_matrix
```

**Last Modified:** November/2022