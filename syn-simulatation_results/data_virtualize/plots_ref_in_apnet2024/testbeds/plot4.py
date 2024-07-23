import matplotlib.pyplot as plt
import numpy as np

species = ("Find", "Greedy", "Pulsar")
penguin_means = {
    'Testbes': (1907, 2923, 775),
    'Simulation': (2792, 3034, 900),
}

plt.rcParams['font.size'] = str(20)
plt.rcParams['font.family'] = 'Arial'

x = np.arange(len(species))  # the label locations
width = 0.25 # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained', figsize=(8, 4))

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Latency (Time Slots)')
#ax.set_title('Penguin attributes by species')
width = 0.12
ax.set_xticks(x + width, species)
ax.legend(loc='center right', ncols=3)
ax.ticklabel_format(axis="y", style="scientific", useMathText="true") # {'sci', 'scientific', 'plain'}
# ax.set_ylim(0, 250)
plt.savefig("testbed_performance" + ".pdf", format="pdf", bbox_inches="tight")
#plt.show()
plt.close("all")