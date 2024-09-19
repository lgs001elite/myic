import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Data
r6_0 = [6597.293, 52013.921, None, 15951.269, 64861.283, None, 66714.299, 130071.206, None]
r6_1 = [154322.943, None, None, None, None, None, None, None, None]
r6_2 = [87863.821, None, None, 181425.569, None, None, None, None, None]

r30_0 = [2413.22, None, None, 9496.919, 280270.01, None, 52464.305, None, None]
r30_1 = [49539.026, None, None, 115880.592, None, None, None, None, None]
r30_2 = [26722.945, None, None, 65915.995, None, None, 253432.151, None, None]

r100_0 = [1717.907, None, None, 10031.278, None, None, 63296.424, None, None]
r100_1 = [23477.457, None, None, 74214.803,None, None, 281989.005, None, None]
r100_2 = [10886.152, None, None, 40334.004, None, None, 171497.294, None, None]

# Collect data into a dictionary
data_lists = {
    '6#[30,120]': r6_0,
    '6#[400,500]': r6_1,
    '6#[100,500]': r6_2,
    '30#[30,120]': r30_0,
    '30#[400,500]': r30_1,
    '30#[100,500]': r30_2,
    '100#[30,120]': r100_0,
    '100#[400,500]': r100_1,
    '100#[100,500]': r100_2,
}


# Define categories and data points
categories = ['Category 1'] * 3 + ['Category 2'] * 3 + ['Category 3'] * 3
data_points = ['Data Point 1', 'Data Point 2', 'Data Point 3'] * 3

# Create DataFrame
tuples = list(zip(categories, data_points))
columns = pd.MultiIndex.from_tuples(tuples, names=['Category', 'Data Point'])
df = pd.DataFrame.from_dict(data_lists, orient='index', columns=columns)

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
columns_with_spacers = pd.MultiIndex.from_tuples(column_tuples, names=['', ''])

# Create DataFrame with spacers
df_with_spacers = pd.DataFrame(columns=columns_with_spacers, index=data_lists.keys())

# Fill in the data
for col in df.columns:
    df_with_spacers[col] = df[col]

# The 'Spacer' columns will remain with NaN values

# Prepare annotations with scientific notation, including spacers
annotations_with_spacers = df_with_spacers.copy()
def format_value(x):
    if pd.isna(x):
        return ''
    else:
        return '{:.2e}'.format(x)
annotations_with_spacers = annotations_with_spacers.applymap(format_value)

# Replace None with np.nan for plotting
df_numeric_with_spacers = df_with_spacers.replace({None: np.nan})

# Your custom x-tick labels
custom_labels = [
    "freebeacon-no-poweroff", "pulsar-no-poweroff", "find-no-poweroff", 
    "freebeacon-1%-poweroff", "pulsar-1%-poweroff", "find-1%-poweroff",
    "freebeacon-5%-poweroff", "pulsar-5%-poweroff", "find-5%-poweroff"
]

# Positions of data columns (excluding spacers)
data_column_positions = [i for i, (category, _) in enumerate(df_with_spacers.columns) if category != 'Spacer']

# Plot the heatmap
plt.rcParams['font.size'] = str(24)
plt.figure(figsize=(28, 8))
ax = sns.heatmap(df_numeric_with_spacers,
                 annot=annotations_with_spacers.values,
                 fmt='',
                 cmap='viridis',
                 linewidths=0.5,
                 linecolor='white',
                 cbar_kws={'label': 'Value'},
                 )  # Increase font size of annotations annot_kws={"fontsize":12}

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
ax.set_xticks([pos + 0.5 for pos in data_column_positions])
ax.set_xticklabels(custom_labels, rotation=45, ha='right')  # Increase font size

# Increase font size of y-tick labels (data list names)
ax.set_yticklabels(ax.get_yticklabels(), rotation=5)

# Increase font size of colorbar tick labels
cbar = ax.collections[0].colorbar
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
#cbar.ax.tick_params() #labelsize=12

# Increase font size of colorbar label
cbar.ax.set_ylabel('Time [s]')

# Increase font size of title and axis labels
#plt.title('Heatmap of Data with Custom X-Tick Labels', fontsize=16)
# plt.xlabel('Data Sets', fontsize=14)
plt.ylabel('#Node num #Chr [slots]')

# Adjust layout to prevent label cutoff
plt.tight_layout()

plt.savefig("ring_simulation.pdf",format='pdf')
# Show the plot
plt.show()
