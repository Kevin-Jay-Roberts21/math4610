#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "bisection.h"

// double fval(double);

// 
// routine to compute approximation of roots
// -----------------------------------------
//
double bisection(double (*f)(), double a, double b, double tol)
{
    //
    // set up storage for the work to be done
    // --------------------------------------
    //
    double fa = f(a);
    double fb = f(b);
    // 
    // test the endpoints for a root in the interval
    // ---------------------------------------------
    //
    if (fa * fb >= 0.0)
    {
        printf("There may not be a root in [a, b]: f(a)*f(b) = %e", fa * fb);
        return 0;
    }
    double c; 
    double fc; 
    // 
    // compute the number of iterations
    // --------------------------------
    //
    int k = ((int)(log(tol) - log(b - a)) / log(0.5) + 1);
    // 
    // do the iterations needed to get a close enough approximation to a root
    // ----------------------------------------------------------------------
    //
    for (int i=0; i<k; i++)
    {
        c = 0.5 * (a + b); 
        fc = f(c);
        //printf("fa = %f, fb = %f, fc = %f", fa, fb, fc);
        if (fa * fc < 0.0)
        {
            b = c; 
            fb = fc; 
        }
        else
        {
            a = c; 
            fa = fc; 
        }
    }
    // 
    // return the computed approximation of the root
    // ---------------------------------------------
    //
    printf("\nroot value = %f\n", c);
    return c;
}
// double fval(double xval){
//     double fval = xval * xval - 4.1;
//     printf("xval = %f, fval = %f\n", xval, fval);
//     return fval; 
// }