/*
 * uart.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */
#include <msp430.h>
// #include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include "swift.h"
#include "uart.h"
#include "uartHex.h"
#include "crc.h"
#include "coordinatorFind.h"

static bool reEntrance = true;
static uint16_t receivedUart = 0;
static int16_t crcCode = 0;

static uint8_t debugVar1 = 0;
void initGPIO()
{
    // LEDs
    COMMS_LED_DIR |= COMMS_LED_PIN;
    COMMS_LED_OUT &= ~COMMS_LED_PIN;
    COMMS_LED_DIR |= COMMS_LED_PIN2;
    COMMS_LED_OUT &= ~COMMS_LED_PIN2;

    // Comp
    // Configure Comp_E C12
    P3SEL1 |= BIT0;
    P3SEL0 |= BIT0; // Select C12 function on P3.0

    // Configure Comp_E COUT
    P1SEL1 |= BIT2;
    P1SEL0 &= ~(BIT2);
    P1DIR |= BIT2; // Select COUT function on P1.2

    // Monitors
    GPIO_MONITOR_DIR6 |= GPIO_MONITOR_PIN2;
    GPIO_MONINOR_OUT6 &= ~GPIO_MONITOR_PIN2;
    GPIO_MONITOR_DIR6 |= GPIO_MONITOR_PIN3;
    GPIO_MONINOR_OUT6 &= ~GPIO_MONITOR_PIN3;

    GPIO_MONITOR_DIR4 |= GPIO_MONITOR_PIN1;
    GPIO_MONINOR_OUT4 &= ~GPIO_MONITOR_PIN1;

    GPIO_MONITOR_DIR4 |= GPIO_MONITOR_PIN2;
    GPIO_MONINOR_OUT4 &= ~GPIO_MONITOR_PIN2;

    GPIO_MONITOR_DIR4 |= GPIO_MONITOR_PIN3;
    GPIO_MONINOR_OUT4 &= ~GPIO_MONITOR_PIN3;

    GPIO_MONITOR_DIR4 |= GPIO_MONITOR_PIN4;
    GPIO_MONINOR_OUT4 &= ~GPIO_MONITOR_PIN4;

    // Configure SPI
    P5SEL0 |= BIT0 | BIT1 | BIT2;
    SLAVE_CS_DIR |= SLAVE_CS_PIN;
    SLAVE_CS_OUT |= SLAVE_CS_PIN;

    P6SEL1 &= ~(BIT0 | BIT1);
    P6SEL0 |= (BIT0 | BIT1); // USCI_A3 UART operation
    PJSEL0 |= BIT4 | BIT5;   // Configure XT1 pins
    PM5CTL0 &= ~LOCKLPM5;
}

void setTimer()
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
    CSCTL0_H = 0;                         // Lock CS registers
}

void initUART()
{
    UCA3CTLW0 |= UCSWRST;
    UCA3CTLW0 |= UCSSEL__SMCLK_L; // Set ACLK = 32768 as UCBRCLK
    UCA3BRW = 3;                  // 9600 baud
    UCA3MCTLW |= 0x5300;          // 32768/9600 - INT(32768/9600)=0.41
                                  // UCBRSx value = 0x53 (See UG)
    UCA3CTLW0 &= ~UCSWRST;        // release from reset
    UCA3IE |= UCRXIE;             // Enable USCI_A3 RX interrupt
}

// Included [min, max]
int uniformInt(int min, int max)
{
    return (rand() % (max - min + 1)) + min;
}

void uart_entry()
{
    __bis_SR_register(GIE);
    while (g_uartSwitch && (g_nodeType == ICNODE))
    {
        __no_operation();
    }
    __no_operation();
}

static inline void uartAction()
{
    GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN3;
    GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN4;
    if (debugVar1 == 1)
    {
        __no_operation();
    }
    if (g_uartSwitch == false)
    {
        return;
    }
    char reDataUart[2];
    reDataUart[0] = g_uartArr[0];
    reDataUart[1] = g_uartArr[1];
    receivedUart = combineBytes2(reDataUart);
    char transBuff[2];
    int index = 0;
    int var = 1;
    for (; var >= 0; var--)
    {
        transBuff[index] = (receivedUart >> (var * 8)) & 0xff;
        index = index + 1;
    }
    crcCode = getUartCRC(transBuff);
    reDataUart[0] = g_uartArr[2];
    reDataUart[1] = g_uartArr[3];
    uint16_t crcReceived = combineBytes2(reDataUart);
    if (crcReceived != crcCode)
    {
        return;
    }
    // COMMS_LED_OUT ^= COMMS_LED_PIN;
    if (g_lastData == receivedUart)
    {
        __no_operation();
        return;
    }
    // COMMS_LED_OUT ^= COMMS_LED_PIN2;
    g_lastData = receivedUart;
    // GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;

    // Judge if exit
    if (receivedUart == 0xffff)
    {
        COMMS_LED_OUT ^= COMMS_LED_PIN;
        COMMS_LED_OUT ^= COMMS_LED_PIN2;
        __no_operation();
        g_uartSwitch = false;
        return;
    }
    // Transfer syn counter
    uint16_t t_synCounter = g_receCounter + 0xafff;
    transUartBytes(t_synCounter);
    GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN3;
    // Transfer delay time
    uint16_t delayTime = 0;
    if (g_synStrategy == Find)
    {
        delayTime = findDelay(receivedUart);
    }
    else if (g_synStrategy == Swift01)
    {
        delayTime = swift_role1(receivedUart);
    }
    else if (g_synStrategy == Swift02)
    {
        delayTime = swift_role2(receivedUart);
    }
    else if (g_synStrategy == NeutronStarNoAli)
    {
        delayTime = coFindDelay(receivedUart);
        if (g_gotoLoc == true)
        {
            g_gotoLoc = false;
            delayTime = delayTime + g_distributedLoc;
        }
    }
    else if (g_synStrategy == Greedy)
    {
        delayTime = 0;
    }
    else if (g_synStrategy == NeutronStar)
    {
        delayTime = coFindDelay(receivedUart);
        g_chTimeSlots = receivedUart;
        if (g_gotoLoc == true)
        {
            g_gotoLoc = false;
            delayTime = delayTime + g_distributedLoc;
        }
    }
    // if (delayTime > 500)
    // {
    //     GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN4;
    // }
    transUartBytes(delayTime);
    if (delayTime == 0)
    {
        g_uartSwitch = false;
    }
    debugVar1 = 1;
    __no_operation();
    GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN4;
}
// UART processsing
#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector = USCI_A3_VECTOR
__interrupt void USCI_A3_ISR(void)
#elif defined(__GNUC__)
void __attribute__((interrupt(USCI_A3_VECTOR))) USCI_A3_ISR(void)
#else
#error Compiler not supported!
#endif
{
    switch (__even_in_range(UCA3IV, USCI_UART_UCTXCPTIFG))
    {
    case USCI_NONE:
        break;
    case USCI_UART_UCRXIFG:
        if (g_receveuartNum == 4)
        {
            int8_t tempChar = UCA3RXBUF; // handle extra messages
        }
        if ((g_receveuartNum < 4) && (reEntrance == true))
        {
            g_uartArr[g_receveuartNum] = UCA3RXBUF;
            g_receveuartNum += 1;
        }
        if (g_receveuartNum == 4)
        {
            // GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN2;
            g_receveuartNum += 1;
            reEntrance = false;
            uartAction();
            reEntrance = true;
            g_receveuartNum = 0;
        }
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
