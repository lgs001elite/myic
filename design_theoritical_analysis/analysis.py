import numpy as np
import matplotlib.pyplot as plt

# Define large M
M = 1e6

# Define the functions with large M
def T1_large(N):
    return np.log2(N + 1) * M

def T2_large(N):
    return M * ((N - 1) + 2 * (M - 1))

def T3_large(N):
    return (N - 1) * M / (np.log2(N) + 1)

# Generate a range of N values
N_values = np.linspace(1, 1000, 1000)

# Calculate the values of the functions
T1_values = T1_large(N_values)
T2_values = T2_large(N_values)
T3_values = T3_large(N_values)

# Plotting the functions
plt.figure(figsize=(10, 6))
plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['font.size'] = str(23)
plt.rcParams['font.family'] = 'Arial'

plt.plot(N_values, T1_values, label=r'Tree-reduced pattern')
plt.plot(N_values, T2_values, label=r'Linked-list-reduced pattern')
plt.plot(N_values, T3_values, label=r'Ring-reduced pattern')

plt.xlabel('Node numbers')
plt.ylabel('Aggregation time [slots]')
#plt.title('Comparison of Functions with Large M')
plt.legend()
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.yscale('log')  # Use logarithmic scale for better visualization
plt.tight_layout()
plt.savefig("performance_patterns.pdf", format='pdf')
plt.close("all")

