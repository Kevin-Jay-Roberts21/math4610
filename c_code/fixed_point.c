#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include "fixed_point.h"

// double fixed_point(); 
// double fval(double);
double g1(double, double);

// 
// routine to compute approximation of roots
// -----------------------------------------
//
double fixed_point(double (*f)(), double initialx, double tol, double maxiter)
{
    //
    // set up storage for the work to be done
    // --------------------------------------
    //
    double error = 10.0 * tol;
    double x0 = initialx;
    double iter = 0;
    
    // printf("Results from g1 iteration method:\n");
    // printf("Iterations, Approx. Root Location, Error\n");

    // 
    // do the iterations needed to get a close enough approximation to a root
    // ----------------------------------------------------------------------
    //

    double x1;
    while (error > tol && iter < maxiter)
    {
        x1 = g1(f(x0), x0);
        error = fabs(x1 - x0);

        // printf("iterations = %f, x1 = %f, error = %f\n", iter, x1, error);
        
        x0 = x1; 
        iter += 1;
    }

    printf("\nFinal Approximation: %f\n", x1);

    return x1;
}
// double fval(double x){
//     double fval = x * exp(-x);
//     return fval; 
// }
double g1(double f, double x){
    double gval = fabs(x - f);
    return gval; 
}

// Special Note: Notice how I'm not including a second g2 function here. Instead of creating another g2 
// function, I'm just going to modify the g1 function for whenever I want to change the fixed_point 
// approximation method. See the software manual for the fixed_point method for more information.