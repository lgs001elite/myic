# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from matplotlib.ticker import ScalarFormatter

# plt.rcParams['font.family'] = 'Helvetica'
# plt.rcParams.update({'font.size': 18})  # Set font size globally

# formatter = ScalarFormatter(useMathText=True)
# formatter.set_scientific(True)

# # Step 1: Read the first CSV file into a DataFrame
# df1_10 = pd.read_csv('set1.csv')
# df1_2 = pd.read_csv('set1_2.csv')
# df1_50 = pd.read_csv('set1_50.csv')

# # Step 2: Read the second CSV file into a DataFrame
# df2_10 = pd.read_csv('set2.csv')
# df2_2 = pd.read_csv('set2_2.csv')
# df2_50 = pd.read_csv('set2_50.csv')

# # Step 3: Choose the columns for which you want to plot the box plot
# # Replace 'data_column' with the actual column names in your CSV files
# data1_2 = df1_2['0']  # for first file
# data1_10 = df1_10['0']  # for first file
# data1_50 = df1_50['0']  # for first file


# data2_2 = df2_2['0']  # for second file
# data2_10 = df2_10['0'] 
# data2_50 = df2_50['0'] 

# data = {
#     'Group': ['#2Nodes', '#2Nodes', '#10Nodes', '#10Nodes', '#50Nodes', '#50Nodes'],
#     'Subgroup': ['Scheduled', 'Random', 'Scheduled', 'Random', 'Scheduled', 'Random'],
#     'Value': [data1_2, data2_2, data1_10, data2_10, data1_50, data2_50]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Step 5: Create the box plot
# plt.figure(figsize=(4, 4))
# # plt.boxplot(data_to_plot, labels=['Random', 'Scheduled'])
# sns.boxplot(x='Group', y='Value', hue='Subgroup', data=df, palette='Set2')

# # Step 6: Add title and labels
# # plt.title('Box Plot of Data from Two Files')
# # plt.xlabel('Files')
# plt.ylabel('Comm. completion count')
# plt.legend()

# # Get the current axis
# ax = plt.gca()

# # Set scientific notation for the y-axis
# # ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
# # ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

# # Optionally adjust the font size of tick labels
# # ax.tick_params(axis='both', which='major', labelsize=12)

# # Step 7: Show the plot
# # plt.grid(True)

# plt.tight_layout()

# # Save the plot with a custom DPI
# plt.savefig("../../figures/find_scheduled.pdf", dpi=300)

# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter

plt.rcParams['font.family'] = 'Helvetica'
plt.rcParams.update({'font.size': 18})  # Set font size globally

formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)

# Step 1: Read the CSV files into DataFrames
df1_2 = pd.read_csv('set1_2.csv')
df1_10 = pd.read_csv('set1.csv')
df1_50 = pd.read_csv('set1_50.csv')

df2_2 = pd.read_csv('set2_2.csv')
df2_10 = pd.read_csv('set2.csv')
df2_50 = pd.read_csv('set2_50.csv')

# Step 2: Extract the '0' column from each DataFrame
data1_2 = df1_2['0']
data1_10 = df1_10['0']
data1_50 = df1_50['0']

data2_2 = df2_2['0']
data2_10 = df2_10['0']
data2_50 = df2_50['0']

# Step 3: Create individual DataFrames for each group and subgroup
df1 = pd.DataFrame({'Group': '#2Nodes', 'Subgroup': 'Scheduled', 'Value': data1_2})
df2 = pd.DataFrame({'Group': '#2Nodes', 'Subgroup': 'Random', 'Value': data2_2})
df3 = pd.DataFrame({'Group': '#10Nodes', 'Subgroup': 'Scheduled', 'Value': data1_10})
df4 = pd.DataFrame({'Group': '#10Nodes', 'Subgroup': 'Random', 'Value': data2_10})
df5 = pd.DataFrame({'Group': '#50Nodes', 'Subgroup': 'Scheduled', 'Value': data1_50})
df6 = pd.DataFrame({'Group': '#50Nodes', 'Subgroup': 'Random', 'Value': data2_50})

# Step 4: Concatenate the DataFrames
df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)

# Step 5: Create the box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Group', y='Value', hue='Subgroup', data=df, palette='Set2')

# Step 6: Add labels and legend
plt.ylabel('Comm. completion count')
plt.xlabel('')
plt.yscale('log')
plt.legend()

# Step 7: Adjust the plot
plt.tight_layout()

# Step 8: Save and show the plot
plt.savefig("../../figures/find_scheduled.pdf", dpi=300)
plt.show()

