/*
 * uart.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */
#include <msp430.h>
#include <stdbool.h>
#include "uart.h"
#include "uartHex.h"
#include "crc.h"


void initGPIO()
{
    // LEDs
    LED_DIR |= LED0_PIN | LED1_PIN;
    LED_OUT &= ~(LED0_PIN | LED1_PIN); // turn off LEDs

    // LEDs
    COMMS_LED_OUT &= ~COMMS_LED_PIN;
    COMMS_LED_DIR |= COMMS_LED_PIN;
    COMMS_LED_OUT &= ~COMMS_LED_PIN2;
    COMMS_LED_DIR |= COMMS_LED_PIN2;

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
    GPIO_MONINOR_OUT6 |= GPIO_MONITOR_PIN2;
    GPIO_MONITOR_DIR6 |= GPIO_MONITOR_PIN3;
    GPIO_MONINOR_OUT6 |= GPIO_MONITOR_PIN3;

    // Configure SPI
    P5SEL0 |= BIT0 | BIT1 | BIT2;
    SLAVE_CS_DIR |= SLAVE_CS_PIN;
    SLAVE_CS_OUT |= SLAVE_CS_PIN;

    P6SEL1 &= ~(BIT0 | BIT1);
    P6SEL0 |= (BIT0 | BIT1); // USCI_A3 UART operation
    PJSEL0 |= BIT4 | BIT5;   // Configure XT1 pins
    PM5CTL0 &= ~LOCKLPM5;
}

void initClockTo16MHzUART()
{
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
}

void initUART()
{
    UCA3CTLW0 |= UCSWRST;
    UCA3CTLW0 |= UCSSEL__ACLK; // Set ACLK = 32768 as UCBRCLK
    UCA3BRW = 3;               // 9600 baud
    UCA3MCTLW |= 0x5300;       // 32768/9600 - INT(32768/9600)=0.41
                               // UCBRSx value = 0x53 (See UG)
    UCA3CTLW0 &= ~UCSWRST;     // release from reset
    UCA3IE |= UCRXIE;          // Enable USCI_A3 RX interrupt
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
        while (!(UCA3IFG & UCTXIFG));
        char temp = (char) UCA3RXBUF;
        if (g_gotoLoc == true)
        {
            g_gotoLoc = false;
            transHexBytes(g_currentLoc * AMPLIFIER);
        }
        if (g_receveuartNum < 6)
        {
            g_uartArr[g_receveuartNum] = temp;
        }
        g_receveuartNum += 1;
        __no_operation();
        break;
    case USCI_UART_UCTXIFG:
        break;
    case USCI_UART_UCSTTIFG:
        break;
    case USCI_UART_UCTXCPTIFG:
        break;
    }
}
