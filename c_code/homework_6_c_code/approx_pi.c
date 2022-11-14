#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double fval(double);

static long n = 100000; 
double step; 
int main () {
    
    clock_t t;
    t = clock();

    // THIS IS WHAT TIM USED IN HIS VIDEO TO APPROXIMATE PI. IT IS THE MIDPOINT METHOD
    // int i; double x, pi, sum = 0.0; 
    // step = 1.0/(double) n; 
    // for (i=0; i < n; i++) {
    //     x = (i + 0.5) * step; 
    //     sum = sum + 4.0/(1.0 + x*x);
    // }
    // pi = step * sum;

    double a = 0; double b = 0.5; int i; double x; double fx0; double fx1; double fx2; double x1; double x2;

    double h = 2 * ((b - a)/n);
    double pi = 0;
    double x0 = (b-a)/n;
    for (i=0; i < n/2; i++) {
        x = x0;
        fx0 = fval(x);
        x1 = x0 + (b-a)/n;
        x = x1;
        fx1 = fval(x);
        x2 = x1 + (b-a)/n;
        x = x2;
        fx2 = fval(x);
        pi += (fx0 + 4*fx1 + fx2)*(h/3);
        x0 = x2;
    }
    pi = pi * 3;


    t = clock() - t;
    double totaltime = ((double)t)/CLOCKS_PER_SEC;
    printf("\nThe time it took to generate pi was: %f\n", totaltime);
    printf("\nThe approximated pi: %f\n", pi);
    printf("\nThe exact value of pi: %f\n", M_PI);
}
double fval(double x){
    double fval = 1 / sqrt(1 - x*x);
    return fval; 
}