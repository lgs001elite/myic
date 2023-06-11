#ifndef _PUBLIC_H_
#define _PUBLIC_H_
#include <stdbool.h>
#include <stddef.h>
#include "stdlib.h"
#include <stdint.h>
#include "spi_packet.h"

#define MAXUINT8   0x7E
#define SENDER     1
#define REALYER    2
#define RECEIVER   3

#define BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS               0x17 /**< Public Target Address. */

extern  uint8_t        g_nodeAddress;
extern  uint8_t        g_seq_data;
extern  uint8_t        g_seq_header;
extern  uint8_t        g_dest_address;
extern  uint8_t        ReceiveBuffer[SPI_DATA_LEN];
extern  uint8_t        g_transBuffer[SPI_DATA_LEN];
extern  uint8_t        g_spiTransLen;
extern  uint8_t        g_node_dimension;
extern  bool           g_if_send_next;
extern  bool           g_if_end_trans;
extern  bool           g_if_sourceNode;
extern  bool           g_if_relayNode;
extern  bool           g_if_relay;
extern  bool           g_if_Rxternimate;
extern  bool           g_if_Txternimate;
extern  uint32_t       g_transDataSeq;
extern  uint8_t        g_receivedNodeAddress;

void start_spi_process(void);
void close_spi_process(void);
void recevedSucess(void);
void recevedFailure(void);
void startTrans(void);
void reInitialize(void);



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
