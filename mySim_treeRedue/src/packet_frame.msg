packet packet_frame {
    int dest_id; 
    int source_id;       
    int sender_id;        
    int msg_type;         
    int msg_id;          
    int charge_cycle;
    int origin_slot;
    int current_slot;
    int lag_bias;
    int delay_bias;
    int sender_type;
    int next_id;
    int vir_id;
    int pass_counter;
    int node_state;
    int reduce_phase;
//    int ic_pass_number;
//    bool sent_flag;
    simtime_t send_time;
}

