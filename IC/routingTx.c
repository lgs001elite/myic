#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "routingTx.h"
#include "public.h"
#include "random.h"
#include "transitionData.h"
#include "source_DB.h"

void free_pointer(uint8_t * pointer)
{
    free(pointer);
    pointer = NULL;
}

void produceData(void)
{
    uint32_t i = 0;
    for (; i < (MAXQUELEN); i++)
    {
        g_packetQueue[g_queueLen].hp_len = 0x1E;
        g_packetQueue[g_queueLen].t_broad_type = BLE_GAP_AD_TYPE;
        g_packetQueue[g_queueLen].src = g_nodeAddress;
        g_packetQueue[g_queueLen].dst = g_nextNodeID;
        g_packetQueue[g_queueLen].layer = g_node_dimension;
        g_packetQueue[g_queueLen].status = PACKAGE_PACKET;
        g_packetQueue[g_queueLen].seq = (g_seq_data + 1) % MAXQUELEN;
        g_packetQueue[g_queueLen].round = g_rounds;
        g_seq_data = g_seq_data + 1;
        if (g_seq_data == MAXQUELEN)
        {
            g_seq_data = 0;
        }
        uint8_t j = 0;
        for (; j < PACKET_DATA_LEN; j++)
        {
            (g_packetQueue[g_queueLen].df)[j] = file_data[g_transDataSeq];
            g_transDataSeq++;
        }
        if (g_transDataSeq == MAXBYTE)
        {
            g_transDataSeq = 0;
        }
        g_queueLen = g_queueLen + 1;
        __delay_cycles(100000);
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
    const uint8_t anchor = 8;
    for (; i < 31; i++)
    {
        uint8_t j = i - anchor;
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

