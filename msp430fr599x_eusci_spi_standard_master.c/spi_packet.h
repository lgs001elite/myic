#ifndef _SPI_PACKET_H_
#define _SPI_PACKET_H_

#include <stdint.h>

typedef struct spi_datagram {
    uint8_t hp_len;
    uint8_t t_broad_type;
    uint8_t seq;                      
    uint8_t status;                
    uint8_t src              : 4,
            dst              : 4;
    uint8_t layer            : 3,
            p_len            : 5;     
    uint8_t df[23];
    uint8_t crc[2];
} SPI_DATAGRAM;

#define SPI_DATA_LEN   0x21 /*  33: for SPI transport */

#endif
