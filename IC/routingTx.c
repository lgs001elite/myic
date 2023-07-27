#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "routingTx.h"
#include "public.h"
#include "random.h"
#include "transitionData.h"


void produceData(uint8_t packetNum)
{
    g_packetQueue.hp_len = 0x1E;
    g_packetQueue.t_broad_type = BLE_GAP_AD_TYPE;
    g_packetQueue.src = g_nodeAddress;
    g_packetQueue.dst = g_nextNodeID;
    g_packetQueue.layer = g_node_dimension;
    g_packetQueue.status = PACKAGE_PACKET;
    g_packetQueue.seq = packetNum;
    g_packetQueue.round = g_rounds;
    g_seq_data = g_seq_data + 1;
    if (g_seq_data == MAXQUELEN)
    {
        g_seq_data = 0;
    }
    uint8_t j = 0;
    for (; j < PACKET_DATA_LEN; j++)
    {
        (g_packetQueue.df)[j] = 0x11;
        g_transDataSeq++;
    }
}

void produceNonPacketData(void)
{
    g_transBuffer[0] = 0x1E;
    g_transBuffer[1] = BLE_GAP_AD_TYPE;
    g_transBuffer[2] = g_waitToFind;
    g_transBuffer[3] = DUBBY;
    g_transBuffer[4] = 0;
    g_transBuffer[5] = 0;
    g_transBuffer[6] = 0;
    g_transBuffer[7] = g_node_dimension;
    uint8_t i = 8;
    // const uint8_t anchor = 8;
    for (; i < 31; i++)
    {
        // uint8_t j = i - anchor;
        g_transBuffer[i] = 0;
    }
    uint8_t crc_input[31];
    i = 0;
    for (; i < 31; i++)
    {
        crc_input[i] = g_transBuffer[i];
    }

    uint16_t crc_result = getCRC(crc_input);
    g_transBuffer[31] = (crc_result & 0xFF00) >> 8;
    g_transBuffer[32] = (crc_result & 0x00FF);

    while (g_transBuffer[31] >= 0x7F)
    {
        g_transBuffer[31] -= 0x7F;
    }

    while (g_transBuffer[32] >= 0x7F)
    {
        g_transBuffer[32] -= 0x7F;
    }
}
