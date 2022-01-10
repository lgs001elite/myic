#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdio.h>
#include <stdbool.h>
#include "spis_data.h"

#define M_BROADCASRLEN 34 // one starting point: 33 + 1
#define S_BROADCASRLEN 33 // 33

void send_datagram_start();

extern volatile bool     g_ifPickNewValue;
extern volatile uint8_t  g_broadcast_counter;

#endif
