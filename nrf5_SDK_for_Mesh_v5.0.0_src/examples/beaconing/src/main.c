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

#define ADVERTISER_BUFFER_SIZE (512)
bool              g_if_sendNext          = false;
advertiser_t      m_discovery_advertiser = {0};
uint8_t           m_adv_buffer_discovery[ADVERTISER_BUFFER_SIZE]; 
void              adv_init(void);
adv_packet_t  *   p_broad_packet         = NULL;
bool listenSwitch = false;
bool sendSwitch = false;
uint8_t listeningTimeout = 0;

void send2bearer(advertiser_t *p_adv, uint8_t *adv_packet)
{
    p_broad_packet = advertiser_packet_alloc(p_adv, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
    if (p_broad_packet)
    {
        memcpy(p_broad_packet->packet.payload, adv_packet, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
        p_broad_packet->config.repeats = 3;
        advertiser_packet_send(p_adv, p_broad_packet);
    }
}

void rx_cb(const nrf_mesh_adv_packet_rx_data_t * p_rx_data)
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step7\n");
    if (listeningTimeout > 100)
    {
        nrf_mesh_rx_cb_clear();
        listenSwitch = false;
    }
    listeningTimeout = listeningTimeout + 1;
    if (p_rx_data->p_payload[1] != BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS)
    {
        return;
    }
    if (p_rx_data->length != BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH)
    {
        return;
    }
    for (uint8_t i = 0; i < BROADCASTLEN; i++)
    {
        m_tx_buf_spi[i] = p_rx_data->p_payload[i];
    }
   // bsp_board_led_invert(0);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step8\n");
}

static void callBackAfterFinish()
{
    listenSwitch = true;
    listeningTimeout = 0;
    sendSwitch = false;
    nrf_mesh_rx_cb_set(rx_cb);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step9\n")
    // nrf_mesh_rx_cb_clear();
}

void adv_init(void)
{
    advertiser_instance_init(&m_discovery_advertiser, callBackAfterFinish, m_adv_buffer_discovery, ADVERTISER_BUFFER_SIZE);
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
    // nrf_mesh_rx_cb_set(rx_cb);
    /* Initialize the advertiser */
    adv_init();
}

void ble_initialize(void)
{
// ble ini
#if defined(NRF51) && defined(NRF_MESH_STACK_DEPTH)
    stack_depth_paint_stack();
#endif
    ERROR_CHECK(app_timer_init());
    hal_leds_init();
    __LOG_INIT(LOG_SRC_APP, LOG_LEVEL_INFO, log_callback_rtt);
    ble_stack_init();
    mesh_init();
    bearer_adtype_add(BLE_GAP_AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS);
    ERROR_CHECK(mesh_stack_start());
    advertiser_enable(&m_discovery_advertiser);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Mesh initialization complete!\n");
}

void initializationSys(void)
{
    spi_initialize();
    ble_initialize();
}

int main(void)
{
    initializationSys();
    spis_execution();
}

