/*
 * uart.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */
#include <msp430.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include "uart.h"
#include "uartHex.h"
#include "crc.h"
#include "coordinatorFind.h"

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


int uniformInt(int min, int max)
{
    return (rand() % (max - min + 1)) + min;
}



void uartAction()
{
    int16_t receivedUart = combineBytes2(g_uartArr);
    if (lastData == receivedUart)
    {
        return;
    }
    lastData = receivedUart;
    if (receivedUart == 1000)
    {
        int i = 0;
        while (i < 3)
        {
            transHexBytes(2110);
            i++;
        }
        __no_operation();
        return;
    }

    if (receivedUart == 2000)
    {
        if (g_systimeCounter > 90000)
        {
            g_receCounter = g_receCounter + 1;
            g_systimeCounter = 0;
            __no_operation();
            // re-initialize some parameters for new star
            g_driftTime = 0;
            g_ifFindCoordinator = false;
        }
        if (g_receCounter == 0)
        {
            g_receCounter = 1000;
        }
        int j = 0;
        while (j < 3)
        {
            j++;
            transHexBytes(g_receCounter);
            __no_operation();
        }
        if (g_receCounter == 1000)
        {
            g_receCounter = 0;
        }
        __no_operation();
        g_uartSwitch = false;
        return;
    }

    if (g_synStrategy == Find)
    {
        findDelay(receivedUart);
        p_test = ((int32_t)p_test) * AMPLIFIER;
        if (g_ifAdjustDrift == true)
        {
            p_test = g_adjusUnits + p_test;
            g_ifAdjustDrift = false;
            g_adjusUnits = 0;
        }
        int k = 0;
        while (k < 3)
        {
            k++;
            transHexBytes((int32_t)p_test);
            __no_operation();
        }
        __no_operation();
    }

    if (g_synStrategy == NeutronStarNoAli)
    {
        int16_t delay3 = coFindDelay(receivedUart);
        if (g_gotoLoc == true)
        {
            g_gotoLoc = false;
            delay3 = delay3 + AMPLIFIER * g_distributedLoc;
        }
        int l = 0;
        while (l < 3)
        {
            l++;
            transHexBytes(delay3);
            __no_operation();
        }
    }

    if (g_synStrategy == CYCLE)
    {
        int bias2 = (receivedUart + 1) % COORDINATOR_CYCLES;
        int delay5 = COORDINATOR_CYCLES - bias2;
        int m = 0;
        while (m < 3)
        {
            m++;
            transHexBytes(delay5);
            __no_operation();
        }
        __no_operation();
    }

    if (g_synStrategy == Greedy)
    {
        int n = 0;
        while (n < 3)
        {
            n++;
            transHexBytes(0);
            __no_operation();
        }
    }

    if (g_synStrategy == NeutronStar)
    {
        int16_t delay1 = coFindDelay(receivedUart);
        __no_operation();
        g_chTimeSlots = receivedUart;
        if (g_ifAdjustDrift == true)
        {
            delay1 = g_adjusUnits + delay1;
            g_ifAdjustDrift = false;
            g_adjusUnits = 0;
        }
        if (g_gotoLoc == true)
        {
            g_gotoLoc = false;
            delay1 = delay1 + AMPLIFIER * g_distributedLoc + 10;
        }
        int o = 0;
        while (o < 3)
        {
            o++;
            transHexBytes(delay1);
            __no_operation();
        }

        __no_operation();
    }

    if (g_synStrategy == NeutronStarPlus)
    {
        srand(time(NULL));
        int randomNumber = uniformInt(1 , 2);
        int16_t delay1 = coFindDelay(receivedUart);
        g_chTimeSlots = receivedUart;
        if (g_ifAdjustDrift == true)
        {
            delay1 = g_adjusUnits + delay1;
            g_ifAdjustDrift = false;
            g_adjusUnits = 0;
        }
        if (g_gotoLoc == true)
        {
            g_gotoLoc = false;
            delay1 = delay1 + AMPLIFIER * g_distributedLoc; // + 10;
        }
        if (randomNumber == 1)
        {
            delay1 = delay1 + COORDINATOR_CYCLES;
        }
        int o = 0;
        while (o < 3)
        {
            o++;
            transHexBytes(delay1);
        }
        
        __no_operation();
    }
    g_systimeCounter = g_systimeCounter + receivedUart * AMPLIFIER;
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
        __no_operation();
        char temp = (char) UCA3RXBUF;
        if (temp == 0xff)
        {
            g_receveuartNum = 0;
            break;
        }
        g_uartArr[g_receveuartNum] = temp;
        if (g_receveuartNum < 2)
        {
            g_receveuartNum += 1;
        }
        if (g_receveuartNum == 2)
        {
            uartAction();
            g_receveuartNum = 0;
        }
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
