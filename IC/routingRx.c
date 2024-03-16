/*
 * routingRx.c
 *
 *  Created on: Dec 20, 2023
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


void data_is_datagramCoor(char *receivedData)
{
    if (g_nodeType == ICNODE)
    {
        int8_t receivedDriftTime = receivedData[10];
        if ((g_ifAdjustDrift == false) && (g_currentNodeLoc != 1))
        {
            g_adjusUnits = g_driftTime  - receivedDriftTime;
            g_ifAdjustDrift = true;
            //g_driftTime = 0;
        }
       // GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN2;
        g_sendAck    = true;
        g_nextNodeID = receivedData[5];
    }
    else
    {
        /*
            to do here;
        */
    }
}

void data_is_ackCoor(char *receivedData)
{
    char aimID = receivedData[6];
    char senderID = receivedData[5];
    char packetSeq = receivedData[2];
    char pairedLoc = receivedData[8];
    char destLoc = receivedData[9];
    if (aimID == g_nodeAddress)
    {
        if (g_nodeType == ICNODE)
        {
            g_distributedLoc = receivedData[8];
            g_currentNodeLoc = receivedData[9];
            g_gotoLoc = true;
            //GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
            // COMMS_LED_OUT ^= COMMS_LED_PIN;
            // COMMS_LED_OUT ^= COMMS_LED_PIN2;
        }
        else
        {
            /*
                to do here;
            */
        }
    }
}

void data_is_datagramIC(char *receivedData)
{
    char packetSeq = receivedData[2];
    char senderID = receivedData[5];
    int8_t receivedDriftTime = receivedData[10];
    int8_t senderLoc = receivedData[9];
    if (g_nodeType == ICNODE)
    {
        // if (g_currentPairedNodeID != -1)
        // {
        //     if (g_currentPairedNodeID != g_transBuffer[5])
        //     {
        //         __no_operation();
        //         return;
        //     }
        // }
        if ((g_ifAdjustDrift == false) && (g_currentNodeLoc == 1) && (senderLoc == 1))
        {
            g_adjusUnits = g_driftTime  - receivedDriftTime;
            g_ifAdjustDrift = true;
            // g_driftTime = 0;
            // GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
            // GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN2;
        }
        // g_sendAck = true;
        if (g_pre_packet_seq != packetSeq)
        {
            // COMMS_LED_OUT ^= COMMS_LED_PIN;
            // COMMS_LED_OUT ^= COMMS_LED_PIN2;
            char locInCoordinator = receivedData[8];
            char desLoc = receivedData[9];
            char tempArr[4];
            tempArr[0] = receivedData[11];
            tempArr[1] = receivedData[12];
            tempArr[2] = receivedData[13];
            tempArr[3] = receivedData[14];
            g_pairedChargeCycles = combineBytes(tempArr);
            g_pre_packet_seq = packetSeq;
            g_nextNodeID = senderID;
            g_receCounter = g_receCounter + 1;
            GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
        }
    }
    else
    {
        /*
            to do here;
        */
    }
}

void data_is_ackIC(char *receivedData)
{
    char aimID = receivedData[6];
    char senderID = receivedData[5];
    char packetSeq = receivedData[2];
    char pairedLoc = receivedData[8];
    char destLoc = receivedData[9];

    if (aimID == g_nodeAddress)
    {
        if (g_currentPairedNodeID == -1)
        {
            g_currentPairedNodeID = senderID;
            if (g_nodeType == ICNODE)
            {
                // if (g_currentPairedNodeID != -1)
                // {
                //     if (g_currentPairedNodeID != g_transBuffer[5])
                //     {
                //         __no_operation();
                //         return;
                //     }
                // }
                // if ((aimID == g_nodeAddress) && (packetSeq == g_queueLen))
                // {
                //     g_receCounter = g_receCounter + 1;
                //     __no_operation();
                // }
                // if (aimID == g_nodeAddress)
                // {
                //     g_receCounter = g_receCounter + 1;
                //     __no_operation();
                // }
            }
            else
            {
                g_sendAck = true;
                // GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN2;
                // COMMS_LED_OUT ^= COMMS_LED_PIN;
                g_nextNodeID = senderID;
                // COMMS_LED_OUT ^= COMMS_LED_PIN2;
                // g_currentNodeLoc = g_currentNodeLoc + 1;
                /**  IN the phase, we do not need the record the node loc */
                // if (hashmap_find(&map, senderID) == -1)
                // {
                //     hashmap_insert(&map, senderID, g_currentNodeLoc);
                //     g_currentNodeLoc = g_currentNodeLoc + 1;
                // }
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
    __no_operation();
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
        // GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN2;
    }
        char sender_dataType = g_receiveBuffer[3];
    char sender_nodeType = g_receiveBuffer[4];
    if (sender_nodeType == COORDINATOR)
    {
        if (g_nodeType == ICNODE)
        {
            g_ifFindCoordinator = true;
            // COMMS_LED_OUT ^= COMMS_LED_PIN;
            // COMMS_LED_OUT ^= COMMS_LED_PIN2;
        }
        switch (sender_dataType)
        {
            case PACKAGE_PACKET:
                data_is_datagramCoor(g_receiveBuffer);
                break;
            case PACKAGE_ACK:
                data_is_ackCoor(g_receiveBuffer);
                break;
            default:
                break;
        }
    }
    if (sender_nodeType == ICNODE)
    {
        switch (sender_dataType)
        {
            case PACKAGE_PACKET:
                data_is_datagramIC(g_receiveBuffer);
                break;
            case PACKAGE_ACK:
                data_is_ackIC(g_receiveBuffer);
                break;
            default:
                break;
        }
    }
}
