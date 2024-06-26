/*
 * global_vars.h
 *
 *  Created on: June 21, 2024
 *      Author: glu250
 */

#ifndef GLOBAL_VARS_H_
#define GLOBAL_VARS_H_
#include <stdint.h>
#include <stdbool.h>
#include "macro.h"

#define HISLEN 20

char g_dest_location;
char g_transBuffer[SPI_DATA_LEN];
int8_t g_preDriftTime;
char g_receiveBuffer[SPI_DATA_LEN];

extern bool g_ifFindCoordinator;
SPI_Mode MasterMode;
uint16_t g_chTimeSlots;
uint16_t g_lastData;
bool g_ICListen;
uint8_t g_nodeID;
char g_nextNodeID;

extern uint8_t g_biasForAlign;
extern char g_arrLoc;
extern char g_accuCharge;
extern  int g_connectionLen;
extern  int g_connectionNum;
extern char g_currentNodeLoc;
extern uint8_t g_distributedNodeLoc;
extern  char g_TXData;
extern int16_t g_MaxChargeCycles;
extern char g_attConn;
extern char g_queueLen;
extern char g_rounds;
extern char g_systemStatus;
extern uint8_t g_distributedLoc;
extern  int g_chargHis[HISLEN];
extern char g_locNum;
extern bool g_gotoLoc;
extern bool g_alignLoc;
extern uint16_t g_receCounter;
extern uint8_t g_packet_id;
// extern double p_test;
extern uint32_t g_systimeCounter;

extern bool g_ifAdjustDrift;

#endif /* GLOBAL_VARS_H_ */
