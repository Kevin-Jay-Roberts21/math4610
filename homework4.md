# Homework 4

## Task 1 

I proved that the approximation is of order h squared. My work can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/homework4_images/CamScanner%2010-14-2022%2010.42.pdf)

## Task 2 

See Software Manual [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/second_derivative_approx.md)

See code function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/approximating_functions/second_derivative_approx.py)

See function call in the main function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py)

## Task 3 

See Software Manual [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/fit_data_sets.md)

See code function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/approximating_functions/second_derivative_approx.py)

See function call in the main function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py)

## Task 4 

I created the python code for absolute error and relative error for this task [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/approximating_functions/error_computations.py).

The usages can be found in the main.py file [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/approximating_functions/second_derivative_approx.py).

I skipped on creating a software manual for the absolute error and relative error code because the code is very very simple. 
We simply take an exact solution and an approximation and find the absolute error and the relative error. Both of which 
can be achieved in one line of code:

Absolute error: ``error = abs(u - v)``

Relative error: ``error = abs(u - v)/abs(u)``

The software manual code for the single precision can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/single_precision_digit_count.md) (written in c code).

The software manual code for the double precision can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/double_precision_digit_count.md) (written in c code).

To finish, I created a shared library. The c codes can be found [here](https://github.com/Kevin-Jay-Roberts21/math4610/tree/master/c_code/homework_4_c_code).

## Task 5 

See Software Manual [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/software_manual_templates/explicit_euler_logistic.md)

See code function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/approximating_functions/second_derivative_approx.py)

See function call in the main function [here](https://github.com/Kevin-Jay-Roberts21/math4610/blob/master/main.py)
