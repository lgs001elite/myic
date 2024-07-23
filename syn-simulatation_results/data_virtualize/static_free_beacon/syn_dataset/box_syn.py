import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv


syn_methods = ["Find", "Flync", "Pulsar", "Free_beacon"]
syn_methods_name = ["Find", "Flync_Find", "Pulsar", "FreeBeacon"]

syn_legend_names = ["Medians", "means"]

#static_sets = [10, 50, 100, 200, 300, 500]
static_sets = [50, 300, 500]

scale_sets = [10, 16, 20, 24, 30, 36, 40, 48, 50]
scale_sets_name = ["10", "16", "20", "24", "30", "36", "40", "48", "50"]

title ="scale_with_51_static_performance"
energy_scenarios =  ["Static_trace"] #["Static_trace", "Stairs_trace"]
energy_scenarios_names = ["Static"]  #["Static", "Stairs"]


colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick', "purple", "tomato",
"pink", "red", "cyan"]

c10_find_static_10        = []
c10_flync_static_10       = []
c10_pulsar_static_10      = []
c10_free_beacon_static_10 = []

c10_find_static_16        = []
c10_10flync_static_16     = []
c10_pulsar_static_16      = []
c10_free_beacon_static_16 = []

c10_find_static_20        = []
c10_flync_static_20       = []
c10_pulsar_static_20      = []
c10_free_beacon_static_20 = []

c10_find_static_24        = []
c10_flync_static_24       = []
c10_pulsar_static_24      = []
c10_free_beacon_static_24 = []

c10_find_static_30        = []
c10_flync_static_30       = []
c10_pulsar_static_30      = []
c10_free_beacon_static_30 = []

c10_find_static_36        = []
c10_flync_static_36       = []
c10_pulsar_static_36      = []
c10_free_beacon_static_36 = []

c10_find_static_40        = []
c10_flync_static_40       = []
c10_pulsar_static_40      = []
c10_free_beacon_static_40 = []

c10_find_static_48        = []
c10_flync_static_48       = []
c10_pulsar_static_48      = []
c10_free_beacon_static_48 = []

c10_find_static_50        = []
c10_flync_static_50       = []
c10_pulsar_static_50      = []
c10_free_beacon_static_50 = []



c50_find_static_10        = []
c50_flync_static_10       = []
c50_pulsar_static_10      = []
c50_free_beacon_static_10 = []

c50_find_static_16        = []
c50_10flync_static_16       = []
c50_pulsar_static_16      = []
c50_free_beacon_static_16 = []

c50_find_static_20        = []
c50_flync_static_20       = []
c50_pulsar_static_20      = []
c50_free_beacon_static_20 = []

c50_find_static_24        = []
c50_flync_static_24       = []
c50_pulsar_static_24      = []
c50_free_beacon_static_24 = []

c50_find_static_30        = []
c50_flync_static_30       = []
c50_pulsar_static_30      = []
c50_free_beacon_static_30 = []

c50_find_static_36        = []
c50_flync_static_36       = []
c50_pulsar_static_36      = []
c50_free_beacon_static_36 = []

c50_find_static_40        = []
c50_flync_static_40       = []
c50_pulsar_static_40      = []
c50_free_beacon_static_40 = []

c50_find_static_48        = []
c50_flync_static_48       = []
c50_pulsar_static_48      = []
c50_free_beacon_static_48 = []

c50_find_static_50        = []
c50_flync_static_50       = []
c50_pulsar_static_50      = []
c50_free_beacon_static_50 = []



c100_find_static_10        = []
c100_flync_static_10       = []
c100_pulsar_static_10      = []
c100_free_beacon_static_10 = []

c100_find_static_16        = []
c100_10flync_static_16       = []
c100_pulsar_static_16      = []
c100_free_beacon_static_16 = []

c100_find_static_20        = []
c100_flync_static_20       = []
c100_pulsar_static_20      = []
c100_free_beacon_static_20 = []

c100_find_static_24        = []
c100_flync_static_24       = []
c100_pulsar_static_24      = []
c100_free_beacon_static_24 = []

c100_find_static_30        = []
c100_flync_static_30       = []
c100_pulsar_static_30      = []
c100_free_beacon_static_30 = []

c100_find_static_36        = []
c100_flync_static_36       = []
c100_pulsar_static_36      = []
c100_free_beacon_static_36 = []

c100_find_static_40        = []
c100_flync_static_40       = []
c100_pulsar_static_40      = []
c100_free_beacon_static_40 = []

c100_find_static_48        = []
c100_flync_static_48       = []
c100_pulsar_static_48      = []
c100_free_beacon_static_48 = []

c100_find_static_50        = []
c100_flync_static_50       = []
c100_pulsar_static_50      = []
c100_free_beacon_static_50 = []




c200_find_static_10        = []
c200_flync_static_10       = []
c200_pulsar_static_10      = []
c200_free_beacon_static_10 = []

c200_find_static_16        = []
c200_10flync_static_16       = []
c200_pulsar_static_16      = []
c200_free_beacon_static_16 = []

c200_find_static_20        = []
c200_flync_static_20       = []
c200_pulsar_static_20      = []
c200_free_beacon_static_20 = []

c200_find_static_24        = []
c200_flync_static_24       = []
c200_pulsar_static_24      = []
c200_free_beacon_static_24 = []

c200_find_static_30        = []
c200_flync_static_30       = []
c200_pulsar_static_30      = []
c200_free_beacon_static_30 = []

c200_find_static_36        = []
c200_flync_static_36       = []
c200_pulsar_static_36      = []
c200_free_beacon_static_36 = []

c200_find_static_40        = []
c200_flync_static_40       = []
c200_pulsar_static_40      = []
c200_free_beacon_static_40 = []

c200_find_static_48        = []
c200_flync_static_48       = []
c200_pulsar_static_48      = []
c200_free_beacon_static_48 = []

c200_find_static_50        = []
c200_flync_static_50       = []
c200_pulsar_static_50      = []
c200_free_beacon_static_50 = []




c300_find_static_10        = []
c300_flync_static_10       = []
c300_pulsar_static_10      = []
c300_free_beacon_static_10 = []

c300_find_static_16        = []
c300_10flync_static_16       = []
c300_pulsar_static_16      = []
c300_free_beacon_static_16 = []

c300_find_static_20        = []
c300_flync_static_20       = []
c300_pulsar_static_20      = []
c300_free_beacon_static_20 = []

c300_find_static_24        = []
c300_flync_static_24       = []
c300_pulsar_static_24      = []
c300_free_beacon_static_24 = []

c300_find_static_30        = []
c300_flync_static_30       = []
c300_pulsar_static_30      = []
c300_free_beacon_static_30 = []

c300_find_static_36        = []
c300_flync_static_36       = []
c300_pulsar_static_36      = []
c300_free_beacon_static_36 = []

c300_find_static_40        = []
c300_flync_static_40       = []
c300_pulsar_static_40      = []
c300_free_beacon_static_40 = []

c300_find_static_48        = []
c300_flync_static_48       = []
c300_pulsar_static_48      = []
c300_free_beacon_static_48 = []

c300_find_static_50        = []
c300_flync_static_50       = []
c300_pulsar_static_50      = []
c300_free_beacon_static_50 = []




c500_find_static_10        = []
c500_flync_static_10       = []
c500_pulsar_static_10      = []
c500_free_beacon_static_10 = []

c500_find_static_16        = []
c500_10flync_static_16     = []
c500_pulsar_static_16      = []
c500_free_beacon_static_16 = []

c500_find_static_20        = []
c500_flync_static_20       = []
c500_pulsar_static_20      = []
c500_free_beacon_static_20 = []

c500_find_static_24        = []
c500_flync_static_24       = []
c500_pulsar_static_24      = []
c500_free_beacon_static_24 = []

c500_find_static_30        = []
c500_flync_static_30       = []
c500_pulsar_static_30      = []
c500_free_beacon_static_30 = []

c500_find_static_36        = []
c500_flync_static_36       = []
c500_pulsar_static_36      = []
c500_free_beacon_static_36 = []

c500_find_static_40        = []
c500_flync_static_40       = []
c500_pulsar_static_40      = []
c500_free_beacon_static_40 = []

c500_find_static_48        = []
c500_flync_static_48       = []
c500_pulsar_static_48      = []
c500_free_beacon_static_48 = []

c500_find_static_50        = []
c500_flync_static_50       = []
c500_pulsar_static_50      = []
c500_free_beacon_static_50 = []











# free beacond
data_sets = [
[

[
c10_find_static_10,
c10_flync_static_10,
c10_pulsar_static_10,
c10_free_beacon_static_10
],

[
c10_find_static_16        ,
c10_10flync_static_16     ,
c10_pulsar_static_16      ,
c10_free_beacon_static_16 
],

[
c10_find_static_20        ,
c10_flync_static_20       ,
c10_pulsar_static_20      ,
c10_free_beacon_static_20 
],

[
c10_find_static_24        ,
c10_flync_static_24       ,
c10_pulsar_static_24      ,
c10_free_beacon_static_24 
],


[
c10_find_static_30        ,
c10_flync_static_30       ,
c10_pulsar_static_30      ,
c10_free_beacon_static_30 
],


[
c10_find_static_36        ,
c10_flync_static_36       ,
c10_pulsar_static_36      ,
c10_free_beacon_static_36 
],


[
c10_find_static_40        ,
c10_flync_static_40       ,
c10_pulsar_static_40      ,
c10_free_beacon_static_40 
],

[
c10_find_static_48       ,
c10_flync_static_48      ,
c10_pulsar_static_48     ,
c10_free_beacon_static_48 
],


[
c10_find_static_50        ,
c10_flync_static_50       ,
c10_pulsar_static_50      ,
c10_free_beacon_static_50 
],

],




[

[
c50_find_static_10        ,
c50_flync_static_10       ,
c50_pulsar_static_10      ,
c50_free_beacon_static_10 
],

[
c50_find_static_16        ,
c50_10flync_static_16     ,
c50_pulsar_static_16      ,
c50_free_beacon_static_16 
],

[
c50_find_static_20        ,
c50_flync_static_20       ,
c50_pulsar_static_20      ,
c50_free_beacon_static_20 
],

[
c50_find_static_24        ,
c50_flync_static_24       ,
c50_pulsar_static_24      ,
c50_free_beacon_static_24 
],


[
c50_find_static_30        ,
c50_flync_static_30       ,
c50_pulsar_static_30      ,
c50_free_beacon_static_30 
],


[
c50_find_static_36        ,
c50_flync_static_36       ,
c50_pulsar_static_36      ,
c50_free_beacon_static_36 
],


[
c50_find_static_40        ,
c50_flync_static_40       ,
c50_pulsar_static_40      ,
c50_free_beacon_static_40 
],

[
c50_find_static_48        ,
c50_flync_static_48       ,
c50_pulsar_static_48      ,
c50_free_beacon_static_48 
],


[
c50_find_static_50        ,
c50_flync_static_50       ,
c50_pulsar_static_50      ,
c50_free_beacon_static_50 
],

],




[

[
c100_find_static_10        ,
c100_flync_static_10       ,
c100_pulsar_static_10      ,
c100_free_beacon_static_10 
],

[
c100_find_static_16        ,
c100_10flync_static_16     ,
c100_pulsar_static_16      ,
c100_free_beacon_static_16 
],

[
c100_find_static_20        ,
c100_flync_static_20       ,
c100_pulsar_static_20      ,
c100_free_beacon_static_20 
],

[
c100_find_static_24        ,
c100_flync_static_24      ,
c100_pulsar_static_24      ,
c100_free_beacon_static_24 
],


[
c100_find_static_30        ,
c100_flync_static_30       ,
c100_pulsar_static_30      ,
c100_free_beacon_static_30 
],


[
c100_find_static_36        ,
c100_flync_static_36       ,
c100_pulsar_static_36      ,
c100_free_beacon_static_36 
],


[
c100_find_static_40        ,
c100_flync_static_40       ,
c100_pulsar_static_40      ,
c100_free_beacon_static_40 
],

[
c100_find_static_48        ,
c100_flync_static_48       ,
c100_pulsar_static_48      ,
c100_free_beacon_static_48 
],


[
c100_find_static_50        ,
c100_flync_static_50       ,
c100_pulsar_static_50     ,
c100_free_beacon_static_50 
],

],


[

[
c200_find_static_10        ,
c200_flync_static_10       ,
c200_pulsar_static_10      ,
c200_free_beacon_static_10 
],

[
c200_find_static_16        ,
c200_10flync_static_16     ,
c200_pulsar_static_16      ,
c200_free_beacon_static_16 
],

[
c200_find_static_20        ,
c200_flync_static_20       ,
c200_pulsar_static_20      ,
c200_free_beacon_static_20 
],

[
c200_find_static_24        ,
c200_flync_static_24       ,
c200_pulsar_static_24      ,
c200_free_beacon_static_24 
],


[
c200_find_static_30        ,
c200_flync_static_30       ,
c200_pulsar_static_30      ,
c200_free_beacon_static_30 
],


[
c200_find_static_36        ,
c200_flync_static_36       ,
c200_pulsar_static_36      ,
c200_free_beacon_static_36 
],


[
c200_find_static_40        ,
c200_flync_static_40       ,
c200_pulsar_static_40      ,
c200_free_beacon_static_40 
],

[
c200_find_static_48        ,
c200_flync_static_48       ,
c200_pulsar_static_48      ,
c200_free_beacon_static_48 
],


[
c200_find_static_50        ,
c200_flync_static_50       ,
c200_pulsar_static_50      ,
c200_free_beacon_static_50 
],

],



[

[
c300_find_static_10        ,
c300_flync_static_10       ,
c300_pulsar_static_10      ,
c300_free_beacon_static_10 
],

[
c300_find_static_16        ,
c300_10flync_static_16     ,
c300_pulsar_static_16      ,
c300_free_beacon_static_16 
],

[
c300_find_static_20        ,
c300_flync_static_20       ,
c300_pulsar_static_20      ,
c300_free_beacon_static_20 
],

[
c300_find_static_24        ,
c300_flync_static_24       ,
c300_pulsar_static_24      ,
c300_free_beacon_static_24 
],


[
c300_find_static_30        ,
c300_flync_static_30       ,
c300_pulsar_static_30      ,
c300_free_beacon_static_30 
],


[
c300_find_static_36        ,
c300_flync_static_36       ,
c300_pulsar_static_36      ,
c300_free_beacon_static_36 
],


[
c300_find_static_40        ,
c300_flync_static_40       ,
c300_pulsar_static_40      ,
c300_free_beacon_static_40 
],

[
c300_find_static_48        ,
c300_flync_static_48       ,
c300_pulsar_static_48      ,
c300_free_beacon_static_48 
],


[
c300_find_static_50        ,
c300_flync_static_50       ,
c300_pulsar_static_50      ,
c300_free_beacon_static_50 
],

],



[

[
c500_find_static_10        ,
c500_flync_static_10       ,
c500_pulsar_static_10      ,
c500_free_beacon_static_10 
],

[
c500_find_static_16        ,
c500_10flync_static_16     ,
c500_pulsar_static_16      ,
c500_free_beacon_static_16 
],

[
c500_find_static_20        ,
c500_flync_static_20       ,
c500_pulsar_static_20      ,
c500_free_beacon_static_20 
],

[
c500_find_static_24        ,
c500_flync_static_24       ,
c500_pulsar_static_24      ,
c500_free_beacon_static_24 
],


[
c500_find_static_30        ,
c500_flync_static_30       ,
c500_pulsar_static_30      ,
c500_free_beacon_static_30 
],


[
c500_find_static_36        ,
c500_flync_static_36       ,
c500_pulsar_static_36      ,
c500_free_beacon_static_36 
],


[
c500_find_static_40        ,
c500_flync_static_40       ,
c500_pulsar_static_40      ,
c500_free_beacon_static_40 
],

[
c500_find_static_48        ,
c500_flync_static_48       ,
c500_pulsar_static_48      ,
c500_free_beacon_static_48 
],


[
c500_find_static_50        ,
c500_flync_static_50       ,
c500_pulsar_static_50      ,
c500_free_beacon_static_50 
],

]
]


# collect the data
static_index = 0
for static_scale in static_sets:
    scale_index = 0
    for scale in scale_sets_name:
        scenario_index = 0
        for scenario in energy_scenarios:
            syn_index = 0
            for syn_method in syn_methods:
                file = open("scalability_51_"+syn_method.lower()+"_syn_in_"+str(static_scale) + \
                   "_" +scenario.upper()+"_"+
                    scale+".csv", mode='r')
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    data_sets[static_index][scale_index][syn_index].append(int(row[0]))
                syn_index = syn_index + 1
            scenario_index = scenario_index + 1
        scale_index = scale_index + 1
    static_index = static_index + 1

static_len = len(static_sets)
scale_len = len(scale_sets_name)
scenario_len = len(energy_scenarios)
syn_len = len(syn_methods)


# plot the data
fig, ax = plt.subplots(nrows=3, ncols=4, figsize=(35, 15))
# Set global font size
fontSize = 25
plt.rcParams.update({'font.size': 25})
lineWidth = 5
for static_scale in range(static_len):
    for syn in range(syn_len):
        _ax = ax[static_scale][syn]
        # Initialize lists to store medians and means
        all_medians = []
        all_means = []
        x_tick_positions = []
        for scale in range(scale_len):
            x_tick_positions.append(syn + 1 + (scale_len + 1) * scale + 10)
            print("syn + 1 + (scale_len + 1) * scale + 10:"+str(syn + 1 + (scale_len + 1) * scale + 10))
            boxplot = _ax.boxplot(data_sets[static_scale][scale][syn],
            positions= [syn + 1 + (scale_len + 1) * scale + 10], patch_artist=True,
            boxprops=dict(facecolor=colors[scale], color=colors[scale], edgecolor=colors[scale]),
            whiskerprops=dict(color=colors[scale], linewidth=lineWidth),
            capprops=dict(color=colors[scale], linewidth=lineWidth),
            medianprops=dict(color=colors[scale], linewidth=lineWidth),
            #flierprops=dict(marker='o', markerfacecolor=colors[scale], markeredgecolor=colors[scale], markersize=lineWidth, alpha=0.5),
            showfliers = False,
            showmeans=True,
            meanprops=dict(markerfacecolor=colors[scale], markeredgecolor=colors[scale], markersize=lineWidth, alpha=0.5),
            )
            # Extract median and mean for this box plot
            median = boxplot['medians'][0].get_ydata()[0]
            mean = boxplot['means'][0].get_ydata()[0]
            # Store medians and means
            all_medians.append((syn + 1 + (scale_len + 1) * scale + 10, median))
            all_means.append((syn + 1 + (scale_len + 1) * scale + 10, mean))
        # Unpack medians and means into x and y coordinates
        median_x, median_y = zip(*all_medians)
        mean_x, mean_y = zip(*all_means)

        _ax.set_xlim(0, syn + 1 + (scale_len + 1) * scale + 10 + 10)

        # Connect medians and means with lines
        if (static_scale == 0) and (syn == (syn_len -1)):
            _ax.plot(median_x, median_y,  linestyle='--', linewidth=lineWidth, marker='o', label=syn_legend_names[0])
            _ax.plot(mean_x, mean_y,  linestyle='--', linewidth=lineWidth, marker='^', label=syn_legend_names[1])
            _ax.legend(loc='upper right')
        else:
            _ax.plot(median_x, median_y, linestyle='--', linewidth=lineWidth, marker='o')
            _ax.plot(mean_x, mean_y,  linestyle='--', linewidth=lineWidth, marker='')
        if syn == 0:
           _ax.set_ylabel(f"Latency (Time Slots)\n #Static {static_sets[static_scale]} (slots)", fontsize=fontSize)
        if static_scale == static_len - 1:
            _ax.set_xlabel("#"+syn_methods_name[syn], fontsize=fontSize)
            _ax.set_xticks(x_tick_positions)
            scale_sets_legend= ["#10", "#16", "#20", "#24", "#30", "#36", "#40", "#48", "#50"]
            _ax.set_xticklabels(scale_sets_legend)
        else:
            _ax.set_xticks([])
       
        #_ax.set_yscale('log')
        _ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        _ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        _ax.set_yscale('log')
        _ax.tick_params(axis='both', which='major', labelsize=fontSize)
        
        
plt.tight_layout()
fig.savefig(f""+title+"_simulation.pdf", format="pdf", bbox_inches='tight')




