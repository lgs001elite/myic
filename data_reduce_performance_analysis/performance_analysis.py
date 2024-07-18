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
plt.rcParams['font.size'] = str(15)
plt.rcParams['font.family'] = 'Arial'
fig = plt.figure(figsize=(18, 6))

# Plot for T1
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(N, M, T1, cmap='viridis')
ax1.set_title(r'$T = O(\log_{2}(N + 1) \times M)$')
ax1.set_xlabel("Node numbers")
ax1.set_ylabel("Message rounds")
ax1.set_zlabel('Time slots')

# Plot for T2
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(N, M, T2, cmap='plasma')
ax2.set_title(r'$T = O\left(\sum_{i=1}^{M} ((N - 1) + 2 \times (i - 1))\right)$')
ax2.set_xlabel("Node numbers")
ax2.set_ylabel("Message rounds")
ax2.set_zlabel('Time slots')

# Plot for T3
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(N, M, T3, cmap='inferno')
ax3.set_title(r'$T = O\left(\frac{(N-1) \times M}{\log_{2}N + 1}\right)$')
ax3.set_xlabel("Node numbers")
ax3.set_ylabel("Message rounds")
ax3.set_zlabel('Time slots')


ax1.ticklabel_format(axis='z', style='sci', scilimits=(0, 0))
ax2.ticklabel_format(axis='z', style='sci', scilimits=(0, 0))
ax3.ticklabel_format(axis='z', style='sci', scilimits=(0, 0))

plt.tight_layout()
plt.savefig("performance_patterns_N_M.pdf", format='pdf')
plt.close("all")


