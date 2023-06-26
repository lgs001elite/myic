#include "transitionData.h"

uint16_t getCRC(unsigned char const message[])
{
    crcInit();
    uint16_t crc_result = crcFast(message, 31);
    return crc_result;  
}


void buf_m2s(uint8_t *buf_data, uint8_t arrLen)
{
    uint8_t start_point = 0;
    for (; start_point < arrLen; start_point++)
    {
        g_transBuffer[start_point] = buf_data[start_point];
    }
}


void s2m(SPI_DATAGRAM *m_transData, uint8_t s_transData[])
{
    m_transData->hp_len = s_transData[0];
    m_transData->t_broad_type = s_transData[1];
    m_transData->seq = s_transData[2];
    m_transData->status = s_transData[3];
    m_transData->src = s_transData[4];
    m_transData->dst = s_transData[5];
    m_transData->layer = s_transData[6];
    m_transData->round = s_transData[8];

    uint8_t i = 9;
    const uint8_t anchor      = 9;
    for (; i < 32; i++)
    {
        uint8_t j      = i - anchor;
        m_transData->df[j] = s_transData[i];
    }
    free_pointer(m_transData);
}


void m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData)
{
    s_transData[0]  = m_transData->hp_len;
    s_transData[1]  = m_transData->t_broad_type;
    s_transData[2]  = m_transData->seq;
    s_transData[3]  = m_transData->status;
    s_transData[4]  = m_transData->round;
    s_transData[5]  = m_transData->src;
    s_transData[6]  = m_transData->dst;
    s_transData[7]  = m_transData->layer;

    uint8_t i = 8;
    const uint8_t anchor = 8;
    for (; i < 31; i++)
    {
        uint8_t j = i - anchor;
        s_transData[i] = (uint8_t)m_transData->df[j];
    }
    uint8_t crc_input[31];
    i = 0;
    for (; i < 31; i++)
    {
        crc_input[i] = s_transData[i];
    }

    uint16_t crc_result = getCRC(crc_input);
    s_transData[31] = (crc_result & 0xFF00) >> 8;
    s_transData[32] = (crc_result & 0x00FF);

    while (s_transData[31] >= 0x7F)
    {
        s_transData[31] -= 0x7F;
    }

    while (s_transData[32] >= 0x7F)
    {
        s_transData[32] -= 0x7F;
    }
}
