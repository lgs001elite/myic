# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.ticker import ScalarFormatter

# # Step 1: Read the first CSV file into a DataFrame
# df1 = pd.read_csv('set1.csv')
# df1_1 = pd.read_csv('set1_20.csv')

# # Step 2: Read the second CSV file into a DataFrame
# df2 = pd.read_csv('set2.csv')
# df2_1 = pd.read_csv('set2_20.csv')

# # Step 3: Choose the columns for which you want to plot the box plot
# # Replace 'data_column' with the actual column names in your CSV files
# data1 = df1['0']  # for first file
# data1_1 = df1_1['0']  # for first file

# data2 = df2['0']  # for second file
# data2_1 = df2_1['0']  # for second file

# # Step 4: Combine the two datasets into a list
# data_to_plot = [data1, data1_1, data2, data2_1]

# # Step 5: Create the box plot
# plt.figure(figsize=(8, 6))
# ax = plt.boxplot(data_to_plot, labels=['Scheduled#10nodes', 'Scheduled#20nodes', 'Random#10nodes', 'Random#20nodes'])
# # Step 6: Add title and labels
# # plt.title('Box Plot of Data from Two Files')
# # plt.xlabel('Files')
# plt.ylabel('Aggregation numbers')


# # Get the current axis
# ax = plt.gca()

# # Set scientific notation for the y-axis
# ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
# ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

# # Optionally adjust the font size of tick labels
# ax.tick_params(axis='both', which='major', labelsize=12)

# # Step 7: Show the plot
# # plt.grid(True)

# plt.savefig("find_dis_aggregation.png")
# plt.show()





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Step 1: Read the CSV files into DataFrames
df1 = pd.read_csv('set1.csv')
df1_1 = pd.read_csv('set1_50.csv')
df2 = pd.read_csv('set2.csv')
df2_1 = pd.read_csv('set2_50.csv')

# Step 2: Choose the columns for which you want to plot the box plot
# Replace '0' with the actual column names in your CSV files if different
data1 = df1['0']
data1_1 = df1_1['0']
data2 = df2['0']
data2_1 = df2_1['0']

# Step 3: Combine the datasets into a list
data_to_plot = [data1, data1_1, data2, data2_1]
print(np.average(data1))
print(np.average(data1_1))

# Step 4: Create the box plot
fig, ax = plt.subplots(figsize=(8, 6))
bp = ax.boxplot(data_to_plot, labels=['Scheduled#10nodes', 'Scheduled#50nodes', 'Random#10nodes', 'Random#50nodes'])

# Step 5: Rotate x-tick labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', fontsize=12)

# Step 6: Add labels and format y-axis
ax.set_ylabel('Aggregation numbers', fontsize=14)

# Set scientific notation for the y-axis
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

# Adjust tick parameters
ax.tick_params(axis='both', which='major', labelsize=12)

# Step 7: Adjust layout and save the plot
plt.tight_layout()
plt.savefig("find_dis_aggregation.png")
plt.show()





