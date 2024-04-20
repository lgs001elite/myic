
#include "rand.h"


// Function to generate a random positive integer with a normal distribution within a specified range
int generate_normal_positive_int(int min, int max, double mean, double stddev)
{
    double n;
    int n_int;
    do
    {
        n = generate_normal(mean, stddev);
        n_int = (int)round(n);
    } while (n_int < min || n_int > max);
    return n_int;
}
