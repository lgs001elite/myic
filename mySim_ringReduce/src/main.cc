/* Copyright (c) 2024, Vrije Universiteit Amsterdam
 * Contributor: Gaosheng Liu
 * All rights reserved.
 */

#include "packet_frame_m.h"
#include <fstream>
#include <sstream>
#include <cmath>
#include "ic_node.h"

using namespace std;

void basic_node::initialize()
{
    this->networkPtr = this->getParentModule();
    simtime_t ptr = simTime();
    net_initialize();
}

void basic_node::handleMessage(cMessage *msg)
{
    net_handleMessage(msg);
}

/**
 * @brief setting nodes' coordinators
 *
 * @param x_pos
 * @param y_pos
 */
void basic_node::place_nodes(int x_pos, int y_pos)
{
    this->x_pos = x_pos;
    this->y_pos = y_pos;
}

/**
 *duplicate frame
 */
void basic_node::duplicate_msg(packet_frame *ori, packet_frame *dMsg)
{
    ori->setCurrent_slot(dMsg->getCurrent_slot());
    ori->setDelay_bias(dMsg->getDelay_bias());
    ori->setDest_id(dMsg->getDest_id());
    ori->setMsg_id(dMsg->getMsg_id());
    ori->setMsg_type(dMsg->getMsg_type());
    ori->setNext_id(dMsg->getNext_id());
    ori->setPass_counter(dMsg->getPass_counter());
    ori->setSend_time(dMsg->getSend_time());
    ori->setSender_id(dMsg->getSender_id());
    ori->setSender_type(dMsg->getSender_type());
    ori->setSource_id(dMsg->getSource_id());
    ori->setOrigin_slot(dMsg->getOrigin_slot());
    ori->setNode_state(dMsg->getNode_state());
    ori->setScale_slot(dMsg->getScale_slot());
}

/**
 * @brief produce msg packets
 *
 * @param dataid
 * @param conTrans
 * @return packet_frame*
 * 0: broad_msg; 1: ack_msg; 2: data_msg
 */
packet_frame *basic_node::produce_msg(int packet_id, int msg_type, int sender_type, int next_id)
{
    packet_frame *dMsg = new packet_frame();
    dMsg->setDest_id(31);
    dMsg->setSource_id(this->g_node_id);
    dMsg->setSender_id(this->g_node_id);
    dMsg->setMsg_type(msg_type);
    dMsg->setSender_type(sender_type);
    dMsg->setMsg_id(packet_id);
    dMsg->setSend_time(0);
    dMsg->setOrigin_slot(this->g_ic_loc);
    dMsg->setCurrent_slot(this->g_ic_dynamic_loc);
    dMsg->setNext_id(next_id);
    dMsg->setPass_counter(0);
    dMsg->setNode_state(IDLE_STATE);
    return dMsg;
}

/**
 * @brief The distance from nodePtr
 * @param nodePtr
 * @return int
 */
double basic_node::distance_to(basic_node *nodePtr)
{
    Enter_Method_Silent(); // Omnet requires this
    return sqrt((this->x_pos - nodePtr->x_pos) * (this->x_pos - nodePtr->x_pos) + (this->y_pos - nodePtr->y_pos) * (this->y_pos - nodePtr->y_pos));
}

void basic_node::determineNodesInRadioRadio()
{
    basic_node *nPtr;
    double distance;
    // ic
    for (int i = 0; i < this->g_ic_num; ++i)
    {
        nPtr = check_and_cast<basic_node *>(this->networkPtr->getSubmodule("ic", i));
        distance = this->distance_to(nPtr);
        if (distance <= this->tx_range && nPtr->g_node_id != this->g_node_id)
        {
            this->nodesInRadioRange.push_back(std::make_pair(nPtr, distance));
        }
    }
    // icc
    nPtr = check_and_cast<basic_node *>(this->networkPtr->getSubmodule("icc"));
    distance = this->distance_to(nPtr);
    if (distance <= this->tx_range && nPtr->g_node_id != this->g_node_id)
    {
        this->nodesInRadioRange.push_back(std::make_pair(nPtr, distance));
    }
    // sink node
    nPtr = check_and_cast<basic_node *>(this->networkPtr->getSubmodule("sink"));
    distance = this->distance_to(nPtr);
    if (distance <= this->tx_range && nPtr->g_node_id != this->g_node_id)
    {
        this->nodesInRadioRange.push_back(std::make_pair(nPtr, distance));
    }
    this->nodesInRadioRange.sort([](const std::pair<basic_node *, int> &p1, const std::pair<basic_node *, int> &p2)
                                 { return p1.second < p2.second; });
}

bool basic_node::ringAction()
{
    if ((this->g_ic_loc % 2) == 0)
    {
        int startPoint = this->g_ic_loc / 2 + 1;
        if (startPoint > g_ic_message_num)
        {
            return false;
        }
    }
    return true;
}

bool basic_node::ringAction_pulsar()
{
    if ((this->g_ic_loc % 2) == 1)
    {
        int startPoint = this->g_ic_loc / 2 + 1;
        if (startPoint > g_ic_message_num)
        {
            return false;
        }
    }
    return true;
}

void basic_node::ringReduce()
{
    simtime_t ptr = simTime();
    if (this->g_node_id == 3)
    {
        EV << "to do ben";
    }
    if ((this->g_ic_dynamic_loc % 2) == 0)
    {
        if ((this->g_ic_loc % 2) == 0)
        {
            if (this->ringAction())
            {
                bool findPkt = false;
                for (auto pkt : this->transmission_queue)
                {
                    if (pkt.getMsg_id() == this->ring_packet_start_seq)
                    {
                        findPkt = true;
                    }
                }
                if (this->transmission_queue[0].getPass_counter() > 0)
                {
                    findPkt = true;
                }
                if (findPkt == true)
                {
                    this->g_reduction_bias_num = 1;
                    this->g_ic_dynamic_loc = (this->g_ic_scale_loc + 1) % this->g_ic_syn_cycle;
                    this->g_if_ic_sending_packets = ic_send_state;
                    this->g_if_reduction_recovery = true;
                    this->ic_listen_counter = 0;
                }
                else
                {
                    this->g_reduction_bias_num = 0;
                    this->g_if_takeup = true;
                    this->g_if_ic_sending_packets = ic_listen_state;
                }
            }
            else
            {
                this->g_reduction_bias_num = 0;
                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
            }
        }
        else
        {
            ptr = simTime();
            if (this->g_ic_reduction_recovery_execution_signal == true)
            {
                this->g_ic_reduction_recovery_execution_signal = false;
                int bias = this->g_ic_dynamic_loc - this->g_ic_scale_loc;
                if (bias < 0)
                {
                    this->g_reduction_bias_num = this->g_ic_scale_loc - this->g_ic_dynamic_loc;
                }
                else
                {
                    this->g_reduction_bias_num = this->g_ic_syn_cycle - this->g_ic_dynamic_loc + this->g_ic_scale_loc;
                }
                this->g_ic_dynamic_loc = this->g_ic_scale_loc;
                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
                this->ic_listen_counter = 0;
            }
            else
            {
                this->g_reduction_bias_num = this->g_ic_syn_cycle - this->g_ic_scale_loc + this->g_ic_dynamic_loc;
                this->ic_listen_counter = 0;
                this->g_if_ic_sending_packets = ic_send_state;
                this->g_if_reduction_recovery = true;
            }
        }
    }
    else
    {
        if ((this->g_ic_loc % 2) == 0)
        {
            // recovery from the bias location
            if (this->g_ic_reduction_recovery_execution_signal == true)
            {
                this->g_ic_reduction_recovery_execution_signal = false;
                int bias = this->g_ic_dynamic_loc - this->g_ic_scale_loc;
                if (bias < 0)
                {
                    this->g_reduction_bias_num = this->g_ic_scale_loc - this->g_ic_dynamic_loc;
                }
                else
                {
                    this->g_reduction_bias_num = this->g_ic_syn_cycle - this->g_ic_dynamic_loc + this->g_ic_scale_loc;
                }
                this->g_ic_dynamic_loc = this->g_ic_scale_loc;

                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
                this->ic_listen_counter = 0;
            }
        }
        else
        {
            this->g_reduction_bias_num = 0;
            this->g_if_takeup = true;
            this->g_if_ic_sending_packets = ic_listen_state;
        }
    }
}

void basic_node::ringReduce_find()
{
    simtime_t ptr = simTime();
    if ((this->g_ic_dynamic_loc % 2) == 0)
    {
        if ((this->g_ic_loc % 2) == 0)
        {
            if (this->ringAction())
            {
                bool findPkt = false;
                for (auto pkt : this->transmission_queue)
                {
                    if (pkt.getMsg_id() == this->ring_packet_start_seq)
                    {
                        findPkt = true;
                    }
                }
                if (this->transmission_queue[0].getPass_counter() > 0)
                {
                    findPkt = true;
                }
                if (findPkt == true)
                {
                    this->g_reduction_bias_num = 1;
                    this->g_ic_dynamic_loc = (this->g_ic_loc + 1) % this->g_ic_cycle;
                    this->g_if_ic_sending_packets = ic_send_state;
                    this->g_if_reduction_recovery = true;
                    this->ic_listen_counter = 0;
                }
                else
                {
                    this->g_reduction_bias_num = 0;
                    this->g_if_takeup = true;
                    this->g_if_ic_sending_packets = ic_listen_state;
                }
            }
            else
            {
                this->g_reduction_bias_num = 0;
                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
            }
        }
        else
        {
            ptr = simTime();
            if (this->g_ic_reduction_recovery_execution_signal == true)
            {
                this->g_ic_reduction_recovery_execution_signal = false;
                int bias = this->g_ic_dynamic_loc - this->g_ic_loc;
                if (bias < 0)
                {
                    this->g_reduction_bias_num = this->g_ic_loc - this->g_ic_dynamic_loc;
                }
                else
                {
                    this->g_reduction_bias_num = this->g_ic_syn_cycle - this->g_ic_dynamic_loc + this->g_ic_loc;
                }
                this->g_ic_dynamic_loc = this->g_ic_loc;
                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
                this->ic_listen_counter = 0;
            }
            else
            {
                this->g_reduction_bias_num = 1;
                this->ic_listen_counter = 0;
                this->g_if_ic_sending_packets = ic_send_state;
                this->g_if_reduction_recovery = true;
            }
        }
    }
    else
    {
        if ((this->g_ic_loc % 2) == 0)
        {
            // recovery from the bias location
            if (this->g_ic_reduction_recovery_execution_signal == true)
            {
                this->g_ic_reduction_recovery_execution_signal = false;
                int bias = this->g_ic_dynamic_loc - this->g_ic_loc;
                if (bias < 0)
                {
                    this->g_reduction_bias_num = this->g_ic_loc - this->g_ic_dynamic_loc;
                }
                else
                {
                    this->g_reduction_bias_num = this->g_ic_syn_cycle - this->g_ic_dynamic_loc + this->g_ic_loc;
                }
                this->g_ic_dynamic_loc = this->g_ic_loc;
                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
                this->ic_listen_counter = 0;
            }
        }
        else
        {
            this->g_reduction_bias_num = 0;
            this->g_if_takeup = true;
            this->g_if_ic_sending_packets = ic_listen_state;
        }
    }
}

void basic_node::ringReduce_pulsar()
{
    simtime_t ptr = simTime();
    if ((this->g_ic_dynamic_loc % 2) == 1)
    {
        if ((this->g_ic_loc % 2) == 1)
        {
            if (this->ringAction_pulsar())
            {
                bool findPkt = false;
                for (auto pkt : this->transmission_queue)
                {
                    if (pkt.getMsg_id() == this->ring_packet_start_seq)
                    {
                        findPkt = true;
                    }
                }
                if (this->transmission_queue[0].getPass_counter() > 0)
                {
                    findPkt = true;
                }
                if (findPkt == true)
                {
                    this->g_reduction_bias_num = 1;
                    this->g_ic_dynamic_loc = (this->g_ic_loc + 1) % this->g_ic_cycle;
                    this->g_if_ic_sending_packets = ic_send_state;
                    this->g_if_reduction_recovery = true;
                    // pulsar adaptive
                    if (this->g_ic_dynamic_loc == 0)
                    {
                        this->g_ic_dynamic_loc = (this->g_ic_loc + 2) % this->g_ic_cycle;
                        this->g_reduction_bias_num = 2;
                    }
                    this->ic_listen_counter = 0;
                }
                else
                {
                    this->g_reduction_bias_num = 0;
                    this->g_if_takeup = true;
                    this->g_if_ic_sending_packets = ic_listen_state;
                }
            }
            else
            {
                this->g_reduction_bias_num = 0;
                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
            }
        }
        else
        {
            ptr = simTime();
            if (this->g_ic_reduction_recovery_execution_signal == true)
            {
                this->g_ic_reduction_recovery_execution_signal = false;
                int bias = this->g_ic_dynamic_loc - this->g_ic_loc;
                if (bias < 0)
                {
                    this->g_reduction_bias_num = this->g_ic_loc - this->g_ic_dynamic_loc;
                }
                else
                {
                    this->g_reduction_bias_num = this->g_ic_cycle - this->g_ic_dynamic_loc + this->g_ic_loc;
                }
                this->g_ic_dynamic_loc = this->g_ic_loc;
                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
                this->ic_listen_counter = 0;
            }
            else
            {
                this->g_reduction_bias_num = 1;
                this->g_if_ic_sending_packets = ic_send_state;
                this->g_if_reduction_recovery = true;
                // pulsar adaptive
                if (this->g_ic_dynamic_loc == 1)
                {
                    this->g_reduction_bias_num = 2;
                }
                this->ic_listen_counter = 0;
            }
        }
    }
    else
    {
        if ((this->g_ic_loc % 2) == 1)
        {
            // recovery from the bias location
            if (this->g_ic_reduction_recovery_execution_signal == true)
            {
                this->g_ic_reduction_recovery_execution_signal = false;
                int bias = this->g_ic_dynamic_loc - this->g_ic_loc;
                if (bias < 0)
                {
                    this->g_reduction_bias_num = this->g_ic_loc - this->g_ic_dynamic_loc;
                }
                else
                {
                    this->g_reduction_bias_num = this->g_ic_cycle - this->g_ic_dynamic_loc + this->g_ic_loc;
                }
                this->g_ic_dynamic_loc = this->g_ic_loc;
                this->g_if_takeup = true;
                this->g_if_ic_sending_packets = ic_listen_state;
                this->ic_listen_counter = 0;
            }
        }
        else
        {
            this->g_reduction_bias_num = 0;
            this->g_if_takeup = true;
            this->g_if_ic_sending_packets = ic_listen_state;
        }
    }
}
