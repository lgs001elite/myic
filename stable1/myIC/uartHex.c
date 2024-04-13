#include <msp430.h>
#include <stdio.h>
#include "uartHex.h"
#include "crc.h"




void transHexBytes(uint16_t num)
{
    char transBuff[2];
    int index = 0;
    int var = 1;
    for (; var >= 0; var--)
    {
        transBuff[index] = (num >> (var * 8)) & 0xff;
        index = index + 1;
    }
    //Start to transmit
    var = 0;
    for (; var < 2; var++)
    {
        while (!(UCA3IFG & UCTXIFG));
        UCA3TXBUF = transBuff[var];
        __delay_cycles(10000);
        __no_operation();
    }
}

int32_t combineBytes(char arr[])
{
    return ((int32_t)arr[0] << 24) | ((int32_t)arr[1] << 16) | ((int32_t)arr[2] << 8) | arr[3];
}

int16_t combineBytes2(char arr[])
{
    return  ((int16_t)arr[0] << 8) | arr[1];
}
