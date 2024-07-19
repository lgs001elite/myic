import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the ranges for M and N
N = np.linspace(1, 100, 50)  # Range for N
M = np.linspace(1, 100, 50)  # Range for M
N, M = np.meshgrid(N, M)  # Create a meshgrid

# Define the three functions
T1 = np.log2(N + 1) * M
T2 = np.array([np.sum([(N - 1) + 2 * (i - 1) for i in range(1, int(n) + 1)]) for N, n in zip(np.ravel(N), np.ravel(M))]).reshape(N.shape)
T3 = ((N - 1) * M) / (np.log2(N) + 1)

# Plotting the three functions in separate subplots
plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['font.size'] = str(21)
plt.rcParams['font.family'] = 'Arial'
fig = plt.figure(figsize=(24, 6), layout="constrained")

# Plot for T1
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(N, M, T1, cmap='viridis')
ax1.set_title(r'Tree-reduced pattern')
ax1.set_xlabel("N",labelpad=20)
ax1.set_ylabel("M",labelpad=20)
#ax1.set_zlabel('Time')

# Plot for T2
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(N, M, T2, cmap='plasma')
ax2.set_title(r'Linked-list-reduced pattern')
ax2.set_xlabel("N",labelpad=20)
ax2.set_ylabel("M",labelpad=20)
#ax2.set_zlabel('Time')

# Plot for T3
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(N, M, T3, cmap='inferno')
ax3.set_title(r'Ring-reduced pattern')
ax3.set_xlabel("N",labelpad=20)
ax3.set_ylabel("M",labelpad=20)
ax3.set_zlabel('T',labelpad=20)


ax1.ticklabel_format(axis='z', style='sci', scilimits=(0, 0))
ax2.ticklabel_format(axis='z', style='sci', scilimits=(0, 0))
ax3.ticklabel_format(axis='z', style='sci', scilimits=(0, 0))

plt.tight_layout()
plt.savefig("performance_patterns_N_M.pdf", format='pdf')
plt.close("all")


