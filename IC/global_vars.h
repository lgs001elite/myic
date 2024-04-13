/*
 * global_vars.h
 *
 *  Created on: Dec 21, 2023
 *      Author: glu250
 */

#ifndef GLOBAL_VARS_H_
#define GLOBAL_VARS_H_
#include <stdint.h>
#include <stdbool.h>
#include "macro.h"
#include "coordinatorList.h"

#define HISLEN 20

char g_node_dimension;
char g_transBuffer[SPI_DATA_LEN];
int16_t g_driftTime;
int8_t g_preDriftTime;
char g_receiveBuffer[SPI_DATA_LEN];
char g_nodeType;

extern bool g_ifFindCoordinator;
SPI_Mode MasterMode;
int32_t g_chTimeSlots;
int32_t lastData;
bool g_ICListen;
char g_nodeAddress;
char g_nextNodeID;

extern char g_arrLoc;
extern char g_accuCharge;
extern  int g_connectionLen;
extern  int g_connectionNum;
extern int8_t g_currentNodeLoc;
extern  char g_TXData;
extern int16_t g_MaxChargeCycles;
extern char g_attConn;
extern char g_queueLen;
extern char g_rounds;
extern char g_systemStatus;
extern int8_t g_distributedLoc;
extern  int g_chargHis[HISLEN];
extern char g_locNum;
extern bool g_gotoLoc;
extern bool g_alignLoc;
extern int32_t g_receCounter;
extern double p_test;
extern uint32_t g_systimeCounter;

extern int16_t g_adjusUnits;
extern bool g_ifAdjustDrift;
Hashmap map;

#endif /* GLOBAL_VARS_H_ */
