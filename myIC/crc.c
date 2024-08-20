#include "crc.h"
#include "global_vars.h"
#define WIDTH (8 * sizeof(crc))
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
#define REFLECT_REMAINDER(X) ((crc)reflect((X), WIDTH))
#else
#undef REFLECT_REMAINDER
#define REFLECT_REMAINDER(X) (X)
#endif



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

crc crcTable[256];
void crcInit(void)
{
    crc remainder;
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

crc crcFast(char const message[], int nBytes)
{
    crc remainder = INITIAL_REMAINDER;
    char data;
    int byte;

    for (byte = 0; byte < nBytes; ++byte)
    {
        data = REFLECT_DATA(message[byte]) ^ (remainder >> (WIDTH - 8));
        remainder = crcTable[data] ^ (remainder << 8);
    }

    return (REFLECT_REMAINDER(remainder) ^ FINAL_XOR_VALUE);
}

int16_t getCRC(char const message[])
{
    int16_t crc_result = crcFast(message, 29);
    return crc_result;
}

int16_t getUartCRC(char const message[])
{
    int16_t crc_result = crcFast(message, 2);
    return crc_result;
}

void update_crc()
{
    char crc_input[29];
    char i = 0;
    for (; i < 29; i++)
    {
        crc_input[i] = g_transBuffer[i];
    }

    int16_t crc_result = getCRC(crc_input);
    g_transBuffer[29] = (crc_result & 0xFF00) >> 8;
    g_transBuffer[30] = (crc_result & 0x00FF);
    while (g_transBuffer[29] >= 0x7f)
    {
        g_transBuffer[29] -= 0x7f;
    }
    while (g_transBuffer[30] >= 0x7f)
    {
        g_transBuffer[30] -= 0x7f;
    }
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






