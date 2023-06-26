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
    for (; i < (MAXQUELEN/2); i++)
    {
        g_packetQueue[g_queueLen].hp_len = 0x1E;
        g_packetQueue[g_queueLen].t_broad_type = BLE_GAP_AD_TYPE;
        g_packetQueue[g_queueLen].src = g_nodeAddress;
        g_packetQueue[g_queueLen].dst = g_nextNodeID;
        g_packetQueue[g_queueLen].layer = g_node_dimension;
        g_packetQueue[g_queueLen].status = PACKAGE_PACKET;
        g_packetQueue[g_queueLen].seq = (g_seq_data + 1) % MAXUINT8;
        g_packetQueue[g_queueLen].round = g_rounds;
        g_seq_data = g_seq_data + 1;
        uint8_t j = 0;
        for (; j < PACKET_DATA_LEN; j++)
        {
            (g_packetQueue[g_queueLen].df)[j] = file_data[g_transDataSeq];
            g_transDataSeq++;
        }
        if (g_transDataSeq == MAXBYTE)
        {
            g_transDataSeq = 0;
            if (g_rounds != 0)
            {
                g_seq_data = (uint8_t)genRanNumb();
            }
        }
        g_queueLen = g_queueLen + 1;
        // waiting to collect data
        __delay_cycles(100000);
    }
}

void produceNonPacketData(void)
{
    g_transBuffer[0] = 0x1E;
    g_transBuffer[1] = BLE_GAP_AD_TYPE;
    g_transBuffer[2] = g_waitToFind;
    g_transBuffer[3] = DUBBY;
    g_transBuffer[4] = g_nodeAddress;
    g_transBuffer[5] = g_nextNodeID;
    g_transBuffer[6] = g_node_dimension;
    g_transBuffer[7] = 0;
    g_transBuffer[8] = 0;
    uint8_t i = 9;
    const uint8_t anchor = 9;
    for (; i < 32; i++)
    {
        uint8_t j = i - anchor;
        g_transBuffer[i] = 0;
    }
    uint8_t crc_input[32];
    i = 0;
    for (; i < 32; i++)
    {
        crc_input[i] = g_transBuffer[i];
    }
    uint16_t crc_result = getCRC(crc_input);
    g_transBuffer[32] = (crc_result & 0xFF00) >> 8;
    g_transBuffer[33] = (crc_result & 0x00FF);
    while (g_transBuffer[32] >= 0x7F)
    {
        g_transBuffer[32] -= 0x7F;
    }
    while (g_transBuffer[33] >= 0x7F)
    {
        g_transBuffer[33] -= 0x7F;
    }
}

