/**********************************************************************
 *
 * Filename:    crc.h
 * 
 * Description: A header file describing the various CRC standards.
 *
 * Notes:       
 *
 * 
 * Copyright (c) 2000 by Michael Barr.  This software is placed into
 * the public domain and may be used for any purpose.  However, this
 * notice must not be changed or removed and no warranty is either
 * expressed or implied by its publication or distribution.
 * 
 * Modefied by Haosheng Liu, This is just for research!
 **********************************************************************/

#ifndef _crc_h
#define _crc_h
#include <stdint.h>

#define FALSE	0
#define TRUE	!FALSE

/*
 * Select the CRC standard from the list that follows.
 */
#define CRC16


typedef uint16_t  crc;

#define CRC_NAME			"CRC-16"
#define POLYNOMIAL			0x8005
#define INITIAL_REMAINDER	0x0000
#define FINAL_XOR_VALUE		0x0000
#define REFLECT_DATA		TRUE
#define REFLECT_REMAINDER	TRUE
#define CHECK_VALUE			0xBB3D

void  crcInit(void);
crc   crcFast(unsigned char const message[], int nBytes);
#endif /* _crc_h */
