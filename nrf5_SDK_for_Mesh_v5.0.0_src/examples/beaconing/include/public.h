#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdio.h>
#include <stdbool.h>
#include "spis_data.h"

#define BROADCASRLEN 40 // 39 + 1, one starting point-
#define STATUSLEN    12

void send_ack_start();
void send_fin_start();
void send_datagram_start();

extern volatile bool g_null_status;
extern volatile bool g_isData;
//static rec_data      m_rx_data                                        = {0};
//bool get_if_send_ack();
//bool get_if_send_data();
//bool get_if_send_fin();
//void set_if_send_ack(bool ackStatus);
//void set_if_send_data(bool sendNext);
//void set_if_send_fin(bool finishTrans);


#endif
