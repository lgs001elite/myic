import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv


syn_methods = ["Find", "Flync", "Pulsar", "Free_beacon"]
syn_methods_name = ["Find", "Flync_Find", "Pulsar", "FreeBeacon"]

syn_legend_names = ["Medians", "means"]

scale_sets = [10, 16, 20, 24, 30, 36, 40, 48, 50]
scale_sets_name = ["10", "16", "20", "24", "30", "36", "40", "48", "50"]

#energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace", "Office_trace", "Stairs_trace", "Washer_trace"]
#energy_scenarios_names = ["Static", "Random", "Cars trace", "Jogging trace", "Office trace", "Stairs trace", "Washer trace"]

energy_scenarios = ["Static_trace", "Jogging_trace"]
energy_scenarios_names = ["#Static_trace", "#Jogging_trace"]

title ="scale_with_51"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick', "purple", "tomato",
"pink", "red", "cyan"]

find_static_10        = []
flync_static_10       = []
pulsar_static_10      = []
free_beacon_static_10 = []

find_static_16        = []
flync_static_16       = []
pulsar_static_16      = []
free_beacon_static_16 = []

find_static_20        = []
flync_static_20       = []
pulsar_static_20      = []
free_beacon_static_20 = []

find_static_24        = []
flync_static_24       = []
pulsar_static_24      = []
free_beacon_static_24 = []

find_static_30        = []
flync_static_30       = []
pulsar_static_30      = []
free_beacon_static_30 = []

find_static_36        = []
flync_static_36       = []
pulsar_static_36      = []
free_beacon_static_36 = []

find_static_40        = []
flync_static_40       = []
pulsar_static_40      = []
free_beacon_static_40 = []

find_static_48        = []
flync_static_48       = []
pulsar_static_48      = []
free_beacon_static_48 = []

find_static_50        = []
flync_static_50       = []
pulsar_static_50      = []
free_beacon_static_50 = []


find_complex_10        = []
flync_complex_10       = []
pulsar_complex_10      = []
free_beacon_complex_10 = []

find_complex_16        = []
flync_complex_16       = []
pulsar_complex_16      = []
free_beacon_complex_16 = []

find_complex_20        = []
flync_complex_20       = []
pulsar_complex_20      = []
free_beacon_complex_20 = []

find_complex_24        = []
flync_complex_24       = []
pulsar_complex_24      = []
free_beacon_complex_24 = []

find_complex_30        = []
flync_complex_30       = []
pulsar_complex_30      = []
free_beacon_complex_30 = []

find_complex_36        = []
flync_complex_36       = []
pulsar_complex_36      = []
free_beacon_complex_36 = []

find_complex_40        = []
flync_complex_40       = []
pulsar_complex_40      = []
free_beacon_complex_40 = []

find_complex_48        = []
flync_complex_48       = []
pulsar_complex_48      = []
free_beacon_complex_48 = []

find_complex_50        = []
flync_complex_50       = []
pulsar_complex_50      = []
free_beacon_complex_50 = []


find_cars_10        = []
flync_cars_10       = []
pulsar_cars_10      = []
free_beacon_cars_10 = []

find_cars_16        = []
flync_cars_16       = []
pulsar_cars_16      = []
free_beacon_cars_16 = []

find_cars_20        = []
flync_cars_20       = []
pulsar_cars_20      = []
free_beacon_cars_20 = []

find_cars_24        = []
flync_cars_24       = []
pulsar_cars_24      = []
free_beacon_cars_24 = []

find_cars_30        = []
flync_cars_30       = []
pulsar_cars_30      = []
free_beacon_cars_30 = []

find_cars_36        = []
flync_cars_36       = []
pulsar_cars_36      = []
free_beacon_cars_36 = []

find_cars_40        = []
flync_cars_40       = []
pulsar_cars_40      = []
free_beacon_cars_40 = []

find_cars_48        = []
flync_cars_48       = []
pulsar_cars_48      = []
free_beacon_cars_48 = []

find_cars_50        = []
flync_cars_50       = []
pulsar_cars_50      = []
free_beacon_cars_50 = []

find_jogging_10        = []
flync_jogging_10       = []
pulsar_jogging_10      = []
free_beacon_jogging_10 = []

find_jogging_16        = []
flync_jogging_16       = []
pulsar_jogging_16      = []
free_beacon_jogging_16 = []

find_jogging_20        = []
flync_jogging_20       = []
pulsar_jogging_20      = []
free_beacon_jogging_20 = []

find_jogging_24        = []
flync_jogging_24       = []
pulsar_jogging_24      = []
free_beacon_jogging_24 = []

find_jogging_30        = []
flync_jogging_30       = []
pulsar_jogging_30      = []
free_beacon_jogging_30 = []

find_jogging_36        = []
flync_jogging_36       = []
pulsar_jogging_36      = []
free_beacon_jogging_36 = []

find_jogging_40        = []
flync_jogging_40       = []
pulsar_jogging_40      = []
free_beacon_jogging_40 = []

find_jogging_48        = []
flync_jogging_48       = []
pulsar_jogging_48      = []
free_beacon_jogging_48 = []

find_jogging_50        = []
flync_jogging_50       = []
pulsar_jogging_50      = []
free_beacon_jogging_50 = []

find_office_10        = []
flync_office_10       = []
pulsar_office_10      = []
free_beacon_office_10 = []

find_office_16        = []
flync_office_16       = []
pulsar_office_16      = []
free_beacon_office_16 = []

find_office_20        = []
flync_office_20       = []
pulsar_office_20      = []
free_beacon_office_20 = []

find_office_24        = []
flync_office_24       = []
pulsar_office_24      = []
free_beacon_office_24 = []

find_office_30        = []
flync_office_30       = []
pulsar_office_30      = []
free_beacon_office_30 = []

find_office_36        = []
flync_office_36       = []
pulsar_office_36      = []
free_beacon_office_36 = []

find_office_40        = []
flync_office_40       = []
pulsar_office_40      = []
free_beacon_office_40 = []

find_office_48        = []
flync_office_48       = []
pulsar_office_48      = []
free_beacon_office_48 = []

find_office_50        = []
flync_office_50       = []
pulsar_office_50      = []
free_beacon_office_50 = []


find_stairs_10        = []
flync_stairs_10       = []
pulsar_stairs_10      = []
free_beacon_stairs_10 = []

find_stairs_16        = []
flync_stairs_16       = []
pulsar_stairs_16      = []
free_beacon_stairs_16 = []

find_stairs_20        = []
flync_stairs_20       = []
pulsar_stairs_20      = []
free_beacon_stairs_20 = []

find_stairs_24        = []
flync_stairs_24       = []
pulsar_stairs_24      = []
free_beacon_stairs_24 = []

find_stairs_30        = []
flync_stairs_30       = []
pulsar_stairs_30      = []
free_beacon_stairs_30 = []

find_stairs_36        = []
flync_stairs_36       = []
pulsar_stairs_36      = []
free_beacon_stairs_36 = []

find_stairs_40        = []
flync_stairs_40       = []
pulsar_stairs_40      = []
free_beacon_stairs_40 = []

find_stairs_48        = []
flync_stairs_48       = []
pulsar_stairs_48      = []
free_beacon_stairs_48 = []

find_stairs_50        = []
flync_stairs_50       = []
pulsar_stairs_50      = []
free_beacon_stairs_50 = []



find_washer_10        = []
flync_washer_10       = []
pulsar_washer_10      = []
free_beacon_washer_10 = []

find_washer_16        = []
flync_washer_16       = []
pulsar_washer_16      = []
free_beacon_washer_16 = []

find_washer_20        = []
flync_washer_20       = []
pulsar_washer_20      = []
free_beacon_washer_20 = []

find_washer_24        = []
flync_washer_24       = []
pulsar_washer_24      = []
free_beacon_washer_24 = []

find_washer_30        = []
flync_washer_30       = []
pulsar_washer_30      = []
free_beacon_washer_30 = []

find_washer_36        = []
flync_washer_36       = []
pulsar_washer_36      = []
free_beacon_washer_36 = []

find_washer_40        = []
flync_washer_40       = []
pulsar_washer_40      = []
free_beacon_washer_40 = []

find_washer_48        = []
flync_washer_48       = []
pulsar_washer_48      = []
free_beacon_washer_48 = []

find_washer_50        = []
flync_washer_50       = []
pulsar_washer_50      = []
free_beacon_washer_50 = []



# free beacond
data_sets = \
[
[free_beacon_static_10, free_beacon_complex_10, free_beacon_cars_10, free_beacon_jogging_10, free_beacon_office_10, 
 free_beacon_stairs_10, free_beacon_washer_10],

[free_beacon_static_16, free_beacon_complex_16, free_beacon_cars_16, free_beacon_jogging_16, free_beacon_office_16, 
 free_beacon_stairs_16, free_beacon_washer_16],

[free_beacon_static_20, free_beacon_complex_20, free_beacon_cars_20, free_beacon_jogging_20, free_beacon_office_20, 
 free_beacon_stairs_20, free_beacon_washer_20],

[free_beacon_static_24, free_beacon_complex_24, free_beacon_cars_24, free_beacon_jogging_24, free_beacon_office_24, 
 free_beacon_stairs_24, free_beacon_washer_24],

[free_beacon_static_20, free_beacon_complex_20, free_beacon_cars_20, free_beacon_jogging_20, free_beacon_office_20, 
 free_beacon_stairs_20, free_beacon_washer_20],

[free_beacon_static_30, free_beacon_complex_30, free_beacon_cars_30, free_beacon_jogging_30, free_beacon_office_30, 
 free_beacon_stairs_30, free_beacon_washer_30],

[free_beacon_static_36, free_beacon_complex_36, free_beacon_cars_36, free_beacon_jogging_36, free_beacon_office_36, 
 free_beacon_stairs_36, free_beacon_washer_36],

[free_beacon_static_40, free_beacon_complex_40, free_beacon_cars_40, free_beacon_jogging_40, free_beacon_office_40, 
 free_beacon_stairs_40, free_beacon_washer_40],

[free_beacon_static_48, free_beacon_complex_48, free_beacon_cars_48, free_beacon_jogging_48, free_beacon_office_48, 
 free_beacon_stairs_48, free_beacon_washer_48],

[free_beacon_static_50, free_beacon_complex_50, free_beacon_cars_50, free_beacon_jogging_50, free_beacon_office_50, 
 free_beacon_stairs_50, free_beacon_washer_50]        
]


# collect the data
i = 0
for scale in scale_sets_name:
    j = 0
    for scenario in energy_scenarios:
        file = open("scalability_51_free_beacon_syn_in_"+ scenario.upper()+"_"+ scale+".csv", mode='r')
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_sets[i][j].append(int(row[0]))
        j += 1
    i += 1

scenarios_len = len(energy_scenarios_names)
methods_len = len(syn_methods_name)
nums_len = len(scale_sets)

# plot the data
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 5))
# Set global font size
fontSize = 14
plt.rcParams.update({'font.size': 14})
lineWidth = 2
    

for i in range(scenarios_len):
    _ax = ax[i]
    # Initialize lists to store medians and means
    all_medians = []
    all_means = []
    for j in range(nums_len):
        boxplot = _ax.boxplot(data_sets[j][i], positions= [j + 1], patch_artist=True,
            boxprops=dict(facecolor=colors[j], color=colors[j], edgecolor=colors[j]),
            whiskerprops=dict(color=colors[j], linewidth=lineWidth),
            capprops=dict(color=colors[j], linewidth=lineWidth),
            medianprops=dict(color=colors[j], linewidth=lineWidth),
            flierprops=dict(marker='o', markerfacecolor=colors[j], markeredgecolor=colors[j], markersize=lineWidth, alpha=0.5),
            showmeans=True,
            meanprops=dict(markerfacecolor=colors[j], markeredgecolor=colors[j], markersize=lineWidth, alpha=0.5),
            )
        # Extract median and mean for this box plot
        median = boxplot['medians'][0].get_ydata()[0]
        mean = boxplot['means'][0].get_ydata()[0]
        # Store medians and means
        all_medians.append((j + 1,median))
        all_means.append((j + 1,mean))
    # Unpack medians and means into x and y coordinates
    median_x, median_y = zip(*all_medians)
    mean_x, mean_y = zip(*all_means)

    # Connect medians and means with lines
    colors_legend = ["plum", "navy"]
    _ax.plot(median_x, median_y, color=colors_legend[0], linestyle='--', linewidth=2, marker='o')
    _ax.plot(mean_x, mean_y, color=colors_legend[1], linestyle='--', linewidth=2, marker='o')
    if i == 0:
        handles = [plt.Line2D([0], [0], color=color, lw=2) for color in colors_legend]
        _ax.legend(handles, syn_legend_names, loc='upper right')
    _ax.set_yscale('log')
    _ax.set_ylabel("Latency (Time Slots)", fontsize=fontSize)
    _ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    _ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    _ax.set_xlabel(energy_scenarios_names[i])
    _ax.tick_params(axis='both', which='major', labelsize=fontSize)
    _ax.set_xticks([])

plt.tight_layout()
fig.savefig(f""+title+"_simulation.pdf", format="pdf", bbox_inches='tight')




