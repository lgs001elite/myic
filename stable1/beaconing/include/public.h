#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdio.h>
#include <stdbool.h>

#define BROADCASTLEN    31

#define DUBBY 0x03

void send_datagram_start();
void initialize();
extern char m_tx_buf_spi[BROADCASTLEN];
extern uint8_t m_recBuf[BROADCASTLEN];
extern uint8_t m_rx_buf_spi[BROADCASTLEN + 1];
extern bool spis_xfer_done;

#endif
