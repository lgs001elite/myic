import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv


syn_methods = ["Find", "Flync", "Pulsar", "Free_beacon"]
syn_methods_name = ["Find", "Flync_Find", "Pulsar", "FreeBeacon"]

node_sets = [2, 12, 30]
node_sets_name = ["2", "12", "30"]

energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace", "Office_trace", "Stairs_trace", "Washer_trace"]
energy_scenarios_names = ["Static", "Random", "Cars trace", "Jogging trace", "Office trace", "Stairs trace", "Washer trace"]

title ="free_beacon_with_30"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick']

find_static_2        = []
flync_static_2       = []
pulsar_static_2      = []
free_beacon_static_2 = []


find_static_12        = []
flync_static_12       = []
pulsar_static_12      = []
free_beacon_static_12 = []



find_static_30        = []
flync_static_30       = []
pulsar_static_30      = []
free_beacon_static_30 = []



find_random_2        = []
flync_random_2       = []
pulsar_random_2      = []
free_beacon_random_2 = []


find_random_12        = []
flync_random_12       = []
pulsar_random_12      = []
free_beacon_random_12 = []


find_random_30        = []
flync_random_30       = []
pulsar_random_30      = []
free_beacon_random_30 = []



find_cars_2        = []
flync_cars_2       = []
pulsar_cars_2      = []
free_beacon_cars_2 = []


find_cars_12        = []
flync_cars_12       = []
pulsar_cars_12      = []
free_beacon_cars_12 = []


find_cars_30        = []
flync_cars_30       = []
pulsar_cars_30      = []
free_beacon_cars_30 = []



find_jogging_2        = []
flync_jogging_2       = []
pulsar_jogging_2      = []
free_beacon_jogging_2 = []



find_jogging_12        = []
flync_jogging_12       = []
pulsar_jogging_12      = []
free_beacon_jogging_12 = []


find_jogging_30        = []
flync_jogging_30       = []
pulsar_jogging_30      = []
free_beacon_jogging_30 = []


find_office_2        = []
flync_office_2       = []
pulsar_office_2      = []
free_beacon_office_2 = []



find_office_12        = []
flync_office_12       = []
pulsar_office_12      = []
free_beacon_office_12 = []



find_office_30        = []
flync_office_30       = []
pulsar_office_30      = []
free_beacon_office_30 = []


find_stairs_2        = []
flync_stairs_2       = []
pulsar_stairs_2      = []
free_beacon_stairs_2 = []



find_stairs_12        = []
flync_stairs_12       = []
pulsar_stairs_12      = []
free_beacon_stairs_12 = []



find_stairs_30        = []
flync_stairs_30       = []
pulsar_stairs_30      = []
free_beacon_stairs_30 = []


find_washer_2        = []
flync_washer_2       = []
pulsar_washer_2      = []
free_beacon_washer_2 = []


find_washer_12        = []
flync_washer_12       = []
pulsar_washer_12      = []
free_beacon_washer_12 = []


find_washer_30        = []
flync_washer_30       = []
pulsar_washer_30      = []
free_beacon_washer_30 = []


fontSize  = 12

lineWidth = 1.5



data_sets = [[[find_static_2, find_static_12, find_static_30], [flync_static_2, flync_static_12, flync_static_30], 
                [pulsar_static_2, pulsar_static_12, pulsar_static_30], [free_beacon_static_2, free_beacon_static_12, free_beacon_static_30]], 
              [[find_random_2, find_random_12, find_random_30], [flync_random_2, flync_random_12, flync_random_30], 
                [pulsar_random_2, pulsar_random_12, pulsar_random_30], [free_beacon_random_2, free_beacon_random_12, free_beacon_random_30]], 
              [[find_cars_2, find_cars_12, find_cars_30], [flync_cars_2, flync_cars_12, flync_cars_30], 
                [pulsar_cars_2, pulsar_cars_12, pulsar_cars_30], [free_beacon_cars_2, free_beacon_cars_12, free_beacon_cars_30]],
              [[find_jogging_2, find_jogging_12, find_jogging_30], [flync_jogging_2, flync_jogging_12, flync_jogging_30], 
                [pulsar_jogging_2, pulsar_jogging_12, pulsar_jogging_30], [free_beacon_jogging_2, free_beacon_jogging_12, free_beacon_jogging_30]], 
              [[find_office_2, find_office_12, find_office_30], [flync_office_2, flync_office_12, flync_office_30], 
                [pulsar_office_2, pulsar_office_12, pulsar_office_30], [free_beacon_office_2, free_beacon_office_12, free_beacon_office_30]], 
              [[find_stairs_2, find_stairs_12, find_stairs_30], [flync_stairs_2, flync_stairs_12, flync_stairs_30], 
                [pulsar_stairs_2, pulsar_stairs_12, pulsar_stairs_30], [free_beacon_stairs_2, free_beacon_stairs_12, free_beacon_stairs_30]], 
              [[find_washer_2, find_washer_12, find_washer_30], [flync_washer_2, flync_washer_12, flync_washer_30], 
                [pulsar_washer_2, pulsar_washer_12, pulsar_washer_30], [free_beacon_washer_2, free_beacon_washer_12, free_beacon_washer_30]]]


# collect the data
i = 0
for scenario in energy_scenarios:
    j = 0
    for method in syn_methods:
        k = 0
        for num in node_sets:
            file = open("no_poweroff_30_general_"+ method.lower()+"_syn_in_"+ scenario.upper()+"_"+ str(num)+".csv", mode='r')
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_sets[i][j][k].append(int(row[0]))
            k += 1
        j += 1
    i += 1

scenarios_len = len(energy_scenarios_names)
methods_len = len(syn_methods_name)
nums_len = len(node_sets)

# plot the data
fig, ax = plt.subplots(nrows=3, ncols=7, figsize=(21, 9),constrained_layout=True)
    

for i in range(nums_len):
    for j in range(scenarios_len):
        _ax = ax[i][j]
        for k in range(methods_len):
            _ax.boxplot(data_sets[j][k][i], positions= [k + i * (methods_len + 1) + 1], patch_artist=True,
            boxprops=dict(facecolor=colors[k], color=colors[k], edgecolor=colors[k]),
            whiskerprops=dict(color=colors[k], linewidth=lineWidth),
            capprops=dict(color=colors[k], linewidth=lineWidth),
            medianprops=dict(color=colors[k], linewidth=lineWidth),
            flierprops=dict(marker='o', markerfacecolor=colors[k], markeredgecolor=colors[k], markersize=lineWidth, alpha=0.5))

        if j == 0:
           _ax.set_ylabel("Latency (Time Slots)", fontsize=fontSize)
        _ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        _ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        _ax.set_yscale('log')
        if (i == (nums_len -1)):
            _ax.set_xlabel(energy_scenarios_names[j])
        if (j == 3):
            _ax.set_title(node_sets_name[i]+" [nodes]")
        _ax.set_xticks([])
        _ax.tick_params(axis='both', which='major', labelsize=fontSize)


handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
fig.legend(handles, syn_methods_name, loc='upper right')
fig.savefig(f""+title+"_simulation.pdf", format="pdf", bbox_inches='tight')

