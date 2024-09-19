import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv



syn_methods = ["Find", "Flync", "Pulsar", "Free_beacon"]
syn_methods_name = ["Find", "Flync_Find", "Pulsar", "FreeBeacon"]

poweroff_rate_sets = [1, 5, 10, 20, 30]
poweroff_rate_name = ["1", "5", "10", "20", "30"]

energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace", "Office_trace", "Stairs_trace", "Washer_trace"]
energy_scenarios_names = ["Static", "Random", "Cars trace", "Jogging trace", "Office trace", "Stairs trace", "Washer trace"]

title ="cdf_poweroff"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick']

find_static_1        = []
flync_static_1       = []
pulsar_static_1      = []
free_beacon_static_1 = []

find_static_5        = []
flync_static_5       = []
pulsar_static_5      = []
free_beacon_static_5 = []

find_static_10        = []
flync_static_10       = []
pulsar_static_10      = []
free_beacon_static_10 = []

find_static_20        = []
flync_static_20       = []
pulsar_static_20      = []
free_beacon_static_20 = []

find_static_30        = []
flync_static_30       = []
pulsar_static_30      = []
free_beacon_static_30 = []


find_complex_1        = []
flync_complex_1       = []
pulsar_complex_1      = []
free_beacon_complex_1 = []

find_complex_5        = []
flync_complex_5       = []
pulsar_complex_5      = []
free_beacon_complex_5 = []

find_complex_10        = []
flync_complex_10       = []
pulsar_complex_10      = []
free_beacon_complex_10 = []

find_complex_20        = []
flync_complex_20       = []
pulsar_complex_20      = []
free_beacon_complex_20 = []

find_complex_30        = []
flync_complex_30       = []
pulsar_complex_30      = []
free_beacon_complex_30 = []

find_cars_1        = []
flync_cars_1       = []
pulsar_cars_1      = []
free_beacon_cars_1 = []

find_cars_5        = []
flync_cars_5       = []
pulsar_cars_5      = []
free_beacon_cars_5 = []

find_cars_10        = []
flync_cars_10       = []
pulsar_cars_10      = []
free_beacon_cars_10 = []

find_cars_20        = []
flync_cars_20       = []
pulsar_cars_20      = []
free_beacon_cars_20 = []

find_cars_30        = []
flync_cars_30       = []
pulsar_cars_30      = []
free_beacon_cars_30 = []



find_jogging_1        = []
flync_jogging_1       = []
pulsar_jogging_1      = []
free_beacon_jogging_1 = []

find_jogging_5        = []
flync_jogging_5       = []
pulsar_jogging_5      = []
free_beacon_jogging_5 = []

find_jogging_10        = []
flync_jogging_10       = []
pulsar_jogging_10      = []
free_beacon_jogging_10 = []

find_jogging_20        = []
flync_jogging_20       = []
pulsar_jogging_20      = []
free_beacon_jogging_20 = []

find_jogging_30        = []
flync_jogging_30       = []
pulsar_jogging_30      = []
free_beacon_jogging_30 = []


find_office_1        = []
flync_office_1       = []
pulsar_office_1      = []
free_beacon_office_1 = []

find_office_5        = []
flync_office_5       = []
pulsar_office_5      = []
free_beacon_office_5 = []

find_office_10        = []
flync_office_10       = []
pulsar_office_10      = []
free_beacon_office_10 = []

find_office_20        = []
flync_office_20       = []
pulsar_office_20      = []
free_beacon_office_20 = []

find_office_30        = []
flync_office_30       = []
pulsar_office_30      = []
free_beacon_office_30 = []



find_stairs_1        = []
flync_stairs_1       = []
pulsar_stairs_1      = []
free_beacon_stairs_1 = []

find_stairs_5        = []
flync_stairs_5       = []
pulsar_stairs_5      = []
free_beacon_stairs_5 = []

find_stairs_10        = []
flync_stairs_10       = []
pulsar_stairs_10      = []
free_beacon_stairs_10 = []

find_stairs_20        = []
flync_stairs_20       = []
pulsar_stairs_20      = []
free_beacon_stairs_20 = []

find_stairs_30        = []
flync_stairs_30       = []
pulsar_stairs_30      = []
free_beacon_stairs_30 = []



find_washer_1        = []
flync_washer_1       = []
pulsar_washer_1      = []
free_beacon_washer_1 = []

find_washer_5        = []
flync_washer_5       = []
pulsar_washer_5      = []
free_beacon_washer_5 = []

find_washer_10        = []
flync_washer_10       = []
pulsar_washer_10      = []
free_beacon_washer_10 = []

find_washer_20        = []
flync_washer_20       = []
pulsar_washer_20      = []
free_beacon_washer_20 = []

find_washer_30        = []
flync_washer_30       = []
pulsar_washer_30      = []
free_beacon_washer_30 = []




fontSize  = 12

lineWidth = 1.5


# free beacond
data_sets = \
[
    [
[find_static_1, find_complex_1, find_cars_1, find_jogging_1, find_office_1, 
 find_stairs_1, find_washer_1],

[flync_static_1, flync_complex_1, flync_cars_1, flync_jogging_1, flync_office_1, 
 flync_stairs_1, flync_washer_1],

 [pulsar_static_1, pulsar_complex_1, pulsar_cars_1, pulsar_jogging_1, pulsar_office_1, 
 pulsar_stairs_1, pulsar_washer_1],

 [free_beacon_static_1, free_beacon_complex_1, free_beacon_cars_1, free_beacon_jogging_1, free_beacon_office_1, 
 free_beacon_stairs_1, free_beacon_washer_1]
    ],

[
[find_static_5, find_complex_5, find_cars_5, find_jogging_5, find_office_5, 
 find_stairs_5, find_washer_5],

[flync_static_5, flync_complex_5, flync_cars_5, flync_jogging_5, flync_office_5, 
 flync_stairs_5, flync_washer_5],

 [pulsar_static_5, pulsar_complex_5, pulsar_cars_5, pulsar_jogging_5, pulsar_office_5, 
 pulsar_stairs_5, pulsar_washer_5],

 [free_beacon_static_5, free_beacon_complex_5, free_beacon_cars_5, free_beacon_jogging_5, free_beacon_office_5, 
 free_beacon_stairs_5, free_beacon_washer_5]
],


[
[find_static_10, find_complex_10, find_cars_10, find_jogging_10, find_office_10, 
 find_stairs_10, find_washer_10],

[flync_static_10, flync_complex_10, flync_cars_10, flync_jogging_10, flync_office_10, 
 flync_stairs_10, flync_washer_10],

 [pulsar_static_10, pulsar_complex_10, pulsar_cars_10, pulsar_jogging_10, pulsar_office_10, 
 pulsar_stairs_10, pulsar_washer_10],

 [free_beacon_static_10, free_beacon_complex_10, free_beacon_cars_10, free_beacon_jogging_10, free_beacon_office_10, 
 free_beacon_stairs_10, free_beacon_washer_10]
],


[
[find_static_20, find_complex_20, find_cars_20, find_jogging_20, find_office_20, 
 find_stairs_20, find_washer_20],

[flync_static_20, flync_complex_20, flync_cars_20, flync_jogging_20, flync_office_20, 
 flync_stairs_20, flync_washer_20],

 [pulsar_static_20, pulsar_complex_20, pulsar_cars_20, pulsar_jogging_20, pulsar_office_20, 
 pulsar_stairs_20, pulsar_washer_20],

 [free_beacon_static_20, free_beacon_complex_20, free_beacon_cars_20, free_beacon_jogging_20, free_beacon_office_20, 
 free_beacon_stairs_20, free_beacon_washer_20]
],


[
[find_static_30, find_complex_30, find_cars_30, find_jogging_30, find_office_30, 
 find_stairs_30, find_washer_30],

[flync_static_30, flync_complex_30, flync_cars_30, flync_jogging_30, flync_office_30, 
 flync_stairs_30, flync_washer_30],

 [pulsar_static_30, pulsar_complex_30, pulsar_cars_30, pulsar_jogging_30, pulsar_office_30, 
 pulsar_stairs_30, pulsar_washer_30],

 [free_beacon_static_30, free_beacon_complex_30, free_beacon_cars_30, free_beacon_jogging_30, free_beacon_office_30, 
 free_beacon_stairs_30, free_beacon_washer_30]
]
       
]


# collect the data
i = 0
for rate in poweroff_rate_name:
    j = 0
    for method in syn_methods:
        k = 0
        for scenario in energy_scenarios:
            file = open("poweroff_"+ method.lower() + "_syn_in_"+ scenario.upper()+"_"+ rate+".csv", mode='r')
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_sets[i][j][k].append(int(row[0]))
            k  += 1
        j += 1
    i += 1

scenarios_len = len(energy_scenarios_names)
methods_len = len(syn_methods_name)
rates_len = len(poweroff_rate_name)

# plot the data
fig, ax = plt.subplots(nrows=5, ncols=7, figsize=(20, 10))

markers = ['o', 's', '^', 'v']

lineStyles  = ['-', '--', '-.', ':']

for i in range(rates_len):
    for j in range(scenarios_len):
        _ax = ax[i][j]
        for k in range(methods_len):
            dataSet = data_sets[i][k][j]
            sorted_set = np.sort(dataSet)
            cdf = np.arange(1, len(sorted_set) + 1) / len(sorted_set)
            _ax.plot(sorted_set, cdf, marker=markers[k], color = colors[k], linestyle = lineStyles[k],
                     linewidth=0.2, markersize=0.2)
        if j == 0:
            _ax.set_ylabel("CDF", fontsize=fontSize)
        _ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        _ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        if (i == (rates_len - 1)):
            _ax.set_xlabel(energy_scenarios_names[j])
        _ax.tick_params(axis='both', which='major', labelsize=fontSize)
        if (j == 3):
           _ax.set_title("["+poweroff_rate_name[i]+"% poweroff rate]")

handles = [plt.Line2D([0], [0], color=color) for color in colors]
fig.legend(handles, syn_methods_name, loc='upper right')
plt.tight_layout()
fig.savefig(f""+title+"_simulation.pdf", format="pdf", bbox_inches='tight')




