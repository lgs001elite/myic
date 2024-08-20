import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv
import glob



cycle_sets = [30, 51, 100]
cycle_sets_name = ["30", "51", "100"]

node_num_sets = [2, 12, 30]
node_num_sets_name = ["[2 nodes]", "[12 nodes]", "[30 nodes]"]

energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace", "Office_trace", "Stairs_trace", "Washer_trace"]
energy_scenarios_names = ["Static", "Random", "Cars trace", "Jogging trace", "Office trace", "Stairs trace", "Washer trace"]

title ="cdf_30-51-100_compare"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick']

#
free_beacon_static_30_2  = []
free_beacon_static_51_2  = []
free_beacon_static_100_2 = []

free_beacon_static_30_12  = []
free_beacon_static_51_12  = []
free_beacon_static_100_12 = []

free_beacon_static_30_30  = []
free_beacon_static_51_30  = []
free_beacon_static_100_30 = []
#



#
free_beacon_random_30_2 = []
free_beacon_random_51_2 = []
free_beacon_random_100_2= []

free_beacon_random_30_12 = []
free_beacon_random_51_12 = []
free_beacon_random_100_12= []

free_beacon_random_30_30 = []
free_beacon_random_51_30 = []
free_beacon_random_100_30= []
#



#
free_beacon_cars_30_2 = []
free_beacon_cars_51_2 = []
free_beacon_cars_100_2= []

free_beacon_cars_30_12 = []
free_beacon_cars_51_12 = []
free_beacon_cars_100_12= []


free_beacon_cars_30_30 = []
free_beacon_cars_51_30 = []
free_beacon_cars_100_30= []
#



#
free_beacon_jogging_30_2  = []
free_beacon_jogging_51_2  = []
free_beacon_jogging_100_2 = []

free_beacon_jogging_30_12  = []
free_beacon_jogging_51_12  = []
free_beacon_jogging_100_12 = []


free_beacon_jogging_30_30  = []
free_beacon_jogging_51_30  = []
free_beacon_jogging_100_30 = []
#


#
free_beacon_office_30_2  = []
free_beacon_office_51_2  = []
free_beacon_office_100_2 = []

free_beacon_office_30_12  = []
free_beacon_office_51_12  = []
free_beacon_office_100_12 = []

free_beacon_office_30_30  = []
free_beacon_office_51_30  = []
free_beacon_office_100_30 = []
#



#
free_beacon_stairs_30_2  = []
free_beacon_stairs_51_2  = []
free_beacon_stairs_100_2 = []

free_beacon_stairs_30_12  = []
free_beacon_stairs_51_12  = []
free_beacon_stairs_100_12 = []


free_beacon_stairs_30_30  = []
free_beacon_stairs_51_30  = []
free_beacon_stairs_100_30 = []
#


#
free_beacon_washer_30_2  = []
free_beacon_washer_51_2  = []
free_beacon_washer_100_2 = []

free_beacon_washer_30_12  = []
free_beacon_washer_51_12  = []
free_beacon_washer_100_12 = []

free_beacon_washer_30_30  = []
free_beacon_washer_51_30  = []
free_beacon_washer_100_30 = []
#


fontSize  = 12

lineWidth = 1.5



data_sets =[
    [
        [free_beacon_static_30_2, free_beacon_static_51_2, free_beacon_static_100_2], 
        [free_beacon_static_30_12, free_beacon_static_51_12, free_beacon_static_100_12], 
        [free_beacon_static_30_30, free_beacon_static_51_30, free_beacon_static_100_30], 
    ],
    
    [
        [free_beacon_random_30_2, free_beacon_random_51_2, free_beacon_random_100_2],
        [free_beacon_random_30_12, free_beacon_random_51_12, free_beacon_random_100_12],
        [free_beacon_random_30_30, free_beacon_random_51_30, free_beacon_random_100_30],
    ],

    [
        [free_beacon_cars_30_2, free_beacon_cars_51_2, free_beacon_cars_100_2],
        [free_beacon_cars_30_12, free_beacon_cars_51_12, free_beacon_cars_100_12],
        [free_beacon_cars_30_30, free_beacon_cars_51_30, free_beacon_cars_100_30],
    ],

    [          
        [free_beacon_jogging_30_2, free_beacon_jogging_51_2, free_beacon_jogging_100_2], 
        [free_beacon_jogging_30_12, free_beacon_jogging_51_12, free_beacon_jogging_100_12], 
        [free_beacon_jogging_30_30, free_beacon_jogging_51_30, free_beacon_jogging_100_30], 
    ],

    [
        [free_beacon_office_30_2, free_beacon_office_51_2, free_beacon_office_100_2], 
        [free_beacon_office_30_12, free_beacon_office_51_12, free_beacon_office_100_12], 
        [free_beacon_office_30_30, free_beacon_office_51_30, free_beacon_office_100_30], 
    ],

    [
        [free_beacon_stairs_30_2, free_beacon_stairs_51_2, free_beacon_stairs_100_2], 
        [free_beacon_stairs_30_12, free_beacon_stairs_51_12, free_beacon_stairs_100_12], 
        [free_beacon_stairs_30_30, free_beacon_stairs_51_30, free_beacon_stairs_100_30], 
    ],

    [
        [free_beacon_washer_30_2, free_beacon_washer_51_2, free_beacon_washer_100_2],
        [free_beacon_washer_30_12, free_beacon_washer_51_12, free_beacon_washer_100_12],
        [free_beacon_washer_30_30, free_beacon_washer_51_30, free_beacon_washer_100_30]
    ]
]


# collect the data
i = 0
for scenario in energy_scenarios:
    j = 0
    for num in node_num_sets:
        k = 0
        for cycle in cycle_sets_name:
            file = open(glob.glob("no_poweroff_"+cycle+"*_beacon_syn_in_"+
            scenario.upper()+"_"+ str(num)+".csv")[0], mode='r')
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_sets[i][j][k].append(int(row[0]))
            k += 1
        j += 1
    i += 1



scenarios_len = len(energy_scenarios_names)
num_len = len(node_num_sets_name)
cycle_len = len(cycle_sets)


fig, ax = plt.subplots(nrows=7, ncols=3, figsize=(10, 15))
markers = ['x', '+', 's', 'v']

lineStyles  = ['-', '--', '-.', ':']  

for i in range(scenarios_len):
    for j in range(num_len):
        _ax = ax[i][j]
        for k in range(cycle_len):
            dataSet = data_sets[i][j][k]
            sorted_set = np.sort(dataSet)
            cdf = np.arange(1, len(sorted_set) + 1) / len(sorted_set)
            _ax.plot(sorted_set, cdf, marker=markers[k], color = colors[k], linestyle = lineStyles[k],
                     linewidth=1, markersize=0.5)

        if j == 0:
           _ax.set_ylabel("CDF", fontsize=fontSize)
        _ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        _ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        _ax.tick_params(axis='both', which='major', labelsize=fontSize)
        if (i == (scenarios_len -1)):
            _ax.set_xlabel(node_num_sets_name[j])
        #_ax.set_xticks([])
        _ax.tick_params(axis='both', which='major', labelsize=fontSize)


handles = [plt.Line2D([0], [0], color=color, lw=1) for color in colors]
fig.legend(handles, cycle_sets_name, loc='upper right')
plt.tight_layout()
fig.savefig(f""+title+"_simulation.pdf", format="pdf", bbox_inches='tight')













