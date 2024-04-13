
#include "rand.h"

// Function to generate an exponentially distributed random number
double generate_exponential(double lambda)
{
    double u = rand() / (RAND_MAX + 1.0);
    return -log(1 - u) / lambda;
}

// Function to generate a random positive integer with an exponential distribution within a specified range
int generate_exponential_int(int min, int max, double lambda)
{
    int n;
    do
    {
        double exp_num = generate_exponential(lambda);
        n = (int)round(exp_num);
    } while (n < min || n > max);
    return n;
}



