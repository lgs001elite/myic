// #include "ad_type_filter.h"
// #include "advertiser.h"
// #include "app_timer.h"
// #include "ble.h"
// #include "ble_softdevice_support.h"
// #include "boards.h"
// #include "crc.h"
// #include "define_broadcast_packet.h"
// #include "example_common.h"
// #include "log.h"
// #include "mesh_app_utils.h"
// #include "mesh_provisionee.h"
// #include "mesh_stack.h"
// #include "nrf_delay.h"
// #include "nrf_drv_spis.h"
// #include "nrf_gpio.h"
// #include "nrf_log_ctrl.h"
// #include "nrf_mesh.h"
// #include "nrf_mesh_config_examples.h"
// #include "nrf_mesh_configure.h"
// #include "simple_hal.h"
// #include <stdbool.h>
// #include <stdio.h>
// #include <string.h>

// #define BROADCASTLEN 31

// #define APP_SCHED_EVENT_SIZE 12
// #define APP_SCHED_QUEUE_SIZE 32

// #define SPIS_INSTANCE 1 /**< SPIS instance index. */

// const nrf_drv_spis_t spis = NRF_DRV_SPIS_INSTANCE(SPIS_INSTANCE);
// static char g_rx_buf_spi_from_boards[BROADCASTLEN] = {0};
// static char g_tx_buf_spi_to_boards[BROADCASTLEN] = {0};

// bool spis_xfer_done = false;

// static bool g_received_success_flag_from_board = false;
// APP_TIMER_DEF(g_my_timer_counter);

// #if defined(NRF51) && defined(NRF_MESH_STACK_DEPTH)
// #include "stack_depth.h"
// #endif

// #define ADVERTISER_BUFFER_SIZE (512)
// bool g_if_sendNext = false;
// advertiser_t m_discovery_advertiser = {0};
// char m_adv_buffer_discovery[ADVERTISER_BUFFER_SIZE];
// adv_packet_t *p_broad_packet = NULL;
// static bool g_listenSwitch = false;
// static bool g_sendSwitch = false;
// static bool g_receivedMessage = false;

// static void send2bearer(advertiser_t *p_adv, char *adv_packet)
// {
//     p_broad_packet = advertiser_packet_alloc(p_adv, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
//     if (p_broad_packet)
//     {
//         memcpy(p_broad_packet->packet.payload, adv_packet, BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH);
//         p_broad_packet->config.repeats = 3;
//         advertiser_packet_send(p_adv, p_broad_packet);
//     }
// }

// void callback_rx_cb(const nrf_mesh_adv_packet_rx_data_t *p_rx_data)
// {
//     __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "-----A message comes-----\n");
//     if (p_rx_data->p_payload[1] != BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS)
//     {
//         return;
//     }
//     if (p_rx_data->length != BLE_ADV_PACKET_PAYLOAD_MAX_LENGTH)
//     {
//         return;
//     }
//     for (int i = 0; i < BROADCASTLEN; i++)
//     {
//         g_tx_buf_spi_to_boards[i] = p_rx_data->p_payload[i];
//     }
//     g_receivedMessage = true;
//     __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "-----A message received-----\n");
// }

// static void callBack_afterBLETRans()
// {
//     g_listenSwitch = true;
//     g_sendSwitch = false;
//     nrf_mesh_rx_cb_set(callback_rx_cb);
//     __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "-----Callback functions after the advertising-----\n")
// }

// void callback_receiver_work_cycle_switch(void)
// {
//     nrf_mesh_rx_cb_clear();
//     g_listenSwitch = false;
// }

// static void node_reset(void)
// {
//     __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- Node reset  -----\n");
//     hal_led_blink_ms(HAL_LED_MASK, LED_BLINK_INTERVAL_MS, LED_BLINK_CNT_RESET);
//     mesh_stack_device_reset();
// }

// void callback_config_server_evt_cb(const config_server_evt_t *p_evt)
// {
//     if (p_evt->type == CONFIG_SERVER_EVT_NODE_RESET)
//     {
//         node_reset();
//     }
// }

// static void mesh_init(void)
// {
//     mesh_stack_init_params_t init_params =
//         {
//             .core.irq_priority = NRF_MESH_IRQ_PRIORITY_THREAD,
//             .core.lfclksrc = DEV_BOARD_LF_CLK_CFG,
//             .models.config_server_cb = callback_config_server_evt_cb};

//     uint32_t status = mesh_stack_init(&init_params, NULL);
//     switch (status)
//     {
//     case NRF_ERROR_INVALID_DATA:
//         __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Data in the persistent memory was corrupted. Device starts as unprovisioned.\n");
//         __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Reboot device before starting of the provisioning process.\n");
//         break;
//     case NRF_SUCCESS:
//         break;
//     default:
//         ERROR_CHECK(status);
//     }
//     advertiser_instance_init(&m_discovery_advertiser, callBack_afterBLETRans, m_adv_buffer_discovery, ADVERTISER_BUFFER_SIZE);
// }

// static void mesh_initialize(void)
// {
//     ERROR_CHECK(app_timer_init());
//     hal_leds_init();
//     __LOG_INIT(LOG_SRC_APP, LOG_LEVEL_INFO, log_callback_rtt);
//     ble_stack_init();
//     mesh_init();
//     bearer_adtype_add(BLE_GAP_AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS);
//     advertiser_enable(&m_discovery_advertiser);
//     ERROR_CHECK(mesh_stack_start());
//     ret_code_t ret = app_timer_create(&g_my_timer_counter, APP_TIMER_MODE_REPEATED, callback_receiver_work_cycle_switch);
//     APP_ERROR_CHECK(ret);
//     __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Mesh initialization complete!\n");
// }

// static bool check_completeness(char *receivedData)
// {
//     crcInit();
//     uint16_t crc_result = crcFast(receivedData, 29);
//     char res1 = (crc_result & 0xFF00) >> 8;
//     char res2 = (crc_result & 0x00FF);

//     if (res1 != receivedData[29])
//     {
//         return false;
//     }

//    if (res2 != receivedData[30])
//    {
//        return false;
//    }

//    return true;
// }

void callback_spis_event_handler(nrf_drv_spis_event_t event)
{
  if (event.evt_type == NRF_DRV_SPIS_XFER_DONE)
  {
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Received messages from main boards\n");
    if ((g_rx_buf_spi_from_boards[0] != 0x1e) || (g_rx_buf_spi_from_boards[1] != 0x17))
    {
      __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Flag: Received the invalid messages\n");
    }
    bool checkResult = check_completeness(g_rx_buf_spi_from_boards);
    if (!checkResult)
    {
      __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "CheckSum: Received the invalid messages%x\n", g_rx_buf_spi_from_boards[9]);
    }
    else
    {
      g_received_success_flag_from_board = true;
    }
    spis_xfer_done = true;
  }
}

// static void run_spi_ble_mesh(void)
// {
//     // close the receiving radio
//     nrf_mesh_rx_cb_clear();
//     ret_code_t ret;
//     while (true) // SPI-BLE_MESH repetitively
//     {
//         bsp_board_led_invert(0); // indication lights
//         // First waiting for receiving messages from main boards
//         __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "-----waiting for messages from main boards-----\n");
g_received_success_flag_from_board = false;
while (g_received_success_flag_from_board == false)
{
  nrfx_spis_buffers_set(&spis, g_tx_buf_spi_to_boards, BROADCASTLEN, g_rx_buf_spi_from_boards, BROADCASTLEN);
  while (!spis_xfer_done)
  {
    (void)sd_app_evt_wait();
  }
}
//         __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "-----finishing data handover-----\n");

//         __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "-----broadcasting the messages from the main boards-----\n");
//         while (1)
//         {
//             send2bearer(&m_discovery_advertiser, g_rx_buf_spi_from_boards);
//        }
//        /*
//        g_sendSwitch = true;
//        while ( g_sendSwitch ) {
//          bool done = nrf_mesh_process( );
//          if ( done ) {
//            callBack_afterBLETRans( );
//            sd_app_evt_wait( );
//          }
//        }
//        __LOG( LOG_SRC_APP, LOG_LEVEL_INFO, "-----broadcasting process finished-----\n" );

//        __LOG( LOG_SRC_APP, LOG_LEVEL_INFO, "-----Starting the receiving process after broadcasting-----\n" );
//        ret = app_timer_start( g_my_timer_counter, APP_TIMER_TICKS( 5 ), NULL ); // set a timer, 5ms
//        while ( ret != NRF_SUCCESS ) {
//          ret = app_timer_start( g_my_timer_counter, APP_TIMER_TICKS( 5 ), NULL ); // set a timer, 5ms
//        }
//        g_receivedMessage = false;
//        while ( g_listenSwitch ) {
//          ( void )sd_app_evt_wait( );
//        }
//        __LOG( LOG_SRC_APP, LOG_LEVEL_INFO, "-----Finishing the receiving process after broadcasting-----\n" );
//        if ( g_receivedMessage == true ) {
//          __LOG( LOG_SRC_APP, LOG_LEVEL_INFO, "-----Received packets-----\n" );
//        }
//        __LOG( LOG_SRC_APP, LOG_LEVEL_INFO, "Starting new round\n" );
//        spis_xfer_done = false;
//        ( void )sd_app_evt_wait( );
//        */
//     }
// }

// static void spi_initialize(void)
// {
nrf_drv_spis_config_t spis_config = NRF_DRV_SPIS_DEFAULT_CONFIG;
spis_config.csn_pin = APP_SPIS_CS_PIN;
spis_config.miso_pin = APP_SPIS_MISO_PIN;
spis_config.mosi_pin = APP_SPIS_MOSI_PIN;
spis_config.sck_pin = APP_SPIS_SCK_PIN;
spis_config.irq_priority = 7;
APP_ERROR_CHECK(nrf_drv_spis_init(&spis, &spis_config, callback_spis_event_handler));
NRF_P0->PIN_CNF[APP_SPIS_MISO_PIN] =
    (GPIO_PIN_CNF_DRIVE_H0H1 << GPIO_PIN_CNF_DRIVE_Pos) | (GPIO_PIN_CNF_INPUT_Connect << GPIO_PIN_CNF_INPUT_Pos) | (GPIO_PIN_CNF_DIR_Output << GPIO_PIN_CNF_DIR_Pos);
// }

// int main(void)
// {
//     spi_initialize();
//     mesh_initialize();
//     run_spi_ble_mesh();
//     return 0;
// }
