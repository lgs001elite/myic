#ifndef _RAND_H_
#define _RAND_H_

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

typedef struct
{
    double mean;
    double stddev;
    double weight;
} GaussianComponent;

double generate_exponential(double lambda);
int generate_exponential_int(int min, int max, double lambda);

double generate_exponential(double lambda);
int choose_component(GaussianComponent *components, int n_components);
int generate_gaussian_mixture_int(GaussianComponent *components, int n_components, int min, int max);

double generate_normal(double mean, double stddev);
int generate_normal_positive_int(int min, int max, double mean, double stddev);


#endif
