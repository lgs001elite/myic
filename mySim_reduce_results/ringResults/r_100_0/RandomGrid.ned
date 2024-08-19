
network RandomGrid
{
    parameters:
        int map_width       = default(10);
        int map_height      = default(10);
        int init_flag          = default(0);
        int g_ic_num            = default(30);
        int g_energy_model  = default(0);
        int g_reduce_scheme = default(0);
        int poweroff_rate = default(0);
        bool power_off_switch  = default(false);
    submodules:
        sink:basic_node;
        icc: basic_node;
        ic[100]: basic_node;
}



