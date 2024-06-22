#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdio.h>
#include <stdbool.h>


uint8_t m_tx_buf_spi[31];
uint8_t m_rx_buf_spi[31];
extern bool spis_xfer_done;
extern bool listenSwitch;
extern bool sendSwitch;
extern uint8_t listeningTimeout;

#endif
