#include <msp430.h>
#include <stdint.h>
#include <stdbool.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "crc.h"
#include "office_1.h"
#include "office_2.h"
#include "stairs_1.h"
#include "stairs_2.h"

#define energy_office_01 0
#define energy_office_02 1
#define energy_stairs_01 2
#define energy_stairs_02 3


#define COUNTER_UNIT 0xffff
#define SLOT_AMPLIFIER 100
#define MAX_ENCOUNTER_THRESHOLD 100
#define INITIAL_UART_TIME 1099999

static int g_office1_length = sizeof(office_1) / sizeof(office_1[0]);
static int g_office2_length = sizeof(office_2) / sizeof(office_2[0]);
static int g_stairs1_length = sizeof(stairs_1) / sizeof(stairs_1[0]);
static int g_stairs2_length = sizeof(stairs_2) / sizeof(stairs_2[0]);


static int g_office1_index = 0;
static int g_office2_index = 0;
static int g_stairs1_index = 0;
static int g_stairs2_index = 0;


static uint16_t chargeCycles = 0;
static uint16_t g_slotUnitCounter = 0;
static uint16_t lastReceivedData = 0;
static char g_uartRecvBuff[4] = {0};
static char g_uartTrasBuff[4] = {0};
static bool g_afterUartWork = false;
static bool g_preventRepeatedUart = true;
static int g_energyMode = energy_office_01;
static int g_synIndex = 0;
static uint16_t g_extraDelayCounter = 0;
static uint8_t g_reCounter = 0;
static bool g_uartTerminalFlag = false;
static bool g_extraDelayIndicator = false;
static bool g_powerOff = false;
static uint16_t g_reUartData = 0;
static int16_t g_crcCode = 0;

#ifndef __debug
#pragma GCC poison printf
#endif

void initGPIO()
{
    P1OUT &= ~BIT2; // Clear P1.0 output latch for a defined power-on state
    P1DIR |= BIT2;  // Set P1.0 to output direction
    P1OUT &= ~BIT0; // Clear P1.0 output latch for a defined power-on state
    P1DIR |= BIT0;  // Set P1.0 to output direction
    P1OUT &= ~BIT1; // Clear P1.0 output latch for a defined power-on state
    P1DIR |= BIT1;  // Set P1.0 to output direction

    P5OUT &= ~BIT3; // Clear P1.0 output latch for a defined power-on state
    P5DIR |= BIT3;  // Set P1.0 to output direction
    // LEDs
    P1DIR |= BIT0 | BIT1;
    P1OUT &= ~(BIT0 | BIT1); // turn off LEDs
    // indicator pins
    P4DIR |= BIT1;
    P4OUT &= ~BIT1;
    P4DIR |= BIT2;
    P4OUT &= ~BIT2;
    P4DIR |= BIT3;
    P4OUT &= ~BIT3;
    P4DIR |= BIT4;
    P4OUT &= ~BIT4;
    P1DIR |= BIT3;
    P1OUT &= ~BIT3;
    // Configure UART
    P6SEL1 &= ~(BIT0 | BIT1); // USCI_A3 UART operation
    P6SEL0 |= BIT0 | BIT1;

    // Configure PJ.5 PJ.4 for external crystal oscillator
    PJSEL0 |= BIT4 | BIT5; // For XT1

    // Disable the GPIO power-on default high-impedance mode to activate
    // previously configured port settings
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

// generate random integers comply by the geomteric distribution
// 5: 0.835; 120:0.127; 500: 0.044
int geometricRandom(double p)
{
    if (p <= 0 || p > 1)
    {
        exit(EXIT_FAILURE);
    }
    // Generate a random value between 0 and 1(
    double u = (double)rand() / RAND_MAX;
    // Calculate the number of trials until the first success
    int k = (int)ceil(log(1 - u) / log(1 - p));
    return k;
}
// Function to generate random integers within a specified range [min, max]
int generateRandomInt(int min, int max)
{
    return (rand() % (max - min + 1)) + min;
}
// Function to generate integer random numbers from an exponential distribution
int exponentialRand(double lambda, int min, int max)
{
    double u = (double)rand() / RAND_MAX;
    double expo_value = -log(1.0 - u) / lambda;
    return (int)fmax(fmin(expo_value, max), min); // Ensure generated integer is within [min, max]
}
// Function to generate integer random numbers from a Gaussian (Normal) distribution
int gaussianRand(int mu, int sigma, int min, int max)
{
    double u1 = (double)rand() / RAND_MAX;
    double u2 = (double)rand() / RAND_MAX;
    double z = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2);
    double gaussian_value = mu + sigma * z;
    return (int)fmax(fmin(gaussian_value, max), min); // Ensure generated integer is within [min, max]
}
// Function to generate integer random numbers from a Gaussian mixture distribution
int gaussianMixtureRand(int num_components, int mu[], int sigma[], double weights[], int min, int max)
{
    double u = (double)rand() / RAND_MAX;
    int component = 0;
    while (u > weights[component])
    {
        u -= weights[component];
        component++;
    }
    double u1 = (double)rand() / RAND_MAX;
    double u2 = (double)rand() / RAND_MAX;
    double z = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2);
    double mixture_value = mu[component] + sigma[component] * z;
    return (int)fmax(fmin(mixture_value, max), min); // Ensure generated integer is within [min, max]
}
// Set energy models
int set_energyModel()
{
    int retValue = 0;
    if (g_energyMode == energy_office_01)
    {
        if (g_office1_index == g_office1_length)
        {
            g_office1_index = generateRandomInt(0,g_office1_length);
        }
        retValue = office_1[g_office1_index];
        g_office1_index = g_office1_index + 1;
    }
    else if (g_energyMode == energy_office_02)
    {
        if (g_office2_index == g_office2_length)
        {
             g_office2_index = generateRandomInt(0,g_office2_length);
        }
        retValue = office_2[g_office2_index];
        g_office2_index = g_office2_index + 1;
    }
    else if (g_energyMode == energy_stairs_01)
    {
        if (g_stairs1_index == g_stairs1_length)
        {
            g_stairs1_index = 0;
        }
        retValue = stairs_1[g_stairs1_index];
        g_stairs1_index = g_stairs1_index + 1;
    }
    else
    {
        if (g_stairs2_index == g_stairs2_length)
        {
            g_stairs2_index = 0;
        }
        retValue = stairs_2[g_stairs2_index];
        g_stairs2_index = g_stairs2_index + 1;
    }
    return retValue;
}

uint16_t combineBytes2(char arr[])
{
    return ((uint16_t)arr[0] << 8) | arr[1];
}



static void uartTransmit(uint16_t num)
{
    int index = 0;
    int var = 1;
    for (; var >= 0; var--)
    {
        char tempVar = (num >> (var * 8)) & 0xff;
        g_uartTrasBuff[index] = tempVar;
        index = index + 1;
    }
    int16_t g_crcCode = getCRC(g_uartTrasBuff);
    var = 1;
    for (; var >= 0; var--)
    {
        char tempVar = (g_crcCode >> (var * 8)) & 0xff;
        g_uartTrasBuff[index] = tempVar;
        index = index + 1;
    }
    UCA3IE |= UCTXIE; // Enable USCI_A3 TX interrupt;
    __no_operation();
}

static void uartAction()
{
    char reDataUart[2];
    reDataUart[0] = g_uartRecvBuff[0];
    reDataUart[1] = g_uartRecvBuff[1];
    g_reUartData = combineBytes2(reDataUart);
    if (g_reUartData != 0xafff)
    {
        __no_operation();
    }
    char transBuff[2];
    int index = 0;
    int var = 1;
    for (; var >= 0; var--)
    {
        transBuff[index] = (g_reUartData >> (var * 8)) & 0xff;
        index = index + 1;
    }
    g_crcCode = getCRC(transBuff);
    __no_operation();
    reDataUart[0] = g_uartRecvBuff[2];
    reDataUart[1] = g_uartRecvBuff[3];
    int16_t crcReceived = combineBytes2(reDataUart);
    if (crcReceived != g_crcCode)
    {
        __no_operation();
        return;
    }
    __no_operation();

    if (g_reUartData == lastReceivedData)
    {
        __no_operation();
        return;
    }
    if (g_uartTerminalFlag == true)
    {
        __no_operation();
        return;
    }
    if (g_reUartData >= 0xafff)
    {
        lastReceivedData = g_reUartData;
        g_reUartData = g_reUartData - 0xafff;
        if (g_synIndex < MAX_ENCOUNTER_THRESHOLD)
        {
            //g_synIndex = g_synIndex + 1;
            g_synIndex = g_reUartData;
        }
        else
        {
            __no_operation();
        }
        __no_operation();
    }
    else
    {
        if (g_extraDelayCounter == 0)
        {
            g_extraDelayCounter = g_reUartData * SLOT_AMPLIFIER;
        }
        lastReceivedData = g_reUartData;
        g_uartTerminalFlag = true;
    }
}


static void uartReceive()
{
    UCA3IE |= UCRXIE; // Enable USCI_A3 RX interrupt
    __bis_SR_register(GIE);
    while (g_reCounter < 4)
    {
    }
    g_reCounter = 0;
    uartAction();
}


static void mosfetSwitch()
{
    P1OUT ^= BIT2;
    P6SEL0 ^= BIT0;
}

int main(void)
{
    WDTCTL = WDTPW | WDTHOLD; // stop watchdog
    // configure uart
    setTimer();
    initGPIO();
    crcInit();
    chargeCycles = set_energyModel();
    g_slotUnitCounter = (chargeCycles + 1) * SLOT_AMPLIFIER;
    //***************************************
    TA0CCTL0 = CCIE; // TACCR0 interrupt enabled
    TA0CCR0 = 0;
    TA0CTL = TASSEL__SMCLK | MC__CONTINOUS; // SMCLK, continuous mode
    __bis_SR_register(GIE); // enable interruption
    initUART();
    P6SEL0 ^= BIT0; // for controlling mosfet
    while (true) // Starting energy condition emulation
    {
        if (g_slotUnitCounter == 0)
        {
            // Calculate the charging time in next round.
            mosfetSwitch();
            __no_operation();
            g_preventRepeatedUart = true;
            g_uartTerminalFlag = false;
            lastReceivedData = 0;
            chargeCycles = set_energyModel();
            P4OUT ^= BIT1;
            g_slotUnitCounter = (chargeCycles + 1) * SLOT_AMPLIFIER;
            if (g_powerOff == true)
            {
                int prob = generateRandomInt(1, 100);
                if (prob <= 10) // power off with 10% probability
                {
                    g_slotUnitCounter = g_slotUnitCounter + SLOT_AMPLIFIER * generateRandomInt(0, 30);
                }
            }
        }
        else if ((g_afterUartWork == true) && (g_extraDelayCounter == 0))
        {
            // Do delay operations if the node received the feedback from the main board.
            g_afterUartWork = false;
            mosfetSwitch(); // turn on switch again after delay
            __no_operation();
            /*
             * Initailing uart time do not be regarded
             * as the charging cycle of an IC node
             */
            __delay_cycles(INITIAL_UART_TIME);
            uartTransmit(0xffff);
            __no_operation();
            __bis_SR_register(GIE);
        }
        else if ((g_slotUnitCounter == SLOT_AMPLIFIER) && (g_preventRepeatedUart == true))
        {
            P4OUT ^= BIT1;
            __no_operation();
            mosfetSwitch(); // Turn the switch
            g_preventRepeatedUart = false;

            // do not consider the the uart time as the part of the working slot
            g_extraDelayIndicator = false;
            __delay_cycles(INITIAL_UART_TIME);
            uartTransmit(chargeCycles);
            uartReceive();
            uartReceive();
            __bis_SR_register(GIE);

            if (g_extraDelayCounter > 0)
            {
                g_afterUartWork = true;
                mosfetSwitch(); // turn off switch for delaying some time
                g_extraDelayIndicator = true;
                __no_operation();
            }
            __no_operation();
        }
    }
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
    TA0CCR0 += COUNTER_UNIT; // Add Offset to TA0CCR0
    if ((g_slotUnitCounter > 0) && (g_extraDelayCounter == 0))
    {
        g_slotUnitCounter--;
    }
    if ((g_extraDelayCounter > 0) && (g_extraDelayIndicator == true))
    {
        g_extraDelayCounter--;
    }
    TA0CCR0 = 0;
}

// UART processsing
#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector = EUSCI_A3_VECTOR
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
        if (g_reCounter < 4)
        {
            g_uartRecvBuff[g_reCounter] = UCA3RXBUF;
            g_reCounter += 1;
        }
        if (g_reCounter == 4)
        {
            UCA3IE &= ~UCRXIE;
            __bic_SR_register_on_exit(GIE);
        }
        break;
    case USCI_UART_UCTXIFG:;
        int var = 0;
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
