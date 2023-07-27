// #include <msp430.h>
// volatile unsigned char RXData = 0;
// volatile unsigned char TXData = 1;
// volatile unsigned int switchUart = 1;
// volatile unsigned int delayCycles = 0;
// volatile unsigned int anchorCycles = 10;
// #define DELAYUNIT 50000
// // Call this function when delayCycles does not equal zero.
// void setDelay()
// {
//     delayCycles = delayCycles + RXData - 1; // Subtract the current slot
// }
// // Call this functions when delayCycles equals zero.
// void setChargeTrace()
// {
//     // delayCycles = ? ; // according to specific trace functions and change anchorCycles values.
// }
// int main(void)
// {
//     WDTCTL = WDTPW | WDTHOLD; // stop watchdog
//     P1OUT &= ~BIT2;           // Clear P1.0 output latch for a defined power-on state
//     P1DIR |= BIT2;            // Set P1.0 to output direction
//     // Configure GPIO
//     P6SEL1 &= ~(BIT0 | BIT1);
//     P6SEL0 |= (BIT0 | BIT1); // USCI_A3 UART operation
//     PJSEL0 |= BIT4 | BIT5;   // Configure XT1 pins
//     PM5CTL0 &= ~LOCKLPM5;
//     // XT1 Setup
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
//     // Configure USCI_A3 for UART mode
//     UCA3CTLW0 |= UCSWRST;
//     UCA3CTLW0 |= UCSSEL__ACLK; // Set ACLK = 32768 as UCBRCLK
//     UCA3BRW = 3;               // 9600 baud
//     UCA3MCTLW |= 0x5300;       // 32768/9600 - INT(32768/9600)=0.41
//                                // UCBRSx value = 0x53 (See UG)
//     UCA3CTLW0 &= ~UCSWRST;     // release from reset
//     UCA3IE |= UCRXIE;          // Enable USCI_A3 RX interrupt
//     //***************************************
//     TA0CCTL0 = CCIE; // TACCR0 interrupt enabled
//     TA0CCR0 = DELAYUNIT;
//     TA0CTL = TASSEL__SMCLK | MC__CONTINOUS; // SMCLK, continuous mode
//     __bis_SR_register(GIE);                 // interrupt
//     //***************************************
//     P1OUT ^= BIT2;
//     delayCycles = anchorCycles;
//     while (1)
//     {
//         while (switchUart)
//         {
//             while (!(UCA3IFG & UCTXIFG))
//                 ;
//             UCA3TXBUF = TXData;
//             __bis_SR_register(GIE);
//             switchUart = 0;
//         }
//         __bis_SR_register(GIE);
//         __no_operation();
//     }
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
//     if (RXData != 0)
//     {
//         setDelay();
//         RXData = 0;
//     }
//     if (delayCycles)
//     {
//         delayCycles--;
//         if (delayCycles == 0)
//         {
//             delayCycles = anchorCycles;
//             P1OUT ^= BIT2;
//         }
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
//         switchUart = 1;
//         __bic_SR_register_on_exit(GIE);
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