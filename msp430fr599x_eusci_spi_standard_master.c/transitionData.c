#include "transitionData.h"


/**
 * @brief free pointer operation
 * 
 */

void free_datagram(SPI_DATAGRAM * datagram)
{
    free(datagram);
    datagram = NULL;
}


/**
 * Setting m2s_buf
 * buf_data: *pointer format, str[]: array format
 */
void buf_m2s(uint8_t *buf_data, uint8_t arrLen)
{
    uint8_t start_point = 0;
    for (; start_point < arrLen; start_point++)
    {
        g_transBuffer[start_point] = buf_data[start_point];
    }
}

/**
 * Transferring data from msp430 to nordic
 * s_transData: pointer "s_transData" points malloced data bytes
 * m_transData:  trans data format, both nordic and msp430 follow this rule.
 */
void data_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData)
{
    s_transData[0]  = 0x41;
    s_transData[1]  = 0x42;
    s_transData[2]  = 0x43;
    s_transData[3]  = (uint8_t)m_transData->hp_len;
    s_transData[4]  = (uint8_t)m_transData->t_broad_type;
    s_transData[5]  = (uint8_t)m_transData->seq;
    s_transData[6]  = (uint8_t)m_transData->status;
    s_transData[7]  = (uint8_t)m_transData->src;
    s_transData[8]  = (uint8_t)m_transData->dst;
    s_transData[9]  = (uint8_t)m_transData->layer;
    s_transData[10] = (uint8_t)m_transData->p_len;

    uint8_t       i           = 11;
    const uint8_t anchor      = 11;
    const uint8_t loopEnding  = (uint8_t)(SPI_DATA_LEN - 3);
    for (; i < loopEnding; i++)
    {
        uint8_t j = i - anchor;
        s_transData[i] = (uint8_t)m_transData->df[j];
    }

    s_transData[36] = 0x58;
    s_transData[37] = 0x59;
    s_transData[38] = 0x5A;

    free_datagram(m_transData);
}

/**
 * Transferring status data from msp430 to nordic
 * s_transData: pointer "s_transData" points malloced data bytes
 * m_transData:  trans data format, both nordic and msp430 follow this rule.
 */
void status_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData)
{
    s_transData[0]  = 0xAA;
    s_transData[1]  = 0xBB;
    s_transData[2]  = 0xCC;
    s_transData[11] = 0xDD;
    s_transData[12] = 0xEE;
    s_transData[13] = 0xFF;

    s_transData[3]  = m_transData->hp_len;
    s_transData[4]  = m_transData->t_broad_type;
    s_transData[5]  = m_transData->seq;
    s_transData[6]  = m_transData->status;
    s_transData[7]  = m_transData->src;
    s_transData[8]  = m_transData->dst;
    s_transData[9]  = m_transData->layer;
    s_transData[10] = m_transData->p_len;

    free_datagram(m_transData);
    m_transData = NULL;
}

/**
 * Transferring ack data from msp430 to nordic
 * s_transData: pointer "s_transData" points malloced data bytes
 * m_transData:  trans data format, both nordic and msp430 follow this rule.
 */
/*
void status_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData)
{
    s_transData[0]  = 0xAA;
    s_transData[1]  = 0xBB;
    s_transData[2]  = 0xCC;
    s_transData[11] = 0xDD;
    s_transData[12] = 0xEE;
    s_transData[13] = 0xFF;

    s_transData[3]  = m_transData->hp_len;
    s_transData[4]  = m_transData->t_broad_type;
    s_transData[5]  = m_transData->seq;
    s_transData[6]  = m_transData->status;
    s_transData[7]  = m_transData->src;
    s_transData[8]  = m_transData->dst;
    s_transData[9]  = m_transData->layer;
    s_transData[10] = m_transData->p_len;

    free_datagram(m_transData);
}

*/

/**
 * Receiving payload data from nordic.
 * m_receicedData is the data from nordic by spi.
 * And return the received payload data
 */
/*
uint8_t * payload_s2m(uint8_t * m_receicedData, bool isStatus)
{
    uint8_t re_dataLen;
    if (isStatus)
    {
        re_dataLen = HEADER_LEN;
    } else {
        re_dataLen = PAYLOAD_LEN;
    }
    uint8_t*  re_payload = (uint8_t *) malloc (sizeof(uint8_t) * re_dataLen);
    if (! re_payload)
    {
        return NULL;
    }

    uint8_t i = 0;
    for (; i < re_dataLen; i++)
    {
        re_payload[i] = m_receicedData[3 + i];
    }
    return re_payload;
}
*/

/**
 * Receiving status data from nordic.
 * m_receicedData is the data from nordic by spi.
 * m_returnData is the info extract from m_receicedData.
 */
/*
STATUS_INFO status_s2m(uint8_t * m_receicedData)
{
    STATUS_INFO m_returnData = {0};
    m_returnData.layer_with_type = m_receicedData[5];
    m_returnData.seq             = m_receicedData[6];
    m_returnData.spi_status      = m_receicedData[1];

    return m_returnData;
}
*/

