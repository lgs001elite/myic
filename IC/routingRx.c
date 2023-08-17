#include <stdbool.h>
#include <string.h>
#include "routingRx.h"
#include "routingTx.h"
#include "public.h"
#include "hash.h"
#include "transitionData.h"
#include "crc.h"


void updateCRC(uint8_t relayPkt[])
{
    uint8_t crc_input[31] = {0};
    uint8_t i = 0;
    for (; i < 31; i++)
    {
        crc_input[i] = relayPkt[i];
    }

    crcInit();
    uint16_t crc_result = crcFast(crc_input, 31);
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
uint8_t *file_sha256(uint8_t *file, uint32_t file_size)
{
    SHA256_CTX ctx;
    sha256_init(&ctx);
    sha256_update(&ctx, file, file_size);
    sha256_final(&ctx, g_sha256_buf);
    return &g_sha256_buf[0];
}

bool check_completeness(uint8_t *receivedData)
{
    uint8_t rec_result[SPI_NONCRC_LEN];
    uint8_t i = 0;
    for (; i < SPI_NONCRC_LEN; i++)
    {
        rec_result[i] = receivedData[i];
    }
    crcInit();
    uint16_t crc_result = crcFast(rec_result, SPI_NONCRC_LEN);
    uint8_t res1 = (crc_result & 0xFF00) >> 8;
    uint8_t res2 = (crc_result & 0x00FF);

    while (res1 >= 0x7F)
    {
        res1 -= 0x7F;
    }

    while (res2 >= 0x7F)
    {
        res2 -= 0x7F;
    }

    if (res1 != receivedData[SPI_NONCRC_LEN])
    {
        return false;
    }

    if (res2 != receivedData[SPI_NONCRC_LEN + 1])
    {
        return false;
    }

    return true;
}

bool data_is_datagram(uint8_t *receivedData)
{
    uint8_t layerSendNode = receivedData[7];
    uint8_t senderID = receivedData[5];
    uint8_t packetSeq = receivedData[2];
    if (layerSendNode <= g_node_dimension)
    {
        return false;
    }
    g_currentPairedNodeID = senderID;
    if (g_pre_packet_seq == packetSeq)
    {
        g_sendAck = true;
        return false;
    }
    g_lastChargeCycles = receivedData[8];
    if (g_nextChargeCycles > g_chargeCycles)
    {
        g_basicChargeCycles = g_lastChargeCycles;
    }
    else
    {
        g_basicChargeCycles = g_chargeCycles;
    }
    g_MaxChargeCycles = g_basicChargeCycles * 3;
    g_attConn = 0;
    g_disConnNum = 0;
    g_pre_packet_seq = packetSeq;
    if (g_queueLen < MAXQUELEN)
    {
        g_queueLen = g_queueLen + 1;
    }
    g_sendAck = true;
    return true;
}

void data_is_ack(uint8_t *receivedData)
{
    uint8_t aimID      = receivedData[6];
    uint8_t senderID   = receivedData[5];
    uint8_t packetSeq  = receivedData[2];
    if ((aimID != g_nodeAddress) || (packetSeq != g_queueLen))
    {
        return;
    }
    if (g_nextNodeID == 0x7e)
    {
        g_nextNodeID = senderID;
    }
    else
    {
        if (g_nextNodeID != senderID)
        {
            return;
        }
    }
    g_nextChargeCycles = receivedData[8];
    if (g_nextChargeCycles > g_chargeCycles)
    {
        g_basicChargeCycles = g_nextChargeCycles;
    }
    else
    {
        g_basicChargeCycles = g_chargeCycles;
    }
    g_MaxChargeCycles = g_basicChargeCycles * 3;
    g_attConn = 0;
    g_queueLen = g_queueLen - 1;
    g_disConnNum = 0;
    if (g_queueLen == 0)
    {
        if (g_rounds > 0)
        {
            g_rounds = g_rounds - 1;
            g_queueLen = MAXQUELEN;
        }
        else
        {
            COMMS_LED_OUT ^= COMMS_LED_PIN;
            COMMS_LED_OUT ^= COMMS_LED_PIN2;
            //g_systemStatus == SINKWAIT;
        }
    }
}

void receiveDataFromNordic()
{
    // For testing find
    if (g_receiveBuffer[3] == 0x12)
    {
        g_findTesting = false;
        g_TXData = 0x50;
        COMMS_LED_OUT ^= COMMS_LED_PIN;
        COMMS_LED_OUT ^= COMMS_LED_PIN2;
        return;
    }
    // For testing find
    uint8_t i = 9;
    uint8_t sinkEcho = 0;
    for (; i < 33; i++)
    {
        if (g_receiveBuffer[i] != 0x01)
        {
            sinkEcho = 1;
        }
    }
    if (sinkEcho == 0)
    {
        uint8_t packetSeq = g_receiveBuffer[2];
        if ((g_receiveBuffer[8] != g_nodeAddress) || (packetSeq != g_queueLen))
        {
            return;
        }
        g_queueLen = g_queueLen - 1;
        GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
        return;
    }
    if ((g_receiveBuffer[3] == 0x33) && (g_receiveBuffer[4] == 0x44) && (g_receiveBuffer[5] == 0x55))
    {
        g_spi_waitThreshold = false;
    }
    if ((g_receiveBuffer[0] != 0x1e) || (g_receiveBuffer[1] != 0x17))
    {
        return;
    }
    bool checkResult = check_completeness(g_receiveBuffer);
    if (!checkResult)
    {
        return;
    }
    uint8_t dataType = g_receiveBuffer[3];
    switch (dataType)
    {
        case PACKAGE_PACKET:
            if (g_systemStatus == TRANSMIT)
            {
                break;
            }
            data_is_datagram(g_receiveBuffer);
            COMMS_LED_OUT ^= COMMS_LED_PIN2;
            break;
        case PACKAGE_ACK:
            data_is_ack(g_receiveBuffer);
            GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
            COMMS_LED_OUT ^= COMMS_LED_PIN;
            break;
        default:
            break;
    }
}
