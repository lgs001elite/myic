#ifndef _ROUTINGRX_H_
#define _ROUTINGRX_H_

#include <stdint.h>

void receiveDataFromNordic();
void data_is_ack(uint8_t receivedData[]);
void data_is_fin();
void data_is_reverseFin();
void data_is_find(uint8_t receivedData[]);
void data_is_datagram(uint8_t receivedData[]);

#endif
