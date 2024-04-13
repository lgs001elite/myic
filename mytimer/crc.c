#include "crc.h"
#define WIDTH (8 * sizeof(int16_t))
#define TOPBIT (1 << (WIDTH - 1))

#if (REFLECT_DATA == TRUE)
/*
 * crc.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */


#undef REFLECT_DATA
#define REFLECT_DATA(X) (( char)reflect((X), 8))
#else
#undef REFLECT_DATA
#define REFLECT_DATA(X) (X)
#endif

#if (REFLECT_REMAINDER == TRUE)
#undef REFLECT_REMAINDER
#define REFLECT_REMAINDER(X) ((int16_t)reflect((X), WIDTH))
#else
#undef REFLECT_REMAINDER
#define REFLECT_REMAINDER(X) (X)
#endif

// in crc
#pragma PERSISTENT(g_chargHis)
int g_chargHis[HISLEN] = {0};

// in crc
#pragma PERSISTENT(g_locNum)
char g_locNum = 0;

static  long reflect( long data,  char nBits)
{
    long reflection = 0x00000000;
    char bit;
    for (bit = 0; bit < nBits; ++bit)
    {
        if (data & 0x01)
        {
            reflection |= (1 << ((nBits - 1) - bit));
        }

        data = (data >> 1);
    }

    return (reflection);
}

int16_t crcTable[256];
void crcInit(void)
{
    int16_t remainder;
    int dividend;
    char bit;
    for (dividend = 0; dividend < 256; ++dividend)
    {
        /*
         * Start with the dividend followed by zeros.
         */
        remainder = dividend << (WIDTH - 8);

        /*
         * Perform modulo-2 division, a bit at a time.
         */
        for (bit = 8; bit > 0; --bit)
        {
            /*
             * Try to divide the current data bit.
             */
            if (remainder & TOPBIT)
            {
                remainder = (remainder << 1) ^ POLYNOMIAL;
            }
            else
            {
                remainder = (remainder << 1);
            }
        }
        crcTable[dividend] = remainder;
    }
}

int16_t crcFast( char const message[], int nBytes)
{
    int16_t remainder = INITIAL_REMAINDER;
    char data;
    int byte;

    for (byte = 0; byte < nBytes; ++byte)
    {
        data = REFLECT_DATA(message[byte]) ^ (remainder >> (WIDTH - 8));
        remainder = crcTable[data] ^ (remainder << 8);
    }
    remainder = (REFLECT_REMAINDER(remainder) ^ FINAL_XOR_VALUE);
    __no_operation();
    return remainder;
}

int16_t getCRC( char const message[])
{
    crcInit();
    int16_t crc_result = crcFast(message, 31);
    return crc_result;
}


int findMax( int arr[], char n)
{
    if (n <= 0)
    {
        return -1;
    }
    int max = arr[0];
    int i = 1;
    for (; i < n; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    return max;
}

float findMaxRate( int arr[], char n)
{
    if (n <= 1)
    {
        return -1;
    }

    float maxRate = 0;
    int i = 0;
    for (; i < (n - 1); i++)
    {
        float rate = arr[i + 1] / arr[i];
        if (rate > maxRate)
        {
            maxRate = rate;
        }
    }
    return maxRate;
}

void putInArray(int num)
{
    if (g_locNum >= HISLEN)
    {
        int i = 0;
        for (; i < (HISLEN - 1); i++)
        {
            g_chargHis[i] = g_chargHis[i + 1];
        }
        g_chargHis[HISLEN - 1] = num;
    }
    else
    {
        g_chargHis[g_locNum] = num;
        g_locNum = g_locNum + 1;
    }
}






