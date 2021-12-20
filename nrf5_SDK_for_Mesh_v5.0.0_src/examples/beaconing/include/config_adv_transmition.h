/**
 * config the paramters in mesh network
 */
//uint8_t  g_start_broadcast = 0;
//uint8_t  g_hop_dimension = 0xFB;
//uint8_t  g_sink_dimension = 0x01;
//uint8_t  g_present_received_address = 0xff;
//uint8_t  g_dest_address = 0x00;
//uint8_t  g_present_packet_seq = 0xff;
//uint8_t  g_pre_packet_seq = 0xff;
//uint8_t  g_received_address = 0xff;
//uint8_t  g_received_seqnum = 0xff;
//uint32_t g_adv_packet_number = 0;
//uint32_t g_packet_j = 0;
//uint8_t  g_seq_packet = 0;
//bool     g_is_send_next = true;
//bool     g_if_received_address = true;
//bool     g_if_ended = false;
//bool     g_if_adv_enable = false;
//bool     g_if_received_node = false;
//bool     g_if_send_data = false;
//bool     g_if_send_finish = false;
//bool     g_if_start_ending = false;
//extern bool     g_if_first_ack = true;
extern volatile bool     g_if_sendNext;
extern volatile bool     g_now_send_ack_packets;
extern volatile bool     g_now_send_adv_packets;
extern volatile bool     g_now_send_end_packets;
