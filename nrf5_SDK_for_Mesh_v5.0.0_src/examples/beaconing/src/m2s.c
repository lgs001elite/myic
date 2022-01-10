#include "m2s.h"
#include "advertiser.h"

static define_adv_packet  * reBuf                 = NULL;

void receiveData_sendout(uint8_t * s_data)
{
    define_adv_packet * receivedBuf = (define_adv_packet *) malloc(sizeof(define_adv_packet));
    if (!receivedBuf)
    {
        return;
    }
    memset(receivedBuf, 0, sizeof(define_adv_packet));
    receivedBuf->hp_len           = s_data[1];
    receivedBuf->t_broad_type     = s_data[2]; 
    receivedBuf->seq              = s_data[3];
    receivedBuf->status           = s_data[4];
    receivedBuf->src              = s_data[5];
    receivedBuf->dst              = s_data[6];
    receivedBuf->layer            = s_data[7];
    receivedBuf->p_len            = s_data[8];
 
    for (uint8_t i = 0; i < 23; i++)
    {
        receivedBuf->df[i] = s_data[9 + i];
    }

    receivedBuf->crc[0]           = s_data[32];
    receivedBuf->crc[1]           = s_data[33];

    reBuf = receivedBuf;
}

define_adv_packet * getData_sendout()
{
    return reBuf;
}
