#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdio.h>
#include <stdbool.h>
#include "spis_data.h"

#define S_BROADCASRLEN 33 // 33

void send_datagram_start();
extern volatile uint8_t  m_tx_buf_spi[S_BROADCASRLEN];
extern volatile uint8_t  m_recBuf[31];
#endif
