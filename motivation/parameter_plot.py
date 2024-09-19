import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Step 1: Read the first CSV file into a DataFrame
df1 = pd.read_csv('set_1_100.csv')

# Step 2: Read the second CSV file into a DataFrame
df2 = pd.read_csv('set_501_100.csv')

# Step 3: Choose the columns for which you want to plot the CDF
# Replace 'data_column' with the actual column names in your CSV files
data1 = df1['0']  # for first file
data2 = df2['0']  # for second file

# Step 4: Sort the data for both datasets
sorted_data1 = np.sort(data1)
sorted_data2 = np.sort(data2)
print(np.average(sorted_data1))
print(np.average(sorted_data2))
# Step 5: Calculate the CDF values for both datasets
cdf1 = np.arange(1, len(sorted_data1) + 1) / len(sorted_data1)
cdf2 = np.arange(1, len(sorted_data2) + 1) / len(sorted_data2)

# Step 6: Plot both CDFs on the same graph
plt.figure(figsize=(8, 6))

# Plot CDF for first dataset
plt.plot(sorted_data1, cdf1, marker='.', linestyle='-', label='Non-fit')

# Plot CDF for second dataset
plt.plot(sorted_data2, cdf2, marker='.', linestyle='--', label='Fit')

# Get the current axis
ax = plt.gca()

# Set scientific notation for the y-axis
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

# Optionally adjust the font size of tick labels
ax.tick_params(axis='both', which='major', labelsize=12)

# Step 7: Add title, labels, and legend
# plt.title('CDF of Data from Two Files')
plt.xlabel('#Syn time [slots]')
plt.ylabel('#CDF')
# plt.grid(True)
plt.legend()

plt.savefig("Find_parameters.pdf")

# Step 8: Show the plot
plt.show()
