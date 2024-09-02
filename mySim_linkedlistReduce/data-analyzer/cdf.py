from itertools import count
from operator import index
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from math import nan, isnan
import seaborn as sns
import os


swift_DataSets = []
find_DataSets  = []

swift_norm = []
find_norm = []

swift_Gau = []
find_Gau = []


swift_Geo = []
find_Geo = []


dataSets = [
            swift_norm, find_norm,
            swift_Gau, find_Gau,
            swift_Geo, find_Geo
            ]

count = 0
os.remove("temp7.csv")
# :ESSP 15
df = pd.read_csv("varyingNormalDiscovery.csv")
temp = df
temp.to_csv('temp2.csv', index=False)
temp = pd.read_csv("temp2.csv", usecols=['slots'])
temp.to_csv('temp2.csv', index=False, header=False)

csv_file = open('temp2.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(3000):
        dataSets[count].append(int(j[var][0]))
    break
count = count + 1

# :find 15
df = pd.read_csv("varyingFindDiscovery-Norm.csv")
temp = df
temp.to_csv('temp3.csv', index=False)
temp = pd.read_csv("temp3.csv", usecols=['slots'])
temp.to_csv('temp3.csv', index=False, header=False)

csv_file = open('temp3.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(3000):
        dataSets[count].append(int(j[var][0]))
    break
count = count + 1


# :ESSP 120
df = pd.read_csv("varyingGaussianDiscovery.csv")
temp = df
temp.to_csv('temp4.csv', index=False)
temp = pd.read_csv("temp4.csv", usecols=['slots'])
temp.to_csv('temp4.csv', index=False, header=False)

csv_file = open('temp4.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(78000):
        dataSets[count].append(int(j[var][0]))
    break
count = count + 1

# :find 120
df = pd.read_csv("varyingFindDiscovery-Gau.csv")
temp = df
temp.to_csv('temp5.csv', index=False)
temp = pd.read_csv("temp5.csv", usecols=['slots'])
temp.to_csv('temp5.csv', index=False, header=False)

csv_file = open('temp5.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(78000):
        dataSets[count].append(int(j[var][0]))
    break
count = count + 1


# :ESSP 498
df = pd.read_csv("varyingGeoDiscovery.csv")
temp = df
temp.to_csv('temp6.csv', index=False)
temp = pd.read_csv("temp6.csv", usecols=['slots'])
temp.to_csv('temp6.csv', index=False, header=False)

csv_file = open('temp6.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(15000):
        dataSets[count].append(int(j[var][0]))
    break
count = count + 1

# :find 498
df = pd.read_csv("varyingFindDiscovery-Geo.csv")
temp = df
temp.to_csv('temp7.csv', index=False)
temp = pd.read_csv("temp7.csv", usecols=['slots'])
temp.to_csv('temp7.csv', index=False, header=False)

csv_file = open('temp7.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(15000):
        dataSets[count].append(int(j[var][0]))
    break
count = count + 1

fSize = 20
mSize = fSize
fig, ax = plt.subplots(1, 3, figsize=(15, 5),  layout="constrained")
plt.rcParams['font.size'] = str(fSize)
plt.rcParams['font.family'] = 'Arial'
markerSet = ["X", "v"]
lineSet = ["-", "--"]
dataLen = len(dataSets)/3
m = 0
tCharTime = ["Norm", "Gau", "Geo"]
tCount = 0
dataSetsName = ["Swift", "Find"]
nCount = 0
rowSeq = 0
for i in range(int(dataLen)):
    if (i == 1):
        rowSeq = rowSeq + 1
    size1 = len(dataSets[i])
    size2 = len(dataSets[i + 2])
    size3 = len(dataSets[i + 4])
    sizeSet1, y1 = np.histogram(dataSets[i], bins=size1)
    pdf1 = sizeSet1/sum(sizeSet1)
    cdf1 = np.cumsum(pdf1)
    sizeSet2, y2 = np.histogram(dataSets[i + 2], bins=size2)
    pdf2 = sizeSet2/sum(sizeSet2)
    cdf2 = np.cumsum(pdf2)
    sizeSet3, y3 = np.histogram(dataSets[i + 4], bins=size3)
    pdf3 = sizeSet3/sum(sizeSet3)
    cdf3 = np.cumsum(pdf3)
    extraMarker1 = 0
    if ((size1 % 3) != 0):
        extraMarker1 = 1
    extraMarker2 = 0
    if ((size2 % 3) != 0):
        extraMarker2 = 1
    extraMarker3 = 0
    if ((size3 % 3) != 0):
        extraMarker3 = 1
    size1 = int(size1 / 3) + extraMarker1
    size2 = int(size2 / 3) + extraMarker2
    size3 = int(size3 / 3) + extraMarker3
    ax[0].plot(np.sort(y1[1:]), cdf1, marker=markerSet[m],
               ls=lineSet[m], markevery=size1, linewidth=2, markersize=mSize)
    ax[1].plot(np.sort(y2[1:]), cdf2, marker=markerSet[m],
               ls=lineSet[m], markevery=size2, linewidth=2, markersize=mSize)
    ax[2].plot(np.sort(y3[1:]), cdf3, marker=markerSet[m],
               ls=lineSet[m], markevery=size3, linewidth=2, markersize=mSize)
    nCount = nCount + 1
    m = m + 1
    if (m == 2):
        m = 0
        nCount = 0
        if (tCount == 1):
            ax[0].set_xlabel("Latency [slots]", fontsize=fSize, loc='left')
            ax[1].set_xlabel("Latency [slots]", fontsize=fSize, loc='left')
            ax[2].set_xlabel("Latency [slots]", fontsize=fSize, loc='left')
        ax[0].yaxis.set_tick_params(labelsize=fSize)
        ax[0].xaxis.set_tick_params(labelsize=fSize)
        ax[0].set_ylim(ymin=0)
        ax[0].set_ylabel("CDF", fontsize=fSize)
        ax[0].ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        ax[0].set_title(tCharTime[0], fontsize=fSize)
        ax[0].xaxis.get_offset_text().set_fontsize(fSize)

        ax[1].yaxis.set_tick_params(labelsize=fSize)
        ax[1].xaxis.set_tick_params(labelsize=fSize)
        ax[1].set_ylim(ymin=0)
        ax[1].ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        ax[1].set_title(tCharTime[1] + " slots", fontsize=fSize)
        ax[1].xaxis.get_offset_text().set_fontsize(fSize)

        ax[2].yaxis.set_tick_params(labelsize=fSize)
        ax[2].xaxis.set_tick_params(labelsize=fSize)
        ax[2].set_ylim(ymin=0)
        ax[2].ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        ax[2].set_title(tCharTime[2] + " slots", fontsize=fSize)
        ax[2].xaxis.get_offset_text().set_fontsize(fSize)

        if (rowSeq == 1):
            handles, tlabels = plt.gca().get_legend_handles_labels()
            order = [0, 1]
            ax[2].legend([handles[idx] for idx in order], [tlabels[idx]
                         for idx in order], fontsize=mSize)
        tCount = tCount + 1
plt.savefig("cdf_Dis.pdf", format="pdf", bbox_inches="tight")
plt.show()
os.remove("temp2.csv")
os.remove("temp3.csv")
os.remove("temp4.csv")
os.remove("temp5.csv")
os.remove("temp6.csv")
