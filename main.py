from root_finding_codes.root_finding_functions import *
from approximating_functions.second_derivative_approx import *
from approximating_functions.error_computations import *

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
# implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 50, 100)
# a = 0.01
# b = 0.0005
# P0 = 10.0
# implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 600, 100)
# a = 2.0
# b = 0.0005
# P0 = 10.0
# implicit_euler_logistic(a, b, P0, 0, "a*P - b*(P*P)", 8, 100)

# Task 2
# testing some time values for the exact logistic equation
a = 0.2
b = 0.0005
P0 = 10.0
exact_logistic("(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", P0, a, b, 2)
exact_logistic("(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", P0, a, b, 5)
exact_logistic("(a*(P0/(a - P0*b))*np.exp(t*a))/(1 + b*(P0/(a - P0*b))*np.exp(t*a))", P0, a, b, 10)
