/*
 * spi.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */
#include <msp430.h>
#include "spi.h"
#include "macro.h"
#include "pins.h"
#include "global_func.h"
#include "global_vars.h"
#include "routingRx.h"
#include "routingTx.h"
#include "crc.h"


bool testSwitch = true;


#define SLAVE_CS_OUT    P5OUT
#define SLAVE_CS_DIR    P5DIR
#define SLAVE_CS_PIN    BIT3

#define SLAVE_RST_OUT   P1OUT
#define SLAVE_RST_DIR   P1DIR
#define SLAVE_RST_PIN   BIT4

void initSPI()
{
    UCB1CTLW0 = UCSWRST;                                                                                   // **Put state machine in reset**
    UCB1CTLW0 |= UCCKPL | UCMSB | UCSYNC | UCMST | UCSSEL__SMCLK_L | UCMODE0 | UCSTEM | UC7BIT_0 | UCCKPH; // Added by me
    UCB1BRW = 0x20;
    UCB1CTLW0 &= ~UCSWRST;
}

void start_spi_process(void)
{
    while (1)
    {
        //GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN2;
        COMMS_LED_OUT ^= COMMS_LED_PIN;
        COMMS_LED_OUT ^= COMMS_LED_PIN2;
        produceNonPacketData();
        if (g_nodeType == ICNODE)
        {
            g_transBuffer[4] = ICNODE;
            if(g_sendAck == true)
            {
                g_transBuffer[3] = PACKAGE_ACK;
                g_sendAck = false;
            }
            else
            {
                g_transBuffer[3] = PACKAGE_PACKET;
            }
        }
        else
        {
            g_transBuffer[8] = g_currentNodeLoc;
            g_transBuffer[9] = g_currentNodeLoc;
            g_transBuffer[3] = PACKAGE_PACKET;
            if (g_sendAck == true)
            {
                g_transBuffer[3] = PACKAGE_ACK;
            }
        }
        update_crc();
        UCB1IE |= UCRXIE;
        // sending
        __delay_cycles(100000);
        SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
        //COMMS_LED_OUT ^= COMMS_LED_PIN;
        // receiving
        __delay_cycles(100000);
        SPI_Master_ReadReg(CMD_TYPE_0_SLAVE, SPI_DATA_LEN);
        __no_operation();
        receiveDataFromNordic();
        __no_operation();
        //GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN3;
    }
}

void SPI_Master_WriteReg(char reg_addr, char count)
{
    MasterMode = TX_REG_ADDRESS_MODE;
    TXByteCtr = count;
    TransmitIndex = 0;
    g_receiveIndex = 0;
    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(reg_addr);
    __bis_SR_register(LPM0_bits + GIE);
    SLAVE_CS_OUT |= SLAVE_CS_PIN;
}

void SPI_Master_ReadReg(char reg_addr, char count)
{
    MasterMode = TX_REG_ADDRESS_MODE;
    RXByteCtr = count;
    TXByteCtr = 0;
    g_receiveIndex = 0;
    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(reg_addr);
    __bis_SR_register(LPM0_bits + GIE);
    SLAVE_CS_OUT |= SLAVE_CS_PIN;
}

void SendUCB1Data(char val)
{
    while (!(UCB1IFG & UCTXIFG))
        ;
    UCB1TXBUF = val;
}


// SPI processing
#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector = USCI_B1_VECTOR
__interrupt void USCI_B1_ISR(void)
#elif defined(__GNUC__)
void __attribute__((interrupt(USCI_B1_VECTOR))) USCI_B1_ISR(void)
#else
#error Compiler not supported!
#endif
{
    char ucb1_rx_val = 0;
    switch (__even_in_range(UCB1IV, USCI_SPI_UCTXIFG))
    {
    case USCI_NONE:
        break;
    case USCI_SPI_UCRXIFG:
        ucb1_rx_val = UCB1RXBUF;
        g_receiveBuffer[g_receiveIndex++] = ucb1_rx_val;
        UCB1IFG &= ~UCRXIFG;
        switch (MasterMode)
        {
        case TX_REG_ADDRESS_MODE:
            if (RXByteCtr)
            {
                MasterMode = RX_DATA_MODE;
                SendUCB1Data(DUMMY);
            }
            else
            {
                MasterMode = TX_DATA_MODE;
                SendUCB1Data(g_transBuffer[TransmitIndex++]);
                TXByteCtr--;
            }
            break;
        case TX_DATA_MODE:
            if (TXByteCtr)
            {
                SendUCB1Data(g_transBuffer[TransmitIndex++]);
                TXByteCtr--;
            }
            else
            {
                MasterMode = IDLE_MODE;
                __bic_SR_register_on_exit(CPUOFF);
            }
            break;
        case RX_DATA_MODE:
            if (RXByteCtr)
            {
                RXByteCtr--;
            }
            if (RXByteCtr == 0)
            {
                MasterMode = IDLE_MODE;
                __bic_SR_register_on_exit(CPUOFF);
            }
            else
            {
                SendUCB1Data(DUMMY);
            }
            break;
        default:
            break;
        }
        break;
    case USCI_SPI_UCTXIFG:
        break;
    default:
        break;
    }
}
