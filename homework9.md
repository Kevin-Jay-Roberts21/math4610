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

For this task I had to first make sure that my inverse_power method was working and the power method. After getting these
functions working properly, I used them to compute the shifted power method. The matrix I chose to input was a small 3x3 
matrix so that I could test it and make sure everything was working. The code I inputted can be found in my main.py file 
[here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py) under Homework 9, under task 2. I chose to include outputs of the power method and inverse method as well so that
it's easy to see what the max, min and middle eigenvalues are. The following code is my input: 

```python
A = [[1, 0.1, 0.1], [0.1, 3, 0.1], [0.1, 0.1, 2]]
v = [1, 2, 3]
tol = 0.00001
maxiter = 10000
print(power_method_2(A, v, tol, maxiter))
print("Running the shifted power method on A and v produced: " + str(shifted_power_method(A, v, tol, maxiter)))
print(inverse_power_method(A, v, tol, maxiter))
```

I got the corresponding outputs: 

```
3.0158521958268265
Running the shifted power method on A and v produced: 2.007647778805279
0.9860852339992875
```

As you can see, the middle eigenvalue is actually supposed to be a little closer to 1.99, but since I added that 0.5 eariler
to account for my code breaking, this eigenvalue will be slightly off. For this computation, it's sufficiently close enough.

The code I wrote for this assignment code be found in my github account [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/linear_algebra_operations/eigen_value_solutions.py). I provided the code also below: 

```python
def shifted_power_method(a, v_0, tol, maxiter):
    error = 10 * tol
    iter = 0
    l_0 = 0
    initial_guess = []
    for i in range(0, len(v_0)):
        initial_guess.append(1)

    lmax = power_method_2(a, v_0, tol, maxiter)
    lmin = inverse_power_method(a, v_0, tol, maxiter)
    lmiddle = int((lmax+lmin)/2) - 0.5 # minus 0.5 because code breaks if mu is too close diagonal element in matrix.

    new_matrix = []
    for i in range(0, len(a)):
        new_row = []
        for j in range(0, len(a)):
            if i == j:
                new_row.append(lmiddle)
            else:
                new_row.append(0)
        new_matrix.append(new_row)

    B = difference_of_matrices(a, new_matrix)
    v = v_0
    while (error > tol and iter < maxiter):
        z = jacobi_iteration(B, v, initial_guess, tol, maxiter)
        y = scalar_mult_of_number_and_vector(1 / L2_norm_of_vector(z), z)
        w = jacobi_iteration(B, y, initial_guess, tol, maxiter)
        l_1 = dot_product(y, w)
        error = abs(l_1 - l_0)
        l_0 = l_1
        v = y
        iter += 1

    return l_0
```

## Task 3 

For this task I wrote it very similar to the shifting power method. The idea is that we have to find the largest eigenvalue
and the smallest eigenvalue of a matrix, and then we have to partition the set into n intervals. The n intervals will be 
exactly the dimensions of the nxn matrix. I'll call this method the shifted_power_special method in my python code. The 
inputs I used were a 4x4 matrix. Again, I chose a small enough matrix to show that this will work out nicely. In the
inputs I proceeded to print out the largest eigenvalue, the eigenvalues in the middle, and the smallest eigenvalue. The 
inputs can be found in my main.py file under Homework 9 under task 3 [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py). 
I'll also show the inputs below: 

```python
A = [[1, 0.1, 0.1, 0.1], 
     [0.1, 3, 0.1, 0.1], 
     [0.1, 0.1, 2, 0.1], 
     [0.1, 0.1, 0.1, 4]]
v = [1, 2, 3, 4]
tol = 0.00001
maxiter = 10000
print("Largest eigen value: " + str(power_method_2(A, v, tol, maxiter)))
middle_eigen_values = shifted_power_special(A, v, tol, maxiter)
for i in range(0, len(middle_eigen_values)):
    print("Middle eigenvalue: " + str(middle_eigen_values[i]))
print("Smallest eigen value: " + str(inverse_power_method(A, v, tol, maxiter)))
```

For the corresponding output, I got the following: 

```

```

Finally, the method I wrote for this assignment can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/linear_algebra_operations/eigen_value_solutions.py) and is show below: 

```python

```

## Task 4 

I couldn't figure out how to write my code in parallel for this task in python specifically, this will be a future research project for me.

## Task 5 


