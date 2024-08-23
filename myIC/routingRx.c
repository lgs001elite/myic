/*
 * routingRx.c
 *
 *  Created on: June 20, 2024
 *      Author: glu250
 */
#include <stdbool.h>
#include <string.h>
#include "routingRx.h"
#include "routingTx.h"
#include "hash.h"
#include "crc.h"
#include "pins.h"
#include "global_func.h"
#include "global_vars.h"
#include "uartHex.h"
#include "uart.h"

bool check_completeness(char *receivedData)
{
    char rec_result[SPI_NONCRC_LEN];
    char i = 0;
    for (; i < SPI_NONCRC_LEN; i++)
    {
        rec_result[i] = receivedData[i];
    }
    int16_t crc_result = getCRC(receivedData);
    char res1 = (crc_result & 0xFF00) >> 8;
    char result = (crc_result & 0x00FF);
    char temp1 = receivedData[29];
    char receive = receivedData[30];

    while (res1 >= 0x7f)
    {
        res1 -= 0x7f;
    }

    if (res1 != temp1)
    {
        return false;
    }

    while (result >= 0x7f)
    {
        result -= 0x7f;
    }

    if (result != receive)
    {
        return false;
    }

    return true;
}

static void received_broad_packet(char *receivedData)
{
    if (g_currentNodeLoc == -1)
    {
        if (g_synStrategy == FREEBEACON)
        {
            g_biasForAlign = receivedData[10];
            g_currentNodeLoc = receivedData[9];
            g_distributedNodeLoc = receivedData[8];
        }
    }
    else
    {
        if (g_synStrategy == FREEBEACON)
        {
            g_biasForAlign = receivedData[10];
        }
    }
}

void receiveDataFromNordic()
{
    if ((g_receiveBuffer[0] != 0x1e) || (g_receiveBuffer[1] != 0x17))
    {
        return;
    }
    bool checkResult = check_completeness(g_receiveBuffer);
    if (checkResult == false)
    {
        __no_operation();
        return;
    }
    char sender_dataType = g_receiveBuffer[3];
    char sender_nodeType = g_receiveBuffer[4];

    // Rewrite from here
    if (sender_dataType == PACKAGE_PACKET)
    {
        if (g_receData == false)
        {
            GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN3;
            g_sendAck = true;
            g_receData = true;
        }
    }
    else if (sender_dataType == PACKAGE_ACK)
    {
        if (g_receAck == false)
        {
            GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN4;
            g_receCounter = g_receCounter + 1;
            g_receData = true;
            g_fbAttemptNum = 0;
        }
    }
    else
    {
        if (sender_nodeType == COORDINATOR)
        {
            received_broad_packet(g_receiveBuffer);
        }
    }
}
