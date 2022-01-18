#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "routingTx.h"
#include "spi_packet.h"
#include "filedata.h"
#include "public.h"
#include "random.h"
#include "transitionData.h"
#include "source_DB.h"
#include "dst_DB.h"

volatile   uint32_t       g_transDataSeq           = 0;
const      uint32_t       g_file_len               = 978; //978;

/**
 * @brief free pointer
 * 
 */
void free_pointer(uint8_t * pointer)
{
    free(pointer);
    pointer = NULL;
}

//#pragma CODE_SECTION(spi_transData,".run_from_ram")
void spi_transData(void)
{
    uint8_t         spi_status  = 0x08;
    SPI_DATAGRAM  * s_transdata = (SPI_DATAGRAM *) malloc (sizeof(SPI_DATAGRAM));
    if (! s_transdata)
    {
        return;
    }
    memset(s_transdata, 0, sizeof(SPI_DATAGRAM));
    
    g_seq_data = (g_seq_data + 1) % MAXUINT8;
    
    s_transdata->hp_len         = 0x1E;
    s_transdata->t_broad_type   = BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS;
    s_transdata->src            = g_nodeAddress;
    s_transdata->dst            = g_dest_address;
    s_transdata->layer          = g_node_dimension;
    s_transdata->status         = spi_status; /* The packet type is adv */
    s_transdata->seq            = g_seq_data;

    uint8_t     packet_i        = 0;  /* 0: the starting point of payload */
    for (; (g_transDataSeq < g_file_len) && (g_if_send_next) && (!g_if_end_trans);)
    {
        (s_transdata->df)[packet_i] = file_data[g_transDataSeq];

        packet_i++;
        g_transDataSeq++;
        if (packet_i == 0x17) /* 0x17: the length of data frame */
        {
            s_transdata->p_len = packet_i; /* Adv actual payload len */
            packet_i = 0;
            g_if_send_next = false;
        }

        if (g_transDataSeq == g_file_len)
        {
            s_transdata->p_len = packet_i; /* Adv actual payload len */
            g_if_end_trans = true;
            g_transDataSeq = 0;
        }
    }

    uint8_t * transmitBuffer = (uint8_t *) malloc (sizeof(uint8_t) * SPI_DATA_LEN);
    if(!transmitBuffer)
    {
        return;
    }
    memset(transmitBuffer, 0, SPI_DATA_LEN);
    data_m2s(transmitBuffer, s_transdata);
    buf_m2s(transmitBuffer, (uint8_t)SPI_DATA_LEN);
    g_spiTransLen = SPI_DATA_LEN; /** For final spi transmition */
    
    free_pointer(transmitBuffer);
}

//#pragma CODE_SECTION(spi_transHeaderStatus,".run_from_ram")
void spi_transHeaderStatus(uint8_t statusValue)
{
    SPI_DATAGRAM  * s_header = (SPI_DATAGRAM *) malloc (sizeof(SPI_DATAGRAM));
    if (! s_header)
    {
        return;
    }
    memset(s_header, 0, sizeof(SPI_DATAGRAM));

    g_seq_header = (g_seq_header + 1) % MAXUINT8;
    s_header->hp_len       = 0x1E;
    s_header->t_broad_type = BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS;
    s_header->src          = g_nodeAddress;
    s_header->dst          = g_receivedNodeAddress;
    s_header->layer        = g_node_dimension;
    s_header->seq          = g_seq_header;
    s_header->status       = statusValue;
    s_header->p_len        = 0;

    uint8_t * transmitBuffer = (uint8_t *) malloc (sizeof(uint8_t) * SPI_DATA_LEN);
    if(!transmitBuffer)
    {
        return;
    }
    memset(transmitBuffer, 0, SPI_DATA_LEN);

    status_m2s(transmitBuffer, s_header);
    buf_m2s(transmitBuffer, (uint8_t)SPI_DATA_LEN);
    g_spiTransLen  = SPI_DATA_LEN;

    free_pointer(transmitBuffer);
}
