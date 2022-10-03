#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include "bisection_newton_hybrid.h"

// double fval(double);

// 
// routine to compute approximation of roots
// -----------------------------------------
//
double bisection_secant_hybrid(double (*f)(), double x0, double x1, double tol, double maxiter)
{
    //
    // set up storage for the work to be done
    // --------------------------------------
    //
    double error = 10.0 * tol;
    double iter = 0;
    double f0 = f(x0);
    double f1 = f(x1);
    
    // printf("Results from Bisection-Secant Hybrid Method:\n");
    // printf("Iterations, Approx. Root Location, Error\n");

    // 
    // do the iterations needed to get a close enough approximation to a root
    // ----------------------------------------------------------------------
    //

    double x2;
    double secanterror;
    while (error > tol && iter < maxiter)
    {
        if (f1-f0 == 0) 
        {
            break;
        }

        x2 = x1 - (f1 * (x1 - x0)/(f1 - f0));
        secanterror = fabs(x2 - x1);

        // double fa; 
        // double fb; 
        double fc;
        double c;
        double a; 
        double b;
        if (secanterror > error)
        {
            a = x1; 
            b = x2;
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
            x0 = a;
            x1 = b; 
            iter += 4;
            f0 = f1; 
            f1 = f(x1);
            iter += 1; 
            // printf("Exiting the bisection method:\n");
        }
        else 
        {
            iter += 1; 
            x0 = x1; 
            x1 = x2;
            f0 = f1; 
            f1 = f(x1);
            error = secanterror; 
        }

        // printf("iterations = %f, x1 = %f, error = %f\n", iter, x1, error);
    }

    printf("\nFinal Approximation: %f\n", x1);

    return x1;
}
// double fval(double x){
//     double fval = x * exp(-x);
//     return fval; 
// }