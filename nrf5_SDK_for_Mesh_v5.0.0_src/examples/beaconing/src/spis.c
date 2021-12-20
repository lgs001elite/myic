#include "spis.h"
#include "nrf_delay.h"
#include "advertiser.h"

#define                SPIS_INSTANCE                1 /**< SPIS instance index. */

bool                   SWITCH2SPI                 = true;
static  const          nrf_drv_spis_t spis        = NRF_DRV_SPIS_INSTANCE(SPIS_INSTANCE);/**< SPIS instance. */                           /** < RX buffer. */
uint8_t                m_rx_buf_spi[BROADCASRLEN] = {0};
volatile uint8_t *     m_tx_buf_spi;
volatile uint8_t       m_tx_length;
static volatile bool   spis_xfer_done;                     /**< Flag used to indicate that SPIS instance completed the transfer. */
volatile bool          g_null_status            = true;


static uint8_t         front_check[3]             = {0x41, 0x42, 0x43};
static uint8_t         rear_check[3]              = {0x58, 0x59, 0x5A};

/**
 * @brief  SPIS check completeness of data
 * 1, 3, 4, 7, 34, 37 etc. frameLen + checkNums
 */
bool check_completeness(uint8_t * receicedData)
{
    for (uint8_t i = 1; i < 4; i++)
    {
        if (receicedData[i] != front_check[i - 1])
        {
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "check failed!, front[%d]: rec%d\n", i, receicedData[i]);
            return false;
        }
    }

    uint8_t dataStatus = receicedData[7];
    if ((dataStatus == 0x04) || (dataStatus == 0x08))
    {
       for (uint8_t j = 0; j < 3; j++)
       {
            if (receicedData[j + 37] != rear_check[j])
            {
                __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "check failed!, front[%d]: rec:%c\n", j, receicedData[j]);
                return false;
            }
        }
    } else if (dataStatus == 0x0C)
    {
        uint8_t p_len  = receicedData[11];
        uint8_t anchor = 12 + p_len;
        for (uint8_t j = 0; j < 3; j++)
        {
            uint8_t offset = anchor + j;
            if (receicedData[offset] != rear_check[j])
            {
                __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "check failed!, front[%d]: rec:%c\n", j, receicedData[j]);
                return false;
            }
        }
    } else {
        for (uint8_t j = 0; j < 3; j++)
        {
            uint8_t offset = 12 + j;
            if (receicedData[offset] != rear_check[j])
            {
                __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "check failed!, front[%d]: rec:%c\n", j, receicedData[j]);
                return false;
            }
        }
    }

    return true;
}

void printCharac()
{
    for (uint8_t i = 4; i < (BROADCASRLEN - 3); i++)
    {
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Transfer completed. Received[%d]: %X \n", i, m_rx_buf_spi[i]);
    }
}
void stop_spis_loop()
{
    SWITCH2SPI = false;
}

void start_spis_loop()
{
    while (SWITCH2SPI)
    {
        SWITCH2SPI = true;
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "free: %d\n", g_null_status);
        uint8_t   *   initArr;
        if (g_null_status)
        {
            initArr = (uint8_t *) malloc (sizeof(uint8_t) * 3);
            if (!initArr)
            {
                return;
            }
            memset(initArr, 0, 3);
            initArr[0] = 0x05;
            initArr[1] = 0x02;
            initArr[2] = 0x08;
            spis_setfrom_slave(initArr, 3); /** Initilization,  filling characters */
            //__LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "anchor5\n");
        } 
        set_transData();
        uint8_t * t_rx_buf_spi = (uint8_t *) malloc(sizeof(uint8_t) * BROADCASRLEN);
        if (!t_rx_buf_spi)
        {
            return;
        }
        memset(t_rx_buf_spi, 0, BROADCASRLEN);
        spis_xfer_done = false;
        APP_ERROR_CHECK(nrfx_spis_buffers_set(&spis, m_tx_buf_spi, m_tx_length, m_rx_buf_spi, BROADCASRLEN));
        while (!spis_xfer_done)
        {
            (void)sd_app_evt_wait();
        }

        bsp_board_led_invert(BSP_BOARD_LED_1);
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "LED\n");
        for (uint8_t i = 0; i < 3; i++)
        {
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Transfer completed. Received[%d]: %X \n", i, m_rx_buf_spi[i]);
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Transfer [%d]: %X \n", i, m_tx_buf_spi[i]);
        }
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "m_tx_length: %d\n", m_tx_length);
        /**
         * @brief Construct a new free object
         * No matter what happend, it should free m_tx_buf_spi
         */
        //printCharac();
        free(m_tx_buf_spi);
        m_tx_buf_spi = NULL;   
    }
}

/**
 * @brief SPIS user event handler.
 *
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
            __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "check failed!\n");
            return;
        }
        /**
         * @brief Begin to transport data
         * 
         */
        g_null_status = false;
        __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "Pass data checking\n");
        uint8_t statusAction =  m_rx_buf_spi[7];
        
        switch (statusAction)
        {
            stop_spis_loop();
            /** The first datagram **/
            case 0x04:
                receiveData_sendout(m_rx_buf_spi);
                send_datagram_start();
                break;
            /** Other datagrams **/
            case 0x08:
                /** Finish last advertiser, prepare a new advertiser for this sending **/
                set_if_terCurrentAdvertiser(true);
                receiveData_sendout(m_rx_buf_spi);
                send_datagram_start();
                break;
            /** ack **/
            case 0x10:
                /** Finish last advertiser, prepare a new advertiser for this sending **/
                set_if_terCurrentAdvertiser(true);
                receiveHeader_sendout(m_rx_buf_spi);
                send_ack_start();
                break;
            /** source fin **/
            case 0x40:
                /** Finish last advertiser, prepare a new advertiser for this sending **/
                set_if_terCurrentAdvertiser(true);
                receiveHeader_sendout(m_rx_buf_spi);
                send_fin_start();
                break;
            /** dst fin **/
            case 0x80:
                /** Finish last advertiser, prepare a new advertiser for this sending **/
                set_if_terCurrentAdvertiser(true);
                receiveHeader_sendout(m_rx_buf_spi);
                send_fin_start();
                break;
            case 0xD0:
                advertiser_disableAndFlush(); // Finishing the current advertiser 
                break;
            default:
                break;
        }
        start_spis_loop();
    }
}

void spis_start(void)
{
    __LOG(LOG_SRC_APP, LOG_LEVEL_INFO, "spis_start\n");

    nrf_drv_spis_config_t spis_config = NRF_DRV_SPIS_DEFAULT_CONFIG;
    spis_config.csn_pin               = APP_SPIS_CS_PIN;
    spis_config.miso_pin              = APP_SPIS_MISO_PIN;
    spis_config.mosi_pin              = APP_SPIS_MOSI_PIN;
    spis_config.sck_pin               = APP_SPIS_SCK_PIN;
    //spis_config.mode                  = NRF_SPIS_MODE_1;

    APP_ERROR_CHECK(nrf_drv_spis_init(&spis, &spis_config, spis_event_handler));
    
    NRF_P0->PIN_CNF[APP_SPIS_MISO_PIN] = 
    (GPIO_PIN_CNF_DRIVE_H0H1 << GPIO_PIN_CNF_DRIVE_Pos) | (GPIO_PIN_CNF_INPUT_Connect
     << GPIO_PIN_CNF_INPUT_Pos) | (GPIO_PIN_CNF_DIR_Output << GPIO_PIN_CNF_DIR_Pos);
    start_spis_loop();
}
