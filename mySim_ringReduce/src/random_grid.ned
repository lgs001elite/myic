
package src;
network RandomGrid
{
    parameters:
        int map_width       = default(10);
        int map_height      = default(10);
        int init_flag          = default(0);
        int g_ic_num            = default(0);
        int g_energy_model  = default(0);
        int poweroff_rate = default(0);
        int g_syn_scheme = default(0);
        int g_ic_freebeacon_syn_cycle = default(0);
    submodules:
        sink:basic_node;
        icc: basic_node;
        ic[30]: basic_node;
}



