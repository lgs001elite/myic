/*
 * main.c
 *
 *  Created on: Dec 20, 2023
 *     Author: glu250
 */

#include "routingRx.h"
#include "routingTx.h"
#include "hash.h"
#include "crc.h"
#include "random.h"
#include "main.h"
#include "bonito.h"
#include "find.h"
#include "mypredic.h"
#include "spi.h"
#include "uart.h"
#include "distribution.h"
#include "joint_distribution.h"
#include "macro.h"
#include "pins.h"
#include "global_func.h"
#include "global_vars.h"
#include "uartHex.h"
#include "coordinatorFind.h"
#include "swift.h"

// #pragma DATA_SECTION(p_test, ".ram_code")
// double p_test = 0;

#pragma PERSISTENT(g_ifFindCoordinator)
bool g_ifFindCoordinator = false;

#pragma PERSISTENT(g_ifAdjustDrift)
bool g_ifAdjustDrift = false;

#pragma PERSISTENT(g_adjustUnits)
uint16_t g_adjustUnits = 0;

#pragma PERSISTENT(g_arrLoc)
char g_arrLoc = 0;

#pragma PERSISTENT(g_accuCharge)
char g_accuCharge = 0;


#pragma PERSISTENT(g_systimeCounter)
uint32_t g_systimeCounter = 0;

#pragma PERSISTENT(g_connectionLen)
int g_connectionLen = 0;

#pragma PERSISTENT(g_connectionNum)
int g_connectionNum = 0;

#pragma PERSISTENT(g_currentNodeLoc)
uint8_t g_currentNodeLoc = 0;

#pragma PERSISTENT(g_TXData)
char g_TXData = 0;

#pragma PERSISTENT(g_MaxChargeCycles)
int16_t g_MaxChargeCycles = 0;

#pragma PERSISTENT(g_attConn)
char g_attConn = 0;

#pragma PERSISTENT(g_queueLen)
char g_queueLen = MAXQUELEN;

#pragma PERSISTENT(g_rounds)
char g_rounds = MAXROUND;

#pragma PERSISTENT(g_systemStatus)
char g_systemStatus = 0;

#pragma PERSISTENT(g_distributedLoc)
uint8_t g_distributedLoc = 0;


#pragma PERSISTENT(swift_attempt)
uint16_t swift_attempt = 0;

#pragma PERSISTENT(swift_inc)
uint16_t swift_inc = 0;

// #pragma PERSISTENT(g_currentLoc)
// int8_t g_currentLoc = 0;

#pragma PERSISTENT(g_gotoLoc)
bool g_gotoLoc = false;

//#pragma PERSISTENT(g_alignLoc)
//bool g_alignLoc = false;

#pragma PERSISTENT(g_receCounter)
uint16_t g_receCounter = 0;

// in crc
#pragma PERSISTENT(g_chargHis)
int g_chargHis[HISLEN] = {0};

// in crc
#pragma PERSISTENT(g_locNum)
char g_locNum = 0;

#pragma PERSISTENT(g_pre_packet_seq)
uint8_t g_pre_packet_seq = 100;

#pragma PERSISTENT(g_packet_id)
uint8_t g_packet_id = 0x00;

// Timer0_A0 interrupt service routine
#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector = TIMER0_A0_VECTOR
    __interrupt void
    Timer0_A0_ISR(void)
#elif defined(__GNUC__)
    void __attribute__((interrupt(TIMER0_A0_VECTOR))) Timer0_A0_ISR(void)
#else
#error Compiler not supported!
#endif
{
    TA0CCR0 += DRIFTUNIT;
    g_driftTime = g_driftTime + 1;
    TA0CCR0 = 0;
}

#ifdef __debug
    #pragma GCC poison printf
#endif



void var_initialization()
{
    MasterMode = IDLE_MODE;
    g_sendAck = false;
    g_receveuartNum = 0;
    g_receiveIndex = 0;
    g_transDataSeq = 0;
    g_seq_data = 0;
    g_currentPairedNodeID = -1;
    g_nextNodeID = 0;
    g_chTimeSlots = 0;
    g_switchUart = 1;
    g_basicChargeCycles = 0;
    g_pairedChargeCycles = 0;
    g_lastChargeCycles = 0;
    g_nodeAddress = 0x02;
    g_node_dimension = 0x03;
    g_MatchNextHop = false;
    g_uartSwitch = true;
    g_nodeType = ICNODE;  // COORDINATOR ICNODE NeutronStar NeutronStarNoAli
    g_synStrategy = Swift02; // Find   NeutronStarPlus  Greedy Swift01 Swift01
    g_preDriftTime = 0;
    g_lastData = 0;
    g_driftTime = 0;
    g_ICListen = true;
    if (g_nodeType == COORDINATOR)
    {
        init_hashmap(&map);
        g_currentNodeLoc = 1;
    }
}

void timer_counter()
{
    TA0CCTL0 = CCIE;
    TA0CCR0 = 0;
    TA0CTL = TASSEL__SMCLK | MC__CONTINOUS;
}

void main(void)
{
    WDTCTL = WDTPW | WDTHOLD;
    setTimer();
    initGPIO();
    crcInit();
    var_initialization();
    timer_counter();
    __bis_SR_register(GIE);
    // uart
   // GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
    initUART();
    uart_entry();
    __no_operation();
    // SPI
    g_ICListen = false;
    // Close uart trans channel
    P6SEL0 ^= BIT0;
    P6SEL0 ^= BIT1;
    //GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN1;
    initSPI();
    start_spi_process();
    //GPIO_MONINOR_OUT4 ^= GPIO_MONITOR_PIN3;
}



