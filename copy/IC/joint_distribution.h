/*
 * joint_distribution.h
 *
 *  Created on: Dec 21, 2023
 *      Author: glu250
 */

#ifndef JOINT_DISTRIBUTION_H_
#define JOINT_DISTRIBUTION_H_

#include <stdio.h>
#include <math.h>

double inverse_exponential_cdf(double q, double lambda);

// Structure for a single Gaussian distribution
typedef struct
{
    double mean;
    double variance;
    double weights;
} Gaussian;

// Structure for a Gaussian mixture model
typedef struct
{
    Gaussian *gaussians;
    int num_components;
} GaussianMixtureModel;

void freeGMM(GaussianMixtureModel *gmm);
double gaussianPDF(double x, Gaussian g);
double gmmPDF(double x, GaussianMixtureModel *gmm);
double cdfGMM(GaussianMixtureModel *gmm, double x);
double inverseCdfGMM(GaussianMixtureModel *gmm, double probability);

double inverse_standard_normal_cdf(double p);
void find_x1_x2_for_joint_probability(double joint_p, double *x1, double *x2);

#endif /* JOINT_DISTRIBUTION_H_ */
