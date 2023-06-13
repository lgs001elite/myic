#ifndef _SPIS_DATA_H_
#define _SPIS_DATA_H_
#include <stdio.h>
#include <stdint.h>


typedef struct Rec_data{
    uint8_t * rx_data_buf;
    uint32_t  rx_data_len;
} rec_data;

typedef struct Sen_data{
    uint8_t * tx_data_buf;
    uint32_t  tx_data_len;

} sen_data;


void spis_setfrom_slave(uint8_t * tx_data_buf, uint32_t  tx_data_len);
sen_data spis_getfrom_slave();
#endif
