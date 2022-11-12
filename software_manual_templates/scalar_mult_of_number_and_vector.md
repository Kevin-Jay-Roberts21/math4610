# Math 4610 Linear Algebra Operation: Scalar Multiplication of a Number and a Vector

**Routine Name:**           scalar_mult_of_number_and_vector

**Author:** Kevin Roberts

**Language:** Python

**Description/Purpose:** This routine will perform the multiplication of a scalar to a vector. The purpose
of creating this routine is to make linear algebra operations easier for future computations and necessary usages.

**Input:** The input for this function includes a number and a vector.

**Output:** The output of this function will be a list (vector) that is the result of a vector being multiplied by a scalar.

**Usage/Example:**

The function will be called with inputs (specified above) like the following: 

      u = [1, 2, 3]
      number = 2
      print("The scalar multiple of number=2 and u is: " + str(scalar_mult_of_number_and_vector(number, u)))

Output from the lines above:

      The scalar multiple of number=2 and u is: [2, 4, 6]

The code output suggests that the vector ``[1, 2, 3]`` after being multiplied by a scalar ``2``, becomes ``[2, 4, 6]``. The function that produced this
output can be found at the bottom of this file. Now let's get into the function itself:

We do not need to make any vector or matrix checks for this operation. We first define a vector ``new_vector`` that we will
return after operations on it are finished. We then iterate through a loop that is as long as the inputted vector ``x``.
In every iteration we multiply an element of ``x`` by the scalar ``number``, then add it to ``new_vector``. Finally, we 
return the ``new_vector``.

**Implementation/Code:** The following is the code for scalar_mult_of_number_and_vector()

```python
def scalar_mult_of_number_and_vector(number, x):

    new_vector = []
    for i in range(0, len(x)):
        new_vector.append(number * x[i])

    return new_vector
```

**Last Modified:** November/2022