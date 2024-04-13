/*
 * random.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */
#include <stdint.h>
#include <stdbool.h>
#include "random.h"

int32_t g_pui32RandomEntropy[16];
int32_t g_ui32RandomSeed = 0;
void RandomAddEntropy(int32_t ui32Entropy)
{
    int32_t g_ui32RandomIndex = 0;
    ((char *)g_pui32RandomEntropy)[g_ui32RandomIndex] = ui32Entropy & 0xff;
    g_ui32RandomIndex = (g_ui32RandomIndex + 1) & 63;
}


void RandomSeed(void)
{
    int32_t ui32A, ui32B, ui32C, ui32D, ui32Temp, ui32Idx;
    ui32A = 0x67452301;
    ui32B = 0xefcdab89;
    ui32C = 0x98badcfe;
    ui32D = 0x10325476;

#define F(a, b, c, d, k, s)                                                  \
    {                                                                        \
        ui32Temp = a + (d ^ (b & (c ^ d))) + g_pui32RandomEntropy[k];        \
        a = (ui32Temp << s) | (ui32Temp >> (32 - s));                        \
    }
    for(ui32Idx = 0; ui32Idx < 16; ui32Idx += 4)
    {
        F(ui32A, ui32B, ui32C, ui32D, ui32Idx + 0, 3);
        F(ui32D, ui32A, ui32B, ui32C, ui32Idx + 1, 7);
        F(ui32C, ui32D, ui32A, ui32B, ui32Idx + 2, 11);
        F(ui32B, ui32C, ui32D, ui32A, ui32Idx + 3, 19);
    }

#define G(a, b, c, d, k, s)                                                  \
    {                                                                        \
        ui32Temp = a + ((b & c) | (b & d) | (c & d)) +                       \
                g_pui32RandomEntropy[k] +   0x5a827999;                   \
        a = (ui32Temp << s) | (ui32Temp >> (32 - s));                        \
    }
    for(ui32Idx = 0; ui32Idx < 4; ui32Idx++)
    {
        G(ui32A, ui32B, ui32C, ui32D, ui32Idx + 0, 3);
        G(ui32D, ui32A, ui32B, ui32C, ui32Idx + 4, 5);
        G(ui32C, ui32D, ui32A, ui32B, ui32Idx + 8, 9);
        G(ui32B, ui32C, ui32D, ui32A, ui32Idx + 12, 13);
    }

#define H(a, b, c, d, k, s)                                                  \
    {                                                                        \
        ui32Temp = a + (b ^ c ^ d) + g_pui32RandomEntropy[k] + 0x6ed9eba1;   \
        a = (ui32Temp << s) | (ui32Temp >> (32 - s));                        \
    }
    for(ui32Idx = 0; ui32Idx < 4; ui32Idx += 2)
    {
        H(ui32A, ui32B, ui32C, ui32D, ui32Idx + 0, 3);
        H(ui32D, ui32A, ui32B, ui32C, ui32Idx + 8, 9);
        H(ui32C, ui32D, ui32A, ui32B, ui32Idx + 4, 11);
        H(ui32B, ui32C, ui32D, ui32A, ui32Idx + 12, 15);

        if(ui32Idx == 2)
        {
            ui32Idx -= 3;
        }
    }
    g_ui32RandomSeed = ui32A + 0x67452301;
}


int32_t genRanNumb(void)
{
    g_ui32RandomSeed = (g_ui32RandomSeed * 1664525) + 1013904223;
    return(g_ui32RandomSeed);
}

