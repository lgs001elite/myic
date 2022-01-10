#ifndef _M2S_H_
#define _M2S_H_
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "define_broadcast_packet.h"
#include "public.h"

void receiveData_sendout(uint8_t * s_data);

define_adv_packet * getData_sendout();

#endif
