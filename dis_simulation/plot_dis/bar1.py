import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter
import csv

# Define your methods, node sets, and scenarios
syn_methods = ["Pulsar", "Free_beacon"]
syn_legend_names = ["Pulsar", "FreeBeacon"]

node_sets = [2, 12, 30]
node_sets_name = ["#2", "#12", "#30"]

energy_scenarios = [
"Cars_trace",
]
energy_scenarios_names = [
"#Cars trace"
]

title = "free_beacon_with_30"
colors = ['steelblue', 'darkorange']

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
            file_name = f"no_poweroff_30_general_{method.lower()}_dis_in_{scenario.upper()}_{num}.csv"
            try:
                with open(file_name, mode='r') as file:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        data_sets[i][j][k].append(int(row[0]))
            except FileNotFoundError:
                print(f"File not found: {file_name}")
                data_sets[i][j][k] = [0]  # Assign a default value or handle as needed

# Compute the average values
average_data = []
for i in range(len(energy_scenarios)):
    scenario_averages = []
    for j in range(len(syn_methods)):
        method_averages = []
        for k in range(len(node_sets)):
            data = data_sets[i][j][k]
            if isinstance(data, list) and len(data) > 0:
                avg = np.mean(data)
            else:
                avg = 0
            method_averages.append(avg)
        scenario_averages.append(method_averages)
    average_data.append(scenario_averages)

# Create the figure and axes
plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 18})  # Set font size globally
fig, ax = plt.subplots(1, 1, figsize=(5, 4), sharey=True)

# Set the positions for each group
positions = np.arange(len(node_sets))
bar_width = 0.35  # Adjusted bar width for two methods

# Plot the data for each scenario
for i in range(len(energy_scenarios)):
    ax_i = ax
    scenario_name = energy_scenarios_names[i]
    pulsar_averages = average_data[i][0]
    freebeacon_averages = average_data[i][1]
    
    x = positions
    ax_i.bar(x - bar_width/2, pulsar_averages, width=bar_width, label='Pulsar', color='steelblue')
    ax_i.bar(x + bar_width/2, freebeacon_averages, width=bar_width, label='FreeBeacon', color='darkorange')
    
    ax_i.set_xlabel(scenario_name)
    ax_i.set_xticks(positions)
    ax_i.set_xticklabels(node_sets_name)
    ax_i.set_yscale('log')
    if i == 0:
        ax_i.set_ylabel('Discovery Time [slots]')
    
# Adjust layout parameters to decrease space between subplots and margins
plt.subplots_adjust(left=0.06, right=0.99, bottom=0.25, top=0.82, wspace=0.1)

# Add a shared legend
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2)

# Save and show the plot
plt.savefig("dis_free_beacon_with_30_simulation.pdf", format="pdf")
plt.show()









