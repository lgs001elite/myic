






import matplotlib.pyplot as plt


linkedlist_0_per   = [179272, 6502493, 83126369, 165779, 2073149, 22691879, 565399, 1030599, 411162799]
linkedlist_1_per   = [211277, 7230143, 95305493, 301439, 2747009, 28288469, 1431799, 1499399, 12152199]
linkedlist_10_per  = [533645, 15536479, 196116665, 967859, 10200539, 92884859, 3268499, 5306899, 43533899]
linkedlist_50_per  = [1749568, 39001449, 488874496, 8299829, 60328409, 546046559, 34816099, 48454999, 327591773]
linkedlist_70_per  = [1884396, 43804235, 536125696, 14767293, 88118307, 796034245, 66365971, 96244831, 575630437]
linkedlist_90_per  = [2077175, 48666979, 560627899, 22006848, 118782899, 1035728326, 114073701, 157400652, 876997398]
linkedlist_100_per = [2251611, 49946454, 563105608, 25933355, 135222199, 1082027865, 144364811, 195476448, 916322162]




ring_0_per   = [616834, 9516634, 118536502, 218910, 32833784, 136554268, 735600, 353078374, 501802661]
ring_1_per   = [705352, 10536758, 130578072, 30112542, 32125390, 107896534, 384362378, 305229642, 619213869]
ring_10_per  = [841840, 19906916, 241200596, 21671352, 36925736, 140578318, 294667998, 262172784, 866343233]
ring_50_per  = [2491492, 53162518, 676890382, 15649106, 55258072, 369094962, 332517407, 355970501, 788348880]
ring_70_per  = [2882081, 56403260, 738498212, 20968646, 67099746, 496292956, 357207966, 455724409, 871205451]
ring_90_per  = [3901786, 77351362, 864714762, 23883792, 83488872, 609834764, 491899022, 324294580, 1099342240]
ring_100_per = [3427353, 71980829, 793629514, 24514819, 95112604, 680013787, 457673281, 546679472, 1179298244]



tree_0_per   = [286451, 8115287, 98918657, 2551919, 4363709, 42498479, 29176499, 8798399, 22418999]
tree_1_per   = [331498, 8982395, 106650401, 2766839, 5819639, 50070869, 40327599, 10227999, 28495699]
tree_10_per  = [728261, 17044071, 199813871, 3180389, 15482399, 118341449, 20436399, 14007799, 77407799]
tree_50_per  = [1581888, 36499777, 445378914, 9948119, 59388742, 507851712, 54707099, 73801599, 392732767]
tree_70_per  = [1807634, 40044406, 471944926, 15193619, 81788019, 688684068, 97691232, 129079399, 656295708]
tree_90_per  = [1961731, 42995672, 518394715, 20949389, 102721259, 831441837, 155209799, 205115714, 923282350]
tree_100_per = [2033194, 44721581, 520537137, 24015690, 113513984, 894032518, 191135217, 247687085, 1084982572]

# Updated x_labels
x_labels = ["6#0", "6#1", "6#2", "30#0", "30#1", "30#2", "100#0", "100#1", "100#2"]

# Plotting the data with the updated x_labels
plt.figure(figsize=(12, 8))

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['font.size'] = str(23)
plt.rcParams['font.family'] = 'Arial'

plt.plot(x_labels, linkedlist_0_per, marker='o', label='#0%')
plt.plot(x_labels, linkedlist_1_per, marker='s', label='#1%')
plt.plot(x_labels, linkedlist_10_per, marker='D', label='#10%')
plt.plot(x_labels, linkedlist_50_per, marker='^', label='#50%')
plt.plot(x_labels, linkedlist_70_per, marker='v', label='#70%')
plt.plot(x_labels, linkedlist_90_per, marker='x', label='#90%')
plt.plot(x_labels, linkedlist_100_per, marker='*', label='#100%')

# plt.plot(x_labels, ring_0_per, marker='o', label='#0%')
# plt.plot(x_labels, ring_1_per, marker='s', label='#1%')
# plt.plot(x_labels, ring_10_per, marker='D', label='#10%')
# plt.plot(x_labels, ring_50_per, marker='^', label='#50%')
# plt.plot(x_labels, ring_70_per, marker='v', label='#70%')
# plt.plot(x_labels, ring_90_per, marker='x', label='#90%')
# plt.plot(x_labels, ring_100_per, marker='*', label='#100%')

# plt.plot(x_labels, tree_0_per, marker='o', label='#0%')
# plt.plot(x_labels, tree_1_per, marker='s', label='#1%')
# plt.plot(x_labels, tree_10_per, marker='D', label='#10%')
# plt.plot(x_labels, tree_50_per, marker='^', label='#50%')
# plt.plot(x_labels, tree_70_per, marker='v', label='#70%')
# plt.plot(x_labels, tree_90_per, marker='x', label='#90%')
# plt.plot(x_labels, tree_100_per, marker='*', label='#100%')

plt.xlabel('Scenarios [node numbers#energy conditions]')
plt.ylabel('Aggregation time [slots (Log Scale)]')
plt.yscale('log')  # Applying logarithmic scale to the y-axis
#plt.title('Performance Comparison Across Different Operations (Log Scale)')
#plt.legend(title='Power-off rates')
plt.grid(True, which="both", ls="--")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("linkedlist_reduce.pdf", format='pdf')

# plt.savefig("ring_reduce.pdf", format='pdf')


# plt.savefig("tree_reduce.pdf", format='pdf')


