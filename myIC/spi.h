/*
 * spi.h
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */

#ifndef SPI_H_
#define SPI_H_
#include <msp430.h>
#include <stdbool.h>
#include <stdint.h>
#include "macro.h"
#include "pins.h"
#include "global_func.h"
#include "global_vars.h"

/* The Register Address/Command to use*/
char RXByteCtr;
char TXByteCtr;
char g_transmitIndex;

char g_receiveIndex;

void SPI_Master_ReadReg(char count);
void SPI_Master_WriteReg(char count);
void CopyArray(char *source, char *dest, char count);
void SendUCB1Data(char val);

void initSPI();
void start_spi_process(void);

#endif /* SPI_H_ */

