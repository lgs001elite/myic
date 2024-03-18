import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

car01 = pd.read_csv('cars_0th.csv')
car02 = pd.read_csv('cars_1th.csv')

jogging01 = pd.read_csv('jogging_0th.csv')
jogging02 = pd.read_csv('jogging_1th.csv')

office01 = pd.read_csv('office_0th.csv')
office02 = pd.read_csv('office_1th.csv')

stairs01 = pd.read_csv('stairs_0th.csv')
stairs02 = pd.read_csv('stairs_1th.csv')

washer01 = pd.read_csv('washer_0th.csv')
washer02 = pd.read_csv('washer_1th.csv')

print("Cars")
car01_mean = car01.mean()
car01_median = car01.median()
car01_min_value = car01.min()
car01_max_value = car01.max()
car02_mean = car02.mean()
car02_median = car02.median()
car02_min_value = car02.min()
car02_max_value = car02.max()
print(car01_mean)
print(car01_median)
print(car01_min_value)
print(car01_max_value)
print(car02_mean)
print(car02_median)
print(car02_min_value)
print(car02_max_value)

print("Jogging")
jogging01_mean = jogging01.mean()
jogging01_median = jogging01.median()
jogging01_min_value = jogging01.min()
jogging01_max_value = jogging01.max()
jogging02_mean = jogging02.mean()
jogging02_median = jogging02.median()
jogging02_min_value = jogging02.min()
jogging02_max_value = jogging02.max()
print(jogging01_mean)
print(jogging01_median)
print(jogging01_min_value)
print(jogging01_max_value)
print(jogging02_mean)
print(jogging02_median)
print(jogging02_min_value)
print(jogging02_max_value)




print("office")
office01_mean = office01.mean()
office01_median = office01.median()
office01_min_value = office01.min()
office01_max_value = office01.max()
office02_mean = office02.mean()
office02_median = office02.median()
office02_min_value = office02.min()
office02_max_value = office02.max()
print(office01_mean)
print(office01_median)
print(office01_min_value)
print(office01_max_value)
print(office02_mean)
print(office02_median)
print(office02_min_value)
print(office02_max_value)



print("stairs")
stairs01_mean = stairs01.mean()
stairs01_median = stairs01.median()
stairs01_min_value = stairs01.min()
stairs01_max_value = stairs01.max()
stairs02_mean = stairs02.mean()
stairs02_median = stairs02.median()
stairs02_min_value = stairs02.min()
stairs02_max_value = stairs02.max()
print(stairs01_mean)
print(stairs01_median)
print(stairs01_min_value)
print(stairs01_max_value)
print(stairs02_mean)
print(stairs02_median)
print(stairs02_min_value)
print(stairs02_max_value)

print("washer")
washer01_mean = washer01.mean()
washer01_median = washer01.median()
washer01_min_value = washer01.min()
washer01_max_value = washer01.max()
washer02_mean = washer02.mean()
washer02_median = washer02.median()
washer02_min_value = washer02.min()
washer02_max_value = washer02.max()
print(washer01_mean)
print(washer01_median)
print(washer01_min_value)
print(washer01_max_value)
print(washer02_mean)
print(washer02_median)
print(washer02_min_value)
print(washer02_max_value)

width = 0.5
fig, ax = plt.subplots(1, 5, figsize=(12, 4))
ax[0].plot(car01)
ax[0].plot(car02)

ax[1].plot(jogging01)
ax[1].plot(jogging02)

ax[2].plot(office01)
ax[2].plot(office02)

ax[3].plot(stairs01)
ax[3].plot(stairs02)

ax[4].plot(washer01, label="Node1")
ax[4].plot(washer02, label="Node2")

fig.suptitle("Real traces distribution")
ax[0].set_title("Cars")
ax[1].set_title("Jogging")
ax[2].set_title("Office")
ax[3].set_title("Stairs")
ax[4].set_title("Washer")

ax[0].set_ylabel('[Slots]')

plt.legend()
plt.savefig("real_traces" + ".pdf", format="pdf", bbox_inches="tight")
plt.show()

