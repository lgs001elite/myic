#include <msp430.h>
#include <ctpl.h>
#include <stdint.h>
#include <stdbool.h>
#include "public.h"
#include "routingRx.h"
#include "routingTx.h"
#include "hash.h"
#include "crc.h"
#include "random.h"
#include "transitionData.h"

//******************************************************************************
// Pin Config ******************************************************************
//******************************************************************************

#define SLAVE_CS_OUT P5OUT
#define SLAVE_CS_DIR P5DIR
#define SLAVE_CS_PIN BIT3

#define COMMS_LED_OUT P1OUT
#define COMMS_LED_DIR P1DIR
#define COMMS_LED_PIN BIT0
#define COMMS_LED_PIN2 BIT1
/** Adding by me **/
#define COMMS_LED_PIN3 BIT2
#define COMMS_LED_PIN4 BIT3

//******************************************************************************
// Example Commands ************************************************************
//******************************************************************************
#define DUMMY 0xFF
#define CMD_TYPE_0_SLAVE 0xAA
#define CMD_TYPE_0_MASTER 0x01
uint8_t SlaveType0[SPI_DATA_LEN] = {0};
void setNode(uint8_t nodeType)
{
    switch (nodeType)
    {
    case ICNODE:
        g_nodeAddress = 0x01;
        g_dest_address = 0x03;
        g_node_dimension = 0xff;
        g_if_sourceNode = true;
        break;
    case SINK:
        g_nodeAddress = 0x03;
        g_dest_address = 0xff;
        g_node_dimension = 0x01;
        g_if_sourceNode = false;
        break;

    default:
        break;
    }
}

/* Used to track the state of the software state machine*/
SPI_Mode MasterMode = IDLE_MODE;

/* The Register Address/Command to use*/
uint8_t TransmitRegAddr = 0;

uint8_t RXByteCtr = 0;
uint8_t ReceiveIndex = 0;
uint8_t TXByteCtr = 0;
uint8_t TransmitIndex = 0;

void CopyArray(uint8_t *source, uint8_t *dest, uint8_t count);
void SendUCB1Data(uint8_t val);

void recevedSucess(void)
{
    COMMS_LED_OUT ^= COMMS_LED_PIN;
    COMMS_LED_OUT ^= COMMS_LED_PIN2;
}

void recevedFailure(void)
{
    COMMS_LED_OUT ^= COMMS_LED_PIN2;
}

void startTrans(void)
{
    uint8_t index = 0;
    for (; index < 3; index++)
    {
        COMMS_LED_OUT ^= COMMS_LED_PIN2;
    }
    produceData();
}

void close_spi_process(void)
{
    SWITCH2SPI = false;
}

void SendUCB1Data(uint8_t val)
{
    while (!(UCB1IFG & UCTXIFG))
        ; // USCI_B1 TX buffer ready?
    UCB1TXBUF = val;
}

void CopyArray(uint8_t *source, uint8_t *dest, uint8_t count)
{
    uint8_t copyIndex = 0;
    for (copyIndex = 0; copyIndex < count; copyIndex++)
    {
        dest[copyIndex] = source[copyIndex];
    }
}

SPI_Mode SPI_Master_WriteReg(uint8_t reg_addr, uint8_t count)
{
    MasterMode = TX_REG_ADDRESS_MODE;
    TransmitRegAddr = reg_addr;

    TXByteCtr = count;
    RXByteCtr = 0;
    ReceiveIndex = 0;
    TransmitIndex = 0;

    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(TransmitRegAddr);

    __bis_SR_register(CPUOFF + GIE); // Enter LPM0 w/ interrupts

    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    return MasterMode;
}

SPI_Mode SPI_Master_ReadReg(uint8_t reg_addr, uint8_t count)
{
    MasterMode = TX_REG_ADDRESS_MODE;
    TransmitRegAddr = reg_addr;
    RXByteCtr = count;
    TXByteCtr = 0;
    ReceiveIndex = 0;
    TransmitIndex = 0;

    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(TransmitRegAddr);

    __bis_SR_register(CPUOFF + GIE); // Enter LPM0 w/ interrupts

    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    return MasterMode;
}

//******************************************************************************
// Device Initialization *******************************************************
//******************************************************************************

void initSPI()
{
    // Clock Polarity: The inactive state is high
    // MSB First, 8-bit, Master, 4-pin mode, Synchronous
    UCB1CTLW0 = UCSWRST; // **Put state machine in reset**

    /**
     * The inactive state is high, Data is captured on the first UCLK edge and changed on the following edge;
     */
    UCB1CTLW0 |= UCCKPL | UCMSB | UCSYNC | UCMST | UCSSEL__SMCLK_L | UCMODE0 | UCSTEM | UC7BIT_0 | UCCKPH; // Added by me
    UCB1BRW = 0x20;
    // UCB1MCTLW = 0;
    UCB1CTLW0 &= ~UCSWRST; // **Initialize USCI state machine**
                           // UCB1IE |= UCRXIE;                          // Enable USCI0 RX interrupt
}

void initGPIO()
{
    // LEDs
    COMMS_LED_OUT &= ~COMMS_LED_PIN;
    COMMS_LED_DIR |= COMMS_LED_PIN;

    // Final result indication
    COMMS_LED_OUT &= ~COMMS_LED_PIN2;
    COMMS_LED_DIR |= COMMS_LED_PIN2;

    // BUTTON_LED_DIR |= BUTTON_LED_PIN;
    // BUTTON_LED_OUT &= ~BUTTON_LED_PIN;

    // Configure SPI
    P5SEL0 |= BIT0 | BIT1 | BIT2;

    SLAVE_CS_DIR |= SLAVE_CS_PIN;
    SLAVE_CS_OUT |= SLAVE_CS_PIN;

    // Disable the GPIO power-on default high-impedance mode to activate
    // previously configured port settings
    PM5CTL0 &= ~LOCKLPM5;
}

void initClockTo16MHz()
{
    FRCTL0 = FRCTLPW | NWAITS_1;

    // Clock System Setup
    CSCTL0_H = CSKEY_H; // Unlock CS registers
    CSCTL1 = DCOFSEL_0; // Set DCO to 1MHz

    // Set SMCLK = MCLK = DCO, ACLK = VLOCLK
    CSCTL2 = SELA__VLOCLK | SELS__DCOCLK | SELM__DCOCLK;

    // Per Device Errata set divider to 4 before changing frequency to
    // prevent out of spec operation from overshoot transient
    CSCTL3 = DIVA__4 | DIVS__4 | DIVM__4; // Set all corresponding clk sources to divide by 4 for errata
    CSCTL1 = DCOFSEL_4 | DCORSEL;         // Set DCO to 16MHz

    // Delay by ~10us to let DCO settle. 60 cycles = 20 cycles buffer + (10us / (1/4MHz))
    __delay_cycles(60);
    CSCTL3 = DIVA__1 | DIVS__1 | DIVM__1; // Set all dividers to 1 for 16MHz operation
    CSCTL0_H = 0;
}

//******************************************************************************
// Main ************************************************************************
// Send and receive three messages containing the example commands *************
//******************************************************************************
int main(void)
{
    WDTCTL = WDTPW | WDTHOLD; // Stop watchdog timer
    initClockTo16MHz();
    initGPIO();
    initSPI();
    ctpl_enterLpm45(CTPL_ENABLE_RESTORE_ON_RESET);
    // SENDER REALYER RECEIVER
    setNode(SINK);
    g_sendAck = false;
    g_finishSend = false;
    g_waitToFind = 0;
    g_findThreshold = MAXFIND;
    g_waitThreshold = MAXWAIT;
    g_queueLen = 0;
    g_rounds = 0;
    g_transDataSeq = 0;
    g_if_end_trans = false;
    g_received_file_real_size = 0;
    g_pre_packet_seq = 0xff;
    g_pre_fin_seq = 0xff;
    g_pre_ack_seq = 0xff;
    g_non_firstDatagram = false;
    g_systemStatus = NONLAYER;
    g_seq_data = (uint8_t)genRanNumb();
    g_seq_header = (uint8_t)genRanNumb();
    g_if_send_next = true;
    g_spiTransLen = SPI_DATA_LEN;
    g_receivedNodeAddress = 0xff;
    g_if_nonFirstAck = false;
    g_currentPairedNodeID = 0xff;
    g_nextNodeID = 0xff;
    g_waitReceiveCounter = 0;
    g_packetQueue = (SPI_DATAGRAM *)malloc(sizeof(SPI_DATAGRAM) * MAXQUELEN);
    produceData();
    start_spi_process();
}

void start_spi_process(void)
{
    SWITCH2SPI = true;
    UCB1IE |= UCRXIE;
    while (SWITCH2SPI)
    {
        // SPI-Sending
        if (g_systemStatus == NONLAYER)
        {
            produceNonPacketData();
            if (g_waitToFind > 0)
            {
                g_waitToFind = g_waitToFind - 1;
            }
            if ((g_node_dimension != 0xff) && (g_waitToFind == 0))
            {
                g_findThreshold = g_findThreshold - 1;
                if (g_findThreshold == 0)
                {
                    g_systemStatus = TRANSMIT;
                }
                g_transBuffer[2] = g_findThreshold;
                g_transBuffer[3] = PACKAGE_FIND;
            }
        }
        else if (g_systemStatus == TRANSMIT)
        {

            if (g_queueLen == 0)
            {
                g_systemStatus = RECEIVE;
                continue;
            }
            if (g_finishSend == true)
            {
                continue;
            }
            uint8_t *transmitBuffer = (uint8_t *)malloc(sizeof(uint8_t) * SPI_DATA_LEN);
            if (!transmitBuffer)
            {
                return;
            }
            memset(transmitBuffer, 0, SPI_DATA_LEN);

            m2s(transmitBuffer, &g_packetQueue[g_queueLen]);
            buf_m2s(transmitBuffer, SPI_DATA_LEN);
        }
        else if (g_systemStatus == RECEIVE)
        {
            if (g_queueLen >= MAXQUELEN)
            {
                g_systemStatus = TRANSMIT;
                continue;
            }
            if (g_waitReceiveCounter > MAXWAIT)
            {
                g_systemStatus = TRANSMIT;
                continue;
            }
            produceNonPacketData();
            if (g_queueLen != 0)
            {
                g_waitReceiveCounter = g_waitReceiveCounter + 1;
            }

            if (g_sendAck == true)
            {
                produceNonPacketData();
                g_transBuffer[3] = PACKAGE_ACK;
                g_sendAck = false;
            }
        }
        else if (g_systemStatus == DONE)
        {
            produceNonPacketData();
            g_transBuffer[3] = PACKAGE_FINISH;
            close_spi_process();
        }
        // SPI-Receiving
        __delay_cycles(720000); // 120 ms
        SPI_Master_ReadReg(CMD_TYPE_0_SLAVE, SPI_DATA_LEN);
        CopyArray(g_receiveBuffer, SlaveType0, SPI_DATA_LEN);
        __delay_cycles(150000); // 25ms
        receiveDataFromNordic();
        __delay_cycles(150000); // 25ms
        SPI_Master_WriteReg(CMD_TYPE_0_MASTER, g_spiTransLen);
        COMMS_LED_OUT ^= COMMS_LED_PIN;
    }
}

//******************************************************************************
// SPI Interrupt ***************************************************************
//******************************************************************************

#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector = USCI_B1_VECTOR
__interrupt void USCI_B1_ISR(void)
#elif defined(__GNUC__)
void __attribute__((interrupt(USCI_B1_VECTOR))) USCI_B1_ISR(void)
#else
#error Compiler not supported!
#endif
{
    uint8_t ucb1_rx_val = 0;
    switch (__even_in_range(UCB1IV, USCI_SPI_UCTXIFG))
    {
    case USCI_NONE:
        break;
    case USCI_SPI_UCRXIFG:
        ucb1_rx_val = UCB1RXBUF;
        g_receiveBuffer[ReceiveIndex++] = ucb1_rx_val;
        UCB1IFG &= ~UCRXIFG;
        switch (MasterMode)
        {
        case TX_REG_ADDRESS_MODE:
            if (RXByteCtr)
            {
                MasterMode = RX_DATA_MODE; // Need to start receiving now
                // Send Dummy To Start
                SendUCB1Data(DUMMY);
            }
            else
            {
                MasterMode = TX_DATA_MODE; // Continue to transmision with the data in Transmit Buffer
                // Send First
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
                // Done with transmission
                MasterMode = IDLE_MODE;
                __bic_SR_register_on_exit(CPUOFF); // Exit LPM0
            }
            break;

        case RX_DATA_MODE:
            if (RXByteCtr)
            {
                // Transmit a dummy
                RXByteCtr--;
            }
            if (RXByteCtr == 0)
            {
                MasterMode = IDLE_MODE;
                __bic_SR_register_on_exit(CPUOFF); // Exit LPM0
            }
            else
            {
                SendUCB1Data(DUMMY);
            }
            break;

        default:
            __no_operation();
            break;
        }
        break;
    case USCI_SPI_UCTXIFG:
        break;
    default:
        break;
    }
}
