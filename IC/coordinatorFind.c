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


int coFindDelay(int c)
{
    int bias = (c + 1) % COORDINATOR_CYCLES;
    int delay = 0;
    if(g_ifFindCoordinator == true)
    {
        delay = COORDINATOR_CYCLES - bias + 1;
        COMMS_LED_OUT ^= COMMS_LED_PIN;
        __no_operation();
    }
    else
    {
        COMMS_LED_OUT ^= COMMS_LED_PIN2;
        delay = COORDINATOR_CYCLES - bias + 1 + 1;
        g_aliaslots = g_aliaslots + 1;
        g_aliaslots = g_aliaslots % COORDINATOR_CYCLES;
        __no_operation();
    }
    return delay;
}





