#ifndef _TRANSITIONDATA_H_
#define _TRANSITIONDATA_H_
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "public.h"
#include "crc.h"

void    s2m(SPI_DATAGRAM *m_transData, uint8_t s_transData[]);
void    buf_m2s(uint8_t *buf_data, uint8_t arrLen);
void    m2s(uint8_t * s_transData, SPI_DATAGRAM * m_transData);

#endif
