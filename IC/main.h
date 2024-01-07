/*
 * main.h
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */


#ifndef MAIN_H
#define MAIN_H

#include <msp430.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <time.h>

bool g_MatchNextHop;
char g_switchUart;
char g_seq_data;
char g_transDataSeq;
// volatile int32_t g_var1;
void recoveryStates();


#endif /* MAIN_H */

