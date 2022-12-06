import numpy as np

from linear_algebra_operations.linear_algebra_operations import *

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

def jacobi_iteration(a, b, x, tol, maxiter):
    pass
