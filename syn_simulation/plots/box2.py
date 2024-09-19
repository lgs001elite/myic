



import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv
import glob

# Define variables
cycle_sets = [30, 51, 100]
cycle_sets_name = ["30", "51", "100"]
node_num = 30  # Focusing on 30 nodes
energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace",
                    "Office_trace", "Stairs_trace", "Washer_trace"]
energy_scenarios_names = ["#Static", "#Random", "#Cars trace", "#Jogging trace",
                          "#Office trace", "#Stairs trace", "#Washer trace"]

box_colors = ['steelblue', 'darkorange', 'forestgreen']
#box_colors = ['red', 'green', 'orange']
box_hatches = ['/', '\\', '|']
median_line_style = '--'
quantile_line_style = ':'
title = "box_30-51-100_compare"

# Initialize data_sets
data_sets = {'30': [], '51': [], '100': []}

# Collect the data
for cycle in cycle_sets_name:
    data_per_scenario = []
    for scenario in energy_scenarios:
        file_pattern = f"no_poweroff_{cycle}*_beacon_syn_in_{scenario.upper()}_{node_num}.csv"
        file_list = glob.glob(file_pattern)
        if not file_list:
            print(f"No file found for cycle {cycle}, scenario {scenario}")
            data_per_scenario.append([0])  # Placeholder for missing data
            continue
        file_name = file_list[0]
        with open(file_name, mode='r') as file:
            csv_reader = csv.reader(file)
            data = []
            for row in csv_reader:
                data.append(int(row[0]))
            data_per_scenario.append(data)
    data_sets[cycle] = data_per_scenario

# Prepare data for plotting
# Each element in scenario_sets corresponds to data across cycles for one scenario
scenario_sets = []
for scenario_idx in range(len(energy_scenarios)):
    scenario_data = []
    for cycle in cycle_sets_name:
        scenario_data.append(data_sets[cycle][scenario_idx])
    scenario_sets.append(scenario_data)

# Transpose scenario_sets to match the expected input
# Now, data_list will have one list per cycle, each containing data across scenarios
data_list = []
for cycle_idx in range(len(cycle_sets_name)):
    cycle_data = []
    for scenario_data in scenario_sets:
        cycle_data.append(scenario_data[cycle_idx])
    data_list.append(cycle_data)

# Plotting
plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 18})  # Set font size globally

fig, ax = plt.subplots(figsize=(20, 4))

# Set the positions for each group
positions = np.arange(len(energy_scenarios))
bar_width = 0.2  # Adjusted bar width for more methods

# Function to customize boxplot
def create_custom_boxplot(ax, data_list, positions, labels):
    num_datasets = len(data_list)
    total_width = bar_width * num_datasets
    offsets = np.linspace(-total_width/2 + bar_width/2, total_width/2 - bar_width/2, num_datasets)
    
    print("Starting********************")
    for idx, (method_data, label, offset) in enumerate(zip(data_list, labels, offsets)):
        pos = positions + offset
        bp = ax.boxplot(
            method_data,
            positions=pos,
            widths=bar_width,
            patch_artist=True,
            showfliers=False
        )
        print(np.average(method_data[0]))
        print(np.average(method_data[1]))
        print(np.average(method_data[2]))
        print(np.average(method_data[3]))
        print(np.average(method_data[4]))
        print(np.average(method_data[5]))
        print(np.average(method_data[6]))
        print("boundary***************")
        
        # Customize boxes
        color = box_colors[idx % len(box_colors)]
        hatch = box_hatches[idx % len(box_hatches)]
        
        for box in bp['boxes']:
            box.set_facecolor(color)
            box.set_hatch(hatch)
            box.set_linewidth(1.5)
        
        # Customize whiskers, caps, and medians
        for whisker in bp['whiskers']:
            whisker.set(linewidth=1.5, linestyle='-', color='black')
    
        for cap in bp['caps']:
            cap.set(linewidth=1.5)
    
        for median in bp['medians']:
            median.set(linewidth=2, linestyle=median_line_style, color='black')
        
        # Add 90th and 99th percentiles as dotted lines
        for i in range(len(method_data)):
            if len(method_data[i]) == 0:
                continue  # Skip if there's no data
            percentile_90 = np.percentile(method_data[i], 90)
            percentile_99 = np.percentile(method_data[i], 99)
            ax.plot(
                [pos[i]] * 2,
                [bp['whiskers'][i * 2 + 1].get_ydata()[1], percentile_90],
                quantile_line_style,
                color='gray'
            )
            ax.plot(
                [pos[i]] * 2,
                [percentile_90, percentile_99],
                quantile_line_style,
                color='purple'
            )
        
        # Add legend labels
        ax.plot([], c=color, label=label, linewidth=1.5)
    
    # Add percentile lines to legend
    ax.plot([], c='black', linestyle=median_line_style, label='Median')
    ax.plot([], c='gray', linestyle=quantile_line_style, label='90th percentile')
    ax.plot([], c='purple', linestyle=quantile_line_style, label='99th percentile')

# Plot the data
create_custom_boxplot(ax, data_list, positions, ["#Cycle 30", '#Cycle 51', '#Cycle 100'])

# Set axis labels and titles
ax.set_ylabel('SynTime [slots]')
ax.set_xlabel(None)
ax.set_yscale('log')
ax.set_xticks(positions)
ax.set_xticklabels(energy_scenarios_names)

# Add a legend
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=6)

# Adjust layout and show the plot
plt.tight_layout()
plt.subplots_adjust(top=0.88)  # Adjust to make room for the shared legend
fig.savefig(f"{title}_simulation.pdf", format="pdf", bbox_inches='tight')
plt.show()




