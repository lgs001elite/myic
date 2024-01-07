#include <msp430.h>
#include "uartHex.h"
#include "crc.h"



void transHexBytes(int32_t num)
{
    int32_t i = 3;
    char  temp[4];
    for (; i >= 0; i--)
    {
        while (!(UCA3IFG & UCTXIFG))
            ;
        UCA3TXBUF  = (num >> (i * 8)) & 0xff;
        temp[3 -i] = (num >> (i * 8)) & 0xff;
    }
    i = 1;
    for (; i >= 0; i--)
    {
        while (!(UCA3IFG & UCTXIFG))
            ;
        UCA3TXBUF = (crcFast(temp, 4) >> (i * 8)) & 0xff;
    }
    __no_operation();
}

int32_t combineBytes(char arr[])
{
    return ((int32_t)arr[0] << 24) | ((int32_t)arr[1] << 16) | ((int32_t)arr[2] << 8) | arr[3];
}

int16_t combineBytes2(char arr[])
{
    return  ((int16_t)arr[4] << 8) | arr[5];
}
