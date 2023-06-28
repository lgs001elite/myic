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
    g_pre_packet_seq = packetSeq;
    if ((g_if_sourceNode) && (g_queueLen < MAXQUELEN))
    {
        receivedData[5] = g_nodeAddress;
        updateCRC(receivedData);
        s2m(&g_packetQueue[g_queueLen], receivedData);
        g_queueLen = g_queueLen + 1;
    }
    g_sendAck = true;
    return true;
}

void data_is_find(uint8_t *receivedData)
{
    uint8_t receivedLayerNum = receivedData[7];
    if (g_node_dimension > (receivedLayerNum + 1))
    {
        g_node_dimension = receivedLayerNum + 1;
        g_waitToFind = receivedData[2] + 0x7e;
    }
}

void data_is_ack(uint8_t *receivedData)
{
    uint8_t aimID = receivedData[6];
    uint8_t senderID = receivedData[5];
    uint8_t packetSeq = receivedData[2];
    if (aimID != g_nodeAddress)
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
    if (packetSeq == g_pre_ack_seq)
    {
        return;
    }
    g_pre_ack_seq = packetSeq;
    g_queueLen = g_queueLen - 1;
    if (g_queueLen == 0)
    {
        if (g_rounds > 0)
        {
            g_rounds = g_rounds - 1;
            produceData();
        }
        else
        {
            COMMS_LED_OUT ^= COMMS_LED_PIN;
            COMMS_LED_OUT ^= COMMS_LED_PIN2;
        }
    }
}

bool receiveDataFromNordic()
{
    if ((g_receiveBuffer[0] != 0x1e) || (g_receiveBuffer[1] != 0x17))
    {
        return false;
    }
    bool checkResult = check_completeness(g_receiveBuffer);
    if (!checkResult)
    {
        return false;
    }
    uint8_t dataType = g_receiveBuffer[3];
    switch (dataType)
    {
    case PACKAGE_FIND:
        data_is_find(g_receiveBuffer);
        COMMS_LED_OUT ^= COMMS_LED_PIN;
        break;
    case PACKAGE_PACKET:
        data_is_datagram(g_receiveBuffer);
        COMMS_LED_OUT ^= COMMS_LED_PIN2;
        break;
    case PACKAGE_ACK:
        data_is_ack(g_receiveBuffer);
        COMMS_LED_OUT ^= COMMS_LED_PIN;
        break;
    default:
        break;
    }
    return true;
}
