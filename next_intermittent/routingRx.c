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
    relayPkt[31]     = (crc_result & 0xFF00)>>8;
    relayPkt[32]     = (crc_result & 0x00FF);

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
uint8_t * file_sha256(uint8_t * file, uint32_t file_size)
{
    SHA256_CTX   ctx;
    sha256_init(&ctx);
    sha256_update(&ctx, file, file_size);
    sha256_final(&ctx, g_sha256_buf);
    return &g_sha256_buf[0];
}

/**
 * @brief  SPIS check completeness of data

 */
bool check_completeness(uint8_t * receivedData)
{
    uint8_t rec_result[SPI_NONCRC_LEN];
    uint8_t i = 0;
    for (; i < SPI_NONCRC_LEN; i++)
    {
        rec_result[i] = receivedData[i];
    }

    crcInit();
    uint16_t crc_result = crcFast(rec_result, SPI_NONCRC_LEN);
    uint8_t res1        = (crc_result & 0xFF00)>>8;
    uint8_t res2        = (crc_result & 0x00FF);

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

void data_is_datagram(uint8_t receivedData[])
{
    // For datapackets, need to judge the relative layers between nodes.
    uint8_t layerSendNode = receivedData[6];
    uint8_t senderID      = receivedData[4];
    uint8_t packetSeq     = receivedData[2];
    if (layerSendNode <= g_node_dimension)
    {
        return;
    }
    if (g_currentPairedNodeID != 0xff)
    {
        if (g_currentPairedNodeID != senderID)
        {
            return;
        }
    }
    else
    {
        g_currentPairedNodeID = senderID;
    }

    // g_pre_packet_seq: for excising repeated frame, g_non_firstDatagram: for judge if starting.
    if ((g_pre_packet_seq == packetSeq) && g_non_firstDatagram)
    {
          return;
    }
    if (!g_non_firstDatagram)
    {
        g_non_firstDatagram = true;
    }
    // If received node, set waiting counter zero.
    g_waitReceiveCounter = 0;
    g_pre_packet_seq = packetSeq;

    uint8_t tempi = 0;
    /* 7: The payload size position */
    uint8_t reveived_payload_size = receivedData[7];
    while(tempi != reveived_payload_size)
    {
        /* 8: The starting position of payload */
        store_received_data[g_received_file_real_size] = receivedData[tempi + 8];
        g_received_file_real_size++;
        tempi++;
    }

    receivedData[4] = g_nodeAddress;
    updateCRC(receivedData);
    s2m(&g_packetQueue[g_queueLen], receivedData);
    g_queueLen = g_queueLen + 1;
    g_sendAck = true;
}

void data_is_fin(uint8_t receivedData[])
{
    uint8_t rec_seq_num  = receivedData[2];
    if (rec_seq_num == g_pre_fin_seq)
    {
        return;
    }
    g_pre_fin_seq        = rec_seq_num;

    uint8_t * gen_sha256 = file_sha256(store_received_data, g_received_file_real_size);
    bool      g_com_pass = true;
    uint8_t file_sha256_true[32] =
        {
            0X3D, 0XC2, 0X90, 0XB1, 0X1, 0XDB, 0XEA, 0XF6, 0X8E, 0X1C, 0XAC, 0X4F, 0X3D, 0X56, 0X1C, 0X7F,
            0X66, 0X5D, 0XCB, 0XE7, 0XFD, 0X4F, 0X21, 0XB5, 0X44, 0X7C, 0X25, 0X9, 0XCC, 0X4, 0XE1, 0X7
        };
    g_com_pass           = (memcmp(file_sha256_true, gen_sha256, SHA256_BLOCK_SIZE) == 0);
    if (g_com_pass)
    {
        //blink the led lights (and / or) transmition to next hop
        recevedSucess();
    } else {
        recevedFailure();
    }
    if (g_rounds == 0)
    {
        g_systemStatus = DONE;
    }
}

void data_is_reverseFin(uint8_t receivedData[])
{
    uint8_t rec_seq_num  = receivedData[2];
    if (rec_seq_num == g_pre_fin_seq)
    {
        return;
    }
    g_pre_fin_seq        = rec_seq_num;
    g_systemStatus = DONE;
    recevedSucess();
}

void data_is_find(uint8_t *receivedData)
{
    uint8_t receivedLayerNum = receivedData[6];
    if (g_node_dimension > receivedLayerNum)
    {
        g_node_dimension = receivedLayerNum;
        g_findThreshold = MAXFIND;
        g_systemStatus = NONLAYER;
        g_waitToFind = receivedData[2];
    }
}

void data_is_ack(uint8_t *receivedData)
{
    uint8_t aimID = receivedData[5];
    uint8_t senderID = receivedData[4];
    uint8_t packetSeq = receivedData[2];
    if (aimID != g_nodeAddress)
    {
        return;
    }
    if (g_nextNodeID == 0xff)
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
    if ((packetSeq == g_pre_ack_seq) && g_if_nonFirstAck)
    {
        return;
    }
    g_pre_ack_seq = packetSeq; // update the pre-seu number
    g_if_nonFirstAck  = true;
    g_queueLen = g_queueLen - 1;
    if (g_queueLen == 0)
    {
        if (g_rounds > 0)
        {
            g_rounds = g_rounds - 1;
        }
        if (g_rounds == 0)
        {
            g_finishSend = true;
            produceNonPacketData();
            g_transBuffer[3] = PACKAGE_FINISH;
            g_transBuffer[5] = senderID;
        }
    }
}


void receiveDataFromNordic()
{
    bool checkResult = check_completeness(g_receiveBuffer);
    if (! checkResult)
    {
         return;
    }
    // DST node checking
    uint8_t dstNodeAddress = g_receiveBuffer[5];
    if (dstNodeAddress != g_nodeAddress)
    {
        return;
    }
    // Recording the node ID of the send node
    g_receivedNodeAddress = g_receiveBuffer[4];
    // Recording the paired node
    uint8_t dataType = g_receiveBuffer[3];
    switch(dataType)
    {
     case PACKAGE_FIND:
         data_is_find(g_receiveBuffer);
         break;
     case PACKAGE_PACKET:
         data_is_datagram(g_receiveBuffer);
         break;
     case PACKAGE_FINISH:
         data_is_fin(g_receiveBuffer);
         break;
     case PACKAGE_RFINISH:
         data_is_reverseFin(g_receiveBuffer);
         break;
     case PACKAGE_ACK:
         data_is_ack(g_receiveBuffer);
         break;
     default:
         break;
    }
}
