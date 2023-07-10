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
#include "spis.h"
#include "m2s.h"
#include "crc.h"
#include "public.h"


#if defined(NRF51) && defined(NRF_MESH_STACK_DEPTH)
#include "stack_depth.h"
#endif

#define ADVERTISER_BUFFER_SIZE  (128)
bool              g_if_sendNext          = false;
advertiser_t      m_discovery_advertiser = {0};
uint8_t           m_adv_buffer_discovery[ADVERTISER_BUFFER_SIZE]; 
void              adv_init(void);
adv_packet_t  *   p_broad_packet         = NULL;

void send2bearer(advertiser_t * p_adv, uint8_t * adv_packet)
{
    if (p_broad_packet)
    {
        memcpy(p_broad_packet->packet.payload, adv_packet, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
        p_broad_packet->config.repeats = 1;
        advertiser_packet_send(p_adv, p_broad_packet);
    }
    p_broad_packet = advertiser_packet_alloc(p_adv, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
}

void send_datagram_start()
{
    send2bearer(&m_discovery_advertiser, m_recBuf);
}

void rx_cb(const nrf_mesh_adv_packet_rx_data_t * p_rx_data)
{
    if (p_rx_data->p_payload[1] != BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS)
    {
        return;
    }
    if (p_rx_data->length != BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH)
    {
        return;
    }
    uint8_t rec_packet[32] = {0};
    rec_packet[0]          = p_rx_data->p_payload[0];
    rec_packet[1]          = p_rx_data->p_payload[1];
    rec_packet[2]          = p_rx_data->p_payload[2];
    rec_packet[3]          = ((p_rx_data->p_payload[3])& 0x0f);
    rec_packet[4]          = ((p_rx_data->p_payload[3])  & 0xF0)>>4;
    rec_packet[5]          = ((p_rx_data->p_payload[4]) & 0x0f);
    rec_packet[6]          = ((p_rx_data->p_payload[4])  & 0xF0)>>4;
    for (uint8_t i = 5; i < 29; i++)
    {
        rec_packet[i + 2] = p_rx_data->p_payload[i];
    }
    for (uint8_t i = 0; i < 31; i++)
    {
        m_tx_buf_spi[i] = rec_packet[i];
    }
    m_tx_buf_spi[31] = p_rx_data->p_payload[29];
    m_tx_buf_spi[32] = p_rx_data->p_payload[30];
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- received successfully  seq: %X-----\n", m_tx_buf_spi[2]);
    spis_xfer_done = true;
}

void adv_init(void)
{
    advertiser_instance_init(&m_discovery_advertiser, NULL, m_adv_buffer_discovery, ADVERTISER_BUFFER_SIZE);
}

void node_reset(void)
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- Node reset  -----\n");
    hal_led_blink_ms(HAL_LED_MASK, LED_BLINK_INTERVAL_MS, LED_BLINK_CNT_RESET);
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
    bearer_adtype_add(BLE_GAP_AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS);
    ERROR_CHECK(mesh_stack_start());
    (void)sd_app_evt_wait();
    advertiser_enable(&m_discovery_advertiser);
    (void)sd_app_evt_wait();
    spis_start();
    (void)sd_app_evt_wait();
}

int main(void)
{
    initialize();
    start();
}

