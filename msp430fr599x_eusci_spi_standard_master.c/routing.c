#include "routing.h"
#include "routingRx.h"
#include "routingTx.h"
#include "public.h"
#include "filedata.h"
#include "random.h"



void start_routing(void)
{
    /**
     * keep spi active status for normal communication
     */
    if (g_if_sourceNode)
    {
        /**
         * First, Initialize relevant seq numbers
         */
        g_seq_header = (uint8_t)genRanNumb();
        g_seq_data   = (uint8_t)genRanNumb();
        spi_transData();

        /**
         * Source node begins to transmite
         */
        start_spi_process();
    } else {
        /** Initialization, fill in transbuf, for spi transition */
        g_transBuffer[0] = 0x04;
        g_transBuffer[1] = 0x03;
        g_transBuffer[2] = 0x00;
        g_spiTransLen    = 3;

        start_spi_process();
    }
}


