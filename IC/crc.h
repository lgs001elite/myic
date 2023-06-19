#ifndef _crc_h
#define _crc_h
#include <stdint.h>

#define FALSE    0
#define TRUE    !FALSE
#define CRC16
typedef uint16_t  crc;

#define CRC_NAME            "CRC-16"
#define POLYNOMIAL            0x8005
#define INITIAL_REMAINDER    0x0000
#define FINAL_XOR_VALUE        0x0000
#define REFLECT_DATA        TRUE
#define REFLECT_REMAINDER    TRUE
#define CHECK_VALUE            0xBB3D

void  crcInit(void);
crc   crcFast(unsigned char const message[], int nBytes);
#endif /* _crc_h */
