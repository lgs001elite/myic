/*
 * uart.h
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */

#ifndef UART_H_
#define UART_H_

#include "macro.h"
#include "pins.h"
#include "global_func.h"
#include "global_vars.h"


#define LED_OUT P1OUT
#define LED_DIR P1DIR
#define LED0_PIN BIT0
#define LED1_PIN BIT1

#define SMCLK_115200 0
#define SMCLK_9600 1
#define ACLK_9600 2
#define UART_MODE SMCLK_115200

#define AMPLIFIER 30
#define UARTTIME 5

#define Find 0
#define NeutronStar 1
#define CYCLE 2
#define NeutronStarNoAli 3
#define Greedy 4
#define NeutronStarPlus 5

char g_synStrategy;
char g_receveuartNum;
char g_uartArr[2];
bool g_uartSwitch;

void initGPIO();
void ClockTo24MHz();
void initUART();
void uartAction();

int uniformInt(int min, int max);

#endif /* UART_H_ */
