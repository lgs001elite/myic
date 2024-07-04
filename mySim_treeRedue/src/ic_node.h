/* Copyright (c) 2024, Vrije Universiteit Amsterdam
 * Contributor: Gaosheng Liu
 * All rights reserved.
 */

#ifndef __ICNode_H
#define __ICNode_H

#include <omnetpp.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cmath>
#include <iomanip>
#include <list>
#include <queue>
#include <utility>
#include <random>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm> // for std::find_if
#include <map>
#include <math.h>
#include "packet_frame_m.h"

using namespace omnetpp;
using namespace std;

// define info states
#define network_initial 0x01
#define sink_handler    0x02
#define ic_sleep_handler 0x03
#define icc_sleep_handler 0x04
#define ic_work_handler 0x06
#define icc_work_handler 0x07
#define sink_receive_data_handler 0x08
#define sink_send_ack_handler 0x09
#define ic_receive_data_handler 0x0A
#define ic_send_ack_data_handler 0x0B
#define ic_send_ack_broad_handler 0x10
#define ic_receive_broad_handler 0x0C
#define icc_broad_handler 0x0D
#define ic_receive_ack_handler 0x0F
#define icc_check_ack_handler 0xA1
#define sink_ack_new_handler 0xA2
#define tree_signal_handler 0xA3
#define tree_send_handler 0xA4

// define msg types
#define broad_msg   0x00
#define ack_msg     0x01
#define data_msg 0x02
#define sink_ack_msg     0x03
#define tree_send_signal 0x04

// define node types
#define type_ic_node 1
#define type_icc_node  2
#define type_sink_node 0

// define the reduce algorithms
#define tree_reduce_algorithm 0
#define linked_list_reduce_algorithm 1
#define ring_reduce_algorithm 2

// define ic nodes states
#define ic_pos_syn_state   0
#define ic_neg_syn_state   1
#define IDLE_STATE 2
#define g_ic_message_num 30

class basic_node : public cSimpleModule
{
private:
    struct SIM_API Point
    {
        double x, y;
        Point(double x, double y) : x(x), y(y) {}
    };
    vector<packet_frame> transmission_queue;
    int g_queue_len;
    packet_frame g_receivedMsg;
    packet_frame *g_ack;
    packet_frame *g_sink_ack;

    bool g_sink_check_all_is_ready;
    bool g_ic_node_ready_reduce;
    bool g_if_node_distribution;
    bool g_if_takeup;
    int g_ic_loc;
    int delay_global_location;
    int icc_global_location;
    int g_if_ic_syn_packets;

    // Simulator Knowledge
    double x_pos;
    double y_pos;
    list<pair<basic_node *, int>> nodesInRadioRange;
    int g_ic_num;
    int g_ic_cycle;
    int ic_charge_cycle;
    int charge_model;
    int ic_attempt_counter;
    int ic_collision_check_counter;
    bool g_if_produce_packets;
    bool g_if_power_off;
    int node_type;
    int g_node_id;
    int g_node_virtual_id;
    int g_ic_virtual_num;
    int g_next_id;
    bool g_link_received_signal;
    int tx_range;
    int g_reduction_bias_num;
    bool g_if_reduction_recovery;
    bool g_ic_self_delay_signal;
    bool g_ic_reduction_recovery_execution_signal;
    bool g_tree_if_listen_wait;
    bool g_if_do_reduce;
    int g_ic_dynamic_loc;
    int g_ic_current_seq_loc;
    int sink_collision_check_counter;
    int ic_reduce_algorithm;
    int ic_tree_reduce_phase;

    int linked_list_packet_send_len;
    int linked_list_packet_start_seq;

    map<int, int> sink_neigh_icc_distribution;
    int icc_charging_cycle;
    int icc_collision_check_counter;

    cGate *radioInGatePtr;
    bool rx_state;

    cModule *networkPtr;
    vector<basic_node *> ic_networkHandler;
    vector<basic_node *> icc_networkHandler;
    vector<basic_node *> sink_networkHandler;

    int energy_range_set[3][2] = {{5, 15}, {40, 120}, {100, 500}};

    simsignal_t discovery_time;
    simsignal_t sim_time;
    double slot_len;
    mt19937 rng;
    void topology_distribution();
    void determineNodesInRadioRadio();

    virtual void initialize();
    void net_initialize();
    virtual void handleMessage(cMessage *msg);
    void net_handleMessage(cMessage *msg);
    double distance_to(basic_node *nodePtr);
    packet_frame *produce_msg(int packet_id, int msg_type, int sender_type, int next_id);
    void receive_message(packet_frame *dMsg);
    void duplicate_msg(packet_frame *ori, packet_frame *dMsg);
    void place_nodes(int x_pos, int y_pos);
    void set_chargingTimeAndDelay();
    void generate_msgs();

    int ic_reduceAction();
    void ic_transmitData();
    void transmitAck();
    void transmitSinkAck();
    void ic_transmitDataToSink();
    void transmitIdleBroadcast(packet_frame *packet);

    int treeReduce();
    void checkAllReady();
    void checkEndSim();
    void ic_tree_send_signal();
    void ic_search_tree_virtualID();

    void distributeLocalNodeVector();

    bool ringAction();
    bool reduceDecision();
};

Define_Module(basic_node);
#endif
