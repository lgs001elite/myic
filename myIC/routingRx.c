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

void updateCRC(char relayPkt[])
{
    char crc_input[31] = {0};
    char i = 0;
    for (; i < 31; i++)
    {
        crc_input[i] = relayPkt[i];
    }
    int16_t crc_result = crcFast(crc_input, 31);
    relayPkt[31] = (crc_result & 0xFF00) >> 8;
    relayPkt[32] = (crc_result & 0x00FF);
}

/** for checking the entire file  **/
char *file_sha256(char *file, int32_t file_size)
{
    SHA256_CTX ctx;
    sha256_init(&ctx);
    sha256_update(&ctx, file, file_size);
    sha256_final(&ctx, g_sha256_buf);
    return &g_sha256_buf[0];
}

bool check_completeness(char *receivedData)
{
    char rec_result[SPI_NONCRC_LEN];
    char i = 0;
    for (; i < SPI_NONCRC_LEN; i++)
    {
        rec_result[i] = receivedData[i];
    }
    int16_t crc_result = getCRC(receivedData);
    char res1  = (crc_result & 0xFF00) >> 8;
    char result  = (crc_result & 0x00FF);
    char temp1 = receivedData[29];
    char receive = receivedData[30];

    if (res1 != temp1)
    {
        return false;
    }

    if (result != receive)
    {
        return false;
    }

    return true;
}

void data_from_ic(char *receivedData)
{
    char dest_id = g_receiveBuffer[6];
    if (dest_id != g_nodeID)
    {
        return;
    }
    g_nextNodeID = g_receiveBuffer[5];
    g_sendAck = true;
}

void ack_from_ic(char *receivedData)
{
    char dest_id = g_receiveBuffer[6];
    if (dest_id != g_nodeID)
    {
        return;
    }
    g_receCounter = g_receCounter + 1;
}

void broad_from_coordinator(char *receivedData)
{
    uint8_t globalLoc = receivedData[10];
    if (g_currentNodeLoc == -1)
    {
        // For two nodes, they have same syn location.
        // Therefore, we do not need to distribute different locations fo synchronization
        if (globalLoc != 0)
        {
            if (g_synStrategy == PULSAR)
            {
                g_biasForAlign = 3 - globalLoc;
            }
            else
            {
                g_biasForAlign = 30 - globalLoc;
            }
            g_alignLoc = true;
        }
        g_currentNodeLoc = 0;
        g_sendAck = true;
    }
    else
    {
        char dest_id = g_receiveBuffer[6];
        if (dest_id != g_nodeID)
        {
            return;
        }
        if (g_distributedLoc != globalLoc)
        {
            if (globalLoc > g_distributedLoc)
            {
                g_biasForAlign = 30 - globalLoc + g_distributedLoc;
            }
            else
            {
                g_biasForAlign = g_distributedLoc - globalLoc;
            }
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
    if (g_systemStatus == TRANSMIT)
    {
        __no_operation();
        return;
    }
    if ((g_ICListen == true))
    {
        return;
    }
    char sender_dataType = g_receiveBuffer[3];
    char sender_nodeType = g_receiveBuffer[4];
    char sender_id = g_receiveBuffer[5];

    // Rewrite from here
    if (sender_dataType == PACKAGE_PACKET)
    {
        data_from_ic(g_receiveBuffer);
    }
    else if (sender_dataType == PACKAGE_ACK)
    {
        ack_from_ic(g_receiveBuffer);
    }
    else
    {
        broad_from_coordinator(g_receiveBuffer);
    }
}
