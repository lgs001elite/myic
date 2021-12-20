#ifndef _TRANSITIONDATA_H_
#define _TRANSITIONDATA_H_
#include <stdint.h>
#include <stdbool.h>
#include "public.h"
#include "spi_packet.h"

void      data_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData);
//uint8_t * payload_s2m(uint8_t * m_receicedData, bool isStatus);
void      buf_m2s(uint8_t *buf_data, uint8_t arrLen);
void      status_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData);
//void      status_m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData);
#endif
