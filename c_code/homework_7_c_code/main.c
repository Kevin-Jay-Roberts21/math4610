#include "/usr/local/Cellar/libomp/15.0.5/include/omp.h"
#include <stdio.h>
static long n = 100000; double step;
#define NUM_THREADS 8

int test1 ();
int** matrix_product(int u[3][3], int v[3][3]);
int** matrix_product_parallel(int u[3][3], int v[3][3]);

int main ()
{
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[3][3] = {{10, 11, 12}, {13, 14, 15}, {16, 17, 18}};
    
    return matrix_product_parallel(A, B);
}

int test1 () {
    int i, nthreads=8; double pi, sum[NUM_THREADS];
    step = 1.0/(double) n;
    omp_set_num_threads(NUM_THREADS);
      #pragma omp parallel
      {
        int i, id, nthrds;
        double x;
        id = omp_get_thread_num();
        nthrds = omp_get_num_threads();
        if (id == 0) nthreads = nthrds;
        for (i=id, sum[id] = 0.0; i < n; i=i+nthrds) {
            x = (i + 0.5) * step;
            sum[id] += 4.0/(1.0 + x*x);
        }
      }
      for (i = 0, pi = 0.0; i < nthreads; i++)
          pi += sum[i] * step;
      printf("%f", pi);
    return pi;
}

int** matrix_product_parallel(int a[3][3], int b[3][3])
{
    int new_matrix[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
    int k, nthreads=8, realsum, sum[NUM_THREADS];
    omp_set_num_threads(NUM_THREADS);
    
    for (int i = 0; i < 3; i++)
    {
        int new_row[3] = {0, 0, 0};
        
        for (int j = 0; j < 3; j++)
        {
            // parallelizing here
            #pragma omp parallel
            {
              int k, id, nthrds;
              id = omp_get_thread_num();
              nthrds = omp_get_num_threads();
              if (id == 0) nthreads = nthrds;
              for (k=id, sum[id] = 0.0; k < 3; k=k+nthrds) {
                  sum[id] += a[i][k] * b[k][j];
              }
            }
            for (k = 0, realsum = 0.0; k < nthreads; k++)
                realsum += sum[k];
            
            new_row[j] = realsum;
        }
        for (int l = 0; l < 3; l++)
        {
            new_matrix[i][l] = new_row[l];
        }
        
    }
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            
            printf("%d ", new_matrix[i][j]);
        }
        printf("\n");
    }
    
    return new_matrix;
}


int** matrix_product(int a[3][3], int b[3][3])
{
    int new_matrix[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
    
    for (int i = 0; i < 3; i++)
    {
        int new_row[3] = {0, 0, 0};
        
        for (int j = 0; j < 3; j++)
        {
            double sum = 0.0;
            // parallelizing here
            for (int k = 0; k < 3; k++)
            {
                sum += a[i][k] * b[k][j];
            }
            new_row[j] = sum;
        }
        for (int l = 0; l < 3; l++)
        {
            new_matrix[i][l] = new_row[l];
        }
        
    }
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            
            printf("%d ", new_matrix[i][j]);
        }
        printf("\n");
    }
    
    return new_matrix;
}
