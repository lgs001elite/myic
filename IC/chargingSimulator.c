// #include <msp430.h>
// #include <stdint.h>
// #include <math.h>
// #include <stdio.h>
// #include <stdlib.h>
// #define INSTANT 0
// #define RANDOM 1
// #define EXPON 2
// #define GUASS 3
// #define GAUSSMIX 4
// #define GEOMATRIX 5
// #define DELAYUNIT 0xffff
// #define AMPLIFER 15
// unsigned int amplifier = AMPLIFER;
// unsigned int skipSignal = 0;
// unsigned char activeFinSig = 0;
// unsigned char RXData = 0;
// unsigned char TXData = 0x01;
// unsigned int switchUart = 0;
// unsigned int delayCycles = 0;
// // generate random integers comply by the geomteric distribution
// // 5: 0.835; 120:0.127; 500: 0.044
// int geometricRandom(double p)
// {
//     if (p <= 0 || p > 1)
//     {
//         exit(EXIT_FAILURE);
//     }
//     // Generate a random value between 0 and 1(
//     double u = (double)rand() / RAND_MAX;
//     // Calculate the number of trials until the first success
//     int k = (int)ceil(log(1 - u) / log(1 - p));
//     return k;
// }
// // Function to generate random integers within a specified range [min, max]
// int generateRandomInt(int min, int max)
// {
//     return (rand() % (max - min + 1)) + min;
// }
// // Function to generate integer random numbers from an exponential distribution
// int exponentialRand(double lambda, int min, int max)
// {
//     double u = (double)rand() / RAND_MAX;
//     double expo_value = -log(1.0 - u) / lambda;
//     return (int)fmax(fmin(expo_value, max), min); // Ensure generated integer is within [min, max]
// }
// // Function to generate integer random numbers from a Gaussian (Normal) distribution
// int gaussianRand(int mu, int sigma, int min, int max)
// {
//     double u1 = (double)rand() / RAND_MAX;
//     double u2 = (double)rand() / RAND_MAX;
//     double z = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2);
//     double gaussian_value = mu + sigma * z;
//     return (int)fmax(fmin(gaussian_value, max), min); // Ensure generated integer is within [min, max]
// }
// // Function to generate integer random numbers from a Gaussian mixture distribution
// int gaussianMixtureRand(int num_components, int mu[], int sigma[], double weights[], int min, int max)
// {
//     double u = (double)rand() / RAND_MAX;
//     int component = 0;
//     while (u > weights[component])
//     {
//         u -= weights[component];
//         component++;
//     }
//     double u1 = (double)rand() / RAND_MAX;
//     double u2 = (double)rand() / RAND_MAX;
//     double z = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2);
//     double mixture_value = mu[component] + sigma[component] * z;
//     return (int)fmax(fmin(mixture_value, max), min); // Ensure generated integer is within [min, max]
// }
// // Call this function when delayCycles does not equal zero.
// void setDelay()
// {
//     delayCycles = delayCycles + RXData;
// }
// // Set energy models
// int setEnergyModel(int energyModel)
// {
//     // Set parameters for each distribution
//     double lambda = 0.1;              // For exponential distribution
//     int mu = 50;                      // Mean of Gaussian distribution
//     int sigma = 10;                   // Standard deviation of Gaussian distribution
//     int num_components = 2;           // Number of Gaussian components in the mixture
//     int mu_components[] = {30, 70};   // Mean of each component in the mixture
//     int sigma_components[] = {5, 10}; // Standard deviation of each component in the mixture
//     double weights[] = {0.6, 0.4};    // Weights of each component in the mixture (should sum to 1)
//     int min = 1;                      // Minimum value of the range
//     int max = 100;                    // Maximum value of the range
//     switch (energyModel)
//     {
//     case INSTANT:
//         return 5;
//         break;
//     case RANDOM:
//         return (generateRandomInt(min, max));
//         break;
//     case EXPON:
//         return (exponentialRand(lambda, min, max));
//         break;
//     case GUASS:
//         return (gaussianRand(mu, sigma, min, max));
//         break;
//     case GAUSSMIX:
//         return (gaussianMixtureRand(num_components, mu_components, sigma_components, weights, min, max));
//         break;
//     case GEOMATRIX:
//         return geometricRandom(0.835);
//         break;
//     default:
//         return 0;
//         break;
//     }
// }
// void uartTrans()
// {
//     while (!(UCA3IFG & UCTXIFG))
//         ;
//     UCA3TXBUF = 0x56;
// }
// void uartTimer()
// {
//     CSCTL0_H = CSKEY_H; // Unlock CS registers
//     CSCTL1 = DCOFSEL_0; // Set DCO to 1MHz
//     CSCTL2 = SELA__LFXTCLK | SELS__DCOCLK | SELM__DCOCLK;
//     CSCTL3 = DIVA__1 | DIVS__1 | DIVM__1; // Set all dividers
//     CSCTL4 &= ~LFXTOFF;                   // Enable LFXT1
//     do
//     {
//         CSCTL5 &= ~LFXTOFFG; // Clear XT1 fault flag
//         SFRIFG1 &= ~OFIFG;
//     } while (SFRIFG1 & OFIFG); // Test oscillator fault flag
//     CSCTL0_H = 0;              // Lock CS registers
// }
// void configUart()
// {
//     UCA3CTLW0 |= UCSWRST;
//     UCA3CTLW0 |= UCSSEL__ACLK; // Set ACLK = 32768 as UCBRCLK
//     UCA3BRW = 3;               // 9600 baud
//     UCA3MCTLW |= 0x5300;       // 32768/9600 - INT(32768/9600)=0.41
//                                // UCBRSx value = 0x53 (See UG)
//     UCA3CTLW0 &= ~UCSWRST;     // release from reset
//     UCA3IE |= UCRXIE;          // Enable USCI_A3 RX interrupt
// }
// int main(void)
// {
//     WDTCTL = WDTPW | WDTHOLD; // stop watchdog
//     P1OUT &= ~BIT2;           // Clear P1.0 output latch for a defined power-on state
//     P1DIR |= BIT2;            // Set P1.0 to output direction
//     P1OUT &= ~BIT0;           // Clear P1.0 output latch for a defined power-on state
//     P1DIR |= BIT0;            // Set P1.0 to output direction
//     P1OUT &= ~BIT1;           // Clear P1.0 output latch for a defined power-on state
//     P1DIR |= BIT1;            // Set P1.0 to output direction
//     // Configure GPIO
//     P6SEL1 &= ~(BIT0 | BIT1);
//     P6SEL0 |= (BIT0 | BIT1); // USCI_A3 UART operation
//     PJSEL0 |= BIT4 | BIT5;   // Configure XT1 pins
//     PM5CTL0 &= ~LOCKLPM5;
//     P6SEL0 ^= BIT0;
//     uartTimer();
//     configUart();
//     //***************************************
//     TA0CCTL0 = CCIE; // TACCR0 interrupt enabled
//     TA0CCR0 = DELAYUNIT;
//     TA0CTL = TASSEL__SMCLK | MC__CONTINOUS; // SMCLK, continuous mode
//     __bis_SR_register(GIE);                 // interrupt
//     //***************************************
//     srand(12);
//     delayCycles = setEnergyModel(INSTANT) + generateRandomInt(0, 5);
//     __no_operation();
// }
// // Timer0_A0 interrupt service routine
// #if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
// #pragma vector = TIMER0_A0_VECTOR
// __interrupt void Timer0_A0_ISR(void)
// #elif defined(__GNUC__)
// void __attribute__((interrupt(TIMER0_A0_VECTOR))) Timer0_A0_ISR(void)
// #else
// #error Compiler not supported!
// #endif
// {
//     TA0CCR0 += DELAYUNIT; // Add Offset to TA0CCR0
//                           //    if (RXData != 0)
//                           //    {
//                           //        setDelay();
//                           //        RXData = 0;
//                           //    }
//     if (delayCycles)
//     {
//         if (amplifier == 0)
//         {
//             delayCycles--;
//             amplifier = AMPLIFER;
//             if (activeFinSig == 1)
//             {
//                 P1OUT ^= BIT2;
//                 activeFinSig = 0;
//                 delayCycles = setEnergyModel(INSTANT);
//                 skipSignal = 0;
//                 switchUart = 0;
//                 P6SEL0 ^= BIT0;
//             }
//         }
//         if ((delayCycles == 1) && (amplifier == AMPLIFER))
//         {
//             P1OUT ^= BIT2;
//             P6SEL0 ^= BIT0;
//             activeFinSig = 1;
//         }
//         if (delayCycles == 1)
//         {
//             uartTrans();
//             __bis_SR_register(GIE);
//         }
//         amplifier--;
//     }
// }
// #if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
// #pragma vector = EUSCI_A3_VECTOR // eUSCI ISR
// __interrupt void USCI_A3_ISR(void)
// #elif defined(__GNUC__)
// void __attribute__((interrupt(EUSCI_A3_VECTOR))) USCI_A3_ISR(void)
// #else
// #error Compiler not supported!
// #endif
// {
//     switch (__even_in_range(UCA3IV, USCI_UART_UCTXCPTIFG))
//     {
//     case USCI_NONE:
//         break;
//     case USCI_UART_UCRXIFG:
//         RXData = UCA3RXBUF;
//         __no_operation();
//         if ((RXData == 0x56) && (delayCycles == 1) && (skipSignal == 0))
//         {
//             P1OUT ^= BIT0;
//             P1OUT ^= BIT1;
//             P6SEL0 ^= BIT0;
//             activeFinSig = 0;
//             switchUart = 0;
//             P1OUT ^= BIT2;
//             skipSignal = 1;
//             delayCycles = delayCycles + 1;
//             // delayCycles = delayCycles + geometricRandom();
//         }
//         break;
//     case USCI_UART_UCTXIFG:
//         break;
//     case USCI_UART_UCSTTIFG:
//         break;
//     case USCI_UART_UCTXCPTIFG:
//         break;
//     default:
//         break;
//     }
// }