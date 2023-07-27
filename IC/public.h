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

// For measuring the time intervals of transmission
#define GPIO_MONINOR_OUT6 P6OUT
#define GPIO_MONITOR_DIR6 P6DIR
#define GPIO_MONINOR_OUT4 P4OUT
#define GPIO_MONITOR_DIR4 P4DIR
#define GPIO_MONITOR_PIN2 BIT2 // Packet around
#define GPIO_MONITOR_PIN3 BIT3 // Single path
// For measuring data produce time
#define GPIO_MONINOR_OUT8 P8OUT
#define GPIO_MONITOR_DIR8 P8DIR
#define GPIO_MONITOR_PIN1 BIT1

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
#define MAXSPIWAIT 10

#define PACKAGE_FIND     0x03
#define PACKAGE_PACKET   0x01
#define PACKAGE_FINISH   0x02
#define PACKAGE_ACK      0x04
#define DUBBY            0x05

#define BLE_GAP_AD_TYPE  0x17
#define PACKET_DATA_LEN  0x17
#define SPI_NONCRC_LEN   0x1F
#define SPI_DATA_LEN     0x21

#define WRITE_SIZE 11
#define TACCR   0x22
#define DELAYUNIT 50000

unsigned char g_RXData;
unsigned char g_TXData;
uint8_t g_switchUart;
uint8_t g_delayCycles;
uint8_t g_anchorCycles;


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

void recoveryStates();
uint8_t g_nextNodeID;
uint8_t g_currentPairedNodeID;
uint8_t g_receiveIndex;
uint8_t g_systemStatus;
uint8_t g_rounds;
uint8_t g_queueLen;
uint16_t g_waitToFind;
uint16_t g_ICWaitCycles;
uint16_t g_chargeCycles;
uint16_t g_nextChargeCycles;
uint16_t g_lastChargeCycles;

uint8_t        g_nodeAddress;
uint8_t        g_seq_data;
uint8_t        g_receiveBuffer[SPI_DATA_LEN];
uint8_t        g_transBuffer[SPI_DATA_LEN ];
uint8_t        g_node_dimension;
bool           g_if_sourceNode;
bool           g_spi_waitThreshold;
bool           g_sendAck;
uint32_t       g_ack_waiter;
uint8_t        g_transDataSeq;
uint8_t        g_sha256_buf[SHA256_BLOCK_SIZE];
uint8_t        g_pre_ack_seq;
uint8_t        g_pre_packet_seq;
SPI_DATAGRAM   g_packetQueue;
uint8_t SlaveType0[SPI_DATA_LEN];

void dummyWait();
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

#if defined(__TI_COMPILER_VERSION__)
#pragma PERSISTENT(FRAM_write)
unsigned long FRAM_write[WRITE_SIZE];
#elif defined(__IAR_SYSTEMS_ICC__)
__persistent unsigned long FRAM_write[WRITE_SIZE];
#elif defined(__GNUC__)
unsigned long __attribute__((persistent)) FRAM_write[WRITE_SIZE];
#else
#error Compiler not supported!
#endif

#endif
