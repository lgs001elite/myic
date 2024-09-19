import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Data
# 0% poweroff
zero_r6_0 = [5230.629, 5175.785, 41203.899,  6242.017, 6076.006, 36782.366, 6597.293, 52013.921, None]
zero_r6_1 = [133052.68, 131902.693, None,  153869.259, 149926.258, None, 154322.943, None, None]
zero_r6_2 = [71849.209, 73006.989, None,  84045.708, 82692.224, None,87863.821, None, None]

zero_r30_0 = [1884.55, 1830.797, 112164.128, 3990.752, 3957.8, 73557.827, 2413.22, None, None]
zero_r30_1 = [45139.501, 44322.714, None, 79778.219, 79442.459, None, 49539.026, None, None]
zero_r30_2 = [23530.207, 22864.173, None, 42563.959, 41731.92, None, 26722.945, None, None]

zero_r100_0 = [1018.28, 969.498, 237194.263,  8891.533, 10637.824, 110096.602, 1717.907, None, None]
zero_r100_1 = [24053.855, 23647.836, None,  55994.499, 56324.669, None, 23477.457, None, None]
zero_r100_2 = [8766.091, 8567.324, None,  22646.117, 22403.92, None, 10886.152, None, None]

# 1% poweroff
one_r6_0 = [34051.232, 215208.47, 52632.118,193609.064, 244350.283, 47612.691, 15951.269, 64861.283, None,]
one_r6_1 = [None, None, None, None, None, None, None, None, None,]
one_r6_2 = [268187.757, None, None, None, None, None, 181425.569, None, None,]

one_r30_0 = [69286.269, None, 144148.765,  None, None, 94139, 9496.919, 280270.01, None, ]
one_r30_1 = [None, None, None, None, None, None, 115880.592, None, None, ]
one_r30_2 = [262768.491, None, None, None, None, None, 65915.995, None, None, ]

one_r100_0 = [173068.851, None, None, None, None, 139263.366, 10031.278, None, None, ]
one_r100_1 = [None, None, None, None, None, None, 74214.803,None, None,]
one_r100_2 = [291705.168, None, None, None, None, None, 40334.004, None, None,]


# 5% poweroff
five_r6_0 = [104672.349, 190026.065, 109584.773, 180686.55, 184447.219, 100502.83, 66714.299, 130071.206, None]
five_r6_1 = [None, None, None, None, None, None, None, None, None]
five_r6_2 = [None, None, None, None, None, None, None, None, None]

five_r30_0 = [205112.707, None, 289125.973, None, None, 199970.763, 52464.305, None, None]
five_r30_1 = [None, None, None, None, None, None, None, None, None]
five_r30_2 = [None, None, None, None, None, None, 253432.151, None, None]

five_r100_0 = [None, None, None, None, None, 286507.081, 63296.424, None, None]
five_r100_1 = [None, None, None, None, None, None, 281989.005, None, None]
five_r100_2 = [None, None, None, None, None, None, 171497.294, None, None]


# Collect data into a dictionary
zero_data_lists = {
    '6#S0': zero_r6_0,
    '6#S1': zero_r6_1,
    '6#S2': zero_r6_2,
    '30#S0': zero_r30_0,
    '30#S1': zero_r30_1,
    '30#S2': zero_r30_2,
    '100#S0': zero_r100_0,
    '100#S1': zero_r100_1,
    '100#S2': zero_r100_2,
}


one_data_lists = {
    '6#S0': one_r6_0,
    '6#S1': one_r6_1,
    '6#S2': one_r6_2,
    '30#S0': one_r30_0,
    '30#S1': one_r30_1,
    '30#S2': one_r30_2,
    '100#S0': one_r100_0,
    '100#S1': one_r100_1,
    '100#S2': one_r100_2,
}


five_data_lists = {
    '6#S0': five_r6_0,
    '6#S1': five_r6_1,
    '6#S2': five_r6_2,
    '30#S0': five_r30_0,
    '30#S1': five_r30_1,
    '30#S2': five_r30_2,
    '100#S0': five_r100_0,
    '100#S1': five_r100_1,
    '100#S2': five_r100_2,
}


data_lists_set = [zero_data_lists, one_data_lists, five_data_lists]


# Define categories and data points
categories = ['Category 1'] * 3 + ['Category 2'] * 3 + ['Category 3'] * 3
data_points = ['Data Point 1', 'Data Point 2', 'Data Point 3'] * 3

# Create DataFrame
tuples = list(zip(categories, data_points))
columns = pd.MultiIndex.from_tuples(tuples, names=['Category', 'Data Point'])
zero_df = pd.DataFrame.from_dict(zero_data_lists, orient='index', columns=columns)
one_df = pd.DataFrame.from_dict(one_data_lists, orient='index', columns=columns)
five_df = pd.DataFrame.from_dict(five_data_lists, orient='index', columns=columns)

df_sets = [zero_df, one_df, five_df]
# Create a list to store column names (tuples) with spacers
column_tuples = []

# Add blank columns between categories
for i in range(len(categories)):
    column_tuples.append((categories[i], data_points[i]))
    # Check if the next category is different
    if i < len(categories) - 1 and categories[i] != categories[i + 1]:
        # Insert a blank column (Spacer)
        column_tuples.append(('Spacer', ''))

# Create MultiIndex with spacers
columns_with_spacers = pd.MultiIndex.from_tuples(column_tuples, names=['',''])#names=['Category', 'Data Point']

# Your custom x-tick labels
custom_labels = [
    "Freebeacon#Linkedlist", "Pulsar#Linkedlist", "Find#Linkedlist", 
    "Freebeacon#Tree", "Pulsar#Tree", "Find#Tree", 
    "Freebeacon#Ring", "Pulsar#Ring", "Find#Ring", 
]

# Replace None with np.nan for plotting

# Plot the heatmap
plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 25})  # Set font size globally
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(28, 24), constrained_layout=True)
for indexDatalist in range(3):
    # Create DataFrame with spacers
    
    df_with_spacers = pd.DataFrame(columns=columns_with_spacers, index=data_lists_set[indexDatalist].keys())
    # Fill in the data
    for col in df_sets[indexDatalist].columns:
        df_with_spacers[col] = df_sets[indexDatalist][col]
    
    # Prepare annotations with scientific notation, including spacers
    annotations_with_spacers = df_with_spacers.copy()
    def format_value(x):
        if pd.isna(x):
            return ''
        else:
            return '{:.2e}'.format(x)
    annotations_with_spacers = annotations_with_spacers.applymap(format_value)
    df_numeric_with_spacers = df_with_spacers.replace({None: np.nan})
    # Positions of data columns (excluding spacers)
    data_column_positions = [i for i, (category, _) in enumerate(df_with_spacers.columns) if category != 'Spacer']
    
    ax = sns.heatmap(df_numeric_with_spacers, 
                 ax=axes[indexDatalist],
                 annot=annotations_with_spacers.values,
                 fmt='',
                 cmap='viridis',
                 linewidths=0.5,
                 linecolor='white',
                 cbar_kws={'label': 'Value'},
    ) 

    # Overlay cross signs on missing data
    for y in range(df_numeric_with_spacers.shape[0]):
        for x in range(df_numeric_with_spacers.shape[1]):
            if pd.isna(df_numeric_with_spacers.iloc[y, x]) and df_with_spacers.columns[x][0] != 'Spacer':
                ax.text(x + 0.5, y + 0.5, '×', horizontalalignment='center',
                    verticalalignment='center', color='red')  # Increase font size of crosses
    # Draw vertical lines at the center of spacer columns
    spacer_positions = [i for i, (category, _) in enumerate(df_with_spacers.columns) if category == 'Spacer']
    for spacer in spacer_positions:
        ax.axvline(spacer + 0.5, color='black', linewidth=2)

    # Set x-ticks at the positions of data columns
    # ax.set_xticks([pos + 0.5 for pos in data_column_positions])
    #ax.set_xticklabels(custom_labels, ha='right')  # Increase font size
    ax.set_xticks([])

    # Increase font size of y-tick labels (data list names)
    ax.set_yticklabels(ax.get_yticklabels())

    # Increase font size of colorbar tick labels
    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.1e'))

    # Increase font size of colorbar label
    cbar.ax.set_ylabel('Time[s]')

plt.ylabel(None)

# Adjust layout to prevent label cutoff
# plt.tight_layout()

plt.savefig("aggregation_results.pdf", format='pdf')
# Show the plot
plt.show()










