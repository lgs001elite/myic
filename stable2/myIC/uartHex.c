#include <msp430.h>
#include <stdio.h>
#include "uartHex.h"
#include "crc.h"
#include "pins.h"


void transUartBytes(uint16_t num)
{
    char transBuff[4]; 
    int index = 0;
    int var = 1;
    for (; var >= 0; var--)
    {
        transBuff[index] = (num >> (var * 8)) & 0xff;
        index = index + 1;
    }
    int16_t crc_temp = getUartCRC(transBuff);
    var = 1;
    for (; var >= 0; var--)
    {
        transBuff[index] = (crc_temp >> (var * 8)) & 0xff;
        index = index + 1;
    }
    // Start to transmit
    int re_trans = 0;
    GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN2;
    while (re_trans < 1)
    {
        re_trans++;
        var = 0;
        for (; var < 4; var++)
        {
            while (!(UCA3IFG & UCTXIFG));
            UCA3TXBUF = transBuff[var];
            GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
            __delay_cycles(100);
        }
        __no_operation();
    }
    GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN2;
    __no_operation();
}

int32_t combineBytes(char arr[])
{
    return ((int32_t)arr[0] << 24) | ((int32_t)arr[1] << 16) | ((int32_t)arr[2] << 8) | arr[3];
}

uint16_t combineBytes2(char arr[])
{
    return  ((uint16_t)arr[0] << 8) | arr[1];
}

