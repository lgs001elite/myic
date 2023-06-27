#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdio.h>
#include <stdbool.h>
#include "spis_data.h"

#define ACTUALDATAUNITS 33
#define BROADCASTLEN    32

#define DUBBY 0x05

void send_datagram_start();
extern  uint8_t  m_tx_buf_spi[ACTUALDATAUNITS];
extern  uint8_t m_recBuf[BROADCASTLEN];

#endif
