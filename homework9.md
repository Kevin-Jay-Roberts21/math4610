# Homework 9
Kevin Roberts

## Task 1 

For this task I chose to write the inverse power method in python. I found that the input matrix for using this method is
critical. Since we are using a jacobi iteration function inside the method, the inputted matrix must be diagonally dominant. 
If it isn't then the function will not run properly. I call this function in my main.py file found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py)
under assignment 9 under Task 1. The inputs look like the following: 

```python
A = [[1, 0.1, 0.1], [0.1, 3, 0.1], [0.1, 0.1, 2]]
v = [1, 2, 3]
tol = 0.00001
maxiter = 10000
print("The smallest eigenvalue of the matrix A: " + str(inverse_power_method(A, v, tol, maxiter)))
```

The corresponding output I got is the following: 

```
The smallest eigenvalue of the matrix A: 1.0141111189184713
```

And the routine I wrote, which can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/linear_algebra_operations/eigen_value_solutions.py) is the following: 

```python
def inverse_power_method(a, v_0, tol, maxiter):
    error = 10 * tol
    iter = 1
    l_0 = 0
    v = v_0
    initial_guess = []
    for i in range(0, len(v)):
        initial_guess.append(1)

    while (error > tol and iter < maxiter):
        y = jacobi_iteration(a, v, initial_guess, tol, maxiter)
        z = scalar_mult_of_number_and_vector(1/L2_norm_of_vector(y), y)
        w = jacobi_iteration(a, z, initial_guess, tol, maxiter)
        l_1 = dot_product(z, w)
        error = abs(l_1 - l_0)
        l_0 = l_1
        v = z
        iter += 1

    return 1/l_0
```

## Task 2 



## Task 3 



## Task 4 



## Task 5 


