simple basic_node
{
    parameters:    
        @signal[discovery_time](type=simtime_t);
        @statistic[discovery_time](title="discovery time"; source="discovery_time"; record=vector,histogram,last,min,max; interpolationmode=none);
        
        @signal[sim_time](type=simtime_t);
        @statistic[sim_time](title="simTime"; source="sim_time"; record=vector,histogram,last,min,max; interpolationmode=none);

        int     tx_range     = default(20) ;     
        double  transmission_duration  = default(0.001);
        int     node_id                = default(0);
        int     node_type              = default(0); 
        bool     g_if_produce_packets  = default(false);
        int     current_charge_cycle   = default(0);

    gates:
       input   ICNodeRadioIn @directIn;
}
