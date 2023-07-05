#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <msp430.h>
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

#define GPIO_MONINOR_OUT6 P6OUT
#define GPIO_MONITOR_DIR6 P6DIR
#define GPIO_MONITOR_PIN2 BIT2

#define DUMMY 0x7e
#define CMD_TYPE_0_SLAVE 0xAA
#define CMD_TYPE_0_MASTER 0x01

#define ICNODE     1
#define SINK       2
#define MAXBYTE    0x17

#define NONLAYER  0
#define TRANSMIT  1
#define SINKWAIT  4

#define MAXQUELEN 12
#define MAXROUND  10
#define MAXSPIWAIT 1000

#define PACKAGE_FIND     0x03
#define PACKAGE_PACKET   0x01
#define PACKAGE_FINISH   0x02
#define PACKAGE_ACK      0x04
#define DUBBY            0x05

#define BLE_GAP_AD_TYPE  0x17
#define PACKET_DATA_LEN  0x17
#define SPI_NONCRC_LEN   0x1F
#define SPI_DATA_LEN     0x21

#define WRITE_SIZE 128

#if defined(__TI_COMPILER_VERSION__)
#pragma PERSISTENT(FRAM_write)
char FRAM_write[WRITE_SIZE];
#elif defined(__IAR_SYSTEMS_ICC__)
__persistent char FRAM_write[WRITE_SIZE];
#elif defined(__GNUC__)
char __attribute__((persistent)) FRAM_write[WRITE_SIZE];
#else
#error Compiler not supported!
#endif

typedef struct spi_datagram
{
    uint8_t hp_len; 
    uint8_t t_broad_type;
    uint8_t seq;
    uint8_t status : 4,
        round : 4;
    uint8_t src : 4,
        dst : 4;
    uint8_t layer;
    uint8_t df[23];
    uint8_t crc[2];
} SPI_DATAGRAM;

uint8_t  g_nextNodeID;
bool g_sendAck;
uint8_t g_currentPairedNodeID;
uint8_t ReceiveIndex;
uint16_t       g_waitToFind;
uint16_t       g_ICWaitCycles;
uint8_t        g_rounds;
uint8_t        g_queueLen;
uint8_t        g_systemStatus;
uint8_t        g_nodeAddress;
uint8_t        g_seq_data;
uint8_t        g_receiveBuffer[SPI_DATA_LEN];
uint8_t        g_transBuffer[SPI_DATA_LEN ];
uint8_t        g_node_dimension;
bool           g_if_sourceNode;
bool           g_if_measure;
bool           g_spi_ack;
uint32_t       g_ack_waiter;
uint8_t        g_transDataSeq;
uint8_t        g_sha256_buf[SHA256_BLOCK_SIZE];
uint8_t        g_pre_ack_seq;
uint8_t        g_pre_packet_seq;
SPI_DATAGRAM   *g_packetQueue;

void FRAMWrite(void);
void update_crc(void);
void start_spi_process(void);
void close_spi_process(void);
uint16_t getCRC(unsigned char const message[]);
bool SWITCH2SPI;
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
