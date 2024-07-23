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
energy_scenarios_names = ["Static", "Random", "Cars trace", "Jogging trace", 
"Office trace", "Stairs trace", "Washer trace"]

energy_legend_names = ["Static", "Random", "Cars trace", "Jogging trace", 
"Office trace", "Stairs trace", "Washer trace","medians", "means"]

title ="box_30-51-100_compare"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick', "purple", "tomato"]


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
        # Initialize lists to store medians and means
        all_medians = []
        all_means = []
        for k in range(cycle_len):
            boxplot = _ax.boxplot(data_sets[i][j][k], positions= [k + i * (cycle_len + 1) + 1], patch_artist=True,
            boxprops=dict(facecolor=colors[k], color=colors[k], edgecolor=colors[k]),
            whiskerprops=dict(color=colors[k], linewidth=lineWidth),
            capprops=dict(color=colors[k], linewidth=lineWidth),
            medianprops=dict(color=colors[k], linewidth=lineWidth),
            flierprops=dict(marker='o', markerfacecolor=colors[k], markeredgecolor=colors[k], markersize=lineWidth, alpha=0.5),
            showmeans=True)
            # Extract median and mean for this box plot
            median = boxplot['medians'][0].get_ydata()[0]
            mean = boxplot['means'][0].get_ydata()[0]
            # Store medians and means
            all_medians.append((k + i * (cycle_len + 1) + 1,median))
            all_means.append((k + i * (cycle_len + 1) + 1,mean))
        # Unpack medians and means into x and y coordinates
        median_x, median_y = zip(*all_medians)
        mean_x, mean_y = zip(*all_means)
        # Connect medians and means with lines
        _ax.plot(median_x, median_y, color=colors[4], linestyle='--', linewidth=2, marker='o')
        _ax.plot(mean_x, mean_y, color=colors[5], linestyle='--', linewidth=2, marker='o')

        if j == 0:
           _ax.set_ylabel("Latency (Time Slots)", fontsize=fontSize)
        _ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        _ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        _ax.set_yscale('log')
        _ax.set_xticks([])
        _ax.tick_params(axis='both', which='major', labelsize=fontSize)


handles = [plt.Line2D([0], [0], color=color, lw=7) for color in colors]
fig.legend(handles, energy_legend_names, loc='upper right')
fig.savefig(f""+title+"_simulation.pdf", format="pdf", bbox_inches='tight')







