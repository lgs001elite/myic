#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdbool.h>
#include <stddef.h>
#include "stdlib.h"
#include <stdint.h>
#include "spi_packet.h"

#define NODE_ADDRESS    0x03
#define MAXUINT8        255

#define BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS               0x17 /**< Public Target Address. */

extern  volatile uint8_t        g_seq_data;
extern  volatile uint8_t        g_seq_header;
extern  volatile uint8_t        g_dest_address;
extern           uint8_t        ReceiveBuffer[SPI_DATA_LEN];
extern           uint8_t        g_transBuffer[SPI_DATA_LEN];
extern  volatile uint8_t        g_spiTransLen;
extern  volatile uint8_t        g_node_dimension;
extern  volatile bool           g_if_send_next;
extern  volatile bool           g_if_end_trans;
extern  volatile bool           g_if_sourceNode;
extern  volatile uint8_t        g_pre_packet_seq;
extern  volatile uint8_t        g_pre_ack_seq;
extern  volatile bool           g_com_pass;
extern  volatile uint8_t        g_pairedNodeAddress;
extern  volatile bool           g_if_paired;
extern  volatile bool           g_if_firstRecAck;
extern  volatile bool           g_if_firstDatagram;
extern  volatile bool           g_if_transDataFromRec;
extern  volatile bool           g_if_relayNode;
extern  volatile uint8_t        g_dstFromSendNode;

void start_spi_process(void);
void close_spi_process(void);
void recevedSucess(void);
void startTrans(void);

//******************************************************************************
// General SPI State Machine ***************************************************
//******************************************************************************

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
