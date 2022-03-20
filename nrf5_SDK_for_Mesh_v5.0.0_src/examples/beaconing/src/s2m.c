#include <stdlib.h>
#include "s2m.h"
#include "spis_data.h"
#include "public.h"
#include "log.h"

void set_transData(void)
{
   /**
     * @brief Setting transition data
     */
    sen_data tx_data = spis_getfrom_slave();

    for (uint32_t i = 0; i < S_BROADCASRLEN; i++)
    {
        m_tx_buf_spi[i] = tx_data.tx_data_buf[i];
        //__LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- m_tx_buf_spi[%d]: %X  -----\n", i, m_tx_buf_spi[i]);
    }

    /**
     * @brief when free it can free in spi loop chunk, when transite data
     * (define in main function), should free here. 
     */
    free(tx_data.tx_data_buf);
    tx_data.tx_data_buf = NULL;   
}
