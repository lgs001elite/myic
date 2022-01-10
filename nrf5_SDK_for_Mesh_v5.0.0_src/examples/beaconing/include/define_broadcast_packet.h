
#ifndef _DEFINE_BROADCAST_PACKET_H_
#define _DEFINE_BROADCAST_PACKET_H_
#include <stdio.h>
#include <stdint.h>
/**
 * Define the adv_broadcast_packet format
 * 
 *** Byte0: len 0
 *** Byte1: type 1
 *** Byte2: src 2
 *** Byte3: dst 3
 *** Byte4: hop: 6 bits, ack: 2 bit 4
 *** Byte5: seq 5
 *** Byte6~30: payload 6
 */

//uint8_t define_adv_packet[31] = {0}; /* 31: Max length of adv payload, [BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH    (31)] */

typedef struct adv_packet_t
{
    uint8_t hp_len;
    uint8_t t_broad_type;
    uint8_t seq;                      
    uint8_t status;                
    uint8_t src              : 4,
            dst              : 4;
    uint8_t layer            : 3,
            p_len            : 5;     
    uint8_t df[23];
    uint8_t crc[2];
} define_adv_packet;

#endif
