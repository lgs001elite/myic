#include "m2s.h"
#include "advertiser.h"


void receiveData_sendout(uint8_t * s_data)
{
    for(uint8_t i = 1; i < 4; i++)
    {
        m_recBuf[i - 1] = s_data[i];
    }
    m_recBuf[3] = (s_data[4] | ((s_data[5]<<4)  & 0XF0));
    m_recBuf[4] = (s_data[6] | ((s_data[7]<<4)  & 0XF0));

    for(uint8_t i = 8; i < 34; i++)
    {
        m_recBuf[i - 3] = s_data[i];
    }
}
