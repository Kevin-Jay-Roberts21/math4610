from root_finding_codes.root_finding_functions import *

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
#fixed_point("x0*np.exp(-x0)", 1.1, 0.0000001, 20)

# Task 3
# Must uncomment out the Task 3 g lines in the fixed_point function (line 32 and 53) AND
# comment out the g1() and g2() function calls in the fixed_point function (line 31 and 52)
# before uncommenting the following line:
#fixed_point("10.14 * np.exp(x0*x0) * np.cos(np.pi / x0)", 2.1, 0.0001, 1000)

# Task 4
#bisection("x0*np.exp(-x0)", -100, 5, 0.0001)
#bisection("10.14 * np.exp(x0*x0) * np.cos(np.pi / x0)", -2.1, 5, 0.0001)

####################
#### HOMEWORK 2 ####
####################

# Task 1
#newtons_method("x*np.exp(-x)", -1, -2, 0.000001, 10000)

# Task 2
# Notes: (only works when both x0 < x1 and both are negative and close to each other)

#secant_method("x*np.exp(-x)", 100, 101, 0.000001, 10000)

# Task 4
#bisection_newton_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", -3, 7, 0.00001, 20)

# Task 5
bisection_secant_hybrid("10.14 * np.exp(x*x) * np.cos(np.pi / x)", -3, 7, 0.00001, 20)
