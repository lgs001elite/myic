#include "m2s.h"
#include "advertiser.h"

void receiveData_sendout(uint8_t * s_data)
{
    for(uint8_t i = 0; i < 31; i++)
    {
        m_recBuf[i] = s_data[i + 1];
    }
}
