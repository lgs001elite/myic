#include <stdbool.h>
#include <string.h>
#include "routingRx.h"
#include "routingTx.h"
#include "spi_packet.h"
#include "public.h"
#include "filedata.h"
#include "hash.h"
#include "transitionData.h"
#include "dst_DB.h"

static   uint32_t     g_received_file_real_size                    = 0;
volatile uint8_t      g_pairedNodeAddress                          = 0xff;
volatile bool         g_if_paired                                  = false;
static   uint8_t      g_sha256_buf[SHA256_BLOCK_SIZE]              = {0};
static   uint8_t      g_pre_ack_seq                                = 0xff;
static   bool         g_if_nonFirstAck                             = false;
static   uint8_t      g_pre_packet_seq                             = 0xff;
static   bool         g_non_firstDatagram                          = false;

static void terminateRoutine()
{
    spi_transHeaderStatus(0x42); /**  terminate advertisers**/
}

void reInitialize()
{
    terminateRoutine();
    g_pairedNodeAddress       = 0xff;  // reinitializing for the next round transmition
    g_if_paired               = false; // re-choose the next paring object
    g_transDataSeq            = 0;
    g_if_end_trans            = 0;
    g_received_file_real_size = 0;
    g_pre_packet_seq          = 0xff;
    g_non_firstDatagram       = false;
}

/** for checking the entire file  **/
uint8_t * file_sha256(uint8_t * file, uint32_t file_size)
{
    SHA256_CTX   ctx;
    sha256_init(&ctx);
    sha256_update(&ctx, file, file_size);
    sha256_final(&ctx, g_sha256_buf);
    return &g_sha256_buf[0];
}

/**
 * @brief  SPIS check completeness of data

 */
bool check_completeness(uint8_t * receivedData)
{
    uint8_t rec_result[31];
    uint8_t i = 0;
    for (; i < 31; i++)
    {
        rec_result[i] = receivedData[i];
    }

    crcInit();
    uint16_t crc_result = crcFast(rec_result, 31);
    uint8_t res1        = (crc_result & 0xFF00)>>8;
    uint8_t res2        = (crc_result & 0x00FF);

    while (res1 > 0x7F)
    {
        res1 -= 0x7F;
    }

    while (res2 > 0x7F)
    {
        res2 -= 0x7F;
    }

    if (res1 != receivedData[31])
    {
        return false;
    }

    if (res2 != receivedData[32])
    {
        return false;
    }

    return true;
}

static void data_is_datagram(uint8_t receivedData[])
{
    // For datapackets, need to judge the relative layers between nodes
    uint8_t RxlayerSendNode = receivedData[6];
    if (RxlayerSendNode <= g_node_dimension)
    {
        return;
    }
    /**
     * g_pre_packet_seq: for excising repeated frame, g_non_firstDatagram: for judge if starting
     */
    if ((g_pre_packet_seq == receivedData[2]) && g_non_firstDatagram)
    {
          return;
    }
    g_pre_packet_seq = receivedData[2];
    g_non_firstDatagram = true;

    uint8_t tempi = 0;
    uint8_t reveived_payload_size = receivedData[7]; /* 7: The payload size position */
    while(tempi != reveived_payload_size)
    {
        store_received_data[g_received_file_real_size] = receivedData[tempi + 8]; /* 8: The starting position of payload */
        g_received_file_real_size++;
        tempi++;
    }
    
    /** After receiving a datagram, then send out an ack **/
    spi_transHeaderStatus(0x10);
}

static void data_is_fin()
{
    uint8_t * gen_sha256 = file_sha256(store_received_data, g_received_file_real_size);
    bool      g_com_pass = true;
    g_com_pass           = (memcmp(file_sha256_true, gen_sha256, SHA256_BLOCK_SIZE) == 0);
    if (g_com_pass)
    {
        //blink the led lights (and / or) transmition to next hop
        recevedSucess();
    } else {
        recevedFailure();
    }
    spi_transHeaderStatus(0x41); // Sending fin by the dst node.
    g_if_Rxternimate = true;
}

static void data_is_reverseFin()
{
    reInitialize();
    g_if_Txternimate = true;
    recevedSucess();
}

static void data_is_find(uint8_t receivedData[])
{
    /**
     * will to do
     */
}

static void data_is_ack(uint8_t *receivedData)
{
    uint8_t recever_packet_seq = receivedData[2];
    if ((recever_packet_seq == g_pre_ack_seq) && g_if_nonFirstAck)
    {
        return;
    }

    g_pre_ack_seq     = receivedData[2]; // update the pre-seu number
    g_if_nonFirstAck  = true;
    if (g_if_end_trans)
    {
        /** Sending fin by the  source node **/
         spi_transHeaderStatus(0x40);
         return;
    } else {
        /** Sending next data **/
         g_if_send_next = true;
         spi_transData();
    }
}


void receiveDataFromNordic()
{
    bool checkResult = check_completeness(ReceiveBuffer);
    if (! checkResult)
    {
         return;
    }

    /**
     * DST node checking
     */
    uint8_t dstFromSendNode = ReceiveBuffer[5];
    if (dstFromSendNode != g_nodeAddress)
    {
        return;
    }

    /**
     * Recording the paired node
     */
    uint8_t dataType = ReceiveBuffer[3];
    uint8_t srcFromSendNode = ReceiveBuffer[4];
    if ((dataType == 0x04) && (!g_if_paired))
    {
        g_pairedNodeAddress = srcFromSendNode;
        g_if_paired = true;
    }

    /**
     * Excluding ineligible packets
     */

    if (g_pairedNodeAddress != 0xff) // paired
    {
        if (g_pairedNodeAddress != srcFromSendNode)
        {
            return;
        }
    } else {  // non-paired
        if ((dataType != 0x04) && (dataType != 0x08)) // status packets
        {
            if (g_dest_address != srcFromSendNode)
            {
                return;
            }
            g_if_paired         = true;
            g_pairedNodeAddress = srcFromSendNode;
        } else {   // discard non-status packets
            return;
        }
    }

    switch(dataType)
    {
     case 0x00:
         data_is_find(ReceiveBuffer);
         break;
     case 0x04:
         data_is_datagram(ReceiveBuffer);
         break;
     case 0x08:
         data_is_datagram(ReceiveBuffer);
         break;
     case 0x40:
         data_is_fin();
         break;
     case 0x41:
         data_is_reverseFin();
         break;
     case 0x10:
         data_is_ack(ReceiveBuffer);
         break;
     default:
         break;
    }
}
