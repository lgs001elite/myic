import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv
import glob

# Define variables
cycle_sets = [30, 51, 100]
cycle_sets_name = ["30", "51", "100"]
node_num = 30  # Focusing on 30 nodes
energy_scenarios = [
 "Cars_trace"
]
energy_scenarios_names = [
  "#Cars trace"
]

colors = ['steelblue', 'darkorange', 'forestgreen']
title = "dis_bar_30-51-100_compare"

# Initialize data_sets
data_sets = {'30': [], '51': [], '100': []}

# Collect the data
for cycle in cycle_sets_name:
    data_per_scenario = []
    for scenario in energy_scenarios:
        file_pattern = f"no_poweroff_{cycle}*_beacon_dis_in_{scenario.upper()}_{node_num}.csv"
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

# Compute average values
average_data = []
for cycle in cycle_sets_name:
    cycle_averages = []
    for scenario_data in data_sets[cycle]:
        if isinstance(scenario_data, list) and len(scenario_data) > 0:
            avg = np.mean(scenario_data)
        else:
            avg = 0
        cycle_averages.append(avg)
    average_data.append(cycle_averages)

# Plotting
plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 18})  # Set font size globally

fig, ax = plt.subplots(figsize=(5, 6))

# Set the positions for each group
positions = np.arange(len(energy_scenarios))
bar_width = 0.25  # Adjusted bar width for three methods

# Plot the data
for idx, (cycle_name, color) in enumerate(zip(cycle_sets_name, colors)):
    x = positions + idx * bar_width - bar_width  # Adjust positions
    averages = average_data[idx]
    ax.bar(x, averages, width=bar_width, label=f'Cycle {cycle_name}', color=color)

# Set axis labels and titles
ax.set_ylabel('Dissemination Time [slots]')
ax.set_xlabel(None)
ax.set_yscale('log')
ax.set_xticks(positions)
ax.set_xticklabels(energy_scenarios_names, rotation=45)

# Add a legend
ax.legend()

# Adjust layout and show the plot
plt.tight_layout()
fig.savefig(f"{title}_simulation.pdf", format="pdf", bbox_inches='tight')
plt.show()
