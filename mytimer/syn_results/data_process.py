import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

line_width = 2.5  # Increase this value for bolder lines


# Load the second CSV file
file_path_1 = './find_10%_poweroff.csv'
df1 = pd.read_csv(file_path_1)
channel_15_ones_df1 = df1[df1['Channel 15'] == 1]
time_values = channel_15_ones_df1['Time [s]'].values
first_value = time_values[0]
intervals = [first_value]  # Start with the first value
intervals.extend(time_values[1:] - time_values[:-1])  # Calculate intervals for the rest
intervals_df1 = pd.DataFrame({
    'Time [s]': time_values,
    'Interval [s]': intervals
})

# Filter the dataframe to only include rows where Channel 15 is 1
file_path_2 = './freedis_10%_poweroff.csv'
df2 = pd.read_csv(file_path_2)
channel_15_ones_df2 = df2[df2['Channel 15'] == 1]
time_values = channel_15_ones_df2['Time [s]'].values
first_value = time_values[0]
intervals = [first_value]  # Start with the first value
intervals.extend(time_values[1:] - time_values[:-1])  # Calculate intervals for the rest
intervals_df2 = pd.DataFrame({
    'Time [s]': time_values,
    'Interval [s]': intervals
})



# Load the second CSV file
file_path_3 = './find_no_poweroff.csv'
df3 = pd.read_csv(file_path_3)
channel_15_ones_df3 = df3[df3['Channel 15'] == 1]
time_values = channel_15_ones_df3['Time [s]'].values
first_value = time_values[0]
intervals = [first_value]  # Start with the first value
intervals.extend(time_values[1:] - time_values[:-1])  # Calculate intervals for the rest
intervals_df3 = pd.DataFrame({
    'Time [s]': time_values,
    'Interval [s]': intervals
})



# Load the second CSV file
file_path_4 = './freedis_no_poweroff.csv'
df4 = pd.read_csv(file_path_4)
channel_15_ones_df4 = df4[df4['Channel 15'] == 1]
time_values = channel_15_ones_df4['Time [s]'].values
first_value = time_values[0]
intervals = [first_value]  # Start with the first value
intervals.extend(time_values[1:] - time_values[:-1])  # Calculate intervals for the rest
intervals_df4 = pd.DataFrame({
    'Time [s]': time_values,
    'Interval [s]': intervals
})






# Extracting intervals from both files
intervals_1 = intervals_df1['Interval [s]'].values
intervals_2 = intervals_df2['Interval [s]'].values
intervals_3 = intervals_df3['Interval [s]'].values
intervals_4 = intervals_df4['Interval [s]'].values


intervals_1_ms = intervals_1 * 1000  # Convert to milliseconds
intervals_2_ms = intervals_2 * 1000  # Convert to milliseconds
intervals_3_ms = intervals_3 * 1000  # Convert to milliseconds
intervals_4_ms = intervals_4 * 1000  # Convert to milliseconds

intervals_1_ms = intervals_1_ms[intervals_1_ms >= 83]
intervals_2_ms = intervals_2_ms[intervals_2_ms >= 83]
intervals_3_ms = intervals_3_ms[intervals_3_ms >= 83]
intervals_4_ms = intervals_4_ms[intervals_4_ms >= 83]
# CDF Plot
# Calculate the CDF for the first dataset
sorted_intervals_1 = np.sort(intervals_1_ms)
cdf_1 = np.arange(1, len(sorted_intervals_1) + 1) / len(sorted_intervals_1)

# Calculate the CDF for the second dataset
sorted_intervals_2 = np.sort(intervals_2_ms)
cdf_2 = np.arange(1, len(sorted_intervals_2) + 1) / len(sorted_intervals_2)

# Calculate the CDF for the second dataset
sorted_intervals_3 = np.sort(intervals_3_ms)
cdf_3 = np.arange(1, len(sorted_intervals_3) + 1) / len(sorted_intervals_3)

# Calculate the CDF for the second dataset
sorted_intervals_4 = np.sort(intervals_4_ms)
cdf_4 = np.arange(1, len(sorted_intervals_4) + 1) / len(sorted_intervals_4)

# Plotting the CDFs
plt.rcParams['font.size'] = str(23)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
#AX1
ax1.plot(sorted_intervals_1, cdf_1, label='Find', linewidth=line_width)
ax1.plot(sorted_intervals_2, cdf_2, label='FreeBeacon', linestyle='--', linewidth=line_width)
ax1.set_xlabel('Syn time[ms]')
ax1.set_ylabel('CDF')
ax1.set_title('With 10% power-off')
# plt.xlim(right=0)
ax1.set_ylim(bottom=0)
ax1.set_xscale('log')
ax1.legend()
print(np.average(sorted_intervals_1))
print(np.average(sorted_intervals_2))
print(2000000/np.size(sorted_intervals_1))
print(2000000/np.size(sorted_intervals_2))
print("****************")

#AX2
ax2.plot(sorted_intervals_3, cdf_3, label='Find', linewidth=line_width)
ax2.plot(sorted_intervals_4, cdf_4, label='FreeBeacon', linestyle='--', linewidth=line_width)
ax2.set_xlabel('Syn time[ms]')
ax2.set_title('With no power-off')
# plt.xlim(right=0)
ax2.set_ylim(bottom=0)
ax2.set_xscale('log')
ax2.legend()
print(np.average(sorted_intervals_3))
print(np.average(sorted_intervals_4))
print(2000000/np.size(sorted_intervals_3))
print(2000000/np.size(sorted_intervals_4))


print(np.size(sorted_intervals_1))
print(np.size(sorted_intervals_2))
print(np.size(sorted_intervals_3))
print(np.size(sorted_intervals_4))


# 131623.85570133332
# 53292.30063135136
# 133333.33333333334
# 54054.05405405405
# ****************
# 162025.72429333333
# 98022.15063111112
# 166666.66666666666
# 111111.11111111111

plt.tight_layout()
plt.savefig("syn_prototype.pdf", format='pdf')
plt.close("all")
