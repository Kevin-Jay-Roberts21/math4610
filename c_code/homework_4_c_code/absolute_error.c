#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "absolute_error.h"

double absolute_error(double u, double v)
{

    double error = fabs(u - v);

    // 
    // return the error
    // ----------------
    //
    printf("\nAbsolute Error: %f\n", error);
    return error;
}