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
    uint8_t df[25];
} SPI_DATAGRAM;

volatile extern uint8_t front_check_arr[3];
volatile extern uint8_t rear_check_arr[3];

#define SPI_DATA_LEN   0x27 /*  39: for SPI transport */
#define SPI_HEADER_LEN 0x0E /*  14: header + checknum: 8 + 6 */

//#define HEADER_LEN     12 /*  12 = 6 + 6 */

//#define PAYLOAD_LEN    33


#endif
