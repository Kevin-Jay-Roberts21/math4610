#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include "secant_method.h"

// double fval(double);
// double fvalderivative(double);

// 
// routine to compute approximation of roots
// -----------------------------------------
//
double secant_method(double (*f)(), double x0, double x1, double tol, double maxiter)
{
    //
    // set up storage for the work to be done
    // --------------------------------------
    //
    double f0 = f(x0);
    double f1 = f(x1);
    double error = 10.0 * tol;
    double iter = 0;
    
    // printf("Results from Secant Method:\n");
    // printf("Iterations, Approx. Root Location, Error\n");

    // 
    // do the iterations needed to get a close enough approximation to a root
    // ----------------------------------------------------------------------
    //

    double x2;
    while (error > tol && iter < maxiter)
    {
        x2 = x1 - (f1 * (x1 - x0)/(f1 - f0));
        error = fabs(x2 - x1);

        // printf("iterations = %f, x1 = %f, error = %f\n", iter, x1, error);
        
        iter += 1;
        x0 = x1; 
        x1 = x2;
        f0 = f1;
        f1 = f(x1);
    }

    printf("\nFinal Approximation: %f\n", x1);

    return x1;
}
// double fval(double x){
//     double fval = x * exp(-x);
//     return fval; 
// }