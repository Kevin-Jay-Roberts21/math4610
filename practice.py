from root_finding_codes.root_finding_functions import *


# The first two calls are the fixed point functional iteration methods. My
# parameters are in order as follows (for the fixed point functions):
# 1. f function 2. initial root guess 3. tolerance 4. maximum iterations.
# the third function call is the bisection method and the parameters are
# in order as follows:
# 1. f function 2. end point a 3. end point b 4. tolerance.

# Task 1 and 2
fixed_point("x0 - (x0*np.exp(-x0))", 0.0003165, 0.0000001, 10)

# Task 3
fixed_point("10.14 * np.exp(x0*x0) * cos(np.pi / x0)", 0, 0.0001, 10)

# Task 4
bisection("10.14 * np.exp(x0*x0) * cos(np.pi / x0)", -5, 5, 0.0001)