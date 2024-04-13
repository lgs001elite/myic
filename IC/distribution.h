/*
 * distribution.h
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */

#ifndef DISTRIBUTION_H_
#define DISTRIBUTION_H_

#include <stdio.h>
#include <math.h>

typedef struct
{
    double mean;
    double variance;
    double weight; // Mixture weight
} GaussianComponentMix;

void initialize_components_gaumix(GaussianComponentMix *components);
double gaussian_pdf_gaumix(double x, double mean, double variance);
void update_component_gaumix(double x, GaussianComponentMix *component, double learning_rate);

void update_parameters_normal(double x, double *mu, double *sigma, double learning_rate);
void update_lambda_expo(double x, double *lambda, double learning_rate);

#endif /* DISTRIBUTION_H_ */
