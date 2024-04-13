#include <msp430.h>
#include "uartHex.h"
#include "crc.h"



void transHexBytes(int32_t num)
{
    int8_t i = 1;
    char  temp[4];
    char  transBuff[3];
    int8_t index = 0;
    transBuff[index] = 0xff;
    index = index + 1;
    for (; i >= 0; i--)
    {
//        while (!(UCA3IFG & UCTXIFG))
//            ;
//        UCA3TXBUF  = (num >> (i * 8)) & 0xff;
        transBuff[index] = (num >> (i * 8)) & 0xff;
        index = index + 1;
       // temp[1 -i] = (num >> (i * 8)) & 0xff;
    }
//     i = 1;
//     for (; i >= 0; i--)
//     {
// //        while (!(UCA3IFG & UCTXIFG))
// //            ;
// //        UCA3TXBUF = (crcFast(temp, 4) >> (i * 8)) & 0xff;
//         transBuff[index] = (crcFast(temp, 4) >> (i * 8)) & 0xff;
//         index = index + 1;
//     }
    i = 0;
    for (; i< 3; i++)
    {
        while (!(UCA3IFG & UCTXIFG));
        UCA3TXBUF  = transBuff[i];
        // __delay_cycles(15000000);
        __no_operation();
    }
    __no_operation();
}

int32_t combineBytes(char arr[])
{
    return ((int32_t)arr[0] << 24) | ((int32_t)arr[1] << 16) | ((int32_t)arr[2] << 8) | arr[3];
}

int16_t combineBytes2(char arr[])
{
    return  ((int16_t)arr[0] << 8) | arr[1];
}
