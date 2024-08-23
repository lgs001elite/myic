/*
 * find.c
 *
 *  Created on: June 3, 2024
 *      Author: glu250
 */

#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include "find.h"
#include "global_vars.h"

int chargingRange[] = {200, 150, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5};
double paraRange[] = {0.08162253468723255, 0.09523721651237368, 0.12756012326620422, 0.13162741909742123,
                      0.1360414666363674, 0.1417278033654288, 0.147068374954429, 0.15295236767946493,
                      0.1594758097419207, 0.1666626448457833, 0.17668204800909043, 0.18621076584626142,
                      0.1971694394831866, 0.20993846405836497, 0.2250532633294418, 0.2487218064633894,
                      0.27290992267137204, 0.30433114845446796, 0.3473958282184392, 0.41162111340203345,
                      0.5243514859675414, 0.8358041858099494};

uint16_t findDelay(uint16_t c)
{
    srand(time(NULL));
    uint8_t find_i = 0;
    uint16_t reValue = 0;
    for (; find_i < 22; find_i++)
    {
        if (c >= chargingRange[find_i])
        {
            double u = rand() / (RAND_MAX + 1.0);
            reValue = (uint16_t)ceil(log(1 - u) / log(1 - paraRange[find_i]));
            break;
        }
    }
    return reValue;
}
uint16_t freeBeaconDelay(uint16_t c)
{
    uint16_t bias = c % 30;
    if (bias != 0)
    {
        bias = 30 - bias;
    }
    return bias;
}
