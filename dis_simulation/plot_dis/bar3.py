import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter
import csv

# Define your methods, power-off rates, and scenarios
syn_methods = ["Pulsar", "Free_beacon"]
syn_legend_names = ["Pulsar", "FreeBeacon"]

poweroff_rates = [1, 5, 10]
poweroff_rates_name = ["1%", "5%", "10%"]

energy_scenarios = [
  "Cars_trace"
]
energy_scenarios_names = [
"Cars trace"
]

title = "dis_free_beacon_with_30"
colors = ['steelblue', 'darkorange']

# Initialize the data_sets list to store your data
data_sets = []
for scenario in energy_scenarios:
    scenario_methods = []
    for method in syn_methods:
        method_poweroff_rates = []
        for rate in poweroff_rates:
            method_poweroff_rates.append([])  # Placeholder for data
        scenario_methods.append(method_poweroff_rates)
    data_sets.append(scenario_methods)

# Collect the data
for i, scenario in enumerate(energy_scenarios):
    for j, method in enumerate(syn_methods):
        for k, rate in enumerate(poweroff_rates):
            file_name = f"poweroff_{method.lower()}_dis_in_{scenario.upper()}_{rate}.csv"
            try:
                with open(file_name, mode='r') as file:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        data_sets[i][j][k].append(int(row[0]))
            except FileNotFoundError:
                print(f"File not found: {file_name}")
                data_sets[i][j][k] = [0]  # Assign a default value or handle as needed

# Compute average values
average_data = []
for i in range(len(energy_scenarios)):
    scenario_averages = []
    for j in range(len(syn_methods)):
        method_averages = []
        for k in range(len(poweroff_rates)):
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
plt.rcParams.update({'font.size': 14})  # Set font size globally

fig, ax = plt.subplots(1, 1, figsize=(5, 5), sharey=True)

# Set the positions for each group
positions = np.arange(len(poweroff_rates))
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

    ax_i.set_xlabel(scenario_name, rotation=45)
    ax_i.set_xticks(positions)
    ax_i.set_xticklabels(poweroff_rates_name)
    ax_i.set_yscale('log')
    if i == 0:
        ax_i.set_ylabel('Synchronization Time [slots]')
    else:
        ax_i.set_ylabel('')
    ax_i.tick_params(axis='x', labelsize=10)
    ax_i.tick_params(axis='y', labelsize=10)

# Adjust layout parameters to decrease space between subplots and margins
plt.subplots_adjust(left=0.06, right=0.99, bottom=0.25, top=0.82, wspace=0.1)

# Add a shared legend
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles[:2], labels[:2], loc='upper center', ncol=2, fontsize=12)

# Adjust subplot positions if needed
total_width = 0.95  # Fraction of figure width to be used for subplots
subplot_width = total_width 
subplot_spacing = 0.005  # Space between subplots


# Calculate the position for each subplot
left = 0.025 + i * (subplot_width + subplot_spacing)
bottom, width, height = 0.25, subplot_width, 0.57  # Adjust bottom and height as needed

# Ensure that the subplots do not exceed the figure boundaries
if left + width > 1.0:
    width = 1.0 - left

# Set the position of each subplot
ax.set_position([left, bottom, width, height])

# Save and show the plot
plt.savefig("poweroff_simulation.pdf", format="pdf", bbox_inches='tight')
plt.show()
