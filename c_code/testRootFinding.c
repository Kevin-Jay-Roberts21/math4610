#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "fixed_point.h"
#include "bisection.h"
#include "secant_method.h"
#include "newtons_method.h"
#include "bisection_newton_hybrid.h"
#include "bisection_secant_hybrid.h"


double fval(double);
double fvalderivative(double);

int main()
{
    double tol; 
    double maxiter; 
    double a; 
    double b; 
    double x0; 
    double x1; 

    /////////////////////////
    // FIXED_POINT TESTING //
    /////////////////////////
    
    // set up and initial some storage/numbers
    x0 = 1.1;  
    tol = 0.000001;
    maxiter = 20; 

    // call the routine
    printf("Running the Fixed Point Method:");
    double fixed_point_eval = fixed_point(fval, x0, tol, maxiter);
    printf("\n\n");

    ///////////////////////
    // BISECTION TESTING //
    ///////////////////////

    // set up and initial some storage/numbers
    a = 1.0; 
    b = 3.0; 
    tol = 0.00001; 

    // call the routine
    printf("Running the Bisection Method:");
    double bisection_eval = bisection(fval, a, b, tol);
    printf("\n\n");


    ////////////////////////////
    // NEWTONS_METHOD TESTING //
    ////////////////////////////

    // set up and initial some storage/numbers
    x0 = -3;  
    tol = 0.000001;
    maxiter = 10; 

    // call the routine
    printf("Running Newtons Method:");
    double newtons_method_eval = newtons_method(fval, fvalderivative, x0, tol, maxiter);
    printf("\n\n");


    ///////////////////////////
    // SECANT_METHOD TESTING //
    ///////////////////////////

    // set up and initial some storage/numbers
    x0 = -5;
    x1 = -1;  
    tol = 0.000001;
    maxiter = 10; 

    // call the routine
    printf("Running the Secant Method:");
    double secant_method_eval = secant_method(fval, x0, x1, tol, maxiter);
    printf("\n\n");


    /////////////////////////////////////
    // BISECTION_NEWTON_HYBRID TESTING //
    /////////////////////////////////////

    // set up and initial some storage/numbers
    a = -3;  
    b = 7;
    tol = 0.000001;
    maxiter = 10; 

    // call the routine
    printf("Running the Bisection Newton Method:");
    double bisection_newton_hybrid_eval = bisection_newton_hybrid(fval, fvalderivative, a, b, tol, maxiter);
    printf("\n\n");

    /////////////////////////////////////
    // BISECTION_SECANT_METHOD TESTING //
    /////////////////////////////////////
    
    // set up and initial some storage/numbers
    x0 = -3;  
    x1 = 7;
    tol = 0.000001;
    maxiter = 20; 
    
    // call the routine
    printf("Running the Bisection Secant Method:");
    double bisection_secant_hybrid_eval = bisection_secant_hybrid(fval, x0, x1, tol, maxiter);
}

double fval(double x){
    double fval = x * exp(-x);
    return fval; 
}
double fvalderivative(double x){
    double fvalderivative = -x * exp(-x) + exp(-x);
    return fvalderivative; 
}

// Special Note: Notice how I'm not including a second g2 function here. Instead of creating another g2 
// function, I'm just going to modify the g1 function for whenever I want to change the fixed_point 
// approximation method. See the software manual for the fixed_point method for more information.