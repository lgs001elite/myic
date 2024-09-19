# import pandas as pd

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.ticker import ScalarFormatter


# # Load the CSV file
# file_path_freebeacon = './l_freebeacon_new.csv'
# df_freebeacon = pd.read_csv(file_path_freebeacon)

# file_path_find = './l_find_new.csv'
# df_find = pd.read_csv(file_path_find)

# # Extract the relevant columns
# df_filtered_freebeacon = df_freebeacon[df_freebeacon['Channel 3'] == 1]  # Filter rows where Channel 3 is 1
# df_filtered_find = df_find[df_find['Channel 3'] == 1]  # Filter rows where Channel 3 is 1

# # Calculate time intervals between consecutive ones in 'Channel 3'
# time_intervals_freebeacon = df_filtered_freebeacon['Time [s]'].diff().dropna()  # Calculate the difference between consecutive times
# time_intervals_find = df_filtered_find['Time [s]'].diff().dropna()  # Calculate the difference between consecutive times



# # Filter out the intervals that are greater than 0
# time_intervals_freebeacon = time_intervals_freebeacon[time_intervals_freebeacon > 14]
# time_intervals_find = time_intervals_find[time_intervals_find > 14]

# print(np.average(time_intervals_freebeacon))
# print(np.average(time_intervals_find))




# data_to_plot = [time_intervals_freebeacon, time_intervals_find]

# # Step 5: Create the box plot
# plt.rcParams['font.size'] = str(35)
# plt.figure(figsize=(8, 6))
# plt.boxplot(data_to_plot, labels=['FreeBeacon', 'Find'])

# # Get the current axis
# ax = plt.gca()

# # Set scientific notation for the y-axis
# ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
# ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

# # Optionally adjust the font size of tick labels
# ax.tick_params(axis='both', which='major')

# # Step 6: Add title and labels
# # plt.title('Box Plot of Data from Two Files')
# # plt.xlabel('Files')
# plt.ylabel('Time [s]')

# # Step 7: Show the plot
# # plt.grid(True)
# plt.savefig("riotee.pdf", format='pdf')
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Load the CSV files
file_path_freebeacon = './l_freebeacon_new.csv'
df_freebeacon = pd.read_csv(file_path_freebeacon)

file_path_find = './l_find_new.csv'
df_find = pd.read_csv(file_path_find)

# Extract the relevant rows where 'Channel 3' is 1
df_filtered_freebeacon = df_freebeacon[df_freebeacon['Channel 3'] == 1]
df_filtered_find = df_find[df_find['Channel 3'] == 1]

# Calculate time intervals between consecutive ones in 'Channel 3'
time_intervals_freebeacon = df_filtered_freebeacon['Time [s]'].diff().dropna()
time_intervals_find = df_filtered_find['Time [s]'].diff().dropna()

# Filter out the intervals that are greater than 14
time_intervals_freebeacon = time_intervals_freebeacon[time_intervals_freebeacon > 14]
time_intervals_find = time_intervals_find[time_intervals_find > 14]

print("Average Time Interval for FreeBeacon:", len(time_intervals_freebeacon))
print("Average Time Interval for Find:", len(time_intervals_find))

data_to_plot = [time_intervals_freebeacon, time_intervals_find]

# Create the horizontal box plot
plt.rcParams['font.family'] = ['Arial']
plt.rcParams['font.size'] = 35
plt.figure(figsize=(12, 6))
plt.boxplot(data_to_plot, labels=['FreeBeacon', 'Find'], vert=False)

# Get the current axis
ax = plt.gca()

# Set scientific notation for the x-axis
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))

# Optionally adjust the font size of tick labels
ax.tick_params(axis='both', which='major')

# Add labels
plt.xlabel('Time [s]')
# plt.ylabel('Methods')  # Optional: Label for the y-axis

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("riotee_horizontal.pdf", format='pdf')
plt.show()

