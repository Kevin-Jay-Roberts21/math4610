#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "absolute_error.h"
#include "relative_error.h"
#include "single_precision_digit_count.h"
#include "double_precision_digit_count.h"

int main()
{
    // 
    // Running Absolute Error function
    // 
    absolute_error(100, 99.99);

    // 
    // Running Relative Error function
    // 
    relative_error(100, 99.99);

    // 
    // Running Single Precision function
    // 
    single_precision_digit_count();

    // 
    // Running Double Precision function
    // 
    double_precision_digit_count();

}