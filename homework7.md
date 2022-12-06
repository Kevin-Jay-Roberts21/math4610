# Homework 7
Kevin Roberts

## Task 1 

I have created python code to produce the product of two matrices and this code can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/linear_algebra_operations/linear_algebra_operations.py) 
along with all  the other linear algebra operations. I converted this code to c code and this code can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/c_code/homework_7_c_code/main.c). 
To reduce complications, I wrote this operation to only take 3 by 3 matrices in c code. To get the product of any other square
matrices, I'll simply have to know the dimensions, and the change in c code can be made. My python code is a little more
flexible as it takes matrices of any dimensions, and they don't have to be square.

The function I wrote in c takes in two multidimensional arrays and I call the function in the ``main`` function: 

```
int main ()
{
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[3][3] = {{10, 11, 12}, {13, 14, 15}, {16, 17, 18}};
    return matrix_product(A, B);
}
```

THe corresponding output from running the code: 

```
84 90 96 
201 216 231 
318 342 366 
Program ended with exit code: 96
```

The function I wrote in c to produce the matrix produce looks like the following:

```
int** matrix_product(int a[3][3], int b[3][3])
{
    int new_matrix[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};

    for (int i = 0; i < 3; i++)
    {
        int new_row[3] = {0, 0, 0};
        
        for (int j = 0; j < 3; j++)
        {
            double sum = 0.0;
            for (int k = 0; k < 3; k++)
            {
                sum += a[i][k] * b[k][j];
            }
            new_row[j] = sum;
        }
        for (int l = 0; l < 3; l++)
        {
            new_matrix[i][l] = new_row[l];
        }
        
    }
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            
            printf("%d ", new_matrix[i][j]);
        }
        printf("\n");
    }
    
    return new_matrix;
}
```

I modified the function above code to use openmp parallel programming. The following is what I wrote that produced the same output: 

```
int** matrix_product_parallel(int a[3][3], int b[3][3])
{
    int new_matrix[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
    int k, nthreads=8, realsum, sum[NUM_THREADS];
    omp_set_num_threads(NUM_THREADS);
    
    for (int i = 0; i < 3; i++)
    {
        int new_row[3] = {0, 0, 0};
        
        for (int j = 0; j < 3; j++)
        {
            // parallelizing here
            #pragma omp parallel
            {
              int k, id, nthrds;
              id = omp_get_thread_num();
              nthrds = omp_get_num_threads();
              if (id == 0) nthreads = nthrds;
              for (k=id, sum[id] = 0.0; k < 3; k=k+nthrds) {
                  sum[id] += a[i][k] * b[k][j];
              }
            }
            for (k = 0, realsum = 0.0; k < nthreads; k++)
                realsum += sum[k];
            
            new_row[j] = realsum;
        }
        for (int l = 0; l < 3; l++)
        {
            new_matrix[i][l] = new_row[l];
        }
        
    }
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            
            printf("%d ", new_matrix[i][j]);
        }
        printf("\n");
    }
    
    return new_matrix;
}
```

## Task 2 

I wrote code in c to compute the hadamard product of two vectors. The following intput in the main function looks like the 
following: 

```
int main ()
{
    int u[3] = {1, 2, 3};
    int v[3] = {4, 5, 6};
    
    return hadamard_product(u, v);
}
```

The lengths of the vectors are set, but again, these vector legnths can be changed easily to compute different vectors. The
corresponding output: 

```
New Vector: 4 10 18 
Program ended with exit code: 48
```

And finally the function I wrote in c to compute this operation (this code can also be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/c_code/homework_7_c_code/main.c)):

```
int* hadamard_product(int u[vector_length], int v[vector_length])
{
    
    int new_vector[vector_length];
    
    for (int i = 0; i < vector_length; i++)
    {
        new_vector[i] = u[i] * v[i];
    }
    //    printing the new vector output
    printf("New Vector: ");
    for (int i = 0; i < vector_length; i++) {
        printf("%d ", new_vector[i]);
    }
    printf("\n");
    
    return new_vector;
}
```

## Task 3 

For this task I parallelized the function I provided above. The parallelized function looks like the following: 

```
int* hadamard_product_parallel(int u[vector_length], int v[vector_length])
{
    int j, nthreads=8, realsum, sum[NUM_THREADS];
    omp_set_num_threads(NUM_THREADS);
    
    
    int new_vector[vector_length];
    
    for (int i = 0; i < vector_length; i++)
    {
        // parallelizing here
        #pragma omp parallel
        {
          int j, id, nthrds;
          id = omp_get_thread_num();
          nthrds = omp_get_num_threads();
          if (id == 0) nthreads = nthrds;
          for (j=id, sum[id] = 0.0; j < 3; j=j+nthrds) {
              sum[id] = u[i] * v[i];
          }
        }
        for (j = 0, realsum = 0.0; j < nthreads; j++)
            realsum += sum[j];
        
        new_vector[i] = realsum;
    }
    //    printing the new vector output
    printf("New Vector: ");
    for (int i = 0; i < vector_length; i++) {
        printf("%d ", new_vector[i]);
    }
    printf("\n");
    
    return new_vector;
}
```

And it produced the same output as the non parallelized function.

## Task 4 

For this task, I wrote my code in python. To test this code on really large matrices, I created loops to populate matrices
with 100 rows and 100 columns. The first matrix A1 contains only 0's and 1's and alternates between 0 and 1 for each element,
starting at 0. The matrix B1 is the exact same, except starting with 1. Thus, I expect the hadamard matrix product to be 
a matrix containing only zeros. The following are my inputs: 

```
A1 = []
B1 = []
for i in range(0, 100):
    new_row = []
    for j in range(0, 100):
        if (j % 2) == 0:
            new_row.append(0)
        else:
            new_row.append(1)
    A1.append(new_row)

for i in range(0, 100):
    new_row = []
    for j in range(0, 100):
        if (j % 2) != 0:
            new_row.append(0)
        else:
            new_row.append(1)
    B1.append(new_row)
print("The Hadamard product of matrix A1 and B1 is: " + str(hadamard_product_of_matrices(A1, B1)))
```

I got the corresponding output (which is a 0 matrix with 100 rows and 100 columns):

```
The Hadamard product of matrix A1 and B1 is: [[0, 0, 0, 0, 0, 0, 0, 0, 0, ...
```

The function that ran the code is the following: 

```
def hadamard_product_of_matrices(a, b):

    # checking for lists
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    for i in range(0, len(b)):
        if type(b[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."

    if len(a[0]) != len(b[0]) or len(a) != len(b):
        return "The # of columns of the first matrix must equal the # of cols of the second matrix and same with number of rows."

    new_matrix = []

    for i in range(0, len(a)):
        new_row = []
        for j in range(0, len(b)):
            element = a[i][j]*b[i][j]
            new_row.append(element)
        new_matrix.append(new_row)

    return new_matrix
```

## Task 5 

I decided to create the outer product of two vectors in python code. The following is what I inputted: 

```
u = [1, 2, 3, 4, 5]
v = [6, 7, 8, 9, 10]
print("The outer product of vectors u and v is: " + str(outer_product(u, v)))
```

The corresponding output: 

```
The outer product of vectors u and v is: [[6, 7, 8, 9, 10], [12, 14, 16, 18, 20], [18, 21, 24, 27, 30], [24, 28, 32, 36, 40], [30, 35, 40, 45, 50]]
```

And finally the code I wrote to do the operations: 

```
def outer_product(u, v):
    new_matrix = []

    # check to make sure the lengths of the vectors are the same
    if len(u) != len(v):
        return "Vectors must be the same length."

    for i in range(0, len(u)):
        new_row = []
        for j in range(0, len(v)):
            element = u[i]*v[j]
            new_row.append(element)
        new_matrix.append(new_row)

    return new_matrix
```

The routine can be extended to matrices. The way to do it would be to take the first row of a matrix A, transpose it, and
multiply it by the first row of a matrix B. The add that outer product to the transpose of the second row of A, multiplied
by the second row of B. This matrix multiplication is now represented as the two outer products of two vectors. The restrictions
of the matrices are similar to that of regular matrix multiplication. Namely, the matrix A being multiplied by matrix B 
must have the same number of columns as the matrix B has rows. To implement an algorithm for the outer product of two vectors
in parallel, I'd do something very similar to what I did in writing the hadamard product of two vectors in parallel. I'd
optimize the number of threads my machine has (which is 8), and use them together to perform all the products of the vector
elements.