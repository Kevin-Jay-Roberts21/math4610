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

def shifted_power_method(a, v_0, tol, maxiter):
    error = 10 * tol
    iter = 0
    l_0 = 0
    initial_guess = []
    for i in range(0, len(v_0)):
        initial_guess.append(1)

    lmax = power_method_2(a, v_0, tol, maxiter)
    lmin = inverse_power_method(a, v_0, tol, maxiter)

    z = jacobi_iteration(a, v_0, initial_guess, tol, maxiter)

    while (error > tol and iter < maxiter):
        y = scalar_mult_of_number_and_vector(1/L2_norm_of_vector(z), z)
        w = jacobi_iteration(a, y, initial_guess, tol, maxiter)
        l_1 = dot_product(w, y)
        error = abs(l_1 - l_0)
        z = w
        l_0 = l_1
        iter += 1

    return 1/l_0



def jacobi_iteration(a, b, x0, tol, maxiter):
    error = 10 * tol
    iter = 0
    r0 = vector_subtraction(b, action_of_matrix_on_vector(a, x0))

    while (error > tol and iter < maxiter):

        for i in range(0, len(a)):
            r0[i] = r0[i]/a[i][i]

        x1 = vector_addition(x0, r0)
        error = L2_norm_of_vector(vector_subtraction(x1, x0))
        iter += 1
        x0 = x1
        r0 = vector_subtraction(b, action_of_matrix_on_vector(a, x1))

    return x0


    # error = 10 * tol
    # iter = 0
    # v = []
    # r = []
    # x1 = []
    # for i in range(0, len(a)):
    #     x1.append(0)
    #
    # for i in range(0, len(a)):
    #     v.append(x0[i])
    #
    # for i in range(0, len(a)):
    #     sum = b[i]
    #     for j in range(0, len(a)):
    #         sum = sum - a[i][j] * v[j]
    #     r.append(sum)
    #
    # while (error > tol and iter < maxiter):
    #     for i in range(0, len(a)):
    #         x1[i] = x0[i] + r[i]/a[i][i]
    #     error = 0.0
    #     for i in range(0, len(a)):
    #         diff = x1[i]-x0[i]
    #         error = error + (diff*diff)
    #     for i in range(0, len(a)):
    #         sum = b[i]
    #         for j in range(0, len(a)):
    #             sum = sum - (a[i][i] * x1[i])
    #         r[i] = sum
    #     for i in range(0, len(a)):
    #         x0[i] = x1[i]
    #
    # return x0
