#ifndef _TRANSITIONDATA_H_
#define _TRANSITIONDATA_H_
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "public.h"
#include "spi_packet.h"
#include "crc.h"

void    data_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData);
void    buf_m2s(uint8_t *buf_data, uint8_t arrLen);
void    status_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData);

#endif
