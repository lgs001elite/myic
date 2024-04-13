import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes 
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


plt.rcParams['font.size'] = str(23)
plt.rcParams['font.family'] = 'Arial'

Threshold = 1000

car1 = pd.read_csv('cars_0th.csv')
sum = 0
car01 = []
index = 0
while True:
    sum = sum + car1.iat[index,0]
    car01.append(car1.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break

car2 = pd.read_csv('cars_1th.csv')
sum = 0
car02 = []
index = 0
while True:
    sum = sum + car2.iat[index,0]
    car02.append(car2.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break



jogging1 = pd.read_csv('jogging_0th.csv')
sum = 0
jogging01 = []
index = 0
while True:
    sum = sum + jogging1.iat[index,0]
    jogging01.append(jogging1.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break



jogging2 = pd.read_csv('jogging_1th.csv')
sum = 0
jogging02 = []
index = 0
while True:
    sum = sum + jogging2.iat[index,0]
    jogging02.append(jogging2.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break


office1 = pd.read_csv('office_1th.csv')
sum = 0
office01 = []
index = 0
while True:
    sum = sum + office1.iat[index,0]
    office01.append(office1.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break



office2 = pd.read_csv('office_2th.csv')
sum = 0
office02 = []
index  = 0
while True:
    sum = sum + office2.iat[index,0]
    office02.append(office2.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break




stairs1 = pd.read_csv('stairs_0th.csv')
sum = 0
stairs01 = []
index = 0
while True:
    sum = sum + stairs1.iat[index,0]
    stairs01.append(stairs1.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break




stairs2 = pd.read_csv('stairs_1th.csv')
sum = 0
stairs02 = []
index = 0
while True:
    sum = sum + stairs2.iat[index,0]
    stairs02.append(stairs2.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break



washer1 = pd.read_csv('washer_0th.csv')
sum = 0
washer01 = []
index = 0
while(True):
    sum = sum + washer1.iat[index,0]
    washer01.append(washer1.iat[index,0])
    index = index + 1
    if (index > Threshold):
        break


washer2 = pd.read_csv('washer_1th.csv')
sum = 0
washer02 = []
index = 0
while(True):
    sum = sum + washer2.iat[index,0]
    washer02.append(washer2.iat[index,0])
    index = index+ 1
    if index > Threshold:
        break


print("Cars")
car01_mean = np.mean(car01)
car01_median = np.median(car01)
car01_min_value = np.min(car01)
car01_max_value = np.max(car01)
# car02_mean = np.mean(car02)
# car02_median = np.median(car02)
# car02_min_value = np.min(car02)
# car02_max_value = np.max(car02)
print("mean:" + str(car01_mean))
print("median:" + str(car01_median))
print("min:" + str(car01_min_value))
print("max:" + str(car01_max_value))
# print("mean:" + str(car02_mean))
# print("median:" + str(car02_median))
# print("min:" + str(car02_min_value))
# print("max:" + str(car02_max_value))

print("Jogging")
jogging01_mean = np.mean(jogging01)
jogging01_median = np.median(jogging01)
jogging01_min_value = np.min(jogging01)
jogging01_max_value = np.max(jogging01)
# jogging02_mean = np.mean(jogging02)
# jogging02_median = np.median(jogging02)
# jogging02_min_value = np.min(jogging02)
# jogging02_max_value = np.max(jogging02)
print("mean:" + str(jogging01_mean))
print("median:" + str(jogging01_median))
print("min:" + str(jogging01_min_value))
print("max:" + str(jogging01_max_value))
# print("mean:" + str(jogging02_mean))
# print("median:" + str(jogging02_median))
# print("min:" + str(jogging02_min_value))
# print("max:" + str(jogging02_max_value))


print("office")
office01_mean = np.mean(office01)
office01_median = np.median(office01)
office01_min_value = np.min(office01)
office01_max_value = np.max(office01)
# office02_mean = np.mean(office02)
# office02_median = np.median(office02)
# office02_min_value = np.min(office02)
# office02_max_value = np.max(office02)
print("mean:" + str(office01_mean))
print("median:" + str(office01_median))
print("min:" + str(office01_min_value))
print("max:" + str(office01_max_value))
# print("mean:" + str(office02_mean))
# print("median:" + str(office02_median))
# print("min:" + str(office02_min_value))
# print("max:" + str(office02_max_value))



print("stairs")
stairs01_mean = np.mean(stairs01)
stairs01_median = np.median(stairs01)
stairs01_min_value = np.min(stairs01)
stairs01_max_value = np.max(stairs01)
# stairs02_mean = np.mean(stairs02)
# stairs02_median = np.median(stairs02)
# stairs02_min_value = np.min(stairs02)
# stairs02_max_value = np.max(stairs02)
print("mean:" + str(stairs01_mean))
print("median:" + str(stairs01_median))
print("min:" + str(stairs01_min_value))
print("max:" + str(stairs01_max_value))
# print("mean:" + str(stairs02_mean))
# print("median:" + str(stairs02_median))
# print("min:" + str(stairs02_min_value))
# print("max:" + str(stairs02_max_value))

print("washer")
washer01_mean = np.mean(washer01)
washer01_median = np.median(washer01)
washer01_min_value = np.min(washer01)
washer01_max_value = np.max(washer01)
# washer02_mean = np.mean(washer02)
# washer02_median = np.median(washer02)
# washer02_min_value = np.min(washer02)
# washer02_max_value = np.max(washer02)
print("mean:" + str(washer01_mean))
print("median:" + str(washer01_median))
print("min:" + str(washer01_min_value))
print("max:" + str(washer01_max_value))
# print("mean:" + str(washer02_mean))
# print("median:" + str(washer02_median))
# print("min:" + str(washer02_min_value))
# print("max:" + str(washer02_max_value))



fig, ax = plt.subplots(5, 1, figsize=(15, 12), layout="constrained")
ax[0].plot(car01, label="Node1")
# ax[0].plot(car02, label="Node2")
x1, x2, y1, y2 = 200, 300, 500, 2500  # subregion of the original image
axins = ax[0].inset_axes([0.5, 0.5, 0.47, 0.47],xlim=(x1, x2), ylim=(y1, y2))
axins.plot(car01)
#axins.plot(car02)
ax[0].indicate_inset_zoom(axins, edgecolor="black", alpha=1) # alpha: transpancy
ax[0].set_xticks([])



ax[1].plot(jogging01)
# ax[1].plot(jogging02)
x1, x2, y1, y2 = 200, 300, 200, 1500  # subregion of the original image
axins = ax[1].inset_axes([0.5, 0.5, 0.47, 0.47],xlim=(x1, x2), ylim=(y1, y2))
axins.plot(jogging01)
#axins.plot(jogging02)
ax[1].indicate_inset_zoom(axins, edgecolor="black", alpha=1)
ax[1].set_xticks([])


ax[2].plot(office01)
ax[2].set_xticks([])
# ax[2].plot(office02)
# x1, x2, y1, y2 = 0, 10, 0, 350  # subregion of the original image
# axins = ax[2].inset_axes([0.5, 0.5, 0.1, 0.5],xlim=(x1, x2), ylim=(y1, y2))
# axins.plot(jogging01)
# axins.plot(jogging02)
# ax[2].indicate_inset_zoom(axins)


ax[3].plot(stairs01)
# ax[3].plot(stairs02)
x1, x2, y1, y2 = 700, 800, 46, 48  # subregion of the original image
axins = ax[3].inset_axes([0.8, 0.5, 0.1, 0.47],xlim=(x1, x2), ylim=(y1, y2))
axins.plot(stairs01)
#axins.plot(stairs02)
ax[3].indicate_inset_zoom(axins, edgecolor="black", alpha=1)
ax[3].set_xticks([])
# x1, x2, y1, y2 = 500, 520, 47, 49  # subregion of the original image
# axins = ax[3].inset_axes([0.1, 0.2, 0.1, 0.47],xlim=(x1, x2), ylim=(y1, y2))
# axins.plot(stairs01)
# axins.plot(stairs02)
# ax[3].indicate_inset_zoom(axins, edgecolor="black")


ax[4].plot(washer01)
# ax[4].plot(washer02)
x1, x2, y1, y2 = 700, 800, 45, 50  # subregion of the original image
axins = ax[4].inset_axes([0.8, 0.5, 0.1, 0.47],xlim=(x1, x2), ylim=(y1, y2))
axins.plot(stairs01)
#axins.plot(stairs02)
ax[4].indicate_inset_zoom(axins, edgecolor="black", alpha=1)

#fig.suptitle("Real traces distribution")
ax[0].set_title("Cars")
ax[1].set_title("Jogging")
ax[2].set_title("Office")
ax[3].set_title("Stairs")
ax[4].set_title("Washer")



# ax[0].set_ylabel('[Slots]')
# ax[1].set_ylabel('[Slots]')
ax[2].set_ylabel('[Slots]')
# ax[3].set_ylabel('[Slots]')
# ax[4].set_ylabel('[Slots]')
ax[4].set_xlabel('Seq', loc="center")

ax[0].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax[1].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax[2].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax[3].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
#ax[3].set_yticks(np.arange(0, 150, 50))
ax[4].ticklabel_format(axis="y", style="sci", scilimits=(0,0))

ax[0].ticklabel_format(axis="x", style="sci", scilimits=(0,0))
ax[1].ticklabel_format(axis="x", style="sci", scilimits=(0,0))
ax[2].ticklabel_format(axis="x", style="sci", scilimits=(0,0))
ax[3].ticklabel_format(axis="x", style="sci", scilimits=(0,0))
ax[4].ticklabel_format(axis="x", style="sci", scilimits=(0,0))

#ax[0].legend(loc="upper left")
#plt.show()
plt.savefig("real_traces" + ".pdf", format="pdf", bbox_inches="tight")
#plt.show()
plt.close("all")
