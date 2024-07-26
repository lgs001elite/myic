
/* Copyright (c) 2024, Vrije Universiteit Amsterdam
 * Contributor: Gaosheng Liu
 * All rights reserved.
 */

#include "ic_node.h"
#include "packet_frame_m.h"
#include <string>
using namespace std;

/**
 * @brief initialization functions
 *
 */
void basic_node::net_initialize()
{
    this->node_type = this->par("node_type");
    this->slot_len = (double)this->par("transmission_duration");
    this->tx_range = this->par("tx_range");
    this->radioInGatePtr = this->gate("ICNodeRadioIn");
    this->g_ic_num = this->networkPtr->par("g_ic_num");
    this->g_ic_cycle = this->networkPtr->par("g_ic_num");
    this->g_queue_len = 0;
    // Starting to initialize every parameter of nodes in the network
    int init_flag = (int)this->networkPtr->par("init_flag");
    if (init_flag == 0)
    {
        this->networkPtr->par("init_flag") = 1;
        this->topology_distribution();
    }
    else
    {
        this->distributeLocalNodeVector();
    }

    if (this->node_type == type_ic_node)
    {
        this->ic_collision_check_counter = 0;
        this->ic_attempt_counter = 0;
        this->charge_model = this->networkPtr->par("g_energy_model");
        this->g_if_node_distribution = false;
        this->g_ic_loc = -1;
        this->delay_global_location = 0;
        this->rx_state = false;
        this->g_if_ic_sending_packets = IDLE_STATE;
        this->g_ic_node_ready_reduce = false;
        this->g_ic_dynamic_loc = -1;
        this->g_next_id = -1;
        this->g_ic_self_delay_signal = false;
        this->g_ic_reduction_recovery_execution_signal = false;
        this->ic_reduce_algorithm = this->networkPtr->par("g_reduce_scheme");
        this->g_ic_current_seq_loc = 0;
        this->g_if_produce_packets = false;
        this->g_reduction_bias_num = 0;
        this->g_if_reduction_recovery = false;
        this->g_if_takeup = false;
        this->g_if_power_off = this->networkPtr->par("power_off_switch");
        // ring-reduce
        if (this->ic_reduce_algorithm == ring_reduce_algorithm)
        {
            int extra = this->g_ic_num % 2;
            int step  = this->g_ic_num /2;
            if ((this->g_node_id%2) == 0)
            {
                this->ring_packet_start_seq= this->g_node_id/2;
            }
            this->ring_packet_send_len = step + extra;
        }
    }

    if (this->node_type == type_icc_node)
    {
        this->icc_charging_cycle = 7;
        this->icc_collision_check_counter = 0;
        this->rx_state = false;
        this->icc_global_location = 0;
    }

    if (this->node_type == type_sink_node)
    {
        this->sink_collision_check_counter = 0;
        this->rx_state = true;
        this->g_sink_check_all_is_ready = false;
        this->discovery_time = registerSignal("discovery_time");
        this->sim_time = registerSignal("sim_time");
    }
    // Every node decides which nodes are in its communication range
    this->determineNodesInRadioRadio();
    scheduleAt(simTime(), new cMessage("Starting actions after the network initialization", network_initial));
}

void basic_node::distributeLocalNodeVector()
{
    // Distribute ICC nodes
    this->icc_networkHandler.push_back(
        check_and_cast<basic_node *>(this->networkPtr->getSubmodule("icc")));
    // Distribute IC nodes
    for (int ic_index = 0; ic_index < this->g_ic_num; ic_index++)
    {
        this->ic_networkHandler.push_back(
            check_and_cast<basic_node *>(this->networkPtr->getSubmodule("ic", ic_index)));
    }
    // Distribute the sink node
    this->sink_networkHandler.push_back(
        check_and_cast<basic_node *>(this->networkPtr->getSubmodule("sink")));
}

void basic_node::topology_distribution()
{
    int x_sink = 5;
    int y_sink = 5;
    // Distribute coordinator nodes
    this->icc_networkHandler.push_back(check_and_cast<basic_node *>(this->networkPtr->getSubmodule("icc")));
    this->icc_networkHandler[0]->g_node_id = this->g_ic_num;
    auto &displayString = this->icc_networkHandler[0]->getDisplayString();
    basic_node::Point pos(x_sink, y_sink);
    this->icc_networkHandler[0]->place_nodes(pos.x, pos.y);
    displayString.setTagArg("p", 0, pos.x);
    displayString.setTagArg("p", 1, pos.y);
    displayString.setTagArg("is", 0, "vs");

    // Distribute IC nodes
    for (int ic_index = 0; ic_index < this->g_ic_num; ic_index++)
    {
        this->ic_networkHandler.push_back(check_and_cast<basic_node *>(this->networkPtr->getSubmodule("ic", ic_index)));
        this->ic_networkHandler[ic_index]->g_node_id = ic_index;
        auto &displayString = this->ic_networkHandler[ic_index]->getDisplayString();
        double x_posR = uniform(0, 10);
        double y_posR = uniform(0, 10);
        basic_node::Point pos(x_posR, y_posR);
        this->ic_networkHandler[ic_index]->place_nodes(pos.x, pos.y);
        displayString.setTagArg("p", 0, pos.x);
        displayString.setTagArg("p", 1, pos.y);
        displayString.setTagArg("is", 0, "vs");
    }

    // Distribute the sink node
    this->sink_networkHandler.push_back(check_and_cast<basic_node *>(this->networkPtr->getSubmodule("sink")));
    this->sink_networkHandler[0]->g_node_id = this->g_ic_num + 1;
    auto &displayString3 = this->sink_networkHandler[0]->getDisplayString();
    basic_node::Point pos2(x_sink, y_sink);
    this->sink_networkHandler[0]->place_nodes(pos2.x, pos2.y);
    displayString3.setTagArg("p", 0, pos2.x);
    displayString3.setTagArg("p", 1, pos2.y);
    displayString3.setTagArg("is", 0, "vs");
}

void basic_node::set_chargingTimeAndDelay()
{
    simtime_t ptr = simTime();
    this->ic_charge_cycle = intuniform(this->energy_range_set[this->charge_model][0],
                                       this->energy_range_set[this->charge_model][1]) + 1;
    // aligh with icc to find topology
    int delay_bias = this->ic_charge_cycle % g_ic_cycle;
    if (delay_bias != 0)
    {
        delay_bias = g_ic_cycle - delay_bias;
    }
    // judge if power off
    if (this->g_if_power_off == true)
    {
         int probNum = intuniform(1, 100);
         if (probNum <= 5)
         {
             //this->g_if_power_off = false;
             int tempChr = intuniform(0, g_ic_cycle - 1);
             if (tempChr > 0)
             {
                 delay_bias = delay_bias + tempChr;
             }
             if ((tempChr > 0) && (this->g_ic_loc != -1))
             {
                 EV<<"bias happend";
             }
        }
    }
    // actual charge plus delay time
    this->ic_charge_cycle = this->ic_charge_cycle + delay_bias;
}

void basic_node::generate_msgs()
{
    // Produce packets
    for (int i = 0; i < g_ic_message_num; i++)
    {
        packet_frame *send_msg = this->produce_msg(g_ic_message_num - i - 1, data_msg, type_ic_node, -1);
        this->g_queue_len = this->g_queue_len + 1;
        this->transmission_queue.insert(this->transmission_queue.begin(), *send_msg);
        delete send_msg;
    }
}

void basic_node::checkEndSim()
{
    if (this->g_queue_len == g_ic_message_num)
    {
        emit(this->sim_time, simTime(), nullptr);
        endSimulation();
    }
}

void basic_node::checkAllReady()
{
    if (this->g_sink_check_all_is_ready == true)
    {
        return;
    }
    // first check ic nodes' location information
    if (this->g_sink_check_all_is_ready == false)
    {
        this->g_sink_check_all_is_ready = true;
        for (int ic_index = 0; ic_index < this->g_ic_num; ic_index++)
        {
            if (this->ic_networkHandler[ic_index]->g_if_node_distribution == false)
            {
                this->g_sink_check_all_is_ready = false;
                break;
            }
        }
    }
    // After syn completed, starting to reduce
    if (this->g_sink_check_all_is_ready == true)
    {
        // endSimulation();
        emit(this->discovery_time, simTime(), nullptr);
        for (int ic_index = 0; ic_index < this->g_ic_num; ic_index++)
        {
            this->ic_networkHandler[ic_index]->g_ic_node_ready_reduce = true;
            this->ic_networkHandler[ic_index]->ic_attempt_counter = 0;
        }
    }
}

/**
 * @brief handleMessage functions
 *  This is for processing every kind of self-messages and radio messages
 */
void basic_node::net_handleMessage(cMessage *msg)
{
    // Initailize node charging time
    if (msg->isSelfMessage() && msg->getKind() == network_initial)
    {
        simtime_t ptr = simTime();
        // Go to the sink function entrance if the node is sink node
        if (this->node_type == type_sink_node)
        {
            scheduleAt(simTime(), new cMessage("Go to the sink node", sink_handler));
        }
        // Go to the icc function entrance if the node is the icc node
        if (this->node_type == type_icc_node)
        {
            /*
              Go to the icc node, firstly icc node needs to sleep
              some certain rounds before
            */
            scheduleAt(simTime(), new cMessage("Go the icc node", icc_sleep_handler));
        }
        // Go to the ic function entrance if the node is the ic node
        if (this->node_type == type_ic_node)
        {
            // Calculate first delay
            this->set_chargingTimeAndDelay();
            // Go to the ic with an initial random location on the distribution cycle
            scheduleAt(simTime() + this->slot_len * intuniform(0, g_ic_cycle - 1),
                       new cMessage("Go to the ic node", ic_sleep_handler));
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == sink_handler)
    {
        simtime_t ptr = simTime();
        this->checkAllReady();
        this->checkEndSim();
        scheduleAt(simTime() + this->slot_len,
                   new cMessage("sink starts a new working slot", sink_handler));
        // Initialize the collision number after every working slot
        this->sink_collision_check_counter = 0;
    }
    else if (msg->isSelfMessage() && msg->getKind() == ic_sleep_handler)
    {
        simtime_t ptr = simTime();
        this->rx_state = false;
        int extraRound = 0;
        if (this->ic_attempt_counter >= g_ic_cycle)
        {
            extraRound = g_ic_cycle * intuniform(0, 1);
            //this->ic_attempt_counter = 0;
        }
        // ic back to its distrited location
        if (this->delay_global_location > 0)
        {
            extraRound = extraRound + this->delay_global_location;
            this->delay_global_location = 0;
        }
        scheduleAt(simTime() + this->slot_len * (this->ic_charge_cycle - 1 + extraRound),
                   new cMessage("ic charging and delaying", ic_work_handler));
    }
    else if (msg->isSelfMessage() && msg->getKind() == icc_sleep_handler)
    {
        simtime_t ptr = simTime();
        this->rx_state = false;
        /*
           The charging cycle of icc is 7, so, it needs to sleep 6 slots and work 1 slot
        */
        scheduleAt(simTime() + this->slot_len * (this->icc_charging_cycle - 1),
                   new cMessage("icc charging", icc_work_handler));
    }
    else if (msg->isSelfMessage() && msg->getKind() == ic_work_handler)
    {
        simtime_t ptr = simTime();
        //int currTime = int(ptr);
        if (this->g_ic_self_delay_signal == true)
        {
            this->g_ic_self_delay_signal = false;

            if (this->g_if_ic_sending_packets == ic_send_state)
            {
                this->ic_transmitData();
            }
            this->ic_collision_check_counter = 0;
            this->rx_state = true;
            this->set_chargingTimeAndDelay();
            scheduleAt(simTime() + this->slot_len,
                       new cMessage("ic from working to sleep ", ic_sleep_handler));
        }
        else
        {
            // restore from poweroff
            int timeout = int(SIMTIME_DBL(ptr) * 1000) + 1;
            int bias = 0;
            bool actionSignal = true;
            if (((timeout%7) == 0) && (this->g_ic_dynamic_loc != -1))
            {
                int currentLoc = timeout%this->g_ic_cycle;
                int realLoc = this->g_ic_loc;
                if (this->g_if_ic_sending_packets == ic_send_state)
                {
                    realLoc = (this->g_ic_loc + 1) %this->g_ic_cycle;
                }
                if (currentLoc != realLoc)
                {
                    actionSignal = false;
                    if (realLoc < currentLoc)
                    {
                         bias = this->g_ic_cycle + realLoc - currentLoc;
                    }
                    else
                    {
                         bias = realLoc - currentLoc;
                    }
                    //this->g_ic_dynamic_loc = realLoc;
                }
            }
            if ((this->g_ic_loc != this->g_ic_dynamic_loc) && (actionSignal == true))
            {
                if (((this->g_ic_loc + 1) % g_ic_cycle) != this->g_ic_dynamic_loc)
                {
                    int currentLoc = timeout%this->g_ic_cycle;
                    int realLoc = this->g_ic_loc;
                    if (this->g_if_ic_sending_packets == ic_send_state)
                    {
                        realLoc = (this->g_ic_loc + 1) %this->g_ic_cycle;
                    }
                    if (realLoc < currentLoc)
                    {
                        bias = this->g_ic_cycle + realLoc - currentLoc;
                    }
                    else
                    {
                        bias = realLoc - currentLoc;
                    }
                    //this->g_ic_dynamic_loc = realLoc;
                }
            }
            int delaySlots = 0;
            if (this->g_ic_loc == -1)
            {
                this->transmitIdleBroadcast(nullptr);
                if (this->ic_attempt_counter < g_ic_cycle)
                {
                    this->ic_attempt_counter = this->ic_attempt_counter + 1;
                }
            }
            else
            {
                // Starting to reduce operation after every
                // ic node has been distributed the unique location
                if (this->g_ic_node_ready_reduce == true)
                {
                     // Generate packets
                     if (this->g_if_produce_packets == false)
                     {
                          // Only generate packets once
                          this->generate_msgs();
                          this->g_if_produce_packets = true;
                     }
                     delaySlots = this->ic_reduceAction();
                }
            }
            delaySlots = delaySlots + bias;
            this->g_ic_self_delay_signal = true;
            scheduleAt(simTime() + this->slot_len * delaySlots,
                       new cMessage("ic delays some time for transmiting to its next", ic_work_handler));
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == icc_work_handler)
    {
        simtime_t ptr = simTime();
        this->icc_global_location = (this->icc_global_location + this->icc_charging_cycle) % g_ic_cycle;
        this->rx_state = true;
        this->icc_collision_check_counter = 0;
        //*** This is just for poweroff scenarios
        /*
        int tempInt = intuniform(0,100);
        if (tempInt < int(50))
        {
            scheduleAt(simTime() + this->slot_len * 0.1, new cMessage("icc node sends rectify loc to ics", icc_check_handler));
        }
        */

        //***
        scheduleAt(simTime() + this->slot_len,
                   new cMessage("icc charging", icc_sleep_handler));
    }
    else if ((msg->getArrivalGate() == this->radioInGatePtr) && this->rx_state)
    {
        simtime_t ptr = simTime();
        // Receive and process the message
        packet_frame *receivedMsg = check_and_cast<packet_frame *>(msg)->dup();
        this->receive_message(receivedMsg);
        delete receivedMsg;
    }
    else if (msg->isSelfMessage() && msg->getKind() == icc_check_ack_handler)
    {
        simtime_t ptr = simTime();
        if (this->icc_collision_check_counter == 1)
        {
            // The location of the ic node on the distributed cycle is same as its id number
            int sender_id = this->g_receivedMsg.getSender_id();
            this->sink_neigh_icc_distribution.insert(pair<int, int>(sender_id, sender_id));
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == sink_receive_data_handler)
    {
        simtime_t ptr = simTime();
        if (this->sink_collision_check_counter == 1)
        {
            // received data and do sth here
            this->transmission_queue.insert(this->transmission_queue.begin(), this->g_receivedMsg);
            g_queue_len = g_queue_len + 1;
            // If the sink node received the msgs successfully, it will give a ack reply
            scheduleAt(simTime() + this->slot_len * 0.1,
                       new cMessage("sink node sends acks", sink_send_ack_handler));
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == sink_send_ack_handler)
    {
        simtime_t ptr = simTime();
        this->transmitAck();
    }
    else if (msg->isSelfMessage() && msg->getKind() == sink_ack_new_handler)
    {
        simtime_t ptr = simTime();
        this->transmitSinkAck();
    }
    else if (msg->isSelfMessage() && msg->getKind() == ic_receive_data_handler)
    {
        simtime_t ptr = simTime();
        if (this->ic_collision_check_counter == 1)
        {
            // Do sth here for reduce data
            // Step1: Check the msg with same id in the msg queue
            // Step2: check if find the msg_type in the vector
            auto pkt_i = find_if(this->transmission_queue.cbegin(), this->transmission_queue.cend(), [this](packet_frame pkt)
                                 { return pkt.getMsg_id() == this->g_receivedMsg.getMsg_id(); });
            if (pkt_i != this->transmission_queue.end())
            {
                if (this->ic_reduce_algorithm == ring_reduce_algorithm)
                {
                    if (this->g_if_takeup == true)
                    {
                        this->g_if_takeup = false;
                    }
                    if ((this->g_ic_loc % 2) != 0)
                    {
                        this->g_ic_dynamic_loc = (this->g_ic_loc + 1) % this->g_ic_cycle;
                    }
                    int localPassNum = pkt_i->getPass_counter();
                    this->transmission_queue.erase(pkt_i);
                    // Step2: increase the reduce number
                    int previousPassNum = this->g_receivedMsg.getPass_counter();
                    if (localPassNum == 0)
                    {
                        if (previousPassNum == 0)
                        {
                            this->g_receivedMsg.setPass_counter(previousPassNum + 2);
                        }
                        else
                        {
                            this->g_receivedMsg.setPass_counter(previousPassNum + 1);
                        }
                        this->transmission_queue.insert(this->transmission_queue.begin(), this->g_receivedMsg);
                    }
                }
            }
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == ic_receive_icc_rectify_handler)
    {
        simtime_t ptr = simTime();
        int currentLoc = this->g_receivedMsg.getCurrent_slot();
        if ((this->ic_collision_check_counter == 1) && (this->g_ic_loc != -1)&&
                (this->g_ic_dynamic_loc != currentLoc))
        {
            int bias = 0;
            if (this->g_ic_dynamic_loc < currentLoc)
            {
                  bias = g_ic_cycle + g_ic_dynamic_loc - currentLoc;
            }
            else
            {
                  bias = g_ic_dynamic_loc - currentLoc;
            }
            this->ic_collision_check_counter = 0;
            this->delay_global_location = bias;
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == ic_receive_broad_handler)
    {
        simtime_t ptr = simTime();
        int currentLoc = this->g_receivedMsg.getCurrent_slot();
        if (this->ic_collision_check_counter == 1)
        {
            int bias = 0;
            if (this->g_ic_loc == -1)
            {
                this->g_ic_loc = this->g_node_id;
                this->g_ic_dynamic_loc = this->g_node_id;
                this->ic_attempt_counter = 0;
                this->g_if_node_distribution = true;

                if (this->g_ic_loc < currentLoc)
                {
                     bias = this->g_ic_cycle + g_ic_loc - currentLoc;
                }
                else
                {
                     bias = g_ic_loc - currentLoc;
                }
            }
            this->delay_global_location = bias;
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == ic_receive_ack_handler)
    {
        simtime_t ptr = simTime();
        if (this->ic_collision_check_counter == 1)
        {
            // Judge if recover to its original location
            this->ic_attempt_counter = 0;
            if (this->ic_reduce_algorithm == ring_reduce_algorithm)
            {
                // received data and do sth here
                if (this->transmission_queue.cbegin()->getPass_counter() > 0)
                {
                    auto checkPkt = this->transmission_queue.begin();
                    if (checkPkt->getPass_counter() != (this->g_ic_num - 1))
                    {
                        if (this->g_if_reduction_recovery == true)
                        {
                            this->g_if_reduction_recovery = false;
                            this->g_ic_reduction_recovery_execution_signal = true;
                        }
                    }
                    else
                    {
                        EV<<"terminal node";
                    }
                    this->transmission_queue.erase(this->transmission_queue.begin());
                }
                else
                {
                    auto pkt_i = find_if(this->transmission_queue.cbegin(), this->transmission_queue.cend(), [this](packet_frame pkt)
                                                 { return pkt.getMsg_id() == this->ring_packet_start_seq; });
                    if (pkt_i != this->transmission_queue.end())
                    {
                         if (this->g_if_reduction_recovery == true)
                         {
                              this->g_if_reduction_recovery = false;
                              this->g_ic_reduction_recovery_execution_signal = true;
                         }
                        this->transmission_queue.erase(pkt_i);
                    }
                    this->ring_packet_start_seq = this->ring_packet_start_seq + this->ring_packet_send_len;
                }
                this->g_queue_len = this->g_queue_len - 1;
            }
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == ic_send_ack_data_handler)
    {
        simtime_t ptr = simTime();
        if (this->ic_collision_check_counter == 1)
        {
            this->transmitAck();
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == ic_send_ack_broad_handler)
    {
        simtime_t ptr = simTime();
        if (this->ic_collision_check_counter == 1)
        {
            this->transmitAck();
        }
    }
    else if (msg->isSelfMessage() && msg->getKind() == icc_broad_handler)
    {
        simtime_t ptr = simTime();
        if (this->icc_collision_check_counter == 1)
        {
            this->transmitIdleBroadcast(&this->g_receivedMsg);
        }
        this->icc_collision_check_counter = 0;
    }
    else if (msg->isSelfMessage() && msg->getKind() == icc_check_handler)
    {
        this->iccCheck();
    }
    else
    {
        // Nothing to do here, waiting for deletion
    }
    delete msg;
}

/**
 the next queued data msg to all neighbours in radio range.
 */
int basic_node::ic_reduceAction()
{
    simtime_t ptr = simTime();
    int delaySlots = 0;
    if (this->ic_reduce_algorithm == ring_reduce_algorithm)
    {
        if ((this->g_ic_loc % 2) == 0)
        {
             if ((((g_ic_message_num -this->g_queue_len) % this->ring_packet_send_len) == 0) && (g_ic_message_num > this->g_queue_len))
             {
                 if (this->g_if_takeup == true)
                 {
                      this->g_if_takeup = false;
                 }
             }
        }

        if ((this->g_if_reduction_recovery == false) && (this->g_if_takeup == false))
        {
            if (this->g_queue_len > 0)
            {
                this->ringReduce();
                delaySlots = this->g_reduction_bias_num;
            }
        }

    }

    return delaySlots;
}

void basic_node::ic_transmitData()
{
    if (this->g_queue_len > 0)
    {
        packet_frame *mPtr = &this->transmission_queue[0];
        if (ic_reduce_algorithm == ring_reduce_algorithm)
        {
            if (mPtr->getPass_counter() == 0)
            {
                auto pkt_i = find_if(this->transmission_queue.begin(), this->transmission_queue.end(), [this](packet_frame pkt)
                                                                { return pkt.getMsg_id() == this->ring_packet_start_seq; });
                if (pkt_i != this->transmission_queue.end())
                {
                    mPtr = &(*pkt_i);
                }
            }
        }
        mPtr->setSender_id(this->g_node_id);
        mPtr->setCurrent_slot(this->g_ic_dynamic_loc);
        // if complete reduce data, next hop is sink node
        if (mPtr->getPass_counter() == this->g_ic_num)
        {
            mPtr->setNext_id((this->g_ic_num + 1));
        }
        else
        {
            mPtr->setNext_id(this->g_ic_dynamic_loc);
        }
        for (auto p : this->nodesInRadioRange)
        {
            this->sendDirect(mPtr->dup(), p.first, "ICNodeRadioIn");
        }

        // attempting increases one and do reduce
        if (this->ic_attempt_counter < g_ic_cycle)
        {
            this->ic_attempt_counter = this->ic_attempt_counter + 1;
        }
    }
}

void basic_node::transmitAck()
{
    // Send a copy of the message to each node in radio range
    for (auto p : this->nodesInRadioRange)
    {
        this->sendDirect(this->g_ack->dup(), p.first, "ICNodeRadioIn");
    }
}

void basic_node::transmitSinkAck()
{
    // Send a copy of the message to each node in radio range
    for (auto p : this->nodesInRadioRange)
    {
        this->sendDirect(this->g_sink_ack->dup(), p.first, "ICNodeRadioIn");
    }
}

void basic_node::transmitIdleBroadcast(packet_frame *packet)
{
    simtime_t ptr = simTime();
    packet_frame *msg_broad;
    if (this->node_type == type_ic_node)
    {
        msg_broad = this->produce_msg(0, broad_msg, type_ic_node, -1);
    }
    else
    {
        msg_broad = this->produce_msg(0, broad_msg, type_icc_node, -1);
        msg_broad->setNext_id(packet->getSender_id());
        msg_broad->setCurrent_slot(this->icc_global_location);
    }

    for (auto p : this->nodesInRadioRange)
    {
        this->sendDirect(msg_broad->dup(), p.first, "ICNodeRadioIn");
    }
    delete msg_broad;
}


void basic_node::iccCheck()
{
    simtime_t ptr = simTime();
    packet_frame *msg_broad;
    msg_broad = this->produce_msg(0, icc_check_msg, type_icc_node, -1);
    msg_broad->setCurrent_slot(this->icc_global_location); // (this->icc_global_location + 1)%g_ic_cycle

    for (auto p : this->nodesInRadioRange)
    {
        this->sendDirect(msg_broad->dup(), p.first, "ICNodeRadioIn");
    }
    delete msg_broad;
}

/**
 * Receiving and processing packets
 */
void basic_node::receive_message(packet_frame *dMsg)
{
    simtime_t ptr = simTime();
    // first duplicate received msg, to prevent deleting msg unexpectedly
    this->duplicate_msg(&this->g_receivedMsg, dMsg);
    // retrieve some info from the packet
    int msg_type = dMsg->getMsg_type();
    int sender_type = dMsg->getSender_type();
    int sender_id = dMsg->getSender_id();
    int delay_bias = dMsg->getDelay_bias();
    int msg_id = dMsg->getMsg_id();
    int source_id = dMsg->getSource_id();
    int next_id = dMsg->getNext_id();
    int origin_slot = dMsg->getOrigin_slot();
    int current_loc = dMsg->getCurrent_slot();
    // process the msgs that received by the sink node
    if ((this->node_type == type_sink_node) && (next_id == this->g_node_id))
    {
        // Statistic the recieved msgs in a time window
        this->sink_collision_check_counter = this->sink_collision_check_counter + 1;
        if ((msg_type == data_msg) && (sender_type == type_ic_node))
        {
            // First, need to check if the packet has been received
            bool receivedMsg = false;
            for (int i = 0; i < this->g_queue_len; i++)
            {
                packet_frame preMsg = this->transmission_queue[i];
                if ((preMsg.getMsg_id() == msg_id) && (preMsg.getSource_id() == source_id))
                {
                    receivedMsg = true;
                    break;
                }
            }
            // Whatever, the sink needs to replay ack if it received msgs and no collisions
            this->g_ack = this->produce_msg(msg_id, ack_msg, type_sink_node, sender_id);
            // new round
            int tempId = sender_id - 1;
            if (tempId < 0)
            {
                tempId = this->g_ic_num + tempId;
            }
            this->g_sink_ack= this->produce_msg(0, sink_ack_msg, type_sink_node, tempId);
            if (receivedMsg == false)
            {
                this->scheduleAt(simTime() + this->slot_len * 0.1,
                                 new cMessage("Sink processes the received msgs", sink_receive_data_handler));
            }
        }
    }

    // process the msgs that received by the icc node
    if (this->node_type == type_icc_node)
    {
        // Statistic the recieved msgs in a time window
        this->icc_collision_check_counter = this->icc_collision_check_counter + 1;
        /*
           ICC received random data/ack packages.
           It will check if the sender (ICs) in its right position
           if not, icc will reply to the sender with right location information
        */
        if ((next_id != this->g_node_id) && (current_loc != -1))
        {
            if (current_loc != this->icc_global_location)
            {

                scheduleAt(simTime() + this->slot_len * 0.1,
                           new cMessage("icc node sends loc to ics", icc_broad_handler));
            }
        }
        /*
           If icc received the ack from an ic , that is sent to it.
           Icc confirms that location has been distributed to the ic
        */
        else if ((msg_type == ack_msg) && (next_id == this->g_node_id))
        {
            scheduleAt(simTime() + this->slot_len * 0.1,
                       new cMessage("icc checks the ack info", icc_check_ack_handler));
        }

        /*
           Initially, ic nodes broadcast packets if ic nodes have not got the location
           from icc node.
        */
        else if (msg_type == broad_msg)
        {
            scheduleAt(simTime() + this->slot_len * 0.1,
                       new cMessage("icc node sends loc to ics", icc_broad_handler));
        }
        else
        {

        }
    }

    // process the msgs that received by the ic node
    if (this->node_type == type_ic_node)
    {
        this->ic_collision_check_counter = this->ic_collision_check_counter + 1;
        // Statistic the recieved msgs in a time window
        if ((msg_type == broad_msg) && (sender_type == type_icc_node))
        {
            this->scheduleAt(simTime() + this->slot_len * 0.1,
                             new cMessage("ic node receives the broad from ic", ic_receive_broad_handler));
            this->g_ack = this->produce_msg(msg_id, ack_msg, type_ic_node, sender_id);
            // Whatever, the sink needs to replay ack
            scheduleAt(simTime() + this->slot_len * 0.2,
                       new cMessage("ic node sends acks to icc", ic_send_ack_broad_handler));
        }
        else if((msg_type == icc_check_msg) && (sender_type == type_icc_node))
        {
            this->scheduleAt(simTime() + this->slot_len * 0.1,
                                         new cMessage("ic node receives rectify info from icc", ic_receive_icc_rectify_handler));
        }
        else
        {
            if (next_id == this->g_node_id)
            {
                if ((msg_type == data_msg) && (this->g_if_takeup == true))
                {
                    // First, need to check if the packet has been received
                    this->scheduleAt(simTime() + this->slot_len * 0.1,
                                     new cMessage("ic node receives the data from the sender ic node", ic_receive_data_handler));
                    this->g_ack = this->produce_msg(msg_id, ack_msg, type_ic_node, sender_id);
                    scheduleAt(simTime() + this->slot_len * 0.2,
                               new cMessage("ic node sends acks", ic_send_ack_data_handler));
                }
                else if (msg_type == ack_msg)
                {
                    this->scheduleAt(simTime() + this->slot_len * 0.1,
                        new cMessage("ic node receives the ack from the sender ic node", ic_receive_ack_handler));
                }
                else
                {

                }
            }
        }
    }
}
