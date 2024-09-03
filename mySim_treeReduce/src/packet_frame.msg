packet packet_frame {
    int dest_id; 
    int source_id;       
    int sender_id;        
    int msg_type;         
    int msg_id;          
    bool syn_signal;
    int origin_slot;
    int current_slot;
    int scale_slot;
    int delay_bias;
    int sender_type;
    int next_id;
    int pass_counter;
    int node_state;
    int reduce_phase;
    simtime_t send_time;
}

