import pandas as pd

df = pd.read_csv('charging_traces/cars_0th.csv')
mean = df.mean()
mean = mean[0]
min_value = df.min()
max_value = df.max()
stddev = df.std()
# print("Mean:\n", int(mean[0]))  # 47  47
print("Minimum:\n", int(min_value[0]))  # 32 32
print("Maximum:\n", int(max_value[0]))  # 138 893
# print("Standard Deviation:\n", int(stddev[0]))  # 11 13

print("lamda:\n", 1 / mean)  #  0.000224 (281, 62734)  0.000333 (171, 87054)

# Scale 100
# 47 32 138
