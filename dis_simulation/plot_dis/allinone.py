import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter
import csv
import glob

# Define methods, scenarios, and colors
syn_methods = ["Pulsar", "Free_beacon"]
syn_legend_names = ["Pulsar", "FreeBeacon"]
colors = ['red', 'green', 'orange', 'purple', 'brown', 'gray']
energy_scenarios = ["Cars_trace"]
energy_scenarios_names = ["Cars trace"]

# Experiment 1: Varying number of nodes
node_sets = [2, 12, 30]
node_sets_name = ["2", "12", "30"]

# Experiment 2: Varying cycle sets
cycle_sets = [30, 51, 100]
cycle_sets_name = ["30", "51", "100"]
node_num = 30  # Node number is fixed at 30

# Experiment 3: Varying power-off rates
poweroff_rates = [1, 5, 10]
poweroff_rates_name = ["1%", "5%", "10%"]

# Initialize data lists
data_exp1 = []
data_exp2 = []
data_exp3 = []

# Collect data for Experiment 1
for scenario in energy_scenarios:
    for method in syn_methods:
        for num in node_sets:
            file_name = f"no_poweroff_30_general_{method.lower()}_dis_in_{scenario.upper()}_{num}.csv"
            try:
                with open(file_name, mode='r') as file:
                    csv_reader = csv.reader(file)
                    data = [int(row[0]) for row in csv_reader]
                    data_exp1.append({'scenario': scenario, 'method': method, 'num_nodes': num, 'data': data})
            except FileNotFoundError:
                print(f"File not found: {file_name}")
                data_exp1.append({'scenario': scenario, 'method': method, 'num_nodes': num, 'data': [0]})

# Collect data for Experiment 2
for cycle in cycle_sets:
    for scenario in energy_scenarios:
        file_pattern = f"no_poweroff_{cycle}*_beacon_dis_in_{scenario.upper()}_{node_num}.csv"
        file_list = glob.glob(file_pattern)
        if not file_list:
            print(f"No file found for cycle {cycle}, scenario {scenario}")
            data_exp2.append({'scenario': scenario, 'cycle_set': cycle, 'data': [0]})
            continue
        file_name = file_list[0]
        with open(file_name, mode='r') as file:
            csv_reader = csv.reader(file)
            data = [int(row[0]) for row in csv_reader]
            data_exp2.append({'scenario': scenario, 'cycle_set': cycle, 'data': data})

# Collect data for Experiment 3
for scenario in energy_scenarios:
    for method in syn_methods:
        for rate in poweroff_rates:
            file_name = f"poweroff_{method.lower()}_dis_in_{scenario.upper()}_{rate}.csv"
            try:
                with open(file_name, mode='r') as file:
                    csv_reader = csv.reader(file)
                    data = [int(row[0]) for row in csv_reader]
                    data_exp3.append({'scenario': scenario, 'method': method, 'poweroff_rate': rate, 'data': data})
            except FileNotFoundError:
                print(f"File not found: {file_name}")
                data_exp3.append({'scenario': scenario, 'method': method, 'poweroff_rate': rate, 'data': [0]})

# Convert data lists to DataFrames
df_exp1 = pd.DataFrame(data_exp1)
df_exp2 = pd.DataFrame(data_exp2)
df_exp3 = pd.DataFrame(data_exp3)

# Compute average data
df_exp1['avg_data'] = df_exp1['data'].apply(lambda x: np.mean(x) if len(x) > 0 else 0)
df_exp2['avg_data'] = df_exp2['data'].apply(lambda x: np.mean(x) if len(x) > 0 else 0)
df_exp3['avg_data'] = df_exp3['data'].apply(lambda x: np.mean(x) if len(x) > 0 else 0)

# Create the figure and axes
plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 20})

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

# Experiment 1: Plotting
ax = axes[0]
positions = np.arange(len(node_sets))
bar_width = 0.35

for method_idx, method in enumerate(syn_methods):
    y_values = []
    for num in node_sets:
        df_row = df_exp1[
            (df_exp1['scenario'] == energy_scenarios[0]) &
            (df_exp1['method'] == method) &
            (df_exp1['num_nodes'] == num)
        ]
        y_value = df_row['avg_data'].values[0] if not df_row.empty else 0
        y_values.append(y_value)
    x = positions + (method_idx - 0.5) * bar_width
    ax.bar(x, y_values, width=bar_width, label=syn_legend_names[method_idx], color=colors[method_idx])

ax.set_xlabel('Number of Nodes')
ax.set_xticks(positions)
ax.set_xticklabels(node_sets_name)
ax.set_ylabel('Discovery Time [slots]')
ax.set_yscale('log')
ax.legend()

# Experiment 2: Plotting
ax = axes[1]
positions = np.arange(len(cycle_sets))
bar_width = 0.35  # Since we have only one method, make the bar wider

y_values = []
for cycle in cycle_sets:
    df_row = df_exp2[
        (df_exp2['scenario'] == energy_scenarios[0]) &
        (df_exp2['cycle_set'] == cycle)
    ]
    y_value = df_row['avg_data'].values[0] if not df_row.empty else 0
    y_values.append(y_value)

ax.bar(positions, y_values, width=bar_width, color=colors[1])
ax.set_xlabel('Cycle Length')
ax.set_xticks(positions)
ax.set_xticklabels(cycle_sets_name)
# ax.set_title('Dissemination Time')
ax.set_yscale('log')

# Experiment 3: Plotting
ax = axes[2]
positions = np.arange(len(poweroff_rates))
bar_width = 0.35

for method_idx, method in enumerate(syn_methods):
    y_values = []
    for rate in poweroff_rates:
        df_row = df_exp3[
            (df_exp3['scenario'] == energy_scenarios[0]) &
            (df_exp3['method'] == method) &
            (df_exp3['poweroff_rate'] == rate)
        ]
        y_value = df_row['avg_data'].values[0] if not df_row.empty else 0
        y_values.append(y_value)
    x = positions + (method_idx - 0.5) * bar_width
    ax.bar(x, y_values, width=bar_width,  color=colors[method_idx])

ax.set_xlabel('Power-off Rate')
ax.set_xticks(positions)
ax.set_xticklabels(poweroff_rates_name)
ax.set_yscale('log')

plt.tight_layout()
plt.savefig("discovery_performance.pdf", format="pdf", bbox_inches='tight')
plt.show()
