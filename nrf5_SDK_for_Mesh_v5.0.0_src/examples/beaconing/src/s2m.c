#include <stdlib.h>
#include "s2m.h"
#include "spis_data.h"
#include "public.h"
#include "log.h"

void set_transData(void)
{
   /**
     * @brief Setting transition data
     * 
     */
    sen_data tx_data = spis_getfrom_slave();
    m_tx_length = tx_data.tx_data_len;
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "m_tx_length: %d\n", m_tx_length);
    m_tx_buf_spi = (uint8_t *) malloc (sizeof(uint8_t) * m_tx_length);
    /*
    if (g_null_status)
    {
        m_tx_buf_spi = (uint8_t *) malloc (sizeof(uint8_t) * 4);
    } else{
        m_tx_buf_spi = (uint8_t *) malloc (sizeof(uint8_t) * m_tx_length);  
    }
    */
   
    if (!m_tx_buf_spi)
    {
        return;
    }
     


    for (uint32_t i = 0; i < m_tx_length; i++)
    {
        m_tx_buf_spi[i] = tx_data.tx_data_buf[i];
    }
    //__LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "m_tx_buf_spi: %d, size: %d, 5th: %d\n", m_tx_buf_spi[3], m_tx_buf_spi[2], m_tx_buf_spi[1]);
    //__LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "tx_data.tx_data_buf: %d, m_tx_length: %d\n", tx_data.tx_data_buf[0], m_tx_length);
    //__LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "free: %d\n", g_null_status);
    
    /**
     * @brief when free it can free in spi loop chunk, when transite data(define in main function), should free here. 
     * 
     */

    free(tx_data.tx_data_buf);
    tx_data.tx_data_buf = NULL;   
}
