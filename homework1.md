# Homework 1

## Task 1

## Task 2 
This part of the assignment is inbedded inside of the functions. Instead of using verbose, I included some print statements inside the root finding functions. The following python code is a print statement to begin the list of numerical values: 

``
print("{:<25} {:<25} {:<25}".format('Iterations','Approx. Root Location','Error'))
``

Further, inside of the loop of the root finding functions, I include information from each iteration:

``
print("{:<25} {:<25} {:<25}".format(iterations, "{:.10f}".format(x1), "{:.10f}".format(error)))
``

The code line `"{:.10f}".format(x1)` will round the root approximation to the tenth decimal, and the same is done with the error variable. This will keep code cleaner as we print out iterations.

Finally, I end with the following print statement, outside of the loop, that displays the final iteration (aka the final root approximation):

``
print("Final Approximation: " + "{:.10f}".format(x1))
``

## Task 3


## Task 4


## Task 5

I have completed task 5, in that I've added you as a collaborator to my github repository and have published all of my code and notes, including this homework1.md file. My repository can be found at the following link: 

https://github.com/Kevin-Jay-Roberts21/math4610