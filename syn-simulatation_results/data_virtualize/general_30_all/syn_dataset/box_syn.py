import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv


syn_methods = ["Find", "Flync", "Pulsar", "Free_beacon"]
syn_legend_names = ["Find", "Flync_Find", "Pulsar", "FreeBeacon", "Medians", "Means"]

node_sets = [2, 12, 30]
node_sets_name = ["2", "12", "30"]

energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace", "Office_trace", "Stairs_trace", "Washer_trace"]
energy_scenarios_names = ["Static trace", "Random trace", "Cars trace", "Jogging trace", "Office trace", "Stairs trace", "Washer trace"]

title ="free_beacon_with_30"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick', "purple", "tomato"]
styles = ['-', '-', '-', '-', '--', '--']

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
methods_len = len(syn_methods)
nums_len = len(node_sets)

# plot the data
fig, ax = plt.subplots(nrows=3, ncols=7, figsize=(21, 9),constrained_layout=True)
# Set global font size
fontSize = 18
plt.rcParams.update({'font.size': 18})
lineWidth = 1.5  

for i in range(nums_len):
    for j in range(scenarios_len):
        _ax = ax[i][j]
        # Initialize lists to store medians and means
        all_medians = []
        all_means = []
        for k in range(methods_len):
            boxplot = _ax.boxplot(data_sets[j][k][i], positions= [k + i * (methods_len + 1) + 1], patch_artist=True,
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
            all_medians.append((k + i * (methods_len + 1) + 1,median))
            all_means.append((k + i * (methods_len + 1) + 1,mean))
        print("ave:"+str(np.mean(data_sets[j][3][i])))
        # Unpack medians and means into x and y coordinates
        median_x, median_y = zip(*all_medians)
        mean_x, mean_y = zip(*all_means)

        # Connect medians and means with lines
        _ax.plot(median_x, median_y, color=colors[4], linestyle='--', linewidth=2, marker='o')
        _ax.plot(mean_x, mean_y, color=colors[5], linestyle='--', linewidth=2, marker='o')

        # Annotate difference
        # Calculate differences and annotate them on the plot
        for u in range(3):
            diff = mean_y[u] / mean_y[3]
            _ax.annotate(f'{diff:.2f}X', xy=(mean_x[u], mean_y[u]), xytext=(mean_x[u], max(mean_y[u], max(data_sets[j][u][i])) + mean_y[u]),
                ha='center', va='top', arrowprops=dict(facecolor='black', arrowstyle='->'),
            bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='yellow', alpha=0.8))
        # Set y_labels
        if j == 0:
           _ax.set_ylabel("Latency (Time Slots)", fontsize=fontSize)
        
        if (j == 6) and (i == 0):
            handles = [plt.Line2D([0], [0], color=color, lw=lineWidth, ls=style ) for color, style in zip(colors, styles)]
            _ax.legend(handles, syn_legend_names, loc='lower right')

        _ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        _ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        _ax.set_yscale('log')
        if (i == (nums_len -1)):
            _ax.set_xlabel(energy_scenarios_names[j], fontsize=(fontSize + 2))
        if (j == 3):
            _ax.set_title(node_sets_name[i]+" [nodes]")
        _ax.set_xticks([])
        _ax.tick_params(axis='both', which='major', labelsize=fontSize)

fig.savefig(f""+title+"_simulation.pdf", format="pdf", bbox_inches='tight')

