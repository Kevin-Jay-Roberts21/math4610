# Homework 3 

## Task 1 

I have created python code to produce the product of two matrices and this code can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/linear_algebra_operations/linear_algebra_operations.py) 
along with all  the other linear algebra operations. I converted this code to c code and this code can be found [here](). 
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



## Task 3 


## Task 4 


## Task 5 
