
#include "rand.h"


double generate_normal(double mean, double stddev)
{
    static double n2 = 0.0;
    static int n2_cached = 0;
    if (!n2_cached)
    {
        double x, y, r;
        do
        {
            x = 2.0 * rand() / RAND_MAX - 1;
            y = 2.0 * rand() / RAND_MAX - 1;
            r = x * x + y * y;
        } while (r == 0.0 || r > 1.0);
        {
            double d = sqrt(-2.0 * log(r) / r);
            double n1 = x * d;
            n2 = y * d;
            double result = n1 * stddev + mean;
            n2_cached = 1;
            return result;
        }
    }
    else
    {
        n2_cached = 0;
        return n2 * stddev + mean;
    }
}

int choose_component(GaussianComponent *components, int n_components)
{
    double rand_val = (double)rand() / RAND_MAX;
    double cumulative_weight = 0.0;
    int i = 0;
    for (; i < n_components; ++i)
    {
        cumulative_weight += components[i].weight;
        if (rand_val <= cumulative_weight)
        {
            return i;
        }
    }
    return n_components - 1; // In case of rounding errors
}

int generate_gaussian_mixture_int(GaussianComponent *components, int n_components, int min, int max)
{
    int component_index = choose_component(components, n_components);
    double mean = components[component_index].mean;
    double stddev = components[component_index].stddev;

    int number;
    do
    {
        double normal_float = generate_normal(mean, stddev);
        number = (int)round(normal_float);
    } while (number < min || number > max);

    return number;
}

