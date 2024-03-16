/*
 * distribution.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */


#include "distribution.h"

// Exponential distribution
void update_lambda_expo(double x, double *lambda, double learning_rate)
{
  // Update lambda based on the new observation x
  *lambda = *lambda - learning_rate * (-1.0 / *lambda + x);
}

// Initialize Gaussian components
void initialize_components_gaumix(GaussianComponentMix *components)
{
  components[0].mean = 0;
  components[0].variance = 1;
  components[0].weight = 0.5;

  components[1].mean = 5;
  components[1].variance = 1;
  components[1].weight = 0.5;
}

// Gaussian PDF
double gaussian_pdf_gaumix(double x, double mean, double variance)
{
  return (1.0 / sqrt(2 * M_PI * variance)) * exp(-pow(x - mean, 2) / (2 * variance));
}

// Update parameters of a component
void update_component_gaumix(double x, GaussianComponentMix *component, double learning_rate)
{
  double diff = x - component->mean;
  component->mean += learning_rate * diff;
  component->variance += learning_rate * (diff * diff - component->variance);
}



// This is for normal distribution
void update_parameters_normal(double x, double *mu, double *sigma, double learning_rate)
{
  double mu_old = *mu;
  double sigma_old = *sigma;

  // Calculate gradients
  double grad_mu = (x - mu_old) / (sigma_old * sigma_old);
  double grad_sigma = -1.0 / sigma_old + (x - mu_old) * (x - mu_old) / (sigma_old * sigma_old * sigma_old);

  // Update parameters
  *mu = mu_old + learning_rate * grad_mu;
  *sigma = sigma_old + learning_rate * grad_sigma;
}

