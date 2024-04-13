#include <msp430.h>
#include <stdint.h>
#include <stdbool.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "rand.h"
#include "crc.h"
#include "chargingSets.h"

#define COORDINATOR 0
#define RANDOM 1
#define EXPON 2
#define GAUSS 3
#define GAUSSMIX 4
#define GEOMATRIX 5
#define STAIRS1 6
#define STAIRS2 7
#define TEST1 8
#define TEST2 9
#define STATIC 10
#define DELAYUNIT 0xffff

#define CAR_SIZE 6
#define JOG_SIZE 5
#define OFFICE_Size 5
#define STAIR_SIZE 6
#define WASHER_SIZE 5
#define MAX_LINE_LENGTH 124
// int32_t MAX_SUMILATION = 60000;
char RXData = 0x01;
char TXData = 0x01;
int32_t delayCycles = 0;
int32_t delayCells = 0;
int32_t g_amplifer = 30;
int8_t g_receCounter = 0;
int32_t g_synCounter = 0;
int32_t g_preReceive = 0;
int32_t lastData = -1;
char g_uartArr[2] = {0};
bool uartSwitch = true;
bool reWork;
bool signal_01 = true;
bool signal_02 = true;
bool signal_03 = true;
bool signal_04 = true;
int8_t uartTime = 5;
int8_t energyMode = STAIRS2; //  STAIRS1 COORDINATOR RANDOM EXPON  GAUSSMIX GEOMATRIX GAUSS STATIC

int32_t g_stairIndex = 0;
int32_t g_testIndex = 0;

#pragma PERSISTENT(g_systemCounter)
uint32_t g_systemCounter = 0;
uint32_t g_lastCounter = 0;
uint32_t g_synStatics[10] = {0};
int indexSyn = 0;

void initGPIO()
{

    P1OUT &= ~BIT2;           // Clear P1.0 output latch for a defined power-on state
    P1DIR |= BIT2;            // Set P1.0 to output direction
    P1OUT &= ~BIT0;           // Clear P1.0 output latch for a defined power-on state
    P1DIR |= BIT0;            // Set P1.0 to output direction
    P1OUT &= ~BIT1;           // Clear P1.0 output latch for a defined power-on state
    P1DIR |= BIT1;            // Set P1.0 to output direction

    P5OUT &= ~BIT3;           // Clear P1.0 output latch for a defined power-on state
    P5DIR |= BIT3;            // Set P1.0 to output direction
    // LEDs
    P1DIR |= BIT0 | BIT1;
    P1OUT &= ~(BIT0 | BIT1);         // turn off LEDs

    // Configure UART
    P6SEL1 &= ~(BIT0 | BIT1);                 // USCI_A3 UART operation
    P6SEL0 |= BIT0 | BIT1;

    // Configure PJ.5 PJ.4 for external crystal oscillator
    PJSEL0 |= BIT4 | BIT5;                    // For XT1

    // Disable the GPIO power-on default high-impedance mode to activate
    // previously configured port settings
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
int setEnergyModel(int energyModel)
{
    // Set parameters for each distribution
    double lambda = 0.1;              // For exponential distribution
    int mean = 10;                    // Mean of Gaussian distribution
    int stddev = 5;                   // Standard deviation of Gaussian distribution
    int min = 1;                      // Minimum value of the range
    int max = 30;                    // Maximum value of the range
    int num_components = 2;           // Number of Gaussian components in the mixture
    int mu_components[] = {30, 70};   // Mean of each component in the mixture
    int sigma_components[] = {5, 10}; // Standard deviation of each component in the mixture
    double weights[] = {0.6, 0.4};    // Weights of each component in the mixture (should sum to 1)
    GaussianComponent components[] = {
               {70.0, 10, 0.7}, // Component 1: mean, stddev, weight
               {30.0, 5,  0.3}  // Component 2: mean, stddev, weight
    };
    int n_components = 2;
    switch (energyModel)
    {
    case STATIC:
        return 30;
    case COORDINATOR:
        return  3;
    case RANDOM:
        return (generateRandomInt(min, max));
    case EXPON:
        return generate_exponential_int(min, max, lambda);
    case GAUSS:
        return generate_normal_positive_int(min, max, mean, stddev);
    case GAUSSMIX:
        return generate_gaussian_mixture_int(components, n_components, min, max);
    case GEOMATRIX:
        return exponentialRand(lambda, min, max);
    case STAIRS1:
        g_stairIndex += 1;
        if (g_stairIndex <= 2000)
        {

            return stairs1[g_stairIndex - 1];
        }
        else
        {
            g_stairIndex = 0;
            return stairs1[g_stairIndex];
        }
    case STAIRS2:
        g_stairIndex += 1;
        if (g_stairIndex <= 2000)
        {

            return stairs2[g_stairIndex - 1];
        }
        else
        {
            g_stairIndex = 0;
            return stairs2[g_stairIndex];
        }
//    case TEST1:
//        g_testIndex += 1;
//        int arrLen = sizeof(test1) / sizeof(test1[0]);
//        if (g_testIndex <= arrLen)
//        {
//
//            return test1[g_testIndex - 1];
//        }
//        else
//        {
//            g_testIndex = 0;
//            return test1[g_testIndex];
//        }
//    case TEST2:
//        g_testIndex += 1;
//        int arrLen2 = sizeof(test2) / sizeof(test2[0]);
//        if (g_testIndex <= arrLen2)
//        {
//
//            return test2[g_testIndex - 1];
//        }
//        else
//        {
//            g_testIndex = 0;
//            return test2[g_testIndex];
//        }
    default:
        return 0;
    }
}


int32_t combineBytes(char arr[])
{
    return ((int32_t)arr[0] << 24) | ((int32_t)arr[1] << 16) | ((int32_t)arr[2] << 8) | arr[3];
}


int16_t combineBytes2(char arr[])
{
    return ((int16_t)arr[0] << 8) | arr[1];
}


void sendBytes(int32_t num)
{
    int var = 1;
    char tempArr[4];
    char temp2[2];
    char transBuff[3];
    int index = 0;
    transBuff[index] =  0xff;
    index = index + 1;
    for (; var >= 0; var--)
    {
        transBuff[index] = (num >> (var * 8)) & 0xff;
        index = index + 1;
        tempArr[1 - var] = (num >> (var * 8)) & 0xff;
    }
    var = 0;
    __no_operation();
    for (; var < 3; var++)
    {
        while (!(UCA3IFG & UCTXIFG));
        UCA3TXBUF = transBuff[var];
        __no_operation();
    }
    __no_operation();
}


void uartAction()
{
    // uart
    if (g_receCounter == 2)
    {
        int16_t receData = combineBytes2(g_uartArr);
        if (receData == lastData)
        {
            return;
        }
        lastData = receData;
        if ((g_preReceive == 2110) && (2110 != receData))
        {
            if (receData != 1000)
            {
                if (receData > g_synCounter)
                {
                    g_synCounter = receData;
                    g_synStatics[indexSyn] = g_systemCounter - g_lastCounter;
                    g_lastCounter = g_systemCounter;
                    indexSyn = indexSyn + 1;
                }
            }
            __no_operation();
            return;
        }
        else if (receData == 2110)
        {
            g_preReceive = receData;
            __no_operation();
            int k = 0;
            while (k < 3)
            {
                k++;
                sendBytes(2000);
            }
            __no_operation();
        }
        else
        {
            if (reWork == false)
            {
                reWork = true;
                P6SEL0 ^= BIT0;
                P1OUT ^= BIT2;
                delayCells = receData + delayCells;
                if (delayCells < 25)
                {
                    delayCells = 25;
                }
            }
            __no_operation();
        }
        __no_operation();
    }
}


int main(void)
{
    WDTCTL = WDTPW | WDTHOLD; // stop watchdog
    reWork = false;
    // configure uart
    initGPIO();
    initClockTo16MHzUART();
    initUART();
    crcInit();
    P6SEL0 ^= BIT0;
    __no_operation();
    //***************************************
    srand(10);
    delayCycles =  setEnergyModel(energyMode);
    if (energyMode == STATIC)
    {
        delayCycles = delayCycles + generateRandomInt(0, 30);
    }
    delayCells  = (delayCycles + 1) * g_amplifer;
    //***************************************
    TA0CCTL0 = CCIE; // TACCR0 interrupt enabled
    TA0CCR0 = DELAYUNIT;
    TA0CTL = TASSEL__SMCLK | MC__CONTINOUS; // SMCLK, continuous mode
    __bis_SR_register(GIE);
    while(uartSwitch)
    {
        if ((delayCells == 0) && (signal_04 == true))
        {
            TA0CCR0 = DELAYUNIT;
            P6SEL0 ^= BIT0;
            signal_04 = false;
            signal_01 = true;
            signal_02 = true;
            signal_03 = true;
            __no_operation();
            P1OUT ^= BIT2;
            lastData = -1;
            g_preReceive = 0;
            delayCycles = setEnergyModel(energyMode);
            delayCells = (delayCycles + 1) * g_amplifer;
            signal_04 = true;
        }

        if (reWork == true)
        {
            P1OUT ^= BIT0;
            if ((delayCells == 20) && (energyMode != COORDINATOR)&& (signal_03 == true))
            {
                P6SEL0 ^= BIT0;
                signal_03 = false;
                __no_operation();
                P1OUT ^= BIT2;
                reWork = false;
                int32_t pre_delayCell_02 = delayCells - uartTime;
                while (delayCells >= pre_delayCell_02)
                {
                    __no_operation();
                }
                pre_delayCell_02 = 0;
                int j = 0;
                while (j < 3)
                {
                    sendBytes(1000);
                    j++;
                    __no_operation();
                }
                __no_operation();
                P1OUT ^= BIT1;
            }
        }
        else
        {
            if ((delayCells == g_amplifer) && (signal_01 == true))
            {
                P6SEL0 ^= BIT0;
                signal_01 = false;
                __no_operation();
                P1OUT ^= BIT2;
            }
            if ((delayCells == 25) && (energyMode != COORDINATOR) && (signal_02 == true))
            {
                int i = 0;
                signal_02 = false;
                while (i < 3)
                {
                    sendBytes(delayCycles);
                    i++;
                    __no_operation();
                }
                __no_operation();
            }
        }

        if (g_synCounter > 10)
        {
            uartSwitch = false;
            P1OUT ^= BIT0;
            P1OUT ^= BIT1;
            __no_operation();
            break;
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
    TA0CCR0 += DELAYUNIT; // Add Offset to TA0CCR0
    if (delayCells > 0)
    {
        delayCells--;
    }
    if (g_synCounter < 10)
    {
        g_systemCounter = g_systemCounter + 1;
    }
    else
    {
        __no_operation();
    }
}


// UART
#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector=USCI_A3_VECTOR
__interrupt void USCI_A3_ISR(void)
#elif defined(__GNUC__)
void __attribute__ ((interrupt(USCI_A3_VECTOR))) USCI_A3_ISR (void)
#else
#error Compiler not supported!
#endif
{
switch(__even_in_range(UCA3IV, USCI_UART_UCTXCPTIFG))
{
    case USCI_NONE: break;
    case USCI_UART_UCRXIFG:
        if (UCA3RXBUF == 0xff)
        {
            g_receCounter = 0;
            break;
        }
        g_uartArr[g_receCounter] = UCA3RXBUF;
        if (g_receCounter < 2)
        {
            g_receCounter = g_receCounter + 1;
        }
        if (g_receCounter == 2)
        {
            uartAction();
            g_receCounter = 0;
        }
        __no_operation();
        break;
    case USCI_UART_UCTXIFG: break;
    case USCI_UART_UCSTTIFG: break;
    case USCI_UART_UCTXCPTIFG: break;
}
}

