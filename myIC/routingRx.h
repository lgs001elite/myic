/*
 * routingRx.h
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */

#ifndef ROUTINGRX_H_
#define ROUTINGRX_H_

#include <stdint.h>
#include <stdbool.h>
#include "macro.h"

#define  rtLength  2
// in Rx
#define TRANSMIT 1
#define SINKWAIT 4
#define MAXQUELEN 12
#define MAXROUND 10
#define SHA256_BLOCK_SIZE 32 // SHA256 outputs a 32 byte digest
// in rx
int32_t g_basicChargeCycles;
int32_t g_pairedChargeCycles;
int32_t g_lastChargeCycles;
bool g_sendAck;

// in rx
char g_sha256_buf[SHA256_BLOCK_SIZE];
extern uint8_t g_pre_packet_seq;
int8_t g_currentPairedNodeID;


void receiveDataFromNordic();
void updateCRC(char relayPkt[]);
void data_is_find(char *receivedData);
void data_is_ackIC(char *receivedData);
void data_is_ackCoor(char *receivedData);
void data_is_datagramIC(char *receivedData);
void data_is_datagramCoor(char *receivedData);
#endif /* ROUTINGRX_H_ */
