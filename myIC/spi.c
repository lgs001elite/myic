/*
 * spi.c
 *
 *  Created on: June 20, 2024
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

#define SLAVE_CS_OUT P5OUT
#define SLAVE_CS_DIR P5DIR
#define SLAVE_CS_PIN BIT3

#define SLAVE_RST_OUT P1OUT
#define SLAVE_RST_DIR P1DIR
#define SLAVE_RST_PIN BIT4

static bool spi_sender_signal = false;
// static bool spi_receiver_signal = false;

void initSPI()
{
    UCB1CTLW0 = UCSWRST;                                                                                   // **Put state machine in reset**
    UCB1CTLW0 |= UCCKPL_H | UCMSB | UCSYNC | UCMST | UCSSEL__SMCLK_L | UC7BIT__8BIT | UCMODE0 | UCSTEM | UCCKPH; // Added by me
    UCB1BRW = 0x20;
    UCB1CTLW0 &= ~UCSWRST;
    UCB1IE |= UCRXIE;
}

void start_spi_process(void)
{
    g_packet_id = g_packet_id + 1;
    g_packet_id = g_packet_id % 100;
    while (true)
    {
        receiveDataFromNordic();
        // If coordinator needs to reply info
        producePackets();
        if (g_currentNodeLoc == -1)
        {
            g_transBuffer[3] = PACKAGE_BROAD;
        }
        else
        {
            if (g_sendAck == true)
            {
                g_transBuffer[3] = PACKAGE_ACK;
                g_sendAck = false;
            }
            else
            {
                g_transBuffer[3] = PACKAGE_PACKET;
                if (g_nodeID == 0)
                {
                    g_nextNodeID = 1;
                }
                else
                {
                    g_nextNodeID = 0;
                }
                g_transBuffer[6] = g_nextNodeID; // updating the next hop id
            }
            g_transBuffer[2] = g_packet_id;
        }
        update_crc();
        // For sending process
        SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
        g_transmitIndex = 0;
        g_receiveIndex = 0;
        while (g_transmitIndex < SPI_DATA_LEN)
        {
            spi_sender_signal = true;
            UCB1IE |= UCTXIE;
            __bis_SR_register(LPM0_bits + GIE);
            __delay_cycles(100);
        }
        SLAVE_CS_OUT |= SLAVE_CS_PIN;
        __no_operation();
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
    switch (__even_in_range(UCB1IV, USCI_SPI_UCTXIFG))
    {
    case USCI_NONE:
        break;
    case USCI_SPI_UCRXIFG:
        if (g_receiveIndex < SPI_DATA_LEN)
        {
            g_receiveBuffer[g_receiveIndex++] = UCB1RXBUF;
            UCB1IFG &= ~UCRXIFG;
        }
        __bic_SR_register_on_exit(LPM0_bits);
        spi_sender_signal = false;
        __no_operation();
        break;
    case USCI_SPI_UCTXIFG:
        if (g_transmitIndex < SPI_DATA_LEN)
        {
            UCB1TXBUF = g_transBuffer[g_transmitIndex++];
            UCB1IE &= ~UCTXIE;
        }
        __no_operation();
        break;
    default:
        break;
    }
}
