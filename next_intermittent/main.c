//******************************************************************************
//   MSP430FR599x Demo - eUSCI_B1, SPI 4-Wire Master multiple byte RX/TX
//
//   Description: SPI master communicates to SPI slave sending and receiving
//   3 different messages of different length. SPI master will enter LPM0 mode
//   while waiting for the messages to be sent/receiving using SPI interrupt.
//   SPI Master will initially wait for a port interrupt in LPM0 mode before
//   starting the SPI communication.
//   ACLK = NA, MCLK = SMCLK = DCO 16MHz.
//
//
//                   MSP430FR5994
//                 -----------------
//            /|\ |             P1.0|-> Comms LED
//             |  |                 |
//             ---|RST          P1.4|-> Slave Reset (GPIO)
//                |                 |
//                |             P5.0|-> Data Out (UCB1SIMO)
//                |                 |
//       Button ->|P5.5         P5.1|<- Data In (UCB1SOMI)
//   Button LED <-|P1.1             |
//                |             P5.2|-> Serial Clock Out (UCB1CLK)
//                |                 |
//                |             P5.3|-> Slave Chip Select (GPIO)
//
//   Nima Eskandari and Ryan Meredith
//   Texas Instruments Inc.
//   January 2018
//   Built with CCS V7.0
//******************************************************************************

#include <msp430.h>
#include <ctpl.h>
#include <stdint.h>
#include <stdbool.h>
#include "spi_packet.h"
#include "public.h"
#include "routing.h"
#include "routingRx.h"
#include "routingTx.h"

//******************************************************************************
// Pin Config ******************************************************************
//******************************************************************************

#define SLAVE_CS_OUT    P5OUT
#define SLAVE_CS_DIR    P5DIR
#define SLAVE_CS_PIN    BIT3

#define COMMS_LED_OUT   P1OUT
#define COMMS_LED_DIR   P1DIR
#define COMMS_LED_PIN   BIT0
#define COMMS_LED_PIN2  BIT1
/** Adding by me **/
#define COMMS_LED_PIN3  BIT2
#define COMMS_LED_PIN4  BIT3

//******************************************************************************
// Example Commands ************************************************************
//******************************************************************************
#define        DUMMY                  0xFF
#define        CMD_TYPE_0_SLAVE       0xAA
#define        CMD_TYPE_0_MASTER      0x01
uint8_t SlaveType0 [SPI_DATA_LEN] = {0};

//******************************************************************************
// Initialize public vars ******************************************************
//******************************************************************************

/**
 * Configure nodes
 */

/**
 *  Specific configuration for the node   
 */
 uint8_t g_receivedNodeAddress  = 0xff;
 bool    g_if_relayNode         = false;
 uint8_t g_nodeAddress;
 uint8_t g_dest_address;
 uint8_t g_node_dimension;
 bool    g_if_sourceNode;
 bool    g_if_relay;

void setNode(uint8_t nodeType)
{
    switch (nodeType)
    {
    case 1:
        g_nodeAddress    = 0x01;
        g_dest_address   = 0x03;
        g_node_dimension = 0x03;
        g_if_relayNode   = false;
        g_if_sourceNode  = true;
        break;
    
    case 2:
        g_nodeAddress    = 0x02;
        g_dest_address   = 0x03;
        g_node_dimension = 0x02;
        g_if_relayNode   = true;
        g_if_sourceNode  = false;
        break;

    case 3:
        g_nodeAddress                   = 0x03;
        g_dest_address                  = 0xff;
        g_node_dimension                = 0x01;
        g_if_relayNode                  = false;
        g_if_sourceNode                 = false;
        break;

    default:
        break;
    }
}

static   bool    SWITCH2SPI                      = false;
 uint8_t ReceiveBuffer[SPI_DATA_LEN]     = {0};
 uint8_t g_transBuffer[SPI_DATA_LEN]     = {0};
 uint8_t g_seq_data                      = 0xff;
 uint8_t g_seq_header                    = 0xff;
 uint8_t g_received_address              = 0xff;
 bool    g_if_end_trans                  = false;
 bool    g_if_send_next                  = true;
 uint8_t g_spiTransLen                   = 0;
 bool    g_if_Rxternimate                = false;
 bool    g_if_Txternimate                = false;

uint8_t          file_sha256_true[32]            =
{
    0x4F, 0x5A, 0xBA, 0xAA, 0xF6, 0xDC, 0x0E, 0x08, 0x7D, 0xD6, 0x19, 0x9D, 0x8B, 0x90, 0x79, 0xF9, 
    0xD9, 0x68, 0x13, 0xC2, 0x97, 0xD3, 0x75, 0x16, 0x53, 0x78, 0x96, 0x83, 0xDA, 0x65, 0x26, 0xD4
};

uint8_t          store_received_data[978]        = {0};


/* Used to track the state of the software state machine*/
SPI_Mode MasterMode                              = IDLE_MODE;

/* The Register Address/Command to use*/
uint8_t TransmitRegAddr                          = 0;

/* ReceiveBuffer: Buffer used to receive data in the ISR
 * RXByteCtr: Number of bytes left to receive
 * ReceiveIndex: The index of the next byte to be received in ReceiveBuffer
 * TransmitBuffer: Buffer used to transmit data in the ISR
 * TXByteCtr: Number of bytes left to transfer
 * TransmitIndex: The index of the next byte to be transmitted in TransmitBuffer
 **/

uint8_t RXByteCtr                                = 0;
uint8_t ReceiveIndex                             = 0;
uint8_t TXByteCtr                                = 0;
uint8_t TransmitIndex                            = 0;

/* SPI Write and Read Functions */

/* For slave device, writes the data specified in *reg_data
 *
 * reg_addr: The register or command to send to the slave.
 *           Example: CMD_TYPE_0_MASTER
 * *reg_data: The buffer to write
 *           Example: MasterType0
 * count: The length of *reg_data
 *           Example: TYPE_0_LENGTH
 *  */


/* For slave device, read the data specified in slaves reg_addr.
 * The received data is available in ReceiveBuffer
 *
 * reg_addr: The register or command to send to the slave.
 *           Example: CMD_TYPE_0_SLAVE
 * count: The length of data to read
 *           Example: TYPE_0_LENGTH
 *  */


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
    spi_transData();
}

void close_spi_process(void)
{
    SWITCH2SPI = false;
}

void SendUCB1Data(uint8_t val)
{
    while (!(UCB1IFG & UCTXIFG));              // USCI_B1 TX buffer ready?
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

    __bis_SR_register(CPUOFF + GIE);              // Enter LPM0 w/ interrupts

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

    __bis_SR_register(CPUOFF + GIE);              // Enter LPM0 w/ interrupts

    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    return MasterMode;
}

//******************************************************************************
// Device Initialization *******************************************************
//******************************************************************************

void initSPI()
{ 
    //Clock Polarity: The inactive state is high
    //MSB First, 8-bit, Master, 4-pin mode, Synchronous
    UCB1CTLW0 = UCSWRST;                       // **Put state machine in reset**

    /**
     * The inactive state is high, Data is captured on the first UCLK edge and changed on the following edge;
     */
    UCB1CTLW0 |= UCCKPL | UCMSB | UCSYNC
                | UCMST | UCSSEL__SMCLK_L
                | UCMODE0 | UCSTEM | UC7BIT_0 | UCCKPH; // Added by me
    UCB1BRW = 0x20;
    //UCB1MCTLW = 0;
    UCB1CTLW0 &= ~UCSWRST;                     // **Initialize USCI state machine**
   // UCB1IE |= UCRXIE;                          // Enable USCI0 RX interrupt
}


void initGPIO()
{
    //LEDs
    COMMS_LED_OUT &= ~COMMS_LED_PIN;
    COMMS_LED_DIR |= COMMS_LED_PIN;

    //Final result indication
    COMMS_LED_OUT &= ~COMMS_LED_PIN2;
    COMMS_LED_DIR |= COMMS_LED_PIN2;

    //BUTTON_LED_DIR |= BUTTON_LED_PIN;
    //BUTTON_LED_OUT &= ~BUTTON_LED_PIN;

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
    CSCTL0_H = CSKEY_H;                     // Unlock CS registers
    CSCTL1 = DCOFSEL_0;                     // Set DCO to 1MHz

    // Set SMCLK = MCLK = DCO, ACLK = VLOCLK
    CSCTL2 = SELA__VLOCLK | SELS__DCOCLK | SELM__DCOCLK;

    // Per Device Errata set divider to 4 before changing frequency to
    // prevent out of spec operation from overshoot transient
    CSCTL3 = DIVA__4 | DIVS__4 | DIVM__4;   // Set all corresponding clk sources to divide by 4 for errata
    CSCTL1 = DCOFSEL_4 | DCORSEL;           // Set DCO to 16MHz

    // Delay by ~10us to let DCO settle. 60 cycles = 20 cycles buffer + (10us / (1/4MHz))
    __delay_cycles(60);
    CSCTL3 = DIVA__1 | DIVS__1 | DIVM__1;   // Set all dividers to 1 for 16MHz operation
    CSCTL0_H = 0;
}

// termination function

static void terminateTrans()
{
    reInitialize();
}

//******************************************************************************
// Main ************************************************************************
// Send and receive three messages containing the example commands *************
//******************************************************************************
int main(void) {
    WDTCTL = WDTPW | WDTHOLD;   // Stop watchdog timer
    initClockTo16MHz();
    initGPIO();
    initSPI();
    ctpl_enterLpm45(CTPL_ENABLE_RESTORE_ON_RESET);
    // SENDER REALYER RECEIVER
    setNode(REALYER);
    start_routing();
}

void start_spi_process(void)
{
    SWITCH2SPI = true;
    uint8_t transRxNum = 0;
    uint8_t transTxNum = 0;
    uint8_t transRtNum = 0;
    UCB1IE |= UCRXIE;
    while (SWITCH2SPI)
    {
        __delay_cycles(720000); // 120 ms
        SPI_Master_ReadReg(CMD_TYPE_0_SLAVE, SPI_DATA_LEN);
        CopyArray(ReceiveBuffer, SlaveType0, SPI_DATA_LEN);
        __delay_cycles(150000); // 25ms
        if (transRxNum <= 5)
        {
            receiveDataFromNordic();
        }
        __delay_cycles(150000); // 25ms
        SPI_Master_WriteReg(CMD_TYPE_0_MASTER, g_spiTransLen);
        COMMS_LED_OUT ^= COMMS_LED_PIN;
        // Judge if terminate transmition from the receiver part
        if (g_if_Rxternimate)
        {
            if (transRxNum == 5) // transmit 5 times
            {
                terminateTrans();
                if (g_if_relayNode)
                {
                    spi_transHeaderStatus(0x40);
                    g_transBuffer[5] = 0x03;
                    updateCRC(g_transBuffer);
                }
            } else if (transRxNum == 10)
            {
                close_spi_process();  // Don't have any tasks, finish the spi process.
                transRxNum = 0;
            }
            transRxNum++;
        }

        //Judge if terminate transmition from the transceiver part
        if (g_if_Txternimate)
        {
            if (transTxNum == 5) // transmit 5 times
            {
                close_spi_process();
            }
            transRxNum = 0;
            transTxNum++;
        }

        //Judge if start to send ack to the source node
        if (g_if_relay)
        {
            if (transRtNum != 5)
            {
                transRtNum       = 0;
                g_if_relay       = false;
            }
            transRtNum++;
        }
    }
}

//******************************************************************************
// SPI Interrupt ***************************************************************
//******************************************************************************

#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector=USCI_B1_VECTOR
__interrupt void USCI_B1_ISR(void)
#elif defined(__GNUC__)
void __attribute__ ((interrupt(USCI_B1_VECTOR))) USCI_B1_ISR (void)
#else
#error Compiler not supported!
#endif
{
    uint8_t ucb1_rx_val = 0;
    switch(__even_in_range(UCB1IV, USCI_SPI_UCTXIFG))
    {
        case USCI_NONE: break;
        case USCI_SPI_UCRXIFG:
            ucb1_rx_val = UCB1RXBUF;
            ReceiveBuffer[ReceiveIndex++] = ucb1_rx_val;
            UCB1IFG &= ~UCRXIFG;
            switch (MasterMode)
            {
                case TX_REG_ADDRESS_MODE:
                    if (RXByteCtr)
                    {
                        MasterMode = RX_DATA_MODE;   // Need to start receiving now
                        //Send Dummy To Start
                        SendUCB1Data(DUMMY);
                    }
                    else
                    {
                        MasterMode = TX_DATA_MODE;        // Continue to transmision with the data in Transmit Buffer
                        //Send First
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
                      //Done with transmission
                      MasterMode = IDLE_MODE;
                      __bic_SR_register_on_exit(CPUOFF);      // Exit LPM0
                    }
                    break;

                case RX_DATA_MODE:
                    if (RXByteCtr)
                    {
                        //Transmit a dummy
                        RXByteCtr--;
                    }
                    if (RXByteCtr == 0)
                    {
                        MasterMode = IDLE_MODE;
                        __bic_SR_register_on_exit(CPUOFF);      // Exit LPM0
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
        default: break;
    }
}
