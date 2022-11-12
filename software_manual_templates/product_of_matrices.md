# Math 4610 Linear Algebra Operation: Product of Two Matrices

**Routine Name:**           product_of_matrices

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the product of two given matrices with correlated dimensions. The purpose 
of creating this routine is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes two multidimensional lists (matrices) with correlated dimensions.

**Output:** The output of this function will be a multidimensional list (a matrix).

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
      print("The product of matrices A and B is: " + str(product_of_matrices(A, B)))

Output from the lines above:

      The product of matrices A and B is: [[84, 90, 96], [201, 216, 231], [318, 342, 366]]

The code output suggests that the product of the matrix ``A`` and ``B`` is ``[[84, 90, 96], [201, 216, 231], [318, 342, 366]]``. 
The function that produced this output can be found at the bottom of this file. Now let's get into the function itself:

The first 6 lines of code in the function are checks to make sure that ``a`` and ``b`` are actually multidimensional lists
(matrices). The next 2 lines of code in the function are checks to make sure that the number of rows, and the number of columns
are the same between ``a`` and ``b``. The next line of code defines a new matrix. Then I start a loop where I go through 
every row of ``a``. Then I define a ``new_row`` because we'll need to add this to the ``new_matrix``. Then I create another
loop that iterates through the number of rows that matrix ``a`` has again. In this iteration, I create a ``sum`` value to 
keep track of the dot product of the rows and columns of ``a`` and ``b``. Next I add yet another loop to run through the 
columns of b. This is where we will add to ``sum``. We add the element ``a[i][k] * b[k][j]`` to the sum. This element is
multiplication of a row element in ``a`` by a column element in ``b``. After this loop finishes, we need to add this summation
to the ``new_row``, and then after the next loop ends, we must add the ``new_row`` to our ``new_matrix``. Then, finally 
we can return the matrix. This ``new_matrix`` is the product of matrix ``a`` * ``b``.

**Implementation/Code:** The following is the code for product_of_matrices()

```python
def product_of_matrices(a, b):

    # checking for lists
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    for i in range(0, len(b)):
        if type(b[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."

    if len(a[0]) != len(b) or len(b[0]) != len(a):
        return "The # of columns of the first matrix must equal the # of rows of the second matrix and vice versa."

    new_matrix = []

    for i in range(0, len(a)):
        new_row = []

        for j in range(0, len(a)):
            sum = 0
            for k in range(0, len(b)):
                sum += a[i][k]*b[k][j]
            new_row.append(sum)
        new_matrix.append(new_row)

    return new_matrix
```

**Last Modified:** November/2022