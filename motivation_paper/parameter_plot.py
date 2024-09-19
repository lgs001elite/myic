import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Helvetica'
plt.rcParams.update({'font.size': 18})  # Set font size globally

# Step 1: Read the first CSV file into a DataFrame
df1 = pd.read_csv('set_1_100_2.csv')

# Step 2: Read the second CSV file into a DataFrame
df2 = pd.read_csv('set_501_100_2.csv')

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
plt.figure(figsize=(4, 4))

# Plot CDF for first dataset
plt.plot(sorted_data1, cdf1, linestyle='-', label='Non-tuned', linewidth=3)

# Plot CDF for second dataset
plt.plot(sorted_data2, cdf2, linestyle='--', label='Tuned', linewidth=3)

# Step 7: Add title, labels, and legend
# plt.title('CDF of Data from Two Files')
plt.xlabel('Discovery time [ms]')
plt.ylabel(r'CDF [$\times 100\%$]')
plt.grid(False)
plt.legend(loc='lower right', frameon=False)

plt.tight_layout()

# Save the plot with a custom DPI
plt.savefig("../../figures/find_parameter.pdf", dpi=300)

# Step 8: Show the plot
plt.show()
