#include "transitionData.h"



/**
 * @brief calculate crc value
 * 
 */

static uint16_t getCRC(unsigned char const message[])
{
    crcInit();
    uint16_t crc_result = crcFast(message, 31);
    return crc_result;
}

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
    s_transData[0]  = (uint8_t)m_transData->hp_len;
    s_transData[1]  = (uint8_t)m_transData->t_broad_type;
    s_transData[2]  = (uint8_t)m_transData->seq;
    s_transData[3]  = (uint8_t)m_transData->status;
    s_transData[4]  = (uint8_t)m_transData->src;
    s_transData[5]  = (uint8_t)m_transData->dst;
    s_transData[6]  = (uint8_t)m_transData->layer;
    s_transData[7]  = (uint8_t)m_transData->p_len;

    uint8_t       i           = 8;
    const uint8_t anchor      = 8;
    for (; i < 31; i++)
    {
        uint8_t j      = i - anchor;
        s_transData[i] = (uint8_t)m_transData->df[j];
    }
    uint8_t crc_input[31];
    i = 0;
    for(; i < 31; i++)
    {
        crc_input[i] = s_transData[i];
    }

    uint16_t crc_result = getCRC(crc_input);
    s_transData[31]     =   (crc_result & 0xFF00)>>8;
    s_transData[32]     =   (crc_result & 0x00FF);

    while (s_transData[31] > 0x7F)
    {
        s_transData[31] -= 0x7F;
    }

    while (s_transData[32] > 0x7F)
    {
        s_transData[32] -= 0x7F;
    }
         
    free_datagram(m_transData);
}

/**
 * Transferring status data from msp430 to nordic
 * s_transData: pointer "s_transData" points malloced data bytes
 * m_transData:  trans data format, both nordic and msp430 follow this rule.
 */
void status_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData)
{
    s_transData[0]  = m_transData->hp_len;
    s_transData[1]  = m_transData->t_broad_type;
    s_transData[2]  = m_transData->seq;
    s_transData[3]  = m_transData->status;
    s_transData[4]  = m_transData->src;
    s_transData[5]  = m_transData->dst;
    s_transData[6]  = m_transData->layer;
    s_transData[7]  = m_transData->p_len;

    uint8_t crc_input[31] = {0};
    uint8_t i = 0;
    for(; i < 8; i++)
    {
        crc_input[i] = s_transData[i];
    }

    for (; i < 31; i++)
    {
        crc_input[i]   = 0;
        s_transData[i] = 0;
    }

    uint16_t crc_result = getCRC(crc_input);
    s_transData[31]     = (crc_result & 0xFF00)>>8;
    s_transData[32]     = (crc_result & 0x00FF);

    while (s_transData[31] > 0x7F)
    {
        s_transData[31] -= 0x7F;
    }

    while (s_transData[32] > 0x7F)
    {
        s_transData[32] -= 0x7F;
    }

    free_datagram(m_transData);
}
