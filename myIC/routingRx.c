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
#include "coordinator.h"

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

    while (relayPkt[31] >= 0x7F)
    {
        relayPkt[31] -= 0x7F;
    }

    while (relayPkt[32] >= 0x7F)
    {
        relayPkt[32] -= 0x7F;
    }
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

    while (res1 >= 0x7F)
    {
        res1 -= 0x7F;
    }
    if (res1 != temp1)
        {
            return false;
        }
    while (result >= 0x7F)
    {
        result -= 0x7F;
    }

    if (result != receive)
    {
        return false;
    }

    return true;
}

void data_from_ic(char *receivedData)
{
    g_sendAck = true;
}

void ack_from_ic(char *receivedData)
{
    g_receCounter = g_receCounter + 1;
}

void data_from_ic_to_coordinator(char *receivedData)
{
    char currentLoc = receivedData[8];
    char senderID = receivedData[5];
    if (currentLoc == -1)
    {
        if (g_synStrategy == FREEBEACON)
        {
            hash_table_insert(g_locTable, senderID, g_distributedNodeLoc);
        }
        else
        {
            g_distributedNodeLoc = 1;
        }
        g_sendBroad = true;
    }
    else
    {
        if (g_synStrategy == FREEBEACON)
        {
            char distributedLoc = hash_table_search(g_locTable, senderID);
            if (distributedLoc != currentLoc)
            {
                g_sendBroad = true;
                g_distributedNodeLoc = distributedLoc;
            }
        }
    }
}

void broad_from_coordinator(char *receivedData)
{
    uint8_t distributedLoc = receivedData[8];
    uint8_t globalLoc = receivedData[10];
    if (g_currentNodeLoc == -1)
    {
        if (globalLoc > distributedLoc)
        {
            g_biasForAlign = 30 - globalLoc + distributedLoc;
        }
        else
        {
            g_biasForAlign = distributedLoc - globalLoc;
        }
        g_currentNodeLoc = distributedLoc;
    }
    else if (distributedLoc != globalLoc)
    {
        if (globalLoc > distributedLoc)
        {
            g_biasForAlign = 30 - globalLoc + distributedLoc;
        }
        else
        {
            g_biasForAlign = distributedLoc - globalLoc;
        }
    }
    else
    {
    }
}

void receiveDataFromNordic()
{
    if ((g_receiveBuffer[3] == 0x33) && (g_receiveBuffer[4] == 0x44) && (g_receiveBuffer[5] == 0x55))
    {
        GPIO_MONINOR_OUT1 ^= GPIO_MONITOR_PIN3;
        return;
    }
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
    if ((g_nodeType == ICNODE) && (g_ICListen == true))
    {
        return;
    }
    char sender_dataType = g_receiveBuffer[3];
    char sender_nodeType = g_receiveBuffer[4];
    char sender_id = g_receiveBuffer[5];
    char dest_id = g_receiveBuffer[6];

    // Rewrite from here
    if (g_nodeType == ICNODE)
    {
        if (dest_id != g_nodeID)
        {
            return;
        }
        if (sender_nodeType == ICNODE)
        {
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
                return;
            }
        }
        else
        {
            if (sender_dataType == PACKAGE_BROAD)
            {
                broad_from_coordinator(g_receiveBuffer);
            }
            else
            {
                return;
            }
        }
    }
    else if (g_nodeType == COORDINATOR)
    {
        if (sender_nodeType == ICNODE)
        {
            data_from_ic_to_coordinator(g_receiveBuffer);
        }
        else
        {
            return;
        }
    }
    else
    {
        return;
    }
}
