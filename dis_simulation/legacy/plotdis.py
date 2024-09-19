# pulsar_0     = [82071, 218902, 70347, 1496802, 272895, 145149, 3197429]
# freebeacon_0 = [22783, 28304, 14358, 452918, 37171, 15863, 258725]



# pulsar_1     = [82289, 184362, 66010, 1834057, 243095, 95282, 2222839]
# freebeacon_1 = [22500, 30259, 25229, 484611, 32555, 18204, 245847]



# pulsar_5     = [131500, 188859, 77410, 1862537, 272209, 103681, 3102167]
# freebeacon_5 = [30347, 22749, 13202, 507896, 43448, 16705, 252227]



# pulsar_10     = [96604, 211347, 81414, 1801680, 277559, 130821, 2625976]
# freebeacon_10 = [17690, 21490, 14966, 538459, 41701, 18267, 220280]

# x_ticks = ["Static", "Random", "Stairs trace", "Cars trace", "Jogging trace", "Office trace", "Washer trace"]




import matplotlib.pyplot as plt
import numpy as np

# Define the data
pulsar_0     = [82071, 218902, 70347, 1496802, 272895, 145149, 3197429]
freebeacon_0 = [22783, 28304, 14358, 452918, 37171, 15863, 258725]

pulsar_1     = [82289, 184362, 66010, 1834057, 243095, 95282, 2222839]
freebeacon_1 = [22500, 30259, 25229, 484611, 32555, 18204, 245847]

pulsar_5     = [131500, 188859, 77410, 1862537, 272209, 103681, 3102167]
freebeacon_5 = [30347, 22749, 13202, 507896, 43448, 16705, 252227]

pulsar_10     = [96604, 211347, 81414, 1801680, 277559, 130821, 2625976]
freebeacon_10 = [17690, 21490, 14966, 538459, 41701, 18267, 220280]

x_ticks = ["Static", "Random", "Stairs trace", "Cars trace", "Jogging trace", "Office trace", "Washer trace"]

# Create a dictionary of data for easier access
data = {
    0: {'Pulsar': pulsar_0, 'FreeBeacon': freebeacon_0},
    1: {'Pulsar': pulsar_1, 'FreeBeacon': freebeacon_1},
    5: {'Pulsar': pulsar_5, 'FreeBeacon': freebeacon_5},
    10: {'Pulsar': pulsar_10, 'FreeBeacon': freebeacon_10},
}

# Trials
trials = [0, 1, 5, 10]
Titles = ["#0% poweroff", "#1% poweroff", "#5% poweroff", "#10% poweroff"]

# Create subplots
plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 18})  # Set font size globally
fig, axes = plt.subplots(2, 2, figsize=(16, 12), sharey=True)
axes = axes.flatten()

for idx, trial in enumerate(trials):
    ax = axes[idx]
    pulsar_data = data[trial]['Pulsar']
    freebeacon_data = data[trial]['FreeBeacon']
    
    x = np.arange(len(x_ticks))
    width = 0.35  # Width of the bars

    # Plot bars
    if idx == 1:
        ax.bar(x - width/2, pulsar_data, width, label='Pulsar', color='steelblue')
        ax.bar(x + width/2, freebeacon_data, width, label='FreeBeacon', color='darkorange')
        ax.legend()
    else:
        ax.bar(x - width/2, pulsar_data, width, color='steelblue')
        ax.bar(x + width/2, freebeacon_data, width, color='darkorange')
    
    ax.set_title(Titles[idx])
    ax.set_xticks(x)
    ax.set_xticklabels(x_ticks, rotation=45)
    ax.set_yscale('log')
    if (idx%2) == 0:
        ax.set_ylabel('Discovery time [slots]')
    ax.grid(True, which="both", ls="--", linewidth=0.5)

# Adjust layout and show the plot
plt.tight_layout()
plt.savefig("disPerformance.pdf", format="pdf")
plt.show()








