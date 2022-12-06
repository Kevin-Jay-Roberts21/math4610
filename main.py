import math

import matplotlib.pyplot as plt

from root_finding_codes.root_finding_functions import *
from approximating_functions.second_derivative_approx import *
from approximating_functions.error_computations import *
from linear_algebra_operations.linear_algebra_operations import *
from linear_algebra_operations.eigen_value_solutions import *

####################
#### HOMEWORK 1 ####
####################

# The first two calls are the fixed point functional iteration methods. My
# parameters are in order as follows (for the fixed point functions):
# 1. f function 2. initial root guess 3. tolerance 4. maximum iterations.
# the third function call is the bisection method and the parameters are
# in order as follows: 1. f function 2. end point a 3. end point b 4. tolerance.

# The reason I use x0 in the functions is because x0 is defined to be a value in
# the functions. If I used a simple x instead, then it would not be recognized because
# it's not defined. x0 is defined so we use it.

# Task 1 and 2
#fixed_point("x*np.exp(-x)", 1.1, 0.0000001, 20)

# Task 3
# Must uncomment out the Task 3 g lines in the fixed_point function (line 32 and 53) AND
# comment out the g1() and g2() function calls in the fixed_point function (line 31 and 52)
# before uncommenting the following line:
#fixed_point("10.14 * np.exp(x*x) * np.cos(np.pi / x)", 2.1, 0.0001, 1000)

# Task 4
#bisection("x*np.exp(-x)", -5, 1, 0.0001)
#bisection("10.14 * np.exp(x*x) * np.cos(np.pi / x)", -2.1, 5, 0.0001)

####################
#### HOMEWORK 2 ####
####################

# Task 1
#newtons_method("x*np.exp(-x)", "-x*np.exp(-x) + np.exp(-x)", -3, 0.000001, 10)

# Task 2
# Notes: (only works when both x0 < x1 and both are negative and close to each other)
#secant_method("x*np.exp(-x)", -5, -1, 0.000001, 10)

# Task 4
# passing in f, fprime, a, b, tol, and maxiter (interval (-2, 7) doesn't work for some reason)
#bisection_newton_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", "10.14*(2*np.exp(x*x)*x*np.cos(np.pi/x) + (np.pi*np.exp(x*x)*np.sin(np.pi/x))/(x*x))", 1, 7, 0.000001, 10)


# Task 5
# passing in f, a, b, tol, maxiter
#bisection_secant_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", 1.2, 1.7, 0.00001, 20)


####################
#### HOMEWORK 4 ####
####################

# Task 2
#second_derivative_approx("((x - np.pi/2) * np.tan(x))/(x*x + 65)", np.pi/4, 0.001)

# Task 3
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = []
# for i in range(0, len(x)):
#     y.append(second_derivative_approx("((x - np.pi/2) * np.tan(x))/(x*x + 65)", x[i], 0.001))
#
# fit_data_sets(x, y)

# Task 4
# absolute_error(100, 99.99)
# relative_error(100, 99.99)


# Task 5
# a = 0.2
# b = 0.0005
# P0 = 10.0
# explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)
# a = 0.01
# b = 0.0005
# P0 = 10.0
# explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
# a = 2.0
# b = 0.0005
# P0 = 10.0
# explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)


####################
#### HOMEWORK 5 ####
####################

# Task 1
# a = 0.2
# b = 0.0005
# P0 = 10.0
# first_implicit = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)
# a = 0.01
# b = 0.0005
# P0 = 10.0
# second_implicit = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
# a = 2.0
# b = 0.0005
# P0 = 10.0
# third_implicit = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)
#
# plt.plot(first_implicit[1], first_implicit[0])
# plt.show()
# plt.plot(second_implicit[1], second_implicit[0])
# plt.show()
# plt.plot(third_implicit[1], third_implicit[0])
# plt.show()

# Task 2
# testing some time values for the exact logistic equation
# a = 0.2
# b = 0.0005
# P0 = 10.0
# exact = exact_logistic(a, b, P0, 0, "(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", 50, 100)
# print("The exact value at " + str(exact[1][2]) + " is " + str(exact[0][2]))
# print("The exact value at " + str(exact[1][5]) + " is " + str(exact[0][5]))
# print("The exact value at " + str(exact[1][10]) + " is " + str(exact[0][10]))

# Task 3
# a = 0.2
# b = 0.0005
# P0 = 10.0
# implicit1 = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)
# explicit1 = explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)
# exact1 = exact_logistic(a, b, P0, 0, "(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", 50, 100)
# a = 0.01
# b = 0.0005
# P0 = 10.0
# implicit2 = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
# explicit2 = explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
# exact2 = exact_logistic(a, b, P0, 0, "(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", 600, 100)
# a = 2.0
# b = 0.0005
# P0 = 10.0
# implicit3 = implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)
# explicit3 = explicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)
# exact3 = exact_logistic(a, b, P0, 0, "(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", 8, 100)
#
# # now we must create a plot with all 3 graphs
# # use label='first plot', to label
# plt.plot(implicit1[1], implicit1[0], label='Implicit')
# plt.plot(explicit1[1], explicit1[0], label='Explicit')
# plt.plot(exact1[1], exact1[0], label='Exact')
# plt.legend()
# plt.show()
# plt.plot(implicit2[1], implicit2[0], label='Implicit')
# plt.plot(explicit2[1], explicit2[0], label='Explicit')
# plt.plot(exact2[1], exact2[0], label='Exact')
# plt.legend()
# plt.show()
# plt.plot(implicit3[1], implicit3[0], label='Implicit')
# plt.plot(explicit3[1], explicit3[0], label='Explicit')
# plt.plot(exact3[1], exact3[0], label='Exact')
# plt.legend()
# plt.show()

# Task 4
# # for n = 2
# a = 0
# b = np.pi/4
# trapezoidal_rule("np.exp(-x*x)", a, b, 2)
# # for n = 4
# a = 0
# b = np.pi/4
# trapezoidal_rule("np.exp(-x*x)", a, b, 4)
# # for n = 8
# a = 0
# b = np.pi/4
# trapezoidal_rule("np.exp(-x*x)", a, b, 8)
# # for n = 16
# a = 0
# b = np.pi/4
# trapezoidal_rule("np.exp(-x*x)", a, b, 16)
# # for n = 32
# a = 0
# b = np.pi/4
# trapezoidal_rule("np.exp(-x*x)", a, b, 32)

# Task 5
# for n = 2
# a = 0
# b = np.pi/4
# simpsons_rule("np.exp(-x*x)", a, b, 2)
# # for n = 4
# a = 0
# b = np.pi/4
# simpsons_rule("np.exp(-x*x)", a, b, 4)
# # for n = 8
# a = 0
# b = np.pi/4
# simpsons_rule("np.exp(-x*x)", a, b, 8)
# # for n = 16
# a = 0
# b = np.pi/4
# simpsons_rule("np.exp(-x*x)", a, b, 16)
# # for n = 32
# a = 0
# b = np.pi/4
# simpsons_rule("np.exp(-x*x)", a, b, 32)

# a = 0
# b = np.pi/4
# xvals = []
# tvals = [2, 4, 8, 16, 32, 64, 128, 256]
# SR_2 = simpsons_rule("np.exp(-x*x)", a, b, 2)
# SR_4 = simpsons_rule("np.exp(-x*x)", a, b, 4)
# SR_8 = simpsons_rule("np.exp(-x*x)", a, b, 8)
# SR_16 = simpsons_rule("np.exp(-x*x)", a, b, 16)
# SR_32 = simpsons_rule("np.exp(-x*x)", a, b, 32)
# SR_64 = simpsons_rule("np.exp(-x*x)", a, b, 64)
# SR_128 = simpsons_rule("np.exp(-x*x)", a, b, 128)
# SR_256 = simpsons_rule("np.exp(-x*x)", a, b, 256)
# # exact value (about)
# SR_5000 = simpsons_rule("np.exp(-x*x)", a, b, 5000)
# xvals.append(abs(SR_5000-SR_2))
# xvals.append(abs(SR_5000-SR_4))
# xvals.append(abs(SR_5000-SR_8))
# xvals.append(abs(SR_5000-SR_16))
# xvals.append(abs(SR_5000-SR_32))
# xvals.append(abs(SR_5000-SR_64))
# xvals.append(abs(SR_5000-SR_128))
# xvals.append(abs(SR_5000-SR_256))
#
# plt.xscale("log")
# plt.plot(xvals, tvals)
# plt.show()




####################
#### HOMEWORK 6 ####
####################

# Task 2

# pi_approx = my_simpsons_rule("1/(np.sqrt(1-(x*x)))", 0, 0.5, 1000000)
# print("Approximation of pi using Simpson's Rule: " + str(pi_approx))
# print("Pi exact (according to computer's np accuracy): " + str(np.pi))

# Task 4

# e_approx = approximate_e(50)
# print("Approximation of e using Maclaurin Series: " + str(e_approx))
# print("e exact (according to the computer's np accuracy): " + str(math.e))



# Task 5
# u = [1, 2, 3]
# v = [4, 5, 6]
# w = [7, 8, 9]
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
# number = 2
# print("The addition of vector u and v is: " + str(vector_addition(u, v)))
# print("The difference of vector u and v is: " + str(vector_subtraction(u, v)))
# print("The scalar multiple of number=2 and u is: " + str(scalar_mult_of_number_and_vector(number, u)))
# print("The L1 norm of u is: " + str(L1_norm_of_vector(u)))
# print("The L2 norm of u is: " + str(L2_norm_of_vector(u)))
# print("The L_infinity norm of u is: " + str(Linf_norm_of_vector(u)))
# print("The dot product of u and v is: " + str(dot_product(u, v)))
# print("The cross product of u and v is: " + str(cross_product(u, v)))
# print("The triple product of u, v and w is: " + str(triple_product(u, v, w)))
# print("The action of matrix A on the vector u is: " + str(action_of_matrix_on_vector(A, u)))
# print("The sum of matrices A and B is: " + str(sum_of_matrices(A, B)))
# print("The difference of matrices A and B is: " + str(difference_of_matrices(A, B)))
# print("The product of matrices A and B is: " + str(product_of_matrices(A, B)))


####################
#### HOMEWORK 7 ####
####################

# Task 4
# A1 = []
# B1 = []
# for i in range(0, 100):
#     new_row = []
#     for j in range(0, 100):
#         if (j % 2) == 0:
#             new_row.append(0)
#         else:
#             new_row.append(1)
#     A1.append(new_row)
#
# for i in range(0, 100):
#     new_row = []
#     for j in range(0, 100):
#         if (j % 2) != 0:
#             new_row.append(0)
#         else:
#             new_row.append(1)
#     B1.append(new_row)
# print("The Hadamard product of matrix A1 and B1 is: " + str(hadamard_product_of_matrices(A1, B1)))

# Task 5

# u = [1, 2, 3, 4, 5]
# v = [6, 7, 8, 9, 10]
# print("The outer product of vectors u and v is: " + str(outer_product(u, v)))



####################
#### HOMEWORK 8 ####
####################

# Task 1

# A = [[1, 2], [3, 4]]
# B = [[0, 5], [6, 7]]
# print("The Kronecker Product of Matrix A and Matrix B is: \n" + str(kronecker_matrix_product(A, B)))

# Task 2

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

# Task 3

print("Resulting lambda from the power method: " + str(power_method_2(A, v, tol, maxiter)))

# Task 5

# creating a giant 100x100 matrix
A = []


v = [1, 2, 3]
tol = 0.00001
maxiter = 1000
print("Resulting lambda from the power method: " + str(power_method_1(A, v, tol, maxiter)))
