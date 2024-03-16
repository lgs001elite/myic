/*
 * pins.h
 *
 *  Created on: Dec 21, 2023
 *      Author: glu250
 */

#ifndef PINS_H_
#define PINS_H_

#include <msp430.h>


#define SLAVE_CS_OUT P5OUT
#define SLAVE_CS_DIR P5DIR
#define SLAVE_CS_PIN BIT3

// in main , rx, tx
#define COMMS_LED_OUT P1OUT
#define COMMS_LED_DIR P1DIR
#define COMMS_LED_PIN BIT0
#define COMMS_LED_PIN2 BIT1

// in main Rx, tx
#define GPIO_MONINOR_OUT6 P6OUT
#define GPIO_MONITOR_DIR6 P6DIR
#define GPIO_MONINOR_OUT4 P4OUT
#define GPIO_MONITOR_DIR4 P4DIR
#define GPIO_MONITOR_PIN2 BIT2 // Packet around
#define GPIO_MONITOR_PIN3 BIT3 // Single path
#define GPIO_MONITOR_PIN1 BIT1




#endif /* PINS_H_ */
