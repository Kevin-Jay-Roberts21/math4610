# Math 4610 Calculating Single Precision Digit Count

**Routine Name:**           single_precision_digit_count

**Author:** Kevin Roberts

**Language:** C

**Description/Purpose:** This routine was created to find out how many digits of accuracy are used in single precision computer
code. We will be decreasing a number until the computer code defines it as being equal to zero.

**Input:** No inputs for this function.

**Output:** This routine outputs the number of digits of accuracy that are used for single precision.

**Usage/Example:**

The function will be called like the following: 

      single_precision_digit_count();

Output from the lines above:

      Iteration: 24, Seps: 0.000000

      Digit Count (seps): 7

The code output suggests that the final iteration is approximately 0.000000 and that the digit count (accuracy is 7). 

The code for this routine can be found at the bottom of this file. Let's begin. The first line of the function is initializing
a digit count. We then define a variable one, seps, appone, all to be floats because we are dealing with single precision.
Then we run through a loop 100 times. The first line inside the loop suggests that we redefine appone (approximated one) 
by adding one and seps (s epsilon). The next line is very important. It asked to see if the absolute value of appone-one 
is zero, then we break out of the loop. If not, then we essentially make seps smaller by multiplying it by 0.5. Finally, 
we need to get the exponent of seps. This is done by taking the log base 10 of seps, then adding 0.5 because of the way 
c code does rounding truncation. Finally, we return the digit count, which is 7.

**Implementation/Code:** The following is the code for single_precision_digit_count():

    #include <stdio.h>
    #include <stdlib.h>
    #include <math.h>
    #include "single_precision_digit_count.h"
    
    float single_precision_digit_count()
    {
    
        int digit_count = 0;
    
        float one = 1.0; 
        float seps = 1.0; 
        float appone = 1.0;
    
        for (int i=0; i<100; i++)
        {
            float appone = one + seps;
            if (fabs(appone - one) == 0.0) {
                printf("Iteration: %d, Seps: %f\n", i, seps);
                break;
            }
            seps = 0.5 * seps;
        }
    
        // 
        // return the digit count
        // ----------------------
        //
        digit_count = -log10(seps)+0.5;
        printf("\nDigit Count (seps): %d\n", digit_count);
        return digit_count;
    }

**Last Modified:** October/2022