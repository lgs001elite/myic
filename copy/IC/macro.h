/*
 * macro.h
 *
 *  Created on: Dec 21, 2023
 *      Author: glu250
 */

#ifndef MACRO_H_
#define MACRO_H_


#define DUMMY 0x7e
#define CMD_TYPE_0_SLAVE 0xAA
#define CMD_TYPE_0_MASTER 0x0
#define SPI_DATA_LEN 0x1f
#define DRIFTUNIT 0xffff

#define COORDINATOR 0x01
#define ICNODE 0x02

#define PACKAGE_PACKET 0x01
#define PACKAGE_ACK 0x02
#define DUBBY 0x03

typedef enum SPI_ModeEnum
{
    IDLE_MODE,
    TX_REG_ADDRESS_MODE,
    RX_REG_ADDRESS_MODE,
    TX_DATA_MODE,
    RX_DATA_MODE
} SPI_Mode;




#endif /* MACRO_H_ */
