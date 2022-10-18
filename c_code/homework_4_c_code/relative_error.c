#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "relative_error.h"

double relative_error(double u, double v)
{

    double error = fabs(u - v)/fabs(u);

    // 
    // return the error
    // ----------------
    //
    printf("\nRelative Error: %f\n", error);
    return error;
}