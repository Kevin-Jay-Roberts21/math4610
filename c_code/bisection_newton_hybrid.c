#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include "bisection_newton_hybrid.h"

// double fval(double);
// double fvalderivative(double);

// 
// routine to compute approximation of roots
// -----------------------------------------
//
double bisection_newton_hybrid(double (*f)(), double (*fprime)(), double a, double b, double tol, double maxiter)
{
    //
    // set up storage for the work to be done
    // --------------------------------------
    //
    double error = 10.0 * tol;
    double iter = 0;
    double x0 = 0.5 * (a + b);
    double f0 = f(x0);
    double fp = fprime(x0);
    
    // printf("Results from Bisection-Newton Hybrid Method:\n");
    // printf("Iterations, Approx. Root Location, Error\n");

    // 
    // do the iterations needed to get a close enough approximation to a root
    // ----------------------------------------------------------------------
    //

    double x1;
    double newterror;
    while (error > tol && iter < maxiter)
    {
        if (fp == 0) 
        {
            break;
        }

        x1 = x0 - (f0 / fp);
        newterror = fabs(x1 - x0);

        // double fa; 
        // double fb; 
        double fc;
        double c;
        if (newterror > error)
        {
            double fa = f(a);
            double fb = f(b);
            // printf("The Newton Error is greater than the general error!\n");
            // printf("Switching to Bisection method:\n");
            for (int i=1; i<5; i++)
            {
                c = 0.5 * (a + b);
                if (c == 0)
                {
                    printf("\nFinal Approximation: %f\n", c);
                    return c;
                }
                fc = f(c);
                // printf("iterations = %f, x1 = %f\n", iter+i, c);
                
                if (fa * fc < 0)
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
            error = fabs(b - a);
            x0 = c;
            iter += 4; 
            // printf("Exiting the bisection method:\n");
        }
        else 
        {
            x0 = x1; 
            error = newterror; 
        }

        // printf("iterations = %f, x1 = %f, error = %f\n", iter, x1, error);
        iter += 1;
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
