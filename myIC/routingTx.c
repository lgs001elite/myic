/*
 * routingTx.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "routingTx.h"
#include "random.h"
#include "macro.h"
#include "pins.h"
#include "global_func.h"
#include "global_vars.h"
#include "crc.h"

void produceNonPacketData(void)
{
    g_transBuffer[0]  = 0x1E;
    g_transBuffer[1]  = BLE_GAP_AD_TYPE;
    g_transBuffer[2]  = 0x01; // For packetSeq
    g_transBuffer[3]  = DUBBY; // message type
    g_transBuffer[4]  = COORDINATOR; // node type
    g_transBuffer[5]  = g_nodeAddress;
    g_transBuffer[6]  = g_nextNodeID;
    g_transBuffer[7]  = g_node_dimension;
    g_transBuffer[8]  = g_currentNodeLoc;
    g_transBuffer[9]  = g_currentNodeLoc; // des in coordinator circle.
    g_transBuffer[10] = g_driftTime;
    int8_t i = 3;
    for (; i >= 0; i--)
    {
        char temp = (g_chTimeSlots >> (i * 8)) & 0xff;
        g_transBuffer[14 - i] = temp;
    }
    i = 15;
    for (; i < 29; i++)
    {
        g_transBuffer[i] = 0;
    }
    char crc_input[29];
    i = 0;
    for (; i < 29; i++)
    {
        crc_input[i] = g_transBuffer[i];
    }
    int16_t crc_result = getCRC(crc_input);
    g_transBuffer[29] = (crc_result & 0xFF00) >> 8;
    g_transBuffer[30] = (crc_result & 0x00FF);

    while (g_transBuffer[29] >= 0x7F)
    {
        g_transBuffer[29] -= 0x7F;
    }

    while (g_transBuffer[30] >= 0x7F)
    {
        g_transBuffer[30] -= 0x7F;
    }
}
