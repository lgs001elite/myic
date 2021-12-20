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

static   uint32_t       g_transDataSeq           = 0;

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
    
    /**
     * @brief Setting the first datagram's status
     * 
     */
    if (g_transDataSeq == 0)
    {
        spi_status = 0x04;
    }

    s_transdata->hp_len         = 0x1E;
    s_transdata->t_broad_type   = BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS;
    s_transdata->src            = NODE_ADDRESS;
    s_transdata->dst            = g_dest_address;
    s_transdata->layer          = g_node_dimension;
    s_transdata->status         = spi_status; /* The packet type is adv */
    s_transdata->seq            = g_seq_data;

    uint8_t     packet_i        = 0;  /* 0: the starting point of payload */
    for (; (g_transDataSeq < g_file_len) && (g_if_send_next) && (!g_if_end_trans);)
    {
        if (g_if_transDataFromRec)
        {
            (s_transdata->df)[packet_i] = store_received_data[g_transDataSeq];
        } else {
            (s_transdata->df)[packet_i] = file_data[g_transDataSeq];
        }

        packet_i++;
        g_transDataSeq++;
        s_transdata->p_len = packet_i; /* Adv payload len */
        if (packet_i == 0x19) /* 0x19: the length of data frame */
        {
            packet_i = 0;
            g_if_send_next = false;
        }

        if (g_transDataSeq == g_file_len)
        {
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
    transmitBuffer = NULL;
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
    s_header->hp_len       = 0x05;
    s_header->t_broad_type = BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS;
    s_header->src          = NODE_ADDRESS;
    s_header->dst          = g_pairedNodeAddress;
    s_header->layer        = g_node_dimension;
    s_header->seq          = g_seq_header;
    s_header->status       = statusValue;
    s_header->p_len        = 0;

    uint8_t * transmitBuffer = (uint8_t *) malloc (sizeof(uint8_t) * SPI_HEADER_LEN);
    if(!transmitBuffer)
    {
        return;
    }
    memset(transmitBuffer, 0, SPI_HEADER_LEN);

    status_m2s(transmitBuffer, s_header);
    buf_m2s(transmitBuffer, (uint8_t)SPI_HEADER_LEN);
    g_spiTransLen  = SPI_HEADER_LEN;

    free_pointer(transmitBuffer);
    transmitBuffer = NULL;
}

/*
//#pragma CODE_SECTION(spi_transHeaderFin,".run_from_ram")
void spi_transHeaderFin(uint8_t trans_status)
{
    g_if_end_trans = false;

    SPI_DATAGRAM  * s_end = (SPI_DATAGRAM *) malloc (sizeof(SPI_DATAGRAM));
    if (! s_end)
    {
        return;
    }

    g_seq_fin = (g_seq_fin + 1) % MAXUINT8;

    s_end->hp_len       = 0x06;
    s_end->spi_status   = 0x00;
    s_end->t_broad_type = BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS;
    s_end->src          = NODE_ADDRESS;
    s_end->dst          = g_dest_address;
    s_end->layer        = g_node_dimension;
    s_end->seq          = g_seq_fin;
    s_end->type         = trans_status;

    uint8_t * transmitBuffer = (uint8_t *) malloc (sizeof(uint8_t) * SPI_HEADER_LEN);
    if(!transmitBuffer)
    {
        return;
    }
    status_m2s(transmitBuffer, s_end);
    buf_m2s(transmitBuffer, (uint8_t)SPI_HEADER_LEN);
    g_spiTransLen = SPI_HEADER_LEN;

    free_pointer(transmitBuffer);
}

//#pragma CODE_SECTION(spi_transHeaderAck,".run_from_ram")
void spi_transHeaderStatus()
{
    SPI_DATAGRAM  * s_header = (SPI_DATAGRAM *) malloc (sizeof(SPI_DATAGRAM));
    if (! s_header)
    {
        return;
    }

    g_seq_ack = (g_seq_ack + 1) % MAXUINT8;

    s_header->hp_len       = 0x05;
    s_header->t_broad_type = BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS;
    s_header->src          = NODE_ADDRESS;
    s_header->dst          = g_pairedNodeAddress;
    s_header->layer        = g_node_dimension;
    s_header->seq          = g_seq_ack;
    s_header->status       = 0x10;
    s_header->p_len        = 0;

    uint8_t * transmitBuffer = (uint8_t *) malloc (sizeof(uint8_t) * SPI_HEADER_LEN);
    if(!transmitBuffer)
    {
        return;
    }
    status_m2s(transmitBuffer, s_header);
    buf_m2s(transmitBuffer, (uint8_t)SPI_HEADER_LEN);
    g_spiTransLen  = SPI_HEADER_LEN;

    free_pointer(transmitBuffer);
    transmitBuffer = NULL;
}
*/
