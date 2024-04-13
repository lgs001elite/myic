/*
 * coordinatorFind.c
 *
 *  Created on: Dec 21, 2023
 *      Author: glu250
 */

#include "coordinatorFind.h"
#include "global_func.h"
#include "global_vars.h"
#include "pins.h"
#include "uart.h"

int16_t coFindDelay(int16_t c)
{
    int16_t bias = (c + 1) % COORDINATOR_CYCLES;
    int16_t delay = COORDINATOR_CYCLES - bias;
    if(g_ifFindCoordinator == false)
    {
        delay = delay + 1;
        delay = delay * AMPLIFIER + 10;
    }
    else
    {
        delay = delay * AMPLIFIER + 2;
    }
    return delay;
}





