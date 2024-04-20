#include "spis.h"
#include "nrf_delay.h"
#include "advertiser.h"
#include "nrf_log_ctrl.h"
#include "nrf_drv_spis.h"

#define SPIS_INSTANCE 1 /**< SPIS instance index. */

const nrf_drv_spis_t spis = NRF_DRV_SPIS_INSTANCE(SPIS_INSTANCE); /**< SPIS instance. */ /** < RX buffer. */
uint8_t m_rx_buf_spi[BROADCASTLEN + 1] = {0};
uint8_t m_tx_buf_spi[BROADCASTLEN] = {0};
bool spi_ack_switch = false;
uint8_t messageCounter = 0;

bool spis_xfer_done = false; /**< Flag used to indicate that SPIS instance completed the transfer. */

void spis_event_handler(nrf_drv_spis_event_t event);
void spi_initialize(void)
{
    nrf_drv_spis_config_t spis_config = NRF_DRV_SPIS_DEFAULT_CONFIG;
    (void)sd_app_evt_wait();
    spis_config.csn_pin = APP_SPIS_CS_PIN;
    (void)sd_app_evt_wait();
    spis_config.miso_pin = APP_SPIS_MISO_PIN;
    (void)sd_app_evt_wait();
    spis_config.mosi_pin = APP_SPIS_MOSI_PIN;
    (void)sd_app_evt_wait();
    spis_config.sck_pin = APP_SPIS_SCK_PIN;
    (void)sd_app_evt_wait();
    spis_config.irq_priority = 7; // keep up with the IRQ of Mesh
    (void)sd_app_evt_wait();
    (void)sd_app_evt_wait();
    APP_ERROR_CHECK(nrf_drv_spis_init(&spis, &spis_config, spis_event_handler));
    (void)sd_app_evt_wait();
    NRF_P0->PIN_CNF[APP_SPIS_MISO_PIN] =
        (GPIO_PIN_CNF_DRIVE_H0H1 << GPIO_PIN_CNF_DRIVE_Pos) | (GPIO_PIN_CNF_INPUT_Connect << GPIO_PIN_CNF_INPUT_Pos) | (GPIO_PIN_CNF_DIR_Output << GPIO_PIN_CNF_DIR_Pos);
    (void)sd_app_evt_wait();
}

bool check_completeness(uint8_t *receivedData)
{
    if (receivedData[1] != BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS)
    {
        return false;
    }
    uint8_t crc_input[29];
    for (uint8_t i = 0; i < 29; i++)
    {
        crc_input[i] = receivedData[i];
    }
    crcInit();
    uint16_t crc_result = crcFast(crc_input, 29);
    uint8_t res1 = (crc_result & 0xFF00) >> 8;
    uint8_t res2 = (crc_result & 0x00FF);

    while (res1 >= 0x7F)
    {
        res1 -= 0x7F;
    }

    while (res2 >= 0x7F)
    {
        res2 -= 0x7F;
    }
    if (res1 != receivedData[29])
    {
        return false;
    }

    if (res2 != receivedData[30])
    {
        return false;
    }

    return true;
}

void spis_event_handler(nrf_drv_spis_event_t event)
{
    if (event.evt_type == NRF_DRV_SPIS_XFER_DONE)
    {
        spis_xfer_done = true;
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step5\n");
        //for (int i = 0; i < BROADCASTLEN; i++)
        //{
        //    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "********************----- m_rx_buf_spi[%d]: %x-----********************\n", i, m_rx_buf_spi[i]);
        //}
        if ((m_rx_buf_spi[0] != 0x1e) || (m_rx_buf_spi[1] != 0x17))
        {
            bsp_board_led_invert(0);
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step5_2\n");
            return;
        }
        bool checkResult = check_completeness(m_rx_buf_spi);
        if (!checkResult)
        {
            bsp_board_led_invert(0);
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step5_3\n");
            return;
        }
        spi_ack_switch = true;
        uint8_t statusAction = m_rx_buf_spi[3];
        switch (statusAction)
        {
        case DUBBY:
            break;
        default:
            bsp_board_led_invert(1);
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step5_1\n");
            send2bearer(&m_discovery_advertiser, m_rx_buf_spi);
            m_rx_buf_spi[0] = 0x01;
            sendSwitch = true;
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step6\n");
        }
    }
}

void spis_execution(void)
{
    while (1)
    {
       // __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step1\n");
        while (sendSwitch)
        {
        }
       // __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step3_1\n");
        while (listenSwitch)
        {
            int inner_counter = 0;
            while (inner_counter < 100000)
            {
                inner_counter = inner_counter + 1;
            }
            nrf_mesh_rx_cb_clear();
            listenSwitch = false;
        }
       // __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step3_2\n");
        memset(m_rx_buf_spi, 0, BROADCASTLEN);
       // __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step2\n");
        if ((sendSwitch == false) && (listenSwitch == false))
        {
            spis_xfer_done = false;
        }
        APP_ERROR_CHECK(nrfx_spis_buffers_set(&spis, m_tx_buf_spi, BROADCASTLEN, m_rx_buf_spi, BROADCASTLEN));
       // __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "********************----- nrfx_spis_buffers_set-----********************\n");
       // __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step3\n");
        bsp_board_led_invert(3);
        //__LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "step4\n");
        int counter = 0;
        while (!spis_xfer_done)
        {
            bsp_board_led_invert(2);
            (void)sd_app_evt_wait();
            counter = counter + 1;
            if (counter > 10000)
            {
                counter = 0;
            }
        }
        //__LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "********************----- spis_xfer_done-----********************\n");
        //__LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- counter: %d-----\n", counter);
    }
}
