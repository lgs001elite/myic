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
bool check_completeness(uint8_t * receicedData)
{
    uint8_t i = 0;
    for (; i < 3; i++)
    {
        if (receicedData[i] != front_check_arr[i])
        {
            return false;
        }
    }

    uint8_t dataStatus = receicedData[6];
    if ((dataStatus == 0x04) || (dataStatus == 0x08))
    {
        uint8_t j = 0;
       for (; j < 3; j++)
       {
            if (receicedData[j + 37] != rear_check_arr[j])
            {
                return false;
            }
        }
    } else if (dataStatus == 0x0C)
    {
        uint8_t p_len  = receicedData[11];
        uint8_t anchor = 12 + p_len;
        uint8_t j = 0;
        for (; j < 3; j++)
        {
            uint8_t offset = anchor + j;
            if (receicedData[offset] != rear_check_arr[j])
            {
                return false;
            }
        }
    } else {
        uint8_t j = 0;
        for (; j < 3; j++)
        {
            uint8_t offset = 12 + j;
            if (receicedData[offset] != rear_check_arr[j])
            {
                return false;
            }
        }
    }

    return true;
}

void data_is_datagram(uint8_t receivedData[])
{
    /**
     * Continue to communicate with other nodes after finishing communication with present node.
     */
    uint8_t layerSendNode   = ReceiveBuffer[9];
    if (layerSendNode <= g_node_dimension)
    {
        return;
    }
    /**
     * g_pre_packet_seq: for excising repeated frame, g_if_firstDatagram: for judge if starting
     */
    if ((g_pre_packet_seq == receivedData[5]) && g_if_firstDatagram)
    {
          return;
    }
    g_pre_packet_seq = receivedData[5];
    g_if_firstDatagram = true;

    uint8_t tempi = 0;
    uint8_t reveived_payload_size = receivedData[10]; /* 10: The payload size position */
    while(tempi != reveived_payload_size)
    {
        store_received_data[g_received_file_real_size] = receivedData[tempi + 11]; /* 11: The starting position of payload */
        g_received_file_real_size++;
        tempi++;
    }
    
    /** After receiving a datagram, then send out an ack **/
    spi_transHeaderStatus(0x10);
}

void terminateRoutine()
{
    spi_transHeaderStatus(0xD0); /**  terminate advertisers**/
    __delay_cycles(100);  /** delay 100 cycles for waiting this transmition finishing **/
    close_spi_process();  // Don't have any tasks, finish the spi process.
}
void data_is_fin()
{
    uint8_t * gen_sha256 = file_sha256(store_received_data, g_received_file_real_size);
    g_com_pass           = (memcmp(file_sha256_true, gen_sha256, SHA256_BLOCK_SIZE) == 0);
    if (g_com_pass)
    {
        //blink the led lights (and / or) transmition to next hop
        recevedSucess();
        g_if_transDataFromRec = true;
    } else {

    }
    spi_transHeaderStatus(0x80); // Sneding fin by the dst node.
    __delay_cycles(100);  /** delay 100 cycles for waiting this transmition finishing **/
    g_pairedNodeAddress = 0xff; // reinitializing for the next round transmition
    
    if (g_if_relayNode)
    {
        g_dest_address = g_dstFromSendNode;
        startTrans();
    } else {
        terminateRoutine();
    }

}

void data_is_reverseFin()
{
    g_pairedNodeAddress = 0xff; // reinitializing for the next round transmition
    terminateRoutine();
}

void data_is_find(uint8_t receivedData[])
{
    /**
     * will to do
     */
}

void data_is_ack(uint8_t *receivedData)
{
    uint8_t recever_packet_seq = receivedData[5];
    if ((recever_packet_seq == g_pre_ack_seq) && g_if_firstRecAck)
    {
        return;
    }

    g_pre_ack_seq     = receivedData[5];
    g_if_firstRecAck  = true;
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
     * receiving the first frame
     */
    uint8_t status_value = ReceiveBuffer[6];
    if (status_value == 0x04)
    {
        g_pairedNodeAddress = ReceiveBuffer[7];
        g_if_paired = true;
    }

    /**
     * Excluding ineligible packets
     */
    uint8_t srcFromSendNode = ReceiveBuffer[7];
    if (g_pairedNodeAddress != 0xff)
    {
        if (g_pairedNodeAddress != srcFromSendNode)
        {
            return;
        }
    }

    g_dstFromSendNode = ReceiveBuffer[8];


    uint8_t dataType = ReceiveBuffer[6];
    switch(dataType)
    {
     case 0x01:
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
     case 0x80:
         data_is_reverseFin();
         break;
     case 0x10:
         data_is_ack(ReceiveBuffer);
         break;
     default:
         break;
    }
}
