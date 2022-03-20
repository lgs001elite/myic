#include "spis.h"
#include "nrf_delay.h"
#include "advertiser.h"
#include "nrf_log_ctrl.h"

#define                SPIS_INSTANCE                1 /**< SPIS instance index. */

static   const         nrf_drv_spis_t spis          = NRF_DRV_SPIS_INSTANCE(SPIS_INSTANCE);/**< SPIS instance. */                           /** < RX buffer. */
static   uint8_t       m_rx_buf_spi[S_BROADCASRLEN + 1] = {0};
uint8_t                m_tx_buf_spi[S_BROADCASRLEN]     = {0};

static volatile bool   spis_xfer_done               = false;  /**< Flag used to indicate that SPIS instance completed the transfer. */

/**
 * @brief  SPIS check completeness of data(checksums of packets)
 */
bool check_completeness(uint8_t * receivedData)
{
    if (receivedData[2] != BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS)
    {
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "receivedData[2]: %X! \n", receivedData[1]);
        return false;
    }

    uint8_t crc_input[31];
    for (uint8_t i = 1; i < 32; i++)
    {
        crc_input[i - 1] = receivedData[i];
       // __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "receivedData[2]: %X! \n", receivedData[i]);
    }
    crcInit();
    uint16_t crc_result = crcFast(crc_input, 31);
    uint8_t  res1       = (crc_result & 0xFF00)>>8;
    uint8_t  res2       = (crc_result & 0x00FF);

    while (res1 >= 0x7F)
    {
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "res1: %X! \n",res1);
        res1 -= 0x7F;
    }

    while (res2 >= 0x7F)
    {
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "res2: %X! \n",res2);
        res2 -= 0x7F;
    }
    
    if (res1 != receivedData[32])
    {
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "failed! res1: %X\
            , receivedData[32]: %X! \n", res1, receivedData[32]);
        return false;
    }

    if (res2 != receivedData[33])
    {
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "failed! res2: %X, \
            receivedData[33]: %X! \n", res2, receivedData[33]);
        return false;
    }

    return true;
}

/**
 * @brief SPIS user event handler.
 * @param event
 */
void spis_event_handler(nrf_drv_spis_event_t event)
{
    if (event.evt_type == NRF_DRV_SPIS_XFER_DONE)
    {         
        spis_xfer_done = true;
        bool checkResult = check_completeness(m_rx_buf_spi);
        if (! checkResult)
        {
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "pass fail!\n");
            return;
        }
        
        uint8_t statusAction = m_rx_buf_spi[4];
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "pass check\n");
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "receive status: %X\n", statusAction);
        switch (statusAction)
        {
            case 0x42:
                break;
            default:
                receiveData_sendout(m_rx_buf_spi);
                send_datagram_start();
                break;
        }
    }
}

static void start_spis_loop()
{
    while (1)
    {
        set_transData();
        APP_ERROR_CHECK(nrfx_spis_buffers_set(&spis, m_tx_buf_spi, S_BROADCASRLEN, m_rx_buf_spi, S_BROADCASRLEN + 1));
        spis_xfer_done = false;
        while (!spis_xfer_done)
        {
            (void) sd_app_evt_wait();
        }
        bsp_board_led_invert(BSP_BOARD_LED_1);
    }
}

void spis_start(void)
{
    nrf_drv_spis_config_t spis_config = NRF_DRV_SPIS_DEFAULT_CONFIG;
    spis_config.csn_pin               = APP_SPIS_CS_PIN;
    spis_config.miso_pin              = APP_SPIS_MISO_PIN;
    spis_config.mosi_pin              = APP_SPIS_MOSI_PIN;
    spis_config.sck_pin               = APP_SPIS_SCK_PIN;         
    spis_config.irq_priority          = 7; // keep up with the IRQ of Mesh

    APP_ERROR_CHECK(nrf_drv_spis_init(&spis, &spis_config, spis_event_handler));
    
    /**
     * @brief  the init set the MISO output pin to H0H1 drive level 
     * in case the signal is too soggy for correct reading. 
     * Ideally at the MSP430 end the output signals SCK, CSN,
     *  MOSI would also be high drive if that is an option.
     */
    NRF_P0->PIN_CNF[APP_SPIS_MISO_PIN] = 
    (GPIO_PIN_CNF_DRIVE_H0H1 << GPIO_PIN_CNF_DRIVE_Pos) | (GPIO_PIN_CNF_INPUT_Connect
     << GPIO_PIN_CNF_INPUT_Pos) | (GPIO_PIN_CNF_DIR_Output << GPIO_PIN_CNF_DIR_Pos);
    
    start_spis_loop();
}
