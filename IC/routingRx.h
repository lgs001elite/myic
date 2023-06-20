#ifndef _ROUTINGRX_H_
#define _ROUTINGRX_H_

#include <stdint.h>

#define  rtLength  2

void receiveDataFromNordic();
void updateCRC(uint8_t relayPkt[]);
void data_is_find(uint8_t *receivedData);
void data_is_ack(uint8_t *receivedData);
void data_is_datagram(uint8_t *receivedData);

#endif
