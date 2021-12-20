#include "m2s.h"
#include "advertiser.h"

define_adv_packet  * reBuf                        = NULL;
static uint8_t       g_receivedAckSeq             = 0xff;
static bool          g_if_SendNexRoundAckStatus  = false;

void receiveHeader_sendout(uint8_t * s_data)
{
    define_adv_packet * receivedBuf = (define_adv_packet *) malloc(sizeof(define_adv_packet));
    if (!receivedBuf)
    {
        return;
    }
    memset(receivedBuf, 0, sizeof(define_adv_packet));
    receivedBuf->hp_len           = s_data[4];
    receivedBuf->t_broad_type     = s_data[5]; 
    receivedBuf->seq              = s_data[6];
    receivedBuf->status           = s_data[7];
    receivedBuf->src              = s_data[8];
    receivedBuf->dst              = s_data[9];
    receivedBuf->layer            = s_data[10];
    receivedBuf->p_len            = s_data[11];

    reBuf = receivedBuf;
}

void receiveData_sendout(uint8_t * s_data)
{
    /**  **/
    set_if_terCurrentAdvertiser(true);
    define_adv_packet * receivedBuf = (define_adv_packet *) malloc(sizeof(define_adv_packet));
    if (!receivedBuf)
    {
        return;
    }
    memset(receivedBuf, 0, sizeof(define_adv_packet));
    receivedBuf->hp_len           = s_data[4];
    receivedBuf->t_broad_type     = s_data[5]; 
    receivedBuf->seq              = s_data[6];
    receivedBuf->status           = s_data[7];
    receivedBuf->src              = s_data[8];
    receivedBuf->dst              = s_data[9];
    receivedBuf->layer            = s_data[10];
    receivedBuf->p_len            = s_data[11];
 
    uint8_t payloadLen = s_data[11];
    for (uint8_t i = 0; i < payloadLen; i++)
    {
        receivedBuf->df[i] = s_data[i + 12];
    }

    reBuf = receivedBuf;
}

define_adv_packet * getData_sendout()
{
    return reBuf;
}

/*
void receiveStatusAction(uint8_t * ackStatus)
{
    uint8_t rAckStatus = ackStatus[4];
    uint8_t seqNum     = ackStatus[5];
    if ((seqNum == g_receivedAckSeq) && g_if_SendNexRoundAckStatus)
    {
        return;
    }
    g_receivedAckSeq           = seqNum;
    g_if_SendNexRoundAckStatus = true;
    switch (rAckStatus)
    {
        case 0x02:
            set_if_send_ack(true);
            break;
        
        case 0x03:
            set_if_send_fin(true);
            break;

        case 0x04:
            set_if_send_data(true);
        default:
            break;
    }
    
}
*/

/*
void selectDadaType(uint8_t * s_data)
{
    uint8_t dataType   =  s_data[9];
    switch (dataType)
    {
        case 0x00:
        case 0x01:
            receiveData_sendout(s_data);
            send_datagram_start();
        case 0x02:
            receiveHeader_sendout(s_data);
            send_fin_start();
        case 0x03:
            receiveHeader_sendout(s_data);
            send_ack_start();
        default:
            break;
    }
}
*/
