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


void initClockTo16MHzSPI()
{
    FRCTL0 = FRCTLPW | NWAITS_1;
    // Clock System Setup
    CSCTL0_H = CSKEY_H; // Unlock CS registers
    CSCTL1 = DCOFSEL_0; // Set DCO to 1MHz
    // Set SMCLK = MCLK = DCO, ACLK = VLOCLK
    CSCTL2 = SELA__VLOCLK | SELS__DCOCLK | SELM__DCOCLK;
    CSCTL3 = DIVA__4 | DIVS__4 | DIVM__4; // Set all corresponding clk sources to divide by 4 for errata
    CSCTL1 = DCOFSEL_4 | DCORSEL;         // Set DCO to 16MHz

    CSCTL0_H = 0; // Lock CS registerss
}

void initSPI()
{
    // Clock Polarity: The inactive state is high
    // MSB First, 8-bit, Master, 4-pin mode, Synchronous
    UCB1CTLW0 = UCSWRST;                                                                                   // **Put state machine in reset**
    UCB1CTLW0 |= UCCKPL | UCMSB | UCSYNC | UCMST | UCSSEL__SMCLK_L | UCMODE0 | UCSTEM | UC7BIT_0 | UCCKPH; // Added by me
    UCB1BRW = 0x20;
    UCB1CTLW0 &= ~UCSWRST;
}

void start_spi_process(void)
{
    SWITCH2SPI = true;
    UCB1IE |= UCRXIE;
    while (1)
    {
        __delay_cycles(10000); // SPI waiting time for reading and writing
        SPI_Master_ReadReg(CMD_TYPE_0_SLAVE, SPI_DATA_LEN);
        CopyArray(g_receiveBuffer, SlaveType0, SPI_DATA_LEN);
        __delay_cycles(10000); // SPI waiting time for reading and writing
        receiveDataFromNordic();
        produceNonPacketData();
        if (g_nodeType == ICNODE)
        {
            if(g_sendAck == true)
            {
                g_transBuffer[4]  = ICNODE;
                g_transBuffer[3]  = PACKAGE_ACK;
            }
            else
            {
                g_transBuffer[3] = PACKAGE_PACKET;
                if (g_distributedLoc != 0)
                {
                    g_transBuffer[4] = ICNODE;
                }
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
        update_crc(g_transBuffer);
        SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
        __no_operation();
    }
}

SPI_Mode SPI_Master_WriteReg(char reg_addr, char count)
{
    MasterMode = TX_REG_ADDRESS_MODE;
    TransmitRegAddr = reg_addr;
    TXByteCtr = count;
    TransmitIndex = 0;
    g_receiveIndex = 0;
    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(TransmitRegAddr);
    __bis_SR_register(LPM0_bits | GIE);
    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    return MasterMode;
}

SPI_Mode SPI_Master_ReadReg(char reg_addr, char count)
{
    MasterMode = TX_REG_ADDRESS_MODE;
    TransmitRegAddr = reg_addr;
    RXByteCtr = count;
    TXByteCtr = 0;
    g_receiveIndex = 0;
    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(TransmitRegAddr);
    __bis_SR_register(LPM0_bits | GIE);
    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    return MasterMode;
}

void SendUCB1Data(char val)
{
    while (!(UCB1IFG & UCTXIFG))
        ;
    UCB1TXBUF = val;
}

void CopyArray(char *source, char *dest, char count)
{
    char copyIndex = 0;
    for (copyIndex = 0; copyIndex < count; copyIndex++)
    {
        dest[copyIndex] = source[copyIndex];
    }
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
