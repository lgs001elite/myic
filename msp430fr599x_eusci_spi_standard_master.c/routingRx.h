#ifndef _ROUTINGRX_H_
#define _ROUTINGRX_H_

#include <stdint.h>

#define  rtLength  2

void receiveDataFromNordic();
void updateCRC(uint8_t relayPkt[]);

#endif
