import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the comparison function to find the index of the minimum value
def compare_functions(Z1, Z2, Z3):
    comparison = np.zeros_like(Z1)
    comparison[Z1 < Z2] = 1
    comparison[(Z1 >= Z2) & (Z2 < Z3)] = 2
    comparison[(Z1 >= Z3) & (Z3 < Z2)] = 3
    return comparison

# Generate a range of values for N and M
N = np.linspace(1, 100, 100)
M = np.linspace(1, 100, 100)
N, M = np.meshgrid(N, M)

# Calculate the values of the functions
Z1 = T1(N, M)
Z2 = T2(N, M)
Z3 = T3(N, M)

# Compare the functions
comparison = compare_functions(Z1, Z2, Z3)

# Plot the comparison results
plt.figure(figsize=(10, 8))
plt.contourf(N, M, comparison, levels=[0, 1, 2, 3], colors=['red', 'green', 'blue'], alpha=0.5)
plt.colorbar(ticks=[1, 2, 3], label='Best Function')
plt.xlabel('N')
plt.ylabel('M')
plt.title('Best Function for Different N and M Combinations')
plt.show()
