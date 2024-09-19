import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import ScalarFormatter
import csv

# Define your methods, node sets, and scenarios
syn_methods = ["Find", "Flync", "Pulsar", "Free_beacon"]
syn_legend_names = ["Find", "Flync_Find", "Pulsar", "FreeBeacon", "Medians", "Means"]

node_sets = [2, 12, 30]
node_sets_name = ["#2", "#12", "#30"]

energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace", "Office_trace", "Stairs_trace", "Washer_trace"]
energy_scenarios_names = ["#Static", "#Random", "#Cars trace", "#Jogging trace", "#Office trace", "#Stairs trace", "#Washer trace"]

title ="free_beacon_with_30"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick', "purple", "tomato"]

# Initialize the data_sets list to store your data
data_sets = []
for scenario in energy_scenarios:
    scenario_methods = []
    for method in syn_methods:
        method_node_sets = []
        for num in node_sets:
            method_node_sets.append([])  # Placeholder for data
        scenario_methods.append(method_node_sets)
    data_sets.append(scenario_methods)

# Collect the data
for i, scenario in enumerate(energy_scenarios):
    for j, method in enumerate(syn_methods):
        for k, num in enumerate(node_sets):
            file_name = f"no_poweroff_30_general_{method.lower()}_syn_in_{scenario.upper()}_{num}.csv"
            try:
                with open(file_name, mode='r') as file:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        data_sets[i][j][k].append(int(row[0]))
            except FileNotFoundError:
                print(f"File not found: {file_name}")
                data_sets[i][j][k] = [0]  # Assign a default value or handle as needed

# Reorganize scenario_sets to align with the expected format
scenario_sets = []
for i in range(len(energy_scenarios)):
    scenario_data = []
    for j in range(len(syn_methods)):
        method_data = []
        for k in range(len(node_sets)):
            # Each method_data[j] should be a list of lists, one per node set
            method_data.append(data_sets[i][j][k])
        scenario_data.append(method_data)
    scenario_sets.append(scenario_data)

# Create the figure and axes

plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 18})  # Set font size globally
fig, ax= plt.subplots(1, 7, figsize=(20, 4), sharey=True)

# Set the positions for each group
positions = np.arange(len(node_sets))
bar_width = 0.22  # Adjusted bar width for more methods

# Define colors and hatches for different box groups
box_colors = ['red', 'green', 'orange', 'purple']
box_hatches = ['/', '\\', '|', '-']
median_line_style = '--'
quantile_line_style = ':'

# Function to customize boxplot
def create_custom_boxplot(ax, data_list, positions, labels):
    num_datasets = len(data_list)
    total_width = bar_width * num_datasets
    offsets = np.linspace(-total_width/2 + bar_width/2, total_width/2 - bar_width/2, num_datasets)
    
    print("starting********************")
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
        print("methods****************")
        
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

# Plot the data for each scenario
for i in range(len(energy_scenarios)):
    create_custom_boxplot(ax[i], scenario_sets[i], positions, ["#Find", '#Flync-Find', '#Pulsar', "#FreeBeacon"])
    ax[i].set_xlabel(energy_scenarios_names[i])
    ax[i].set_yscale('log')
    ax[i].set_xticks(positions)
    ax[i].set_xticklabels(node_sets_name)

# plt.subplots_adjust(left=0, right=2, bottom=0, top=0.82, wspace=0)

# Set axis labels and titles
ax[0].set_ylabel('#Syn Time [slots]')

# Add a shared legend
handles, labels = ax[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=7)

# Adjust layout and show the plot
# plt.tight_layout()
# plt.subplots_adjust(top=0.88)  # Adjust to make room for the shared legend





# Adjust layout parameters
# Adjust layout parameters to decrease space between subplots and margins
plt.subplots_adjust(left=0.06, right=0.99, bottom=0.25, top=0.82, wspace=0.1)

total_width = 0.9  # Fraction of figure width to be used for subplots
subplot_width = total_width / len(ax)
subplot_spacing = 0  # Space between subplots
# Adjust the spacing between subplots individually if needed
for i, ax1 in enumerate(ax):
    # Calculate the position for each subplot
    left = 0.05 + i * (subplot_width + subplot_spacing)
    bottom, width, height = 0.2, subplot_width, 0.6  # Adjust bottom and height as needed

    # Ensure that the subplots do not exceed the figure boundaries
    if left + width > 1.0:
        width = 1.0 - left

    # Set the position of each subplot
    ax1.set_position([left, bottom, width, height])


plt.savefig("free_beacon_with_30_simulation.pdf", format="pdf")
plt.show()





