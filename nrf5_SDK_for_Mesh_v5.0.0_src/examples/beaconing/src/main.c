/* Copyright (c) 2010 - 2020, Nordic Semiconductor ASA
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this
 * list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form, except as embedded into a Nordic
 *    Semiconductor ASA integrated circuit in a product or a software update for
 *    such product, must reproduce the above copyright notice, this list of
 *    conditions and the following disclaimer in the documentation and/or other
 *    materials provided with the distribution.
 *
 * 3. Neither the name of Nordic Semiconductor ASA nor the names of its
 *    contributors may be used to endorse or promote products derived from this
 *    software without specific prior written permission.
 *
 * 4. This software, with or without modification, must only be used with a
 *    Nordic Semiconductor ASA integrated circuit.
 *
 * 5. Any software provided in binary form under this license must not be reverse
 *    engineered, decompiled, modified and/or disassembled.
 *
 * THIS SOFTWARE IS PROVIDED BY NORDIC SEMICONDUCTOR ASA "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL NORDIC SEMICONDUCTOR ASA OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 * GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
 * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */


#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "nrf_delay.h"
#include "nrf_gpio.h"
#include "ble.h"
#include "boards.h"
#include "simple_hal.h"
#include "nrf_mesh.h"
#include "log.h"
#include "nrf_log_ctrl.h"
#include "advertiser.h"
#include "mesh_app_utils.h"
#include "mesh_stack.h"
#include "ble_softdevice_support.h"
#include "mesh_provisionee.h"
#include "nrf_mesh_config_examples.h"
#include "app_timer.h"
#include "example_common.h"
#include "nrf_mesh_configure.h"
#include "ad_type_filter.h"
#include "define_broadcast_packet.h"
#include "config_adv_transmition.h"
#include "app_scheduler.h"
#include "spis.h"
#include "spis_data.h"
#include "m2s.h"
#include "crc.h"
#include "public.h"


#if defined(NRF51) && defined(NRF_MESH_STACK_DEPTH)
#include "stack_depth.h"
#endif

/*****************************************************************************
 * Definitions
 *****************************************************************************/
#define ADVERTISER_BUFFER_SIZE  (64)
bool              g_if_sendNext          = false;
advertiser_t      m_discovery_advertiser = {0};
uint8_t           m_adv_buffer_discovery[ADVERTISER_BUFFER_SIZE]; 
void              adv_init(void);
adv_packet_t  *   p_broad_packet         = NULL;

/**
 * @brief pass datagram to the bearer layer
 * @param p_adv: advertiser entity
 * @param adv_packet: datagram
 */
void send2bearer(advertiser_t * p_adv, define_adv_packet * adv_packet)
{
    p_broad_packet = advertiser_packet_alloc(p_adv, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
    if (p_broad_packet)
    {
        memcpy(p_broad_packet->packet.payload, adv_packet, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
        /* Repeat once */
        p_broad_packet->config.repeats = 1;
        advertiser_packet_send(p_adv, p_broad_packet);
    }
}

/**
 * @brief sending datagram
 * 
 */
void send_datagram_start()
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "********************* Adv --- starting *****************\n"); 
    send2bearer(&m_discovery_advertiser, m_recBuf);
}

/**
 * @brief receiving datagram from the bearer layer
 * @param p_rx_data: received datagram  
 */
void rx_cb(const nrf_mesh_adv_packet_rx_data_t * p_rx_data)
{
    if (p_rx_data->p_payload[1] != BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS)
    {
        return;
    }

    if (p_rx_data->length != BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH)
    {
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- p_rx_data->length:%d  -----\n", p_rx_data->length);
        return;
    }

    // receing and check the packets
    uint8_t rec_packet[31] = {0};
    rec_packet[0]          = p_rx_data->p_payload[0];
    rec_packet[1]          = p_rx_data->p_payload[1];
    rec_packet[2]          = p_rx_data->p_payload[2];
    rec_packet[3]          = p_rx_data->p_payload[3];
    rec_packet[4]          = ((p_rx_data->p_payload[4])  & 0x0F);
    rec_packet[5]          = ((p_rx_data->p_payload[4])  & 0xF0)>>4;
    rec_packet[6]          = ((p_rx_data->p_payload[5])  & 0x07);
    rec_packet[7]          = (((p_rx_data->p_payload[5]) & 0xF8)>>3) & 0x1F;
    for (uint8_t i = 6; i < 29; i++) // 6: payload starting point, 29: crc starting point
    {
        rec_packet[i + 2] = p_rx_data->p_payload[i];
    }
    
    // chekcing packet's crc
    crcInit();
    uint16_t crc_result = crcFast(rec_packet, 31);
    uint8_t  res1       = (crc_result & 0xFF00)>>8;
    uint8_t  res2       = (crc_result & 0x00FF);

    while (res1 >= 0x7F)
    {
        res1 -= 0x7F;
    }

    while (res2 >= 0x7F)
    {
        res2 -= 0x7F;
    }

    if ((res1 != p_rx_data->p_payload[29]) || (res2 != p_rx_data->p_payload[30]))
    {
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- res1: %X, res2: %X, p_rx_data->p_payload[29]: %X,p_rx_data->p_payload[30]: %X, check failure ------\n", res1, res2, p_rx_data->p_payload[29], p_rx_data->p_payload[30]);
        return;
    }


    for (uint8_t i = 0; i < 31; i++)
    {
        m_tx_buf_spi[i] = rec_packet[i];
    }
    m_tx_buf_spi[31] = res1;
    m_tx_buf_spi[32] = res2;
    spis_setfrom_slave(m_tx_buf_spi, S_BROADCASRLEN);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- received successfully  seq: %X-----\n", m_tx_buf_spi[2]);
}

void adv_init(void)
{
    advertiser_instance_init(&m_discovery_advertiser, NULL, m_adv_buffer_discovery, ADVERTISER_BUFFER_SIZE);
}

void node_reset(void)
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- Node reset  -----\n");
    hal_led_blink_ms(HAL_LED_MASK, LED_BLINK_INTERVAL_MS, LED_BLINK_CNT_RESET);
    /* This function may return if there are ongoing flash operations. */
    mesh_stack_device_reset();
}

void config_server_evt_cb(const config_server_evt_t * p_evt)
{
    if (p_evt->type == CONFIG_SERVER_EVT_NODE_RESET)
    {
        node_reset();
    }
}

void mesh_init(void)
{
    mesh_stack_init_params_t init_params =
    {
        .core.irq_priority       = NRF_MESH_IRQ_PRIORITY_LOWEST,
        .core.lfclksrc           = DEV_BOARD_LF_CLK_CFG,
        .models.config_server_cb = config_server_evt_cb
    };

    uint32_t status = mesh_stack_init(&init_params, NULL);
    switch (status)
    {
        case NRF_ERROR_INVALID_DATA:
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Data in the persistent memory was corrupted. Device starts as unprovisioned.\n");
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Reboot device before starting of the provisioning process.\n");
            break;
        case NRF_SUCCESS:
            break;
        default:
            ERROR_CHECK(status);
    }

    /* Start listening for incoming packets */
    nrf_mesh_rx_cb_set(rx_cb);

    /* Initialize the advertiser */
    adv_init();
}

void initialize(void)
{
#if defined(NRF51) && defined(NRF_MESH_STACK_DEPTH)
    stack_depth_paint_stack();
#endif
    
    ERROR_CHECK(app_timer_init());
    hal_leds_init();
    __LOG_INIT(LOG_SRC_APP, LOG_LEVEL_INFO, log_callback_rtt);

    ble_stack_init();
    mesh_init();
 
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Mesh initialization complete!\n");
}

void start(void)
{  
    /* Let scanner accept Complete Local Name AD Type. */
    bearer_adtype_add(BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS);
    ERROR_CHECK(mesh_stack_start());
    advertiser_enable(&m_discovery_advertiser);     /* Check if adv_instance is enable */
    spis_start();
}

int main(void)
{
    initialize();
    start();
}
