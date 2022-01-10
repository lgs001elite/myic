#ifndef _SPIS_H_
#define _SPIS_H_
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "sdk_config.h" /* For external interface */
#include "nrfx_spis.h"
#include "nrf_drv_spis.h"
#include "nrf_gpio.h"
#include "nrf_delay.h"
#include "boards.h"
#include "app_error.h"
#include "log.h"
#include "spis_data.h"
#include "define_broadcast_packet.h"
#include "public.h"
#include "m2s.h"
#include "s2m.h"
#include "crc.h"

void spis_start(void);

#endif
