#include <string.h>
#include <stdlib.h>
#include "spis_data.h"
#include "public.h"
#include "log.h"

sen_data m_tx_data  = {0};

void spis_setfrom_slave(uint8_t * tx_data_buf, uint32_t  tx_data_len)
{
    m_tx_data.tx_data_buf = tx_data_buf;
    m_tx_data.tx_data_len = tx_data_len;
}

sen_data spis_getfrom_slave()
{
    sen_data tx_data;
    tx_data.tx_data_buf = m_tx_data.tx_data_buf;
    tx_data.tx_data_len = m_tx_data.tx_data_len;
    return tx_data;
}
