

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import csv

findSet = [96886, 75900, 1650, 1650, 1650, 1650, 1650, 1650, 1650, 3300]
findSet = [x//30 for x in findSet]
pulsarSet = [1706, 3440, 3394, 10182, 8005, 7653, 4560, 5890, 3908, 3336]
pulsarSet = [x//30 for x in pulsarSet]
pulsarNASet = [28654, 32112, 21986, 20418, 20378, 23668, 23668, 21986, 22100, 1717]
pulsarNASet = [x//30 for x in pulsarNASet]
print(type(findSet))

findSet_sorted = np.sort(findSet)
pulsarSet_sorted = np.sort(pulsarSet)
pulsarNASet_sorted = np.sort(pulsarNASet)
print(np.mean(findSet))
print(np.mean(pulsarSet))
print(np.mean(pulsarNASet))

cdf_find = np.arange(1, len(findSet_sorted) + 1) / len(findSet_sorted)
cdf_pulsar = np.arange(1, len(pulsarSet_sorted) + 1) / len(pulsarSet_sorted)
# cdf_pulsarNA = np.arange(1, len(pulsarNASet_sorted) + 1) / len(pulsarNASet_sorted)

plt.figure(layout="constrained", figsize=(4,2))
plt.plot(findSet_sorted, cdf_find, label="Find")
plt.plot(pulsarSet_sorted, cdf_pulsar, label="Pulsar")
# plt.plot(pulsarNASet_sorted, cdf_pulsarNA, label="PulsarNA")
plt.xlabel("Time [slots]")
plt.ylabel("CDF")
plt.legend()
plt.grid()
plt.savefig("cdf_testbed_performance" +".pdf", format="pdf", bbox_inches="tight")
plt.close("all")