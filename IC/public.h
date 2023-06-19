#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdbool.h>
#include <stddef.h>
#include "stdlib.h"
#include <stdint.h>
#include "hash.h"

#define SLAVE_CS_OUT P5OUT
#define SLAVE_CS_DIR P5DIR
#define SLAVE_CS_PIN BIT3

#define COMMS_LED_OUT P1OUT
#define COMMS_LED_DIR P1DIR
#define COMMS_LED_PIN BIT0
#define COMMS_LED_PIN2 BIT1
// #define COMMS_LED_PIN3 BIT2
// #define COMMS_LED_PIN4 BIT3

#define DUMMY 0x7e
#define CMD_TYPE_0_SLAVE 0xAA
#define CMD_TYPE_0_MASTER 0x01

#define MAXUINT8 0x5f
#define ICNODE     1
#define SINK       2
#define MAXBYTE    120

#define NONLAYER  0
#define TRANSMIT  1
#define RECEIVE   2
#define DONE      3
#define SINKWAIT  4

#define MAXQUELEN 6
#define MAXROUND  10
#define MAXFIND   10
#define MAXWAIT   10

#define PACKAGE_FIND     0x00
#define PACKAGE_PACKET   0x01
#define PACKAGE_FINISH   0x02
#define PACKAGE_RFINISH  0x03
#define PACKAGE_ACK      0x04
#define DUBBY            0x05

#define BLE_GAP_AD_TYPE  0x17
#define PACKET_DATA_LEN  0x17
#define SPI_NONCRC_LEN   0x20
#define SPI_DATA_LEN     0x22

typedef struct spi_datagram
{
    uint8_t hp_len;
    uint8_t t_broad_type;
    uint8_t seq;
    uint8_t status : 4,
        round : 4;
    uint8_t src : 4,
        dst : 4;
    uint8_t layer : 3,
        p_len : 5;
    uint8_t df[23];
    uint8_t crc[2];
} SPI_DATAGRAM;

uint16_t g_waitReceiveCounter;
uint16_t g_waitSendCounter;
uint8_t  g_currentPairedNodeID;
uint8_t  g_nextNodeID;
bool g_sendAck;
bool g_finishSend;
uint16_t       g_waitToFind;
uint8_t        g_rounds;
uint8_t        g_queueLen;
uint8_t        g_preQueLen;
uint8_t        g_systemStatus;
uint8_t        g_nodeAddress;
uint8_t        g_seq_data;
uint8_t        g_seq_header;
uint8_t        g_receiveBuffer[SPI_DATA_LEN];
uint8_t        g_transBuffer[SPI_DATA_LEN];
uint8_t        g_node_dimension;
bool           g_if_send_next;
bool           g_if_end_trans;
bool           g_if_sourceNode;
uint32_t       g_transDataSeq;
uint8_t        g_receivedNodeAddress;
uint32_t       g_received_file_real_size;
uint8_t        g_sha256_buf[SHA256_BLOCK_SIZE];
uint8_t        g_pre_ack_seq;
uint8_t        g_pre_packet_seq;
uint8_t        g_pre_fin_seq;
bool           g_if_nonFirstAck;
bool           g_non_firstDatagram;
SPI_DATAGRAM   *g_packetQueue;

void update_crc(void);
void start_spi_process(void);
void close_spi_process(void);
void recevedSucess(void);
void recevedFailure(void);
void startTrans(void);
uint16_t getCRC(unsigned char const message[]);
bool SWITCH2SPI;
uint8_t store_received_data[MAXBYTE];
typedef enum SPI_ModeEnum{
    IDLE_MODE,
    TX_REG_ADDRESS_MODE,
    RX_REG_ADDRESS_MODE,
    TX_DATA_MODE,
    RX_DATA_MODE
} SPI_Mode;

SPI_Mode SPI_Master_ReadReg(uint8_t reg_addr, uint8_t count);
SPI_Mode SPI_Master_WriteReg(uint8_t reg_addr, uint8_t count);


#endif
