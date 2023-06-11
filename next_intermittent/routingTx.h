#ifndef _ROUTINGTX_H_
#define _ROUTINGTX_H_

#include <stdint.h>

void spi_transData(void);
void spi_transHeaderStatus(uint8_t statusValue);

#endif
