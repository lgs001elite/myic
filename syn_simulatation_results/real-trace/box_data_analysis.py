import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv



trace_csv_names = ["cars_", "jogging_", "office_", "stairs_", "washer_"]
trace_names = ["Cars", "Jogging", "Office", "Stairs", "Washer", "Static", "Random"]
title ="energy_trace_"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick', "purple", "tomato", "lime"]


fontSize  = 16
lineWidth = 1.5



cars_set    = []
jogging_set = []
office_set  = []
stairs_set  = []
washer_set  = []
random_set  = []
static_set  = []


data_sets = [cars_set, jogging_set, office_set, stairs_set, washer_set, random_set, static_set]


# collect the data
index_set = 0
for prefix in trace_csv_names:
    for i in range(2):
        file = open(prefix+str(i)+"th.csv", mode='r')
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_sets[index_set].append(int(row[0]))
    index_set = index_set + 1


for i in range(2000):
    data_sets[6].append(np.random.randint(100, 501))

for i in range(2000):
    data_sets[5].append(100)

# plot the data
fig, ax = plt.subplots(figsize=(8, 6))
all_medians = []
all_means = []
sets_len = len(data_sets)
for i in range(sets_len):
    boxplot = ax.boxplot(data_sets[i], positions= [i + (sets_len + 1) + 1], patch_artist=True,
        boxprops=dict(facecolor=colors[i], color=colors[i], edgecolor=colors[i]),
        whiskerprops=dict(color=colors[i], linewidth=lineWidth),
        capprops=dict(color=colors[i], linewidth=lineWidth),
        medianprops=dict(color=colors[i], linewidth=lineWidth),
        flierprops=dict(marker='o', markerfacecolor=colors[i], markeredgecolor=colors[i], markersize=lineWidth, alpha=0.5),
        showmeans=True)
    print(trace_names[i]+":")
    print("min value:"+ str(np.min(data_sets[i])))
    print("max value:"+ str(np.max(data_sets[i])))
    print("ave value:"+ str(np.mean(data_sets[i])))
    print("var value:"+ str(np.var(data_sets[i])))
    print("sample standard deviation:"+ str(np.std(data_sets[i], ddof=1)))
    print("default standard deviation:"+ str(np.std(data_sets[i])))
    print("*****")
    # Extract median and mean for this box plot
    median = boxplot['medians'][0].get_ydata()[0]
    mean = boxplot['means'][0].get_ydata()[0]
    # Store medians and means
    all_medians.append((i + (sets_len + 1) + 1, median))
    all_means.append((i +  (sets_len + 1) + 1, mean))
# Unpack medians and means into x and y coordinates
median_x, median_y = zip(*all_medians)
mean_x, mean_y = zip(*all_means)

# Connect medians and means with lines
ax.plot(median_x, median_y, color=colors[4], linestyle='--', linewidth=2, marker='o')
ax.plot(mean_x, mean_y, color=colors[5], linestyle='--', linewidth=2, marker='o')

ax.set_ylabel("Charging time (slots))", fontsize=fontSize)
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax.set_yscale('log')
ax.set_xticks(range((sets_len + 1) + 1, (sets_len + 1) + 1 + 7))
ax.set_xticklabels(trace_names)
ax.set_xlabel("# Enery traces", fontsize=fontSize)
ax.tick_params(axis='both', which='major', labelsize=fontSize)


plt.savefig(f""+title+"_analysis.pdf", format="pdf", bbox_inches='tight')

