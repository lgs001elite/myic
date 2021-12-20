#ifndef _M2S_H_
#define _M2S_H_
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "define_broadcast_packet.h"
#include "public.h"

extern define_adv_packet *reBuf;

void receiveData_sendout(uint8_t * s_data);
void receiveHeader_sendout(uint8_t * s_data);
//void selectDadaType(uint8_t * s_data);
//void receiveStatusAction(uint8_t * ackStatus);

define_adv_packet * getData_sendout();


#endif
