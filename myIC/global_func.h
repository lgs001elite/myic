/*
 * global_func.h
 *
 *  Created on: June 21, 2024
 *      Author: glu250
 */

#ifndef GLOBAL_FUNC_H_
#define GLOBAL_FUNC_H_
#include <stdint.h>

uint16_t findDelay(uint16_t c);
uint16_t flyncDelay(uint16_t c);
uint16_t pulsarDelay(uint16_t c);
uint16_t freeBeaconDelay(uint16_t c);
void start_spi_process(void);

#endif /* GLOBAL_FUNC_H_ */
