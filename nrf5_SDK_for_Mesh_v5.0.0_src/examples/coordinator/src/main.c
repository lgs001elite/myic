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
#include "crc.h"
#include "public.h"
#include "hal_timer.h"

#define MS 1000
#define WORK_PERIOD 100
#define SLEEP_PERIOD WORK_PERIOD * 6
#define WORKING_CYCLE 30
#define BROADCASTLEN 32
#define SPI_NONCRC_LEN 31

static uint8_t m_tx_buf_spi[31];
static uint8_t m_rx_buf_spi[31];

static int current_loc_cycle = 0;
static uint16_t g_chTimeSlots = 7; // if the syn scheme is pulsar. the value is 3.

APP_TIMER_DEF(my_timer_counter);



#define ADVERTISER_BUFFER_SIZE (512)
static bool g_if_sendNext = false;
advertiser_t m_discovery_advertiser = {0};
static uint8_t m_adv_buffer_discovery[ADVERTISER_BUFFER_SIZE];
adv_packet_t *p_broad_packet = NULL;
uint8_t listeningTimeout = 0;
static bool g_work_cycle_switch = false;

static int16_t getCRC(unsigned char const message[])
{
    int16_t crc_result = crcFast(message, 29);
    return crc_result;
}


static void coordinator_work_cycle_switch(void * p_context)
{
   g_work_cycle_switch = false;
}

static void send2bearer(advertiser_t *p_adv, uint8_t *adv_packet)
{
    p_broad_packet = advertiser_packet_alloc(p_adv, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
    if (p_broad_packet)
    {
        memcpy(p_broad_packet->packet.payload, adv_packet, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
        p_broad_packet->config.repeats = 3;
        advertiser_packet_send(p_adv, p_broad_packet);
       // (void)sd_app_evt_wait();
    }
}


static void rx_cb(const nrf_mesh_adv_packet_rx_data_t *p_rx_data)
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step7\n");
    if (listeningTimeout > 100)
    {
        nrf_mesh_rx_cb_clear();
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
    uint8_t i = 0;
    for (; i < 32; i++)
    {
        m_rx_buf_spi[i] = p_rx_data->p_payload[i];
    }
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step8\n");
}

static void producePackets(void)
{
    m_tx_buf_spi[0] = 0x1E;
    m_tx_buf_spi[1] = 0x17;
    m_tx_buf_spi[2] = 0x1; // For packetSeq
    m_tx_buf_spi[3] = 0x4; // message type
    m_tx_buf_spi[4] = 0x1; // node type
    m_tx_buf_spi[5] = 0x30;
    m_tx_buf_spi[6] = 0x1;
    m_tx_buf_spi[7] = 0x1;
    m_tx_buf_spi[8] = 0x1;
    m_tx_buf_spi[9] = 0x0; // des in coordinator circle.
    m_tx_buf_spi[10] = 0x0;
    int8_t i = 3;
    for (; i >= 0; i--)
    {
        char temp = (g_chTimeSlots >> (i * 8)) & 0xff;
        m_tx_buf_spi[14 - i] = temp;
    }
    i = 15;
    for (; i < 29; i++)
    {
        m_tx_buf_spi[i] = 0;
    }
    char crc_input[29];
    i = 0;
    for (; i < 29; i++)
    {
        crc_input[i] = m_tx_buf_spi[i];
    }
    int16_t crc_result = getCRC(crc_input);
    m_tx_buf_spi[29] = (crc_result & 0xFF00) >> 8;
    m_tx_buf_spi[30] = (crc_result & 0x00FF);

    while (m_tx_buf_spi[29] >= 0x7F)
    {
        m_tx_buf_spi[29] -= 0x7F;
    }

    while (m_tx_buf_spi[30] >= 0x7F)
    {
        m_tx_buf_spi[30] -= 0x7F;
    }
}


static void node_reset(void)
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- Node reset  -----\n");
    hal_led_blink_ms(HAL_LED_MASK, LED_BLINK_INTERVAL_MS, LED_BLINK_CNT_RESET);
    mesh_stack_device_reset();
}

static void config_server_evt_cb(const config_server_evt_t *p_evt)
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
            .core.irq_priority = NRF_MESH_IRQ_PRIORITY_THREAD,
            .core.lfclksrc = DEV_BOARD_LF_CLK_CFG,
            .models.config_server_cb = config_server_evt_cb};

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
    /* Initialize the advertiser */
    advertiser_instance_init(&m_discovery_advertiser, NULL, m_adv_buffer_discovery, ADVERTISER_BUFFER_SIZE);
}


static void ble_initialize(void)
{
// ble ini
#if defined(NRF51) && defined(NRF_MESH_STACK_DEPTH)
    stack_depth_paint_stack();
#endif
    ERROR_CHECK(app_timer_init());
    hal_leds_init();
    ret_code_t ret = app_timer_create(&my_timer_counter, APP_TIMER_MODE_REPEATED, coordinator_work_cycle_switch);
    APP_ERROR_CHECK(ret);
    __LOG_INIT(LOG_SRC_APP, LOG_LEVEL_INFO, log_callback_rtt);
    ble_stack_init();
    mesh_init();
    bearer_adtype_add(BLE_GAP_AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS);
    ERROR_CHECK(mesh_stack_start());
    advertiser_enable(&m_discovery_advertiser);
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Mesh initialization complete!\n");
}

static bool check_completeness(char *receivedData)
{
    int16_t crc_result = getCRC(receivedData);
    char res1 = (crc_result & 0xFF00) >> 8;
    char result = (crc_result & 0x00FF);
    char temp1 = receivedData[29];
    char receive = receivedData[30];

    while (res1 >= 0x7F)
    {
        res1 -= 0x7F;
    }
    if (res1 != temp1)
    {
        return false;
    }
    while (result >= 0x7F)
    {
        result -= 0x7F;
    }

    if (result != receive)
    {
        return false;
    }

    return true;
}

static void ble_execution(void)
{
    nrf_mesh_rx_cb_clear();
    (void)sd_app_evt_wait();
    while (1)
    {
        ret_code_t ret = app_timer_start(my_timer_counter, APP_TIMER_TICKS(5), NULL);
        APP_ERROR_CHECK(ret);
        g_work_cycle_switch = true;
        nrf_mesh_rx_cb_set(rx_cb); // starting to listening
        current_loc_cycle = current_loc_cycle + 7 % WORKING_CYCLE;
        current_loc_cycle = current_loc_cycle % WORKING_CYCLE;
        uint32_t startCounter = app_timer_cnt_get();
        while (g_work_cycle_switch == true)
        {
            if (check_completeness(m_rx_buf_spi) == true)
            {
                producePackets();
                m_tx_buf_spi[10] = current_loc_cycle;
                send2bearer(&m_discovery_advertiser, m_tx_buf_spi); // sending acks
                __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "success\n");
            }
            listeningTimeout = 0;
        }
        uint32_t endCounter = app_timer_cnt_get();
        uint32_t time_interval = endCounter - startCounter;
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "value:%d\n", time_interval);
    }
}

int main(void)
{
    ble_initialize();
    ble_execution();
}
