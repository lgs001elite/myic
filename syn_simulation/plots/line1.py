import numpy as np
import matplotlib.pyplot as plt

# Example data generation
# Replace with your actual data
days_of_week = ['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.']
traffic_inter_data = np.random.normal(0.5, 0.1, 100)  # Random data simulating inter-data-center traffic
traffic_customer_facing = np.random.normal(0.6, 0.2, 100)  # Random data simulating customer-facing traffic

# Prepare figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

# Subplot 1: Inter-data-center traffic
axs[0].plot(np.tile(days_of_week, len(traffic_inter_data)//len(days_of_week)), traffic_inter_data, color='blue')
axs[0].set_title('(a) Inter-data-center traffic')
axs[0].set_ylabel('STD / Mean')
axs[0].set_xlabel('Day of Week')
axs[0].set_xticks(np.arange(len(days_of_week)))
axs[0].set_xticklabels(days_of_week)
axs[0].set_ylim([0, 1])

# Subplot 2: Customer-facing traffic
axs[1].plot(np.tile(days_of_week, len(traffic_customer_facing)//len(days_of_week)), traffic_customer_facing, color='blue')
axs[1].set_title('(b) Customer-facing traffic')
axs[1].set_xlabel('Day of Week')
axs[1].set_xticks(np.arange(len(days_of_week)))
axs[1].set_xticklabels(days_of_week)

# Adjust layout and show the plot
plt.tight_layout()
plt.savefig("traffic_variability.pdf", dpi=300)
plt.show()



