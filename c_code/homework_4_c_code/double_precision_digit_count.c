#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "double_precision_digit_count.h"

double double_precision_digit_count()
{

    int digit_count = 0;

    double one = 1.0; 
    double seps = 1.0; 
    double appone = 1.0;

    for (int i=0; i<100; i++)
    {
        double appone = one + seps;
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