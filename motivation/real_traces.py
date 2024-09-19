import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter

formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-3, 3))

# Load the dataset
file_path_new = './cars_0th.csv'
df_new = pd.read_csv(file_path_new)

# Extract the data from the first column
new_data = df_new[df_new.columns[0]]

# Calculate the median value of the data
median_value = new_data.median()


plt.rcParams.update({'font.size': 14})  # Set font size globally
# Create the violin plot and line plot with shared y-axis, keeping the original violin plot and zooming on the median without overlap
fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharey=True, gridspec_kw={'width_ratios': [2, 1]})



# Line plot without y-axis and without grid lines
ax[0].plot(new_data)
#ax[0].set_title('Line: Cars Scenario')
ax[0].grid(False)  # Remove grid lines
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].set_ylabel('Charging times [ms]')

# Create an inset within the right plot with adjusted y-axis limit
ax_inset_left = ax[0].inset_axes([0.1, 0.5, 0.4, 0.4])  # Adjusted position for the inset (shifted to the left)
ax_inset_left.plot(new_data)
ax_inset_left.grid(False)  # Remove grid lines in the zoomed inset plot

# Zoom in on the x-axis between 550 and 650, with y-axis ranging from 0 to 20000
ax_inset_left.set_xlim(550, 650)
ax_inset_left.set_ylim(0, 20000)  # Adjust the y-axis to start from 0 to 20000 for the zoomed section
#ax_inset_left.set_title('Zoomed Section [550, 650]')
ax_inset_left.yaxis.set_major_formatter(formatter)

# Add arrows from the non-zoomed plot's x-axis to the zoomed plot's x-axis, in the correct direction
ax[0].annotate('', xy=(0.2, 0), xytext=(550, 0), 
               textcoords='data', xycoords=ax_inset_left.transAxes, arrowprops=dict(facecolor='black', arrowstyle='->'))
ax[0].annotate('', xy=(0.8, 0), xytext=(650, 0), 
               textcoords='data', xycoords=ax_inset_left.transAxes, arrowprops=dict(facecolor='black', arrowstyle='->'))



# Violin plot with the full data range
sns.violinplot(data=new_data, ax=ax[1])
#ax[1].set_title('Violin: Cars Scenario')
ax[1].grid(False)  # Remove grid lines
ax[1].tick_params(left=False, right=False, labelleft=False)  # Remove y-axis ticks and labels for the right plot
ax[1].spines['left'].set_visible(False)  # Remove the left y-axis spine
ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)


# Adjust the inset to zoom in on the median, without overlapping the original plot
ax_inset_box  = ax[1].inset_axes([0.1, 0.6, 0.2, 0.3])  # Place the inset outside the original violin plot
box = sns.boxplot(data=new_data, ax=ax_inset_box, width=0.3, showfliers=False, showmeans=True) 
#ax_inset_box.set_title('Zoomed Box Plot')
ax_inset_box.set_ylabel('')
ax_inset_box.grid(False)
ax_inset_box.yaxis.set_major_formatter(formatter)




print(max(new_data))
print(min(new_data))
print(np.percentile(new_data, 25))
print(np.percentile(new_data, 75))

# ax[0].annotate('', xy=(0.5, median_value), xycoords='data', xytext=(0.25, 0.6),
#                textcoords='figure fraction', arrowprops=dict(facecolor='black', arrowstyle='->'))

# Add an arrow from the median value on the main plot to the zoomed inset
ax[1].annotate('', xy=(0.4, 0),  xytext=(0, median_value),
               textcoords='data', xycoords=ax_inset_box.transAxes,  arrowprops=dict(facecolor='black', arrowstyle='->'))





ax[0].yaxis.set_major_formatter(formatter)
ax[1].yaxis.set_major_formatter(formatter)

# Display the plots
plt.tight_layout()
plt.show()










