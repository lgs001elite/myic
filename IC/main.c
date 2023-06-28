#include <stdint.h>
#include <stdbool.h>
#include "public.h"
#include "routingRx.h"
#include "routingTx.h"
#include "hash.h"
#include "crc.h"
#include "random.h"
#include "transitionData.h"

uint8_t SlaveType0[SPI_DATA_LEN] = {0};
void setNode(uint8_t nodeType)
{
    switch (nodeType)
    {
    case ICNODE:
        g_nodeAddress = 0x01;
        g_node_dimension = 0x7e;
        g_if_sourceNode = true;
        g_waitToFind = 0;
        break;
    case SINK:
        g_nodeAddress = 0x03;
        g_node_dimension = 0x01;
        g_waitToFind = 0x7e;
        g_if_sourceNode = false;
        break;

    default:
        break;
    }
}

/* Used to track the state of the software state machine*/
SPI_Mode MasterMode = IDLE_MODE;

/* The Register Address/Command to use*/
uint8_t TransmitRegAddr = 0;

uint8_t RXByteCtr = 0;
uint8_t TXByteCtr = 0;
uint8_t TransmitIndex = 0;

void CopyArray(uint8_t *source, uint8_t *dest, uint8_t count);
void SendUCB1Data(uint8_t val);

void close_spi_process(void)
{
    SWITCH2SPI = false;
}

void SendUCB1Data(uint8_t val)
{
    while (!(UCB1IFG & UCTXIFG))
        ; // USCI_B1 TX buffer ready?
    UCB1TXBUF = val;
}

void CopyArray(uint8_t *source, uint8_t *dest, uint8_t count)
{
    uint8_t copyIndex = 0;
    for (copyIndex = 0; copyIndex < count; copyIndex++)
    {
        dest[copyIndex] = source[copyIndex];
    }
}

SPI_Mode SPI_Master_WriteReg(uint8_t reg_addr, uint8_t count)
{
    MasterMode = TX_REG_ADDRESS_MODE;
    TransmitRegAddr = reg_addr;
    TXByteCtr = count;
//    RXByteCtr = 0;
    TransmitIndex = 0;
    ReceiveIndex = 0;
    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(TransmitRegAddr);
    __bis_SR_register(CPUOFF + GIE); // Enter LPM0 w/ interrupts
    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    return MasterMode;
}

SPI_Mode SPI_Master_ReadReg(uint8_t reg_addr, uint8_t count)
{
    MasterMode = TX_REG_ADDRESS_MODE;
    TransmitRegAddr = reg_addr;
    RXByteCtr = count;
    TXByteCtr = 0;
    ReceiveIndex = 0;
//    TransmitIndex = 0;
    SLAVE_CS_OUT &= ~(SLAVE_CS_PIN);
    SendUCB1Data(TransmitRegAddr);
    __bis_SR_register(CPUOFF + GIE); // Enter LPM0 w/ interrupts

    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    return MasterMode;
}

void initSPI()
{
    // Clock Polarity: The inactive state is high
    // MSB First, 8-bit, Master, 4-pin mode, Synchronous
    UCB1CTLW0 = UCSWRST; // **Put state machine in reset**
    UCB1CTLW0 |= UCCKPL | UCMSB | UCSYNC | UCMST | UCSSEL__SMCLK_L | UCMODE0 | UCSTEM | UC7BIT_0 | UCCKPH; // Added by me
    UCB1BRW = 0x20;
    // UCB1MCTLW = 0;
    UCB1CTLW0 &= ~UCSWRST;
}

void initGPIO()
{
    // LEDs
    COMMS_LED_OUT &= ~COMMS_LED_PIN;
    COMMS_LED_DIR |= COMMS_LED_PIN;
    COMMS_LED_OUT &= ~COMMS_LED_PIN2;
    COMMS_LED_DIR |= COMMS_LED_PIN2;
    // Configure SPI
    P5SEL0 |= BIT0 | BIT1 | BIT2;
    SLAVE_CS_DIR |= SLAVE_CS_PIN;
    SLAVE_CS_OUT |= SLAVE_CS_PIN;
    PM5CTL0 &= ~LOCKLPM5;
}

void initClockTo16MHz()
{
    FRCTL0 = FRCTLPW | NWAITS_1;
    // Clock System Setup
    CSCTL0_H = CSKEY_H; // Unlock CS registers
    CSCTL1 = DCOFSEL_0; // Set DCO to 1MHz

    // Set SMCLK = MCLK = DCO, ACLK = VLOCLK
    CSCTL2 = SELA__VLOCLK | SELS__DCOCLK | SELM__DCOCLK;
    CSCTL3 = DIVA__4 | DIVS__4 | DIVM__4; // Set all corresponding clk sources to divide by 4 for errata
    CSCTL1 = DCOFSEL_4 | DCORSEL;         // Set DCO to 16MHz

}
int main(void)
{
    // Stop watchdog timer
    WDTCTL = WDTPW | WDTHOLD;
    initClockTo16MHz();
    initGPIO();
    initSPI();
    setNode(ICNODE);
    g_sendAck = false;
    g_queueLen = 0;
    ReceiveIndex = 0;
    g_preQueLen = 0;
    g_transDataSeq = 0;
    g_if_end_trans = false;
    g_received_file_real_size = 0;
    g_pre_packet_seq = 0x7e;
    g_pre_fin_seq = 0x7e;
    g_pre_ack_seq = 0x7e;
    g_systemStatus = NONLAYER;
    g_seq_data = (uint8_t)genRanNumb();
    g_seq_header = (uint8_t)genRanNumb();
    g_if_send_next = true;
    g_currentPairedNodeID = 0x7e;
    g_nextNodeID = 0x7e;
    g_waitReceiveCounter = 0;
    g_waitSendCounter = 0;
    if (g_if_sourceNode)
    {
        g_rounds = MAXROUND;
        g_packetQueue = (SPI_DATAGRAM *)malloc(sizeof(SPI_DATAGRAM) * MAXQUELEN);
        if (!g_packetQueue)
        {
            free(g_packetQueue);
            return 0;
        }
    }
    else
    {
        g_rounds = 0;
    }
    if (g_node_dimension != 0x01)
    {
        produceData();
    }
    start_spi_process();
}

void update_crc(void)
{
    uint8_t crc_input[32];
    uint8_t i = 0;
    for (; i < 31; i++)
    {
        crc_input[i] = g_transBuffer[i];
    }

    uint16_t crc_result = getCRC(crc_input);
    g_transBuffer[31] = (crc_result & 0xFF00) >> 8;
    g_transBuffer[32] = (crc_result & 0x00FF);

    while (g_transBuffer[31] >= 0x7F)
    {
        g_transBuffer[31] -= 0x7F;
    }

    while (g_transBuffer[32] >= 0x7F)
    {
        g_transBuffer[32] -= 0x7F;
    }
}

void start_spi_process(void)
{
    SWITCH2SPI = true;
    UCB1IE |= UCRXIE;
    while (SWITCH2SPI)
    {
        SPI_Master_ReadReg(CMD_TYPE_0_SLAVE, SPI_DATA_LEN );
        CopyArray(g_receiveBuffer, SlaveType0, SPI_DATA_LEN);
        receiveDataFromNordic();
        if (g_sendAck == true)
        {
            produceNonPacketData();
            g_transBuffer[2] = g_pre_packet_seq;
            g_transBuffer[3] = PACKAGE_ACK;
            g_transBuffer[6] = g_currentPairedNodeID;
            update_crc();
            SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
            g_sendAck = false;
            continue;
        }
        if (g_systemStatus == NONLAYER)
        {
            if (g_if_sourceNode)
            {
                if (g_node_dimension == 0x7e)
                {
                    continue;
                }
                if (g_waitToFind == 0)
                {
                    g_systemStatus = TRANSMIT;
                }
            }
            else
            {
                if (g_waitToFind == 0)
                {
                    g_systemStatus = SINKWAIT;
                }
            }
            produceNonPacketData();
            g_transBuffer[3] = PACKAGE_FIND;
            update_crc();
            SPI_Master_WriteReg(CMD_TYPE_0_MASTER, 33);
            g_waitToFind = g_waitToFind - 1;
        }
        else if (g_systemStatus == TRANSMIT)
        {
            if (g_currentPairedNodeID != 0x7e)
            {
                g_currentPairedNodeID = 0x7e;
            }
            if (g_waitReceiveCounter != 0)
            {
                g_waitReceiveCounter = 0;
            }
            if (g_queueLen == 0)
            {
                g_systemStatus = RECEIVE;
                continue;
            }
            if (g_waitSendCounter > MAXWAIT)
            {
                g_systemStatus = RECEIVE;
                g_nextNodeID = 0x7e;
                continue;
            }
            if (g_preQueLen == g_queueLen)
            {
                g_waitSendCounter = g_waitSendCounter + 1;
            }
            else
            {
                g_waitSendCounter = 0;
            }
            uint8_t *transmitBuffer = (uint8_t *)malloc(sizeof(uint8_t) * SPI_DATA_LEN);
            if (!transmitBuffer)
            {
                free(transmitBuffer);
                return;
            }
            memset(transmitBuffer, 0, SPI_DATA_LEN);
            m2s(transmitBuffer, &g_packetQueue[g_queueLen - 1]);
            buf_m2s(transmitBuffer, SPI_DATA_LEN);
            g_preQueLen = g_queueLen;
            if (g_queueLen == 1)
            {
                g_transBuffer[3] = PACKAGE_FINISH;
                update_crc();
            }
            SPI_Master_WriteReg(CMD_TYPE_0_MASTER, SPI_DATA_LEN);
        }
        else if (g_systemStatus == RECEIVE)
        {
            if (g_waitSendCounter != 0)
            {
                g_waitSendCounter = 0;
            }
            if (g_queueLen >= MAXQUELEN)
            {
                g_systemStatus = TRANSMIT;
                continue;
            }
            if (g_waitReceiveCounter > MAXWAIT)
            {
                g_systemStatus = TRANSMIT;
                continue;
            }

            if (g_queueLen != 0)
            {
                g_waitReceiveCounter = g_waitReceiveCounter + 1;
            }
        }
        else if (g_systemStatus == SINKWAIT)
        {
            // To do ben
        }
    }
}

#if defined(__TI_COMPILER_VERSION__) || defined(__IAR_SYSTEMS_ICC__)
#pragma vector = USCI_B1_VECTOR
__interrupt void USCI_B1_ISR(void)
#elif defined(__GNUC__)
void __attribute__((interrupt(USCI_B1_VECTOR))) USCI_B1_ISR(void)
#else
#error Compiler not supported!
#endif
{
    uint8_t ucb1_rx_val = 0;
    switch (__even_in_range(UCB1IV, USCI_SPI_UCTXIFG))
    {
    case USCI_NONE:
        break;
    case USCI_SPI_UCRXIFG:
        ucb1_rx_val = UCB1RXBUF;
        g_receiveBuffer[ReceiveIndex++] = ucb1_rx_val;
        UCB1IFG &= ~UCRXIFG;
        switch (MasterMode)
        {
        case TX_REG_ADDRESS_MODE:
            if (RXByteCtr)
            {
                MasterMode = RX_DATA_MODE; // Need to start receiving now
                // Send Dummy To Start
                SendUCB1Data(DUMMY);
            }
            else
            {
                MasterMode = TX_DATA_MODE; // Continue to transmision with the data in Transmit Buffer
                // Send First
                SendUCB1Data(g_transBuffer[TransmitIndex++]);
                TXByteCtr--;
            }
            break;
        case TX_DATA_MODE:
            if (TXByteCtr)
            {
                SendUCB1Data(g_transBuffer[TransmitIndex++]);
                TXByteCtr--;
            }
            else
            {
                // Done with transmission
                MasterMode = IDLE_MODE;
                __bic_SR_register_on_exit(CPUOFF); // Exit LPM0
            }
            break;
        case RX_DATA_MODE:
            if (RXByteCtr)
            {
                RXByteCtr--;
            }
            if (RXByteCtr == 0)
            {
                MasterMode = IDLE_MODE;
                __bic_SR_register_on_exit(CPUOFF); // Exit LPM0
            }
            else
            {
                SendUCB1Data(DUMMY);
            }
            break;
        default:
            __no_operation();
            break;
        }
        break;
    case USCI_SPI_UCTXIFG:
        break;
    default:
        break;
    }
}
