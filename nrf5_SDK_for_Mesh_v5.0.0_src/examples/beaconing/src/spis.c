#include "spis.h"
#include "nrf_delay.h"
#include "advertiser.h"
#include "nrf_log_ctrl.h"
#include "nrf_drv_spis.h"

#define    SPIS_INSTANCE    1 /**< SPIS instance index. */

const  nrf_drv_spis_t spis              = NRF_DRV_SPIS_INSTANCE(SPIS_INSTANCE);/**< SPIS instance. */                           /** < RX buffer. */
uint8_t  m_rx_buf_spi[ACTUALDATAUNITS + 1] = {0};
uint8_t  m_tx_buf_spi[ACTUALDATAUNITS] = {0};
uint8_t  m_recBuf[32]                  = {0} ;

bool   spis_xfer_done =   false;  /**< Flag used to indicate that SPIS instance completed the transfer. */

bool check_completeness(uint8_t * receivedData)
{
    if (receivedData[2] != BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS)
    {
        return false;
    }
    uint8_t crc_input[31];
    for (uint8_t i = 1; i < 32; i++)
    {
        crc_input[i - 1] = receivedData[i];
    }
    crcInit();
    uint16_t crc_result = crcFast(crc_input, 31);
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
    if (res1 != receivedData[32])
    {
        return false;
    }

    if (res2 != receivedData[33])
    {
        return false;
    }

    return true;
}

void spis_event_handler(nrf_drv_spis_event_t event)
{
    if (event.evt_type == NRF_DRV_SPIS_XFER_DONE)
    {
        if ((m_rx_buf_spi[0] == 0) && (m_rx_buf_spi[1] == 0))
        {
           return;
        }
        spis_xfer_done = true;
        bool checkResult = check_completeness(m_rx_buf_spi);
        if (! checkResult)
        {
            return;
        }

        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "----- received successfully  seq: %X-----\n", m_rx_buf_spi[4]);
        uint8_t statusAction = m_rx_buf_spi[4];
        switch (statusAction)
        {
            case DUBBY:
              break;
            default:
              receiveData_sendout(m_rx_buf_spi);
              send_datagram_start();
              break;
        }
    }
}


void spis_start(void)
{
    nrf_drv_spis_config_t spis_config = NRF_DRV_SPIS_DEFAULT_CONFIG;
    (void)sd_app_evt_wait();
    spis_config.csn_pin               = APP_SPIS_CS_PIN;
    (void)sd_app_evt_wait();
    spis_config.miso_pin              = APP_SPIS_MISO_PIN;
    (void)sd_app_evt_wait();
    spis_config.mosi_pin              = APP_SPIS_MOSI_PIN;
    (void)sd_app_evt_wait();
    spis_config.sck_pin               = APP_SPIS_SCK_PIN;     
    (void)sd_app_evt_wait();
    spis_config.irq_priority          = 7; // keep up with the IRQ of Mesh
    (void)sd_app_evt_wait();
    (void)sd_app_evt_wait();
    APP_ERROR_CHECK(nrf_drv_spis_init(&spis, &spis_config, spis_event_handler));
    (void)sd_app_evt_wait();
    NRF_P0->PIN_CNF[APP_SPIS_MISO_PIN] = 
    (GPIO_PIN_CNF_DRIVE_H0H1 << GPIO_PIN_CNF_DRIVE_Pos) | (GPIO_PIN_CNF_INPUT_Connect
     << GPIO_PIN_CNF_INPUT_Pos) | (GPIO_PIN_CNF_DIR_Output << GPIO_PIN_CNF_DIR_Pos);
     (void)sd_app_evt_wait();
    
    //start_spis_loop();
    while (1)
    {
        APP_ERROR_CHECK(nrfx_spis_buffers_set(&spis, m_tx_buf_spi, ACTUALDATAUNITS, m_rx_buf_spi, ACTUALDATAUNITS + 1));
        spis_xfer_done = false;
        while (!spis_xfer_done)
        {
            (void) sd_app_evt_wait();
        }
        bsp_board_led_invert(BSP_BOARD_LED_1);
    }
}
