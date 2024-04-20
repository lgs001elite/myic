/*
 * crc.h
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */

#ifndef crc_h
#define crc_h
#include <stdint.h>

#define FALSE    0
#define TRUE    !FALSE
#define CRC16
typedef int16_t  crc;

#define CRC_NAME            "CRC-16"
#define POLYNOMIAL            0x8005
#define INITIAL_REMAINDER    0x0000
#define FINAL_XOR_VALUE        0x0000
#define REFLECT_DATA        TRUE
#define REFLECT_REMAINDER    TRUE
#define CHECK_VALUE            0xBB3D




// in crc
void update_crc();

// in crc, tx
int16_t getCRC(char const message[]);
int16_t getUartCRC(char const message[]);

void crcInit(void);
crc   crcFast(char const message[], int nBytes);
#endif /* crc_h */
