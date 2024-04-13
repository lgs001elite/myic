# import matplotlib.pyplot as plt
# import numpy as np


# fig = plt.figure(constrained_layout=True)
# fig.suptitle('Figure title')

# # create 3x1 subfigs
# subfigs = fig.subfigures(nrows=3, ncols=1)
# for row, subfig in enumerate(subfigs):
#     subfig.suptitle(f'Subfigure title {row}')

#     # create 1x3 subplots per subfig
#     axs = subfig.subplots(nrows=1, ncols=3)
#     for col, ax in enumerate(axs):
#         ax.plot()
#         ax.set_xlabel("r")
#         ax.set_ylabel("r")
#         ax.set_title(f'Plot title {col}')

# plt.show()


import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np

# Step 1: Create the main plot
# Generate the data
x = np.linspace(0, 10, 1000)
y = np.sin(x)

fig, ax = plt.subplots()  # Create a figure and an axes
ax.plot(x, y, label='Sine Wave')  # Plot sine wave

# Step 2: Add an inset axes at the desired location on the main plot
# The inset_axes function arguments specify the parent axes (ax), width, height, and location
axins = inset_axes(ax, width="30%", height="30%", loc='upper right')

# Step 3: Plot the same data on the inset axes, focusing on the zoom region
# Define the zoom region (x1, x2, y1, y2)
x1, x2, y1, y2 = 2, 3, -1, 1
axins.plot(x, y)
axins.set_xlim(x1, x2)  # Set x-limits for the inset axes
axins.set_ylim(y1, y2)  # Set y-limits for the inset axes

# Step 4: Optionally, highlight the zoomed region on the main plot
# This function draws a rectangle and connects it with lines to the inset axes.
ax.indicate_inset_zoom(axins, edgecolor="black")

plt.show()

plt.close()