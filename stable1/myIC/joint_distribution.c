/*
 * joint_distribution.c
 *
 *  Created on: Dec 21, 2023
 *      Author: glu250
 */

#include "joint_distribution.h"



double inverse_exponential_cdf(double q, double lambda)
{
    return -log(1 - q) / lambda;
}




// Function to free a GMM
void freeGMM(GaussianMixtureModel *gmm)
{
    free(gmm->gaussians);
    free(gmm);
}

// Function to compute the PDF of a Gaussian at a given point
double gaussianPDF(double x, Gaussian g)
{
    return (1 / sqrt(2 * M_PI * g.variance)) * exp(-pow(x - g.mean, 2) / (2 * g.variance));
}

// Function to compute the PDF of a GMM at a given point
double gmmPDF(double x, GaussianMixtureModel *gmm)
{
    double pdf = 0.0;
    int i = 0;
    for (;i < gmm->num_components; ++i)
    {
        pdf += gmm->gaussians[i].weights * gaussianPDF(x, gmm->gaussians[i]);
    }
    return pdf;
}

// Function to compute the CDF of a GMM at a given point using numerical integration
double cdfGMM(GaussianMixtureModel *gmm, double x)
{
    double sum = 0.0;
    double dx = 0.01;       // Step size for integration
    double start = x - 100; // Start point for integration (assuming enough for GMM)

    double i = start;
    for (; i <= x; i += dx)
    {
        sum += gmmPDF(i, gmm) * dx;
    }

    return sum;
}

// Function to find the inverse CDF of a GMM using binary search
double inverseCdfGMM(GaussianMixtureModel *gmm, double probability)
{
    double lower = -100; // Lower bound of the search interval
    double upper = 100;  // Upper bound of the search interval
    double mid;
    double epsilon = 0.001; // Tolerance for the approximation

    while (upper - lower > epsilon)
    {
        mid = (lower + upper) / 2;
        double cdf_mid = cdfGMM(gmm, mid);

        if (cdf_mid < probability)
        {
            lower = mid;
        }
        else
        {
            upper = mid;
        }
    }

    return (lower + upper) / 2;
}




// Function to compute the inverse CDF (quantile function) of a standard normal distribution
double inverse_standard_normal_cdf(double p)
{
    // Coefficients for the rational approximation
    const double a[] = {-3.969683028665376e+01, 2.209460984245205e+02,
                        -2.759285104469687e+02, 1.383577518672690e+02,
                        -3.066479806614716e+01, 2.506628277459239e+00};
    const double b[] = {-5.447609879822406e+01, 1.615858368580409e+02,
                        -1.556989798598866e+02, 6.680131188771972e+01,
                        -1.328068155288572e+01};
    const double c[] = {-7.784894002430293e-03, -3.223964580411365e-01,
                        -2.400758277161838e+00, -2.549732539343734e+00,
                        4.374664141464968e+00, 2.938163982698783e+00};
    const double d[] = {7.784695709041462e-03, 3.224671290700398e-01,
                        2.445134137142996e+00, 3.754408661907416e+00};

    // Define break-points
    double p_low = 0.02425;
    double p_high = 1 - p_low;

    // Rational approximation for the lower region
    if (p < p_low)
    {
        double q = sqrt(-2 * log(p));
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) /
               ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1);
    }

    // Rational approximation for the central region
    if (p <= p_high)
    {
        double q = p - 0.5;
        double r = q * q;
        return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q /
               (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1);
    }

    // Rational approximation for the upper region
    double q = sqrt(-2 * log(1 - p));
    return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) /
           ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1);
}

// Function to find x1 and x2 for the joint CDF
void find_x1_x2_for_joint_probability(double joint_p, double *x1, double *x2)
{
    double sqrt_p = sqrt(joint_p); // Approximation for standard normal
    *x1 = inverse_standard_normal_cdf(sqrt_p);
    *x2 = inverse_standard_normal_cdf(sqrt_p);
}






