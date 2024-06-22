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

    GPIO_MONITOR_DIR1 |= GPIO_MONITOR_PIN3;
    GPIO_MONINOR_OUT1 &= ~GPIO_MONITOR_PIN3;

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
}

// Included [min, max]
int uniformInt(int min, int max)
{
    return (rand() % (max - min + 1)) + min;
}
static void uartAction();
void static uartReceive()
{
    while (g_receveuartNum != 4)
    {
        __no_operation();
    }
    g_receveuartNum = 0;
    uartAction();
}

void static uartTrasmit(uint16_t num)
{
    int index = 0;
    int var = 1;
    for (; var >= 0; var--)
    {
        g_uartTrasBuff[index] = (num >> (var * 8)) & 0xff;
        index = index + 1;
    }
    int16_t crc_temp = getUartCRC(g_uartTrasBuff);
    var = 1;
    for (; var >= 0; var--)
    {
        g_uartTrasBuff[index] = (crc_temp >> (var * 8)) & 0xff;
        index = index + 1;
    }
    UCA3IE |= UCTXIE; // Enable USCI_A3 TX interrupt
    __bis_SR_register(GIE);
}

void uart_entry()
{
    while (g_uartSwitch == true)
    {
        UCA3IE |= UCRXIE;
        __bis_SR_register(GIE);
        uartReceive();
        __no_operation();
    }
    __bis_SR_register(GIE); // re-enbale interrupt
    __no_operation();
}

static void uartAction()
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
    reDataUart[0] = g_uartRecvBuff[0];
    reDataUart[1] = g_uartRecvBuff[1];
    receivedUart = combineBytes2(reDataUart);
    __no_operation();
    char transBuff[2];
    int index = 0;
    int var = 1;
    for (; var >= 0; var--)
    {
        transBuff[index] = (receivedUart >> (var * 8)) & 0xff;
        index = index + 1;
    }
    crcCode = getUartCRC(transBuff);
    reDataUart[0] = g_uartRecvBuff[2];
    reDataUart[1] = g_uartRecvBuff[3];
    uint16_t crcReceived = combineBytes2(reDataUart);
    if (crcReceived != crcCode)
    {
        return;
    }
    if (g_lastData == receivedUart)
    {
        __no_operation();
        return;
    }
    g_lastData = receivedUart;

    // Judge if exit
    if (receivedUart == 0xffff)
    {
        __no_operation();
        g_uartSwitch = false;
        return;
    }
    // Transfer syn counter
    uint16_t t_synCounter = g_receCounter + 0xafff;
    uartTrasmit(t_synCounter);
    __bis_SR_register(GIE); // re-open interrupt
    // Transfer delay time
    uint16_t delayTime = 0;
    if (g_synStrategy == FIND)
    {
        delayTime = findDelay(receivedUart);
    }
    else if (g_synStrategy == FLYNC)
    {
        delayTime = flyncDelay(receivedUart);
    }
    else if (g_synStrategy == PULSAR)
    {
        delayTime = pulsarDelay(receivedUart);
    }
    else if (g_synStrategy == FREEBEACON)
    {
        delayTime = freeBeaconDelay(receivedUart);
        delayTime = delayTime + g_freeBeaconBias;
        g_freeBeaconBias = 0;
    }
    else
    {
        delayTime = 0;
    }

    __delay_cycles(100000);
    uartTrasmit(delayTime);
    if (delayTime == 0)
    {
        GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN3;
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
        if (g_receveuartNum < 4)
        {
            g_uartRecvBuff[g_receveuartNum] = UCA3RXBUF;
            g_receveuartNum += 1;
        }
        if (g_receveuartNum == 4)
        {
            UCA3IE &= ~UCRXIE;
            __bic_SR_register_on_exit(GIE);
        }
        break;
    case USCI_UART_UCTXIFG:
        __no_operation();
        uint8_t var = 0;
        for (; var < 4; var++)
        {
            UCA3TXBUF = g_uartTrasBuff[var];
            __delay_cycles(100);
        }
        UCA3IE &= ~UCTXIE;
        __bic_SR_register_on_exit(GIE);
        break;
    case USCI_UART_UCSTTIFG:
        break;
    case USCI_UART_UCTXCPTIFG:
        break;
    default:
        break;
    }
}
