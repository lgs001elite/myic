#include <msp430.h>
#include <stdio.h>
#include "uartHex.h"
#include "crc.h"
#include "pins.h"

uint16_t combineBytes2(char arr[])
{
    return  ((uint16_t)arr[0] << 8) | arr[1];
}

