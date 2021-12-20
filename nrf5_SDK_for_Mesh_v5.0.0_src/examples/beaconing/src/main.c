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
#include <memory.h>
#include <string.h>
#include "nrf_delay.h"
#include "nrf_gpio.h"
#include "ble.h"
#include "boards.h"
#include "simple_hal.h"
#include "nrf_mesh.h"
#include "log.h"
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
#include "spis.h"
#include "spis_data.h"
#include "m2s.h"
#include "public.h"


#if defined(NRF51) && defined(NRF_MESH_STACK_DEPTH)
#include "stack_depth.h"
#endif

/*****************************************************************************
 * Definitions
 *****************************************************************************/
#define ADVERTISER_BUFFER_SIZE  (64)

volatile bool     g_if_sendNext = false;
volatile bool     g_now_send_ack_packets = false;
volatile bool     g_now_send_adv_packets = false;
volatile bool     g_now_send_end_packets = false;

advertiser_t        m_discovery_advertiser = {0};
volatile bool       g_isData               = false;
static uint8_t       m_adv_buffer_discovery[ADVERTISER_BUFFER_SIZE];
static void          adv_init(void);

/**
 * @brief pass datagram to the bearer layer
 * 
 * @param p_adv: advertiser entity
 * @param adv_packet: datagram
 */
static void send2bearer(advertiser_t * p_adv, define_adv_packet * adv_packet)
{
    adv_packet_t * p_packet = advertiser_packet_alloc(p_adv, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
    if (p_packet)
    {
        /* Construct packet contents */
        memcpy(p_packet->packet.payload, adv_packet, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
        /* Repeat forever */
        p_packet->config.repeats = ADVERTISER_REPEAT_INFINITE;

        advertiser_packet_send(p_adv, p_packet);
    } else {
        if (g_now_send_ack_packets == true)
        {
            advertiser_disableAndFlush();
            send_ack_start();
        } else if (g_now_send_adv_packets == true){
            advertiser_disableAndFlush();
            send_datagram_start();
        } else if (g_now_send_end_packets == true) {
            advertiser_disableAndFlush();
            send_fin_start();
        }
    }
}

/**
 * @brief free pointer operation
 * 
 */
 void freeAdvpacket(define_adv_packet * advPacket)
 {
     free(advPacket);
     advPacket = NULL;
 }


/**
 * @brief sending datagram
 * 
 */
void send_datagram_start()
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "********************* Adv --- starting *****************\n");
    advertiser_enable(&m_discovery_advertiser);     /* Check if adv_instance is enable */
    set_if_terCurrentAdvertiser(false); // Don't terminate the current advertiser
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Starting to send adv packets\n");
    define_adv_packet * recData = getData_sendout();
    nrf_delay_ms(20); /* For fill the payload completely*/

    g_now_send_adv_packets = true;
    send2bearer(&m_discovery_advertiser,recData);
    g_now_send_adv_packets = false;
    freeAdvpacket(recData);
}

/**
 * @brief sending fin header
 * 
 */
void send_fin_start()
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Starting to send ending beacons\n");
    advertiser_enable(&m_discovery_advertiser);
    set_if_terCurrentAdvertiser(false); // Don't terminate the current advertiser
    define_adv_packet * recData = getData_sendout();
    g_now_send_end_packets = true;
    send2bearer(&m_discovery_advertiser, recData);
    g_now_send_end_packets = false;
    freeAdvpacket(recData);
}

/**
 * @brief sending ack header
 * 
 */
void send_ack_start()
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Starting to send acks!\n");
    advertiser_enable(&m_discovery_advertiser);
    set_if_terCurrentAdvertiser(false); // Don't terminate the current advertiser
    define_adv_packet * recData = getData_sendout();
    g_now_send_ack_packets = true;
    send2bearer(&m_discovery_advertiser, recData);
    g_now_send_ack_packets = false;
    freeAdvpacket(recData);
}

/**
 * @brief receiving datagram from the bearer layer
 * 
 * @param p_rx_data: received datagram  
 */
static void rx_cb(const nrf_mesh_adv_packet_rx_data_t * p_rx_data)
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "p_rx_data->p_payload[1]: %d\n",  p_rx_data->p_payload[1]);
    if (p_rx_data->p_payload[1] != BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS)
    {
        return;
    }

    if (p_rx_data->length != BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH)
    {
        return;
    }
    
    uint8_t data_status = p_rx_data->p_payload[3];
    uint8_t *spi_data2mster;
    if ((data_status == 0x04) || (data_status == 0x08) || (data_status == 0x0C))
    {
        spi_data2mster= (uint8_t *) malloc(sizeof(uint8_t) * (BROADCASRLEN - 1));
        g_isData = true;
    } else {
        spi_data2mster= (uint8_t *) malloc(sizeof(uint8_t) * (STATUSLEN));
        g_isData = false;
    }
    
    if (! spi_data2mster)
    {
        return;
    }

    if (g_isData)
    {
        memset(spi_data2mster, 0, sizeof(uint8_t) * (BROADCASRLEN - 1));
    } else {
        memset(spi_data2mster, 0, sizeof(uint8_t) * STATUSLEN);
    }
    
    /**
     * @brief setting check bytes
     * 
     */
    spi_data2mster[0]  = 0x41;
    spi_data2mster[1]  = 0x42;
    spi_data2mster[2]  = 0x43;
    spi_data2mster[36] = 0x58;
    spi_data2mster[37] = 0x59;
    spi_data2mster[38] = 0x5A;

    spi_data2mster[3]  = p_rx_data->p_payload[0];
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster[3]: %d\n",  spi_data2mster[3]);
    spi_data2mster[4]  = p_rx_data->p_payload[1];
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster[4]: %d\n",  spi_data2mster[4]);
    spi_data2mster[5]  = p_rx_data->p_payload[2];
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster[5]: %d\n",  spi_data2mster[5]);
    spi_data2mster[6]  = p_rx_data->p_payload[3];
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster[6]: %d\n",  spi_data2mster[6]);
    spi_data2mster[7]  = ((p_rx_data->p_payload[4]) | 0x0F)>>4;
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster[7]: %d\n",  spi_data2mster[7]);
    spi_data2mster[8]  = ((p_rx_data->p_payload[4]) | 0xF0);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster[8]: %d\n",  spi_data2mster[8]);
    spi_data2mster[9]  = ((p_rx_data->p_payload[5]) | 0x07);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster[9]: %d\n",  spi_data2mster[9]);
    spi_data2mster[10] = ((p_rx_data->p_payload[5]) | 0xF8);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster[10]: %d\n", spi_data2mster[10]);
    
    if (g_isData)
    {
        for (uint8_t i = 6; i < BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH; i++)
        {
            uint8_t anchor = i + 5;
            spi_data2mster[anchor] = p_rx_data->p_payload[i];
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spi_data2mster: %d\n", spi_data2mster[anchor]);
        }
    }

    if (g_isData)
    {
        spis_setfrom_slave(spi_data2mster, BROADCASRLEN - 1);
    } else {
        spis_setfrom_slave(spi_data2mster, STATUSLEN);
    }
    
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Starting normal data transition\n");
}

static void adv_init(void)
{
    advertiser_instance_init(&m_discovery_advertiser, NULL, m_adv_buffer_discovery, ADVERTISER_BUFFER_SIZE);
}

static void node_reset(void)
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- Node reset  -----\n");
    hal_led_blink_ms(HAL_LED_MASK, LED_BLINK_INTERVAL_MS, LED_BLINK_CNT_RESET);
    /* This function may return if there are ongoing flash operations. */
    mesh_stack_device_reset();
}

static void config_server_evt_cb(const config_server_evt_t * p_evt)
{
    if (p_evt->type == CONFIG_SERVER_EVT_NODE_RESET)
    {
        node_reset();
    }
}

static void mesh_init(void)
{
    mesh_stack_init_params_t init_params =
    {
        .core.irq_priority = NRF_MESH_IRQ_PRIORITY_LOWEST,
        .core.lfclksrc     = DEV_BOARD_LF_CLK_CFG,
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

static void initialize(void)
{
#if defined(NRF51) && defined(NRF_MESH_STACK_DEPTH)
    stack_depth_paint_stack();
#endif

    ERROR_CHECK(app_timer_init());
    hal_leds_init();

    __LOG_INIT(LOG_SRC_APP, LOG_LEVEL_INFO, log_callback_rtt);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- Bluetooth Mesh Beacon Example -----\n");

    ble_stack_init();

    mesh_init();

    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Initialization complete!\n");

}

static void start(void)
{   
    spis_start();

    ERROR_CHECK(mesh_stack_start());
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Bluetooth Mesh Beacon example started!\n");
}

int main(void)
{
    initialize();
    start();

    for (;;)
    {
        (void)sd_app_evt_wait();
    }
}
