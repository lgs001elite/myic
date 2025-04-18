//#include <stdint.h>
//#include <stdbool.h>
//#include <math.h>
//#include <time.h>
//#include <stdlib.h>
//#include "public.h"
//#include "routingRx.h"
//#include "routingTx.h"
//#include "hash.h"
//#include "crc.h"
//#include "random.h"
//#include "transitionData.h"
//
//#define DRIFTUNIT 1000
//// Fram write and read
// #pragma PERSISTENT(g_queueLen)
//uint8_t g_queueLen = MAXQUELEN;
//
// #pragma PERSISTENT(g_rounds)
//uint8_t g_rounds = MAXROUND;
//
// #pragma PERSISTENT(g_systemStatus)
//uint8_t g_systemStatus = TRANSMIT;
//
// #pragma PERSISTENT(g_attConn)
//int8_t  g_attConn = -1;
//
// #pragma PERSISTENT(g_accuCharge)
//uint8_t g_accuCharge = 0;
//
// #pragma PERSISTENT(g_MaxChargeCycles)
//uint16_t g_MaxChargeCycles = 0;
//
//
//#pragma PERSISTENT(g_TXData)
//unsigned char g_TXData = 0x56;
//
///* Used to track the state of the software state machine*/
//SPI_Mode MasterMode = IDLE_MODE;
//
///* The Register Address/Command to use*/
//uint8_t TransmitRegAddr = 0;
//
//uint8_t RXByteCtr = 0;
//uint8_t TXByteCtr = 0;
//uint8_t TransmitIndex = 0;
//
//void CopyArray(uint8_t *source, uint8_t *dest, uint8_t count);
//void SendUCB1Data(uint8_t val);
//void SendUCB1Data(uint8_t val)
//{
//    while (!(UCB1IFG & UCTXIFG))
//        ;
//    UCB1TXBUF = val;
//}
//
//void CopyArray(uint8_t *source, uint8_t *dest, uint8_t count)
//{
//    uint8_t copyIndex = 0;
//    for (copyIndex = 0; copyIndex < count; copyIndex++)
//    {
//        dest[copyIndex] = source[copyIndex];
//    }
//}
//
//SPI_Mode SPI_Master_WriteReg(uint8_t reg_addr, uint8_t count)
//{
//    MasterMode = TX_REG_ADDRESS_MODE;
//    TransmitRegAddr = reg_addr;
//    TXByteCtr = count;
//    TransmitIndex = 0;
//    g_receiveIndex = 0;
//    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
//    SendUCB1Data(TransmitRegAddr);
//    __bis_SR_register(LPM0_bits | GIE);
//    SLAVE_CS_OUT |= SLAVE_CS_PIN;
//    return MasterMode;
//}
//
//SPI_Mode SPI_Master_ReadReg(uint8_t reg_addr, uint8_t count)
//{
//    MasterMode = TX_REG_ADDRESS_MODE;
//    TransmitRegAddr = reg_addr;
//    RXByteCtr = count;
//    TXByteCtr = 0;
//    g_receiveIndex = 0;
//    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
//    SendUCB1Data(TransmitRegAddr);
//    __bis_SR_register(LPM0_bits | GIE);
//    SLAVE_CS_OUT |= SLAVE_CS_PIN;
//    return MasterMode;
//}
//
//void dummyWait()
//{
//    uint8_t i = 0;
//    for (; i < SPI_DATA_LEN; i++)
//    {
//        g_transBuffer[i] = i + 0x20;
//    }
//    g_ack_waiter = 0;
//    SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
//}
//
//void initSPI()
//{
//    // Clock Polarity: The inactive state is high
//    // MSB First, 8-bit, Master, 4-pin mode, Synchronous
//    UCB1CTLW0 = UCSWRST;                                                                                   // **Put state machine in reset**
//    UCB1CTLW0 |= UCCKPL | UCMSB | UCSYNC | UCMST | UCSSEL__SMCLK_L | UCMODE0 | UCSTEM | UC7BIT_0 | UCCKPH; // Added by me
//    UCB1BRW = 0x20;
//    UCB1CTLW0 &= ~UCSWRST;
//}
//
//void initGPIO()
//{
//    // LEDs
//    COMMS_LED_OUT &= ~COMMS_LED_PIN;
//    COMMS_LED_DIR |= COMMS_LED_PIN;
//    COMMS_LED_OUT &= ~COMMS_LED_PIN2;
//    COMMS_LED_DIR |= COMMS_LED_PIN2;
//
//    // Comp
//    // Configure Comp_E C12
//    P3SEL1 |= BIT0;
//    P3SEL0 |= BIT0; // Select C12 function on P3.0
//
//    // Configure Comp_E COUT
//    P1SEL1 |= BIT2;
//    P1SEL0 &= ~(BIT2);
//    P1DIR |= BIT2; // Select COUT function on P1.2
//
//    // Monitors
//    GPIO_MONITOR_DIR6 |= GPIO_MONITOR_PIN2;
//    GPIO_MONINOR_OUT6 |= GPIO_MONITOR_PIN2;
//    GPIO_MONITOR_DIR6 |= GPIO_MONITOR_PIN3;
//    GPIO_MONINOR_OUT6 |= GPIO_MONITOR_PIN3;
//    GPIO_MONITOR_DIR8 |= GPIO_MONITOR_PIN1;
//    GPIO_MONINOR_OUT8 |= GPIO_MONITOR_PIN1;
//    GPIO_MONITOR_DIR4 |= GPIO_MONITOR_PIN1;
//    GPIO_MONINOR_OUT4 |= GPIO_MONITOR_PIN1;
//
//    // Configure SPI
//    P5SEL0 |= BIT0 | BIT1 | BIT2;
//    SLAVE_CS_DIR |= SLAVE_CS_PIN;
//    SLAVE_CS_OUT |= SLAVE_CS_PIN;
//
//    P6SEL1 &= ~(BIT0 | BIT1);
//    P6SEL0 |= (BIT0 | BIT1); // USCI_A3 UART operation
//    PJSEL0 |= BIT4 | BIT5;   // Configure XT1 pins
//    PM5CTL0 &= ~LOCKLPM5;
//}
//
//void uartTimer()
//{
//    CSCTL0_H = CSKEY_H;                     // Unlock CS registers
//    CSCTL1 = DCOFSEL_0;                     // Set DCO to 1MHz
//    CSCTL2 = SELA__LFXTCLK | SELS__DCOCLK | SELM__DCOCLK;
//    CSCTL3 = DIVA__1 | DIVS__1 | DIVM__1;   // Set all dividers
//    CSCTL4 &= ~LFXTOFF;                     // Enable LFXT1
//    do
//    {
//        CSCTL5  &= ~LFXTOFFG;                // Clear XT1 fault flag
//        SFRIFG1 &= ~OFIFG;
//    } while (SFRIFG1 & OFIFG);              // Test oscillator fault flag
//    CSCTL0_H = 0;                           // Lock CS registers       // Set DCO to 16MHz
//}
//
//void initWAIT()
//{
//    TA0CCTL0 = CCIE; // TACCR0 interrupt enabled
//    TA0CCR0 = DRIFTUNIT;
//    TA0CTL = TASSEL__SMCLK | MC__CONTINOUS;
//    __bis_SR_register(GIE); // Enter interrupt
//}
//
//// Timer0_A0 interrupt service routine
//#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
//#pragma vector = TIMER0_A0_VECTOR
//__interrupt void Timer0_A0_ISR(void)
//#elif defined(__GNUC__)
//void __attribute__((interrupt(TIMER0_A0_VECTOR))) Timer0_A0_ISR(void)
//#else
//#error Compiler not supported!
//#endif
//{
//    GPIO_MONITOR_DIR4 ^= GPIO_MONITOR_PIN1;
//    TA0CCR0 += DRIFTUNIT;
//    g_driftTime = g_driftTime + 1;
//}
//
//void uartConfig()
//{
//    UCA3CTLW0 |= UCSWRST;
//    UCA3CTLW0 |= UCSSEL__ACLK;                // Set ACLK = 32768 as UCBRCLK
//    UCA3BRW = 3;                            // 9600 baud
//    UCA3MCTLW |= 0x5300;                    // 32768/9600 - INT(32768/9600)=0.41
//                                              // UCBRSx value = 0x53 (See UG)
//    UCA3CTLW0 &= ~UCSWRST;                   // release from reset
//    UCA3IE |= UCRXIE;                       // Enable USCI_A3 RX interrupt
//}
//
//void initClockTo16MHz()
//{
//    FRCTL0 = FRCTLPW | NWAITS_1;
//     // Clock System Setup
//     CSCTL0_H = CSKEY_H; // Unlock CS registers
//     CSCTL1 = DCOFSEL_0; // Set DCO to 1MHz
//     // Set SMCLK = MCLK = DCO, ACLK = VLOCLK
//     CSCTL2 = SELA__VLOCLK | SELS__DCOCLK | SELM__DCOCLK;
//     CSCTL3 = DIVA__4 | DIVS__4 | DIVM__4; // Set all corresponding clk sources to divide by 4 for errata
//     CSCTL1 = DCOFSEL_4 | DCORSEL;         // Set DCO to 16MHz
//}
//
//void accuDelay()
//{
//    if (g_chargeCycles > g_basicChargeCycles)
//    {
//        int times = g_chargeCycles / g_basicChargeCycles;
//        int remainder = g_chargeCycles % g_basicChargeCycles;
//        if (remainder > 0)
//        {
//            remainder = 1;
//        }
//        g_delayCycles = g_basicChargeCycles * (times + remainder) - g_chargeCycles;
//    }
//    else
//    {
//        g_delayCycles = g_basicChargeCycles - g_chargeCycles;
//    }
//    g_accuCharge = g_delayCycles + g_chargeCycles + g_accuCharge;
//}
//
//int main(void)
//{
//    WDTCTL = WDTPW | WDTHOLD;
//    g_sendAck = false;
//    g_receveuartNum = 0;
//    g_receiveIndex = 0;
//    g_transDataSeq = 0;
//    g_ack_waiter = 0;
//    g_pre_packet_seq = 0x7e;
//    g_seq_data = 0;
//    g_currentPairedNodeID = 0;
//    g_nextNodeID = 0x7e;
//    g_ICWaitCycles = 0;
//    g_RXData = 0;
//    g_switchUart = 1;
//    g_delayCycles = 0;
//    g_anchorCycles = 10;
//    g_chargeCycles = 10;
//    g_stayBackCycles = 0;
//    g_stayForwardCycles = 0;
//    g_basicChargeCycles = 0;
//    g_MaxChargeCycles = 0;
//    g_nextChargeCycles = 0;
//    g_lastChargeCycles = 0;
//    g_nodeAddress = 0x02;    // 0x02 0x01
//    g_node_dimension = 0x03; // 0x03 0x02
//    g_waitToFind = 0;
//    g_MatchNextHop = false;
//    g_attConn = -1;
//    g_accuCharge = 0;
//    g_driftTime = 0;
//    g_findTesting = true;
//    g_uartSwitch = true;
//    g_ifAdjustDrift = false;
//    g_receivedDriftTime = 0;
//    g_adjstUnits = 0;
//    g_ICRole = 0;
//    matchedNext = false;
//    // Configure GPIO
//    g_ifAdjustDrift = true;
//    g_adjstUnits = 0x30;
//    initGPIO();
//    uartTimer();
//    uartConfig();
//    initWAIT();
//    while (g_uartSwitch)
//    {
//        if ((g_ifAdjustDrift == true) && (g_adjstUnits != 0))
//        {
//            while (!(UCA3IFG & UCTXIFG))
//                         ;
//            UCA3TXBUF = g_adjstUnits;
//            g_adjstUnits = 0;
//        }
//        if ((g_ICRole == 1) && (matchedNext == false))
//        {
//            while (!(UCA3IFG & UCTXIFG))
//                         ;
//            UCA3TXBUF = 0x56;
//        }
//        __bis_SR_register(GIE);
//        COMMS_LED_OUT ^= COMMS_LED_PIN2;
//    }
//    initClockTo16MHz();
//    initSPI();
//    start_spi_process();
//    return 0;
//}
//
//void update_crc(void)
//{
//    uint8_t crc_input[32];
//    uint8_t i = 0;
//    for (; i < 31; i++)
//    {
//        crc_input[i] = g_transBuffer[i];
//    }
//
//    uint16_t crc_result = getCRC(crc_input);
//    g_transBuffer[31] = (crc_result & 0xFF00) >> 8;
//    g_transBuffer[32] = (crc_result & 0x00FF);
//
//    while (g_transBuffer[31] >= 0x7F)
//    {
//        g_transBuffer[31] -= 0x7F;
//    }
//
//    while (g_transBuffer[32] >= 0x7F)
//    {
//        g_transBuffer[32] -= 0x7F;
//    }
//}
//
//void start_spi_process(void)
//{
//    SWITCH2SPI = true;
//    UCB1IE |= UCRXIE;
//    while (SWITCH2SPI)
//    {
//        COMMS_LED_OUT ^= COMMS_LED_PIN;
//        __delay_cycles(10000); // SPI waiting time for reading and writing
//        SPI_Master_ReadReg(CMD_TYPE_0_SLAVE, SPI_DATA_LEN);
//        CopyArray(g_receiveBuffer, SlaveType0, SPI_DATA_LEN);
//        __delay_cycles(10000); // SPI waiting time for reading and writing
//        receiveDataFromNordic();
//        produceNonPacketData();
//        SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
//    }
//}
//
//// UART
//#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
//#pragma vector = EUSCI_A3_VECTOR // eUSCI ISR
//__interrupt void
//USCI_A3_ISR(void)
//#elif defined(__GNUC__)
//void __attribute__((interrupt(EUSCI_A3_VECTOR))) USCI_A3_ISR(void)
//#else
//#error Compiler not supported!
//#endif
//{
//    switch (__even_in_range(UCA3IV, USCI_UART_UCTXCPTIFG))
//    {
//    case USCI_NONE:
//        break;
//    case USCI_UART_UCRXIFG:
//        g_RXData = UCA3RXBUF;
//        while (!(UCA3IFG & UCTXIFG))
//            ;
//        UCA3TXBUF     = g_TXData;
//        if (g_receveuartNum == 10)
//        {
//            g_uartSwitch  = false;
//        }
//        g_receveuartNum = g_receveuartNum + 1;
//        break;
//    case USCI_UART_UCTXIFG:
//        break;
//    case USCI_UART_UCSTTIFG:
//        break;
//    case USCI_UART_UCTXCPTIFG:
//        break;
//    default:
//        break;
//    }
//}
//
//#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
//#pragma vector = USCI_B1_VECTOR
//__interrupt void USCI_B1_ISR(void)
//#elif defined(__GNUC__)
//void __attribute__((interrupt(USCI_B1_VECTOR))) USCI_B1_ISR(void)
//#else
//#error Compiler not supported!
//#endif
//{
//    uint8_t ucb1_rx_val = 0;
//    switch (__even_in_range(UCB1IV, USCI_SPI_UCTXIFG))
//    {
//    case USCI_NONE:
//        break;
//    case USCI_SPI_UCRXIFG:
//        ucb1_rx_val = UCB1RXBUF;
//        g_receiveBuffer[g_receiveIndex++] = ucb1_rx_val;
//        UCB1IFG &= ~UCRXIFG;
//        switch (MasterMode)
//        {
//        case TX_REG_ADDRESS_MODE:
//            if (RXByteCtr)
//            {
//                MasterMode = RX_DATA_MODE;
//                SendUCB1Data(DUMMY);
//            }
//            else
//            {
//                MasterMode = TX_DATA_MODE;
//                SendUCB1Data(g_transBuffer[TransmitIndex++]);
//                TXByteCtr--;
//            }
//            break;
//        case TX_DATA_MODE:
//            if (TXByteCtr)
//            {
//                SendUCB1Data(g_transBuffer[TransmitIndex++]);
//                TXByteCtr--;
//            }
//            else
//            {
//                MasterMode = IDLE_MODE;
//                __bic_SR_register_on_exit(CPUOFF);
//            }
//            break;
//        case RX_DATA_MODE:
//            if (RXByteCtr)
//            {
//                RXByteCtr--;
//            }
//            if (RXByteCtr == 0)
//            {
//                MasterMode = IDLE_MODE;
//                __bic_SR_register_on_exit(CPUOFF);
//            }
//            else
//            {
//                SendUCB1Data(DUMMY);
//            }
//            break;
//        default:
//            break;
//        }
//        break;
//    case USCI_SPI_UCTXIFG:
//        break;
//    default:
//        break;
//    }
//}
