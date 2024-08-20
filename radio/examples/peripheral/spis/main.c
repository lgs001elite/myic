#include "app_timer.h"
#include "boards.h"
#include "bsp.h"
#include "nordic_common.h"
#include "nrf_delay.h"
#include "nrf_drv_spis.h"
#include "nrf_error.h"
#include "nrf_gpio.h"
#include "nrf_radio.h"
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#include "nrf_log.h"
#include "nrf_log_ctrl.h"
#include "nrf_log_default_backends.h"

#include "./crc.h"

#define BROADCASTLEN 31
static char packet_sender[ BROADCASTLEN ] = { 0 };   /**< Packet to transmit. */
static char packet_receiver[ BROADCASTLEN ] = { 0 }; /**< Packet to receive. */

#define SPIS_INSTANCE 1 /**< SPIS instance index. */

const nrf_drv_spis_t spis = NRF_DRV_SPIS_INSTANCE( SPIS_INSTANCE );

APP_TIMER_DEF( g_my_work_timer_counter );
APP_TIMER_DEF( g_my_sleep_timer_counter );
#define TIME_UNIT 1
#define SLEEP_LEN ( 6 * TIME_UNIT )
#define WORK_LEN ( 7 * TIME_UNIT )
#define CHARGE_CYCLE ( 2 * TIME_UNIT )

#define IC_CYCLE ( 51 * TIME_UNIT )

static bool g_if_inSleep = false;
static bool g_if_inWork = false;
static int g_curr_loc = 0;

bool spis_xfer_done = false;

#define DATA_PACKAGE 0
#define ACK_PACKAGE 1
#define BROAD_PACKAGE 2
#define NODE_ID 6

#define PACKAGE_BROAD 0x04
#define COORDINATOR 0x01

static bool check_completeness( char *receivedData ) {
  crcInit( );
  int16_t crc_result = crcFast( receivedData, 29 );
  char res1 = ( crc_result & 0xFF00 ) >> 8;
  char result = ( crc_result & 0x00FF );
  char temp1 = receivedData[ 29 ];
  char receive = receivedData[ 30 ];

  while ( res1 >= 0x7F ) {
    res1 -= 0x7F;
  }
  if ( res1 != temp1 ) {
    return false;
  }
  while ( result >= 0x7F ) {
    result -= 0x7F;
  }

  if ( result != receive ) {
    return false;
  }

  return true;
}

void callback_spis_event_handler( nrf_drv_spis_event_t event ) {
  if ( event.evt_type == NRF_DRV_SPIS_XFER_DONE ) {
    NRF_LOG_INFO( "Received messages from main boards\n" );
    if ( ( packet_sender[ 0 ] != 0x1e ) || ( packet_sender[ 1 ] != 0x17 ) ) {
      NRF_LOG_INFO( "Flag: Received the invalid messages\n" );
    }
    bool checkResult = check_completeness( packet_sender );
    if ( !checkResult ) {
      NRF_LOG_INFO( "CheckSum: Received the invalid messages%x\n", packet_sender[ 9 ] );
    }
    spis_xfer_done = true;
  }
}

static void producePackets( char currLoc, char nextID ) {
  packet_sender[ 0 ] = 0x1E;
  packet_sender[ 1 ] = 0x17;
  packet_sender[ 2 ] = 0x1;           // For packetSeq
  packet_sender[ 3 ] = PACKAGE_BROAD; // message type
  packet_sender[ 4 ] = COORDINATOR;   // node type
  packet_sender[ 5 ] = currLoc;
  packet_sender[ 6 ] = nextID;
  packet_sender[ 7 ] = 0x1;
  packet_sender[ 8 ] = 0x1;
  packet_sender[ 9 ] = 0x0; // des in coordinator circle.
  packet_sender[ 10 ] = 0x0;
  int8_t i = 3;
  for ( ; i >= 0; i-- ) {
    packet_sender[ 14 - i ] = i;
  }
  i = 15;
  for ( ; i < 29; i++ ) {
    packet_sender[ i ] = 0;
  }
  char crc_input[ 29 ];
  i = 0;
  for ( ; i < 29; i++ ) {
    crc_input[ i ] = packet_sender[ i ];
  }
  crcInit( );
  int16_t crc_result = crcFast( crc_input, 29 );
  packet_sender[ 29 ] = ( crc_result & 0xFF00 ) >> 8;
  packet_sender[ 30 ] = ( crc_result & 0x00FF );

  while ( packet_sender[ 29 ] >= 0x7F ) {
    packet_sender[ 29 ] -= 0x7F;
  }

  while ( packet_sender[ 30 ] >= 0x7F ) {
    packet_sender[ 30 ] -= 0x7F;
  }
}

/**@brief Function for sending packet.
 */
void send_packet( ) {
  // send the packet:
  NRF_RADIO->EVENTS_READY = 0U;
  NRF_RADIO->TASKS_TXEN = 1U;

  while ( NRF_RADIO->EVENTS_READY == 0U ) {
    // wait
  }
  NRF_RADIO->EVENTS_END = 0U;
  NRF_RADIO->TASKS_START = 1U;

  while ( NRF_RADIO->EVENTS_END == 0U ) {
    // wait
  }

  NRF_LOG_INFO( "The packet was sent" );

  NRF_RADIO->EVENTS_DISABLED = 0U;
  // Disable radio
  NRF_RADIO->TASKS_DISABLE = 1U;

  while ( NRF_RADIO->EVENTS_DISABLED == 0U ) {
    // wait
  }
}

/**@brief Function for reading packet.
 */
uint32_t read_packet( ) {
  uint8_t *result = 0;

  NRF_RADIO->EVENTS_READY = 0U;
  // Enable radio and wait for ready
  NRF_RADIO->TASKS_RXEN = 1U;

  while ( NRF_RADIO->EVENTS_READY == 0U ) {
    // wait
  }
  NRF_RADIO->EVENTS_END = 0U;
  // Start listening and wait for address received event
  NRF_RADIO->TASKS_START = 1U;

  // Wait for end of packet or buttons state changed
  uint32_t counter = 0;
  while ( NRF_RADIO->EVENTS_END == 0U ) {
    // wait
    counter = counter + 1;
    if ( counter > 11101 ) {
      break;
    }
  }
  NRF_LOG_INFO( "Waiting for receiving:%d\n", counter );
  NRF_LOG_FLUSH( );
  if ( NRF_RADIO->CRCSTATUS == 1U ) {
    result = packet_receiver;
  }
  NRF_RADIO->EVENTS_DISABLED = 0U;
  // Disable radio
  NRF_RADIO->TASKS_DISABLE = 1U;

  while ( NRF_RADIO->EVENTS_DISABLED == 0U ) {
    // wait
  }
  return result;
}

/**@brief Function for initialization oscillators.
 */
void clock_initialization( ) {
  /* Start 16 MHz crystal oscillator */
  NRF_CLOCK->EVENTS_HFCLKSTARTED = 0;
  NRF_CLOCK->TASKS_HFCLKSTART = 1;

  /* Wait for the external oscillator to start up */
  while ( NRF_CLOCK->EVENTS_HFCLKSTARTED == 0 ) {
    // Do nothing.
  }

  /* Start low frequency crystal oscillator for app_timer(used by bsp)*/
  NRF_CLOCK->LFCLKSRC = ( CLOCK_LFCLKSRC_SRC_Xtal << CLOCK_LFCLKSRC_SRC_Pos );
  NRF_CLOCK->EVENTS_LFCLKSTARTED = 0;
  NRF_CLOCK->TASKS_LFCLKSTART = 1;

  while ( NRF_CLOCK->EVENTS_LFCLKSTARTED == 0 ) {
    // Do nothing.
  }
}

void callback_coordinator_work_cycle_switch( void *p_context ) {
  g_if_inWork = false;
}

void callback_coordinator_sleep_cycle_switch( void *p_context ) {
  g_if_inSleep = false;
}

static void initialization( ) {
  uint32_t err_code = NRF_SUCCESS;

  clock_initialization( );
  // app_timer registration
  APP_ERROR_CHECK( app_timer_create( &g_my_work_timer_counter, APP_TIMER_MODE_REPEATED,
      callback_coordinator_work_cycle_switch ) );
  APP_ERROR_CHECK( app_timer_create( &g_my_sleep_timer_counter, APP_TIMER_MODE_REPEATED,
      callback_coordinator_sleep_cycle_switch ) );

  err_code = app_timer_init( );
  APP_ERROR_CHECK( err_code );

  err_code = NRF_LOG_INIT( NULL );
  APP_ERROR_CHECK( err_code );

  NRF_LOG_DEFAULT_BACKENDS_INIT( );

  // err_code = bsp_init(BSP_INIT_LEDS | BSP_INIT_BUTTONS, bsp_evt_handler);
  // APP_ERROR_CHECK(err_code);

  // Set radio configuration parameters
  radio_configure_sender( );

  // err_code = bsp_indication_set(BSP_INDICATE_USER_STATE_OFF);
  NRF_LOG_INFO( "Radio transmitter example started." );
  NRF_LOG_INFO( "Press Any Button" );
  APP_ERROR_CHECK( err_code );
  NRF_LOG_FLUSH( );

  // SPI
  nrf_drv_spis_config_t spis_config = NRF_DRV_SPIS_DEFAULT_CONFIG;
  spis_config.csn_pin = APP_SPIS_CS_PIN;
  spis_config.miso_pin = APP_SPIS_MISO_PIN;
  spis_config.mosi_pin = APP_SPIS_MOSI_PIN;
  spis_config.sck_pin = APP_SPIS_SCK_PIN;
  spis_config.irq_priority = 7;
  APP_ERROR_CHECK( nrf_drv_spis_init( &spis, &spis_config, callback_spis_event_handler ) );
  NRF_P0->PIN_CNF[ APP_SPIS_MISO_PIN ] =
      ( GPIO_PIN_CNF_DRIVE_H0H1 << GPIO_PIN_CNF_DRIVE_Pos ) |
      ( GPIO_PIN_CNF_INPUT_Connect << GPIO_PIN_CNF_INPUT_Pos ) | ( GPIO_PIN_CNF_DIR_Output << GPIO_PIN_CNF_DIR_Pos );
}

/**
 * @brief Function for application main entry.
 * @return 0. int return type required by ANSI/ISO standard.
 */
int main( void ) {
  initialization( );
  while ( true ) {
    // Step1: SPI operations
    nrfx_spis_buffers_set( &spis, packet_receiver, BROADCASTLEN, packet_sender, BROADCASTLEN );
    while ( !spis_xfer_done ) {
      __WFE( );
    }
    packet_receiver[ 0 ] = 0xff;
    spis_xfer_done = false;
    // Step2: Sending
    NRF_RADIO->PACKETPTR = packet_sender;
    send_packet( );
    // Step3: Receving
    NRF_RADIO->PACKETPTR = packet_receiver;
    uint8_t *received = read_packet( );
    // interpret the packet
    if ( check_completeness( packet_receiver ) == true ) {
      NRF_LOG_INFO( "Receiving the correct format of data!\n" )
      NRF_LOG_FLUSH( );
    }
    __WFE( );
  }
}
