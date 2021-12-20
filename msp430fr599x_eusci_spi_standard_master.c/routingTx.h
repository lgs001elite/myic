#ifndef _ROUTINGTX_H_
#define _ROUTINGTX_H_

#include <stdint.h>
void spi_transData(void);
//void spi_transHeaderFin(uint8_t trans_status);
//void spi_transHeaderStatus();
void spi_transHeaderStatus(uint8_t statusValue);


#endif
