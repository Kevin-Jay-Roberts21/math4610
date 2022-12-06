# Homework 8
Kevin Roberts

## Task 1 

For this Task I wrote code in python that will compute the kronecker product of two matrices. The routine can be found in
the file [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/linear_algebra_operations/linear_algebra_operations.py), 
and I ran the code in the main.py file under Homework 8 [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py).

The inputs I used: 

```
A = [[1, 2], [3, 4]]
B = [[0, 5], [6, 7]]

print("The Kronecker Product of Matrix A and Matrix B is: \n" + str(kronecker_matrix_product(A, B)))
```

And the corresponding output: 

```
The Kronecker Product of Matrix A and Matrix B is: 
[0, 5, 0, 10]
[6, 7, 12, 14]
[0, 15, 0, 20]
[18, 21, 24, 28]
```

The code I wrote to perform this operation: 

```

```


## Task 2 

For this task I chose to write a version of the power method in python code. The code I wrote for computing the method can
be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/linear_algebra_operations/eigen_value_solutions.py) 
and I called the function in my main.py file under Homework 8 under Task 2 [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py). 
My inputs look like the following: 

```
A = [[1, 2, 3, 2, 4, 1, 2, 5, 3, 4],
     [3, 2, 1, 4, 2, 5, 3, 1, 5, 3],
     [2, 1, 3, 3, 2, 1, 2, 2, 1, 2],
     [2, 3, 4, 5, 3, 2, 1, 4, 5, 3],
     [3, 2, 1, 4, 3, 2, 1, 5, 5, 1],
     [1, 1, 1, 2, 4, 2, 5, 2, 1, 4],
     [3, 2, 4, 5, 3, 2, 3, 4, 1, 2],
     [4, 3, 1, 2, 1, 3, 4, 3, 5, 2],
     [1, 1, 1, 1, 2, 3, 5, 4, 3, 2],
     [4, 4, 3, 2, 1, 1, 2, 2, 3, 5]]
v = [3, 2, 2, 3, 2, 1, 4, 3, 2, 2]
tol = 0.00001
maxiter = 1000
print("Resulting lambda from the power method: " + str(power_method_1(A, v, tol, maxiter)))
```

The corresponding output I got is:

```
Resulting lambda from the power method: 26.565865437705927
```

Finally, the function I wrote to compute the eigen value approximation: 

```python
# For two matrix-vector products per iteration of the main loop
def power_method_1(a, v_0, tol, maxiter):

    l_0 = 0.0
    v = v_0
    error = 10 * tol
    iter = 0

    while (error > tol and iter < maxiter):
        y = action_of_matrix_on_vector(a, v)
        z = scalar_mult_of_number_and_vector(1/L2_norm_of_vector(y), y)
        l_1 = dot_product(z, action_of_matrix_on_vector(a, v))
        error = abs(l_1 - l_0)
        iter += 1
        v = z
        l_0 = l_1

    return l_0
```

Notice further that I am using my linear algebra operations that I wrote earlier in the course. Again, these linear algebra 
functions can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/linear_algebra_operations/linear_algebra_operations.py).

## Task 3 

This task is very similar to the one above, I used the exact same inputs only I used the function, namely, ``power_method_2``,
to compute the lambda approximation. This function, instead of computing two matrix vector operations per loop iteration, 
only computes one matrix-vector operation per iteration in the loop. The output I got was the same from task 2: 

```
Resulting lambda from the power method: 26.565865437705927
```

And the code I wrote to do this power method operation:

```python
# For one matrix-vector product per iteration of the main loop
def power_method_2(a, v_0, tol, maxiter):

    l_0 = 0.0
    v = v_0
    error = 10 * tol
    iter = 0
    y = action_of_matrix_on_vector(a, v)

    while (error > tol and iter < maxiter):
        z = scalar_mult_of_number_and_vector(1/L2_norm_of_vector(y), y)
        w = action_of_matrix_on_vector(a, z)
        l_1 = dot_product(z, w)
        error = abs(l_1 - l_0)
        iter += 1
        y = w
        l_0 = l_1

    return l_0
```

## Task 4 



## Task 5 

