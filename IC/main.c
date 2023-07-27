#include <stdint.h>
#include <stdbool.h>
#include "public.h"
#include "routingRx.h"
#include "routingTx.h"
#include "hash.h"
#include "crc.h"
#include "random.h"
#include "transitionData.h"

#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector = EUSCI_A3_VECTOR // eUSCI ISR
__interrupt void USCI_A3_ISR(void)
#elif defined(__GNUC__)
void __attribute__((interrupt(EUSCI_A3_VECTOR))) USCI_A3_ISR(void)
#else
#error Compiler not supported!
#endif
{
    switch (__even_in_range(UCA3IV, USCI_UART_UCTXCPTIFG))
    {
    case USCI_NONE:
        break;
    case USCI_UART_UCRXIFG:
        g_RXData = UCA3RXBUF;
        g_switchUart = 0;
        __bic_SR_register_on_exit(GIE);
        break;
    case USCI_UART_UCTXIFG:
        break;
    case USCI_UART_UCSTTIFG:
        break;
    case USCI_UART_UCTXCPTIFG:
        break;
    default:
        break;
    }
}



void setNode(uint8_t nodeType)
{
    switch (nodeType)
    {
    case ICNODE:
        g_nodeAddress = 0x01;
        g_node_dimension = 0x7e;
        g_if_sourceNode = true;
        g_waitToFind = 0;
        break;
    case SINK:
        g_nodeAddress = 0x03;
        g_node_dimension = 0x01;
        g_waitToFind = 0x7e;
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
uint8_t TXByteCtr = 0;
uint8_t TransmitIndex = 0;

void CopyArray(uint8_t *source, uint8_t *dest, uint8_t count);
void SendUCB1Data(uint8_t val);

void close_spi_process(void)
{
    SWITCH2SPI = false;
}

void SendUCB1Data(uint8_t val)
{
    while (!(UCB1IFG & UCTXIFG))
        ;
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
    TransmitIndex = 0;
    g_receiveIndex = 0;
    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(TransmitRegAddr);
    __bis_SR_register(LPM0_bits | GIE);
    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    return MasterMode;
}

SPI_Mode SPI_Master_ReadReg(uint8_t reg_addr, uint8_t count)
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

void dummyWait()
{
    uint8_t i = 0;
    for (; i < SPI_DATA_LEN; i++)
    {
        g_transBuffer[i] = i + 0x20;
    }
    g_spi_waitThreshold = true;
    g_ack_waiter = 0;
    SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
    GPIO_MONINOR_OUT6 ^= GPIO_MONITOR_PIN2;
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

void initGPIO()
{
    // LEDs
    COMMS_LED_OUT &= ~COMMS_LED_PIN;
    COMMS_LED_DIR |= COMMS_LED_PIN;
    COMMS_LED_OUT &= ~COMMS_LED_PIN2;
    COMMS_LED_DIR |= COMMS_LED_PIN2;

    // Monitors
    GPIO_MONITOR_DIR6 |= GPIO_MONITOR_PIN2;
    GPIO_MONINOR_OUT6 |= GPIO_MONITOR_PIN2;
    GPIO_MONITOR_DIR6 |= GPIO_MONITOR_PIN3;
    GPIO_MONINOR_OUT6 |= GPIO_MONITOR_PIN3;
    GPIO_MONITOR_DIR8 |= GPIO_MONITOR_PIN1;
    GPIO_MONINOR_OUT8 |= GPIO_MONITOR_PIN1;
    GPIO_MONITOR_DIR4 |= GPIO_MONITOR_PIN1;
    GPIO_MONINOR_OUT4 |= GPIO_MONITOR_PIN1;

    // Configure SPI
    P5SEL0 |= BIT0 | BIT1 | BIT2;
    SLAVE_CS_DIR |= SLAVE_CS_PIN;
    SLAVE_CS_OUT |= SLAVE_CS_PIN;

    P6SEL1 &= ~(BIT0 | BIT1);
    P6SEL0 |= (BIT0 | BIT1); // USCI_A3 UART operation
    PJSEL0 |= BIT4 | BIT5;   // Configure XT1 pins
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
    CSCTL3 = DIVA__4 | DIVS__4 | DIVM__4; // Set all corresponding clk sources to divide by 4 for errata
    CSCTL1 = DCOFSEL_4 | DCORSEL;         // Set DCO to 16MHz
}

void initWAIT()
{
    TA0CCTL0 = CCIE; // TACCR0 interrupt enabled
    TA0CCR0 = TACCR;
    TA0CTL = TASSEL__SMCLK | MC__UPDOWN;
    __bis_SR_register(GIE); // Enter interrupt
}

// Timer0_A0 interrupt service routine
#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector = TIMER0_A0_VECTOR
__interrupt void Timer0_A0_ISR(void)
#elif defined(__GNUC__)
void __attribute__((interrupt(TIMER0_A0_VECTOR))) Timer0_A0_ISR(void)
#else
#error Compiler not supported!
#endif
{
    if (g_ack_waiter == MAXSPIWAIT)
    {
        g_spi_waitThreshold = false;
        g_ack_waiter = 0;
        TA0CCTL0 = CCIE_0;
        GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
    }
    P1OUT ^= BIT0;
    TA0CCR0 += TACCR;
    g_ack_waiter = g_ack_waiter + 1;
}

void recoveryStates()
{
    g_nextNodeID = FRAM_write[0];
    g_currentPairedNodeID = FRAM_write[1];
    g_receiveIndex = FRAM_write[2];
    g_systemStatus = FRAM_write[3];
    g_rounds = FRAM_write[4];
    g_queueLen = FRAM_write[5];
    g_waitToFind = FRAM_write[6];
    g_ICWaitCycles = FRAM_write[7];
    g_chargeCycles = FRAM_write[8];
    g_nextChargeCycles = FRAM_write[9];
    g_lastChargeCycles = FRAM_write[10];
}

int main(void)
{
    WDTCTL = WDTPW | WDTHOLD;
    g_sendAck = false;
    g_queueLen = 0;
    g_receiveIndex = 0;
    g_transDataSeq = 0;
    g_ack_waiter = 0;
    g_pre_packet_seq = 0x7e;
    g_pre_ack_seq = 0x7e;
    g_systemStatus = NONLAYER;
    g_seq_data = 0;
    g_currentPairedNodeID = 0;
    g_nextNodeID   = 0x7e;
    g_ICWaitCycles = 0;
    g_spi_waitThreshold  = false;
    g_RXData = 0;
    g_TXData = 0;
    g_switchUart = 1;
    g_delayCycles = 0;
    g_anchorCycles = 10;
    g_chargeCycles = 10;
    FRAM_write[8] = g_chargeCycles;
    /** do some pre-processing*/

    // Configure GPIO
    initGPIO();
    //***************************************
    //    TA0CCTL0 = CCIE; // TACCR0 interrupt enabled
    //    TA0CCR0 = DELAYUNIT;
    //    TA0CTL = TASSEL__SMCLK | MC__CONTINOUS; // SMCLK, continuous mode
    //    __bis_SR_register(GIE);                 // interrupt
    //***************************************
    // XT1 Setup
    CSCTL0_H = CSKEY_H; // Unlock CS registers
    CSCTL1 = DCOFSEL_0; // Set DCO to 1MHz
    CSCTL2 = SELA__LFXTCLK | SELS__DCOCLK | SELM__DCOCLK;
    CSCTL3 = DIVA__1 | DIVS__1 | DIVM__1; // Set all dividers
    CSCTL4 &= ~LFXTOFF;                   // Enable LFXT1
    do
    {
        CSCTL5 &= ~LFXTOFFG; // Clear XT1 fault flag
        SFRIFG1 &= ~OFIFG;
    } while (SFRIFG1 & OFIFG); // Test oscillator fault flag
    CSCTL0_H = 0;              // Lock CS registers
    // Configure USCI_A3 for UART mode
    UCA3CTLW0 |= UCSWRST;
    UCA3CTLW0 |= UCSSEL__ACLK; // Set ACLK = 32768 as UCBRCLK
    UCA3BRW = 3;               // 9600 baud
    UCA3MCTLW |= 0x5300;       // 32768/9600 - INT(32768/9600)=0.41
                               // UCBRSx value = 0x53 (See UG)
    UCA3CTLW0 &= ~UCSWRST;     // release from reset
    UCA3IE |= UCRXIE;          // Enable USCI_A3 RX interrupt
    while (g_switchUart)
    {
        while (!(UCA3IFG & UCTXIFG))
            ;
        UCA3TXBUF = g_TXData;
        __bis_SR_register(GIE); // Enter LPM0, interrupts enabled LPM0_bits |
    }
    __no_operation();
    /*do some pre-processing*/

    initClockTo16MHz();
    initSPI();
    setNode(SINK);

    if (g_if_sourceNode)
    {
        g_rounds = MAXROUND;
    }
    else
    {
        g_rounds = 0;
    }
    if (g_node_dimension != 0x01)
    {
        GPIO_MONINOR_OUT8 ^= GPIO_MONITOR_PIN1;
        g_queueLen = MAXQUELEN;
        GPIO_MONINOR_OUT8 ^= GPIO_MONITOR_PIN1;
    }
    /* Checking  system states from FRAM_write*/
    recoveryStates();
    start_spi_process();
}

void update_crc(void)
{
    uint8_t crc_input[32];
    uint8_t i = 0;
    for (; i < 31; i++)
    {
        crc_input[i] = g_transBuffer[i];
    }

    uint16_t crc_result = getCRC(crc_input);
    g_transBuffer[31] = (crc_result & 0xFF00) >> 8;
    g_transBuffer[32] = (crc_result & 0x00FF);

    while (g_transBuffer[31] >= 0x7F)
    {
        g_transBuffer[31] -= 0x7F;
    }

    while (g_transBuffer[32] >= 0x7F)
    {
        g_transBuffer[32] -= 0x7F;
    }
}

void start_spi_process(void)
{
    SWITCH2SPI = true;
    UCB1IE |= UCRXIE;
    while (SWITCH2SPI)
    {
        initWAIT();
        if (g_spi_waitThreshold == true)
        {
            continue;
        }
        __delay_cycles(10000); // SPI waiting time for reading and writing
        SPI_Master_ReadReg(CMD_TYPE_0_SLAVE, SPI_DATA_LEN);
        CopyArray(g_receiveBuffer, SlaveType0, SPI_DATA_LEN);
        __delay_cycles(10000); // SPI waiting time for reading and writing
        receiveDataFromNordic();
        if (g_sendAck == true)
        {
            produceNonPacketData();
            g_transBuffer[2] = g_pre_packet_seq;
            g_transBuffer[3] = PACKAGE_ACK;
            g_transBuffer[6] = g_currentPairedNodeID;
            update_crc();
            SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
            GPIO_MONINOR_OUT6 ^= GPIO_MONITOR_PIN3;
            g_sendAck = false;
            g_spi_waitThreshold = true;
            g_ack_waiter = 0;
            continue;
        }
        if (g_systemStatus == NONLAYER)
        {
            if (g_if_sourceNode)
            {
                if (g_node_dimension == 0x7e)
                {
                    dummyWait();
                    continue;
                }
                if (g_ICWaitCycles > 0)
                {
                    g_ICWaitCycles = g_ICWaitCycles - 1;
                    FRAM_write[7] = g_ICWaitCycles;
                    dummyWait();
                    continue;
                }
                if (g_waitToFind == 0)
                {
                    g_systemStatus = TRANSMIT;
                    FRAM_write[3] = g_systemStatus;
                    dummyWait();
                }
            }
            else
            {
                if (g_waitToFind == 0)
                {
                    g_systemStatus = SINKWAIT;
                    FRAM_write[3] = g_systemStatus;
                }
            }
            produceNonPacketData();
            g_transBuffer[3] = PACKAGE_FIND;
            update_crc();
            SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
            GPIO_MONINOR_OUT6 ^= GPIO_MONITOR_PIN3;
            g_waitToFind = g_waitToFind - 1;
            FRAM_write[6] = g_waitToFind;
            g_spi_waitThreshold = true;
        }
        else if (g_systemStatus == TRANSMIT)
        {
            if (g_queueLen == 0)
            {
                dummyWait();
                continue;
            }
            uint8_t *transmitBuffer = (uint8_t *) malloc (sizeof(uint8_t) * SPI_DATA_LEN);
            if (!transmitBuffer)
            {
                free(transmitBuffer);
                dummyWait();
                continue;
            }
            memset(transmitBuffer, 0, SPI_DATA_LEN);
            produceData(g_queueLen);
            m2s(transmitBuffer, &g_packetQueue);
            buf_m2s(transmitBuffer, SPI_DATA_LEN);
            free(transmitBuffer);
            transmitBuffer = NULL;
            SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
            GPIO_MONINOR_OUT6 ^= GPIO_MONITOR_PIN3;
            g_spi_waitThreshold = true;
            g_ack_waiter = 0;
        }
        else if (g_systemStatus == SINKWAIT)
        {
            dummyWait();
        }
    }
}

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
        g_receiveBuffer[g_receiveIndex++] = ucb1_rx_val;
        FRAM_write[2] = g_receiveIndex;
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
