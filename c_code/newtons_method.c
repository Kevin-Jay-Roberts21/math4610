#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include "newtons_method.h"

// double fval(double);
// double fvalderivative(double);

// 
// routine to compute approximation of roots
// -----------------------------------------
//
double newtons_method(double (*f)(), double (*fprime)(), double initialx, double tol, double maxiter)
{
    //
    // set up storage for the work to be done
    // --------------------------------------
    //
    double x0 = initialx;
    double f0 = f(x0);
    double fp = fprime(x0);
    double error = 10.0 * tol;
    double iter = 0;
    
    // printf("Results from Newtons Method:\n");
    // printf("Iterations, Approx. Root Location, Error\n");

    // 
    // do the iterations needed to get a close enough approximation to a root
    // ----------------------------------------------------------------------
    //

    double x1;
    while (error > tol && iter < maxiter)
    {
        x1 = x0 - (f0 / fp);
        error = fabs(x1 - x0);

        // printf("iterations = %f, x1 = %f, error = %f\n", iter, x1, error);
        
        iter += 1;
        x0 = x1; 
        f0 = f(x0);
        fp = fprime(x0);
    }

    printf("\nFinal Approximation: %f\n", x1);

    return x1;
}
// double fval(double x){
//     double fval = x * exp(-x);
//     return fval; 
// }
// double fvalderivative(double x){
//     double fvalderivative = -x * exp(-x) + exp(-x);
//     return fvalderivative; 
// }
