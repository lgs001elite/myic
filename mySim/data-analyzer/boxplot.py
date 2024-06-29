import numpy as np
import pandas as pd
# from sklearn import datasets
import matplotlib.pyplot as plt
# Load Iris dataset

import pandas as pd
import csv
import os


primeGau =[]
findGau = []

primeNorm = []
findNorm = []

primeGeo =[]
findGeo = []


dataSets = [primeGau, findGau, primeNorm, findNorm, primeGeo, findGeo]
count = 0
os.remove("temp5.csv")
#:ESSP Gau
df = pd.read_csv("varyingGaussianDiscovery.csv")
temp = df
temp.to_csv('temp.csv', index=False)
temp=pd.read_csv("temp.csv", usecols=['slots'])
temp.to_csv('temp.csv', index=False, header=False)

csv_file = open('temp.csv')
csv_reader = csv.reader(csv_file)

temp= pd.DataFrame([csv_reader], index=None)
count1 = 0
count2 = 0
for i, j in temp.iterrows():
    count1 = count1 + 1
    for var in range(16200):
        count2 = count2 + 1
        dataSets[count].append(int(j[var][0]))
    count = count + 1

# :Find Gau
df = pd.read_csv("varyingFindDiscovery-Gau.csv")
temp = df
temp.to_csv('temp1.csv', index=False)
temp = pd.read_csv("temp1.csv", usecols=['slots'])
temp.to_csv('temp1.csv', index=False, header=False)

csv_file = open('temp1.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(16200):
        dataSets[count].append(int(j[var][0]))
    count = count + 1

# :ESSP Norm
df = pd.read_csv("varyingNormalDiscovery.csv")
temp = df
temp.to_csv('temp2.csv', index=False)
temp = pd.read_csv("temp2.csv", usecols=['slots'])
temp.to_csv('temp2.csv', index=False, header=False)

csv_file = open('temp2.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(16200):
        dataSets[count].append(int(j[var][0]))
    count = count + 1

# :Find Norm
df = pd.read_csv("varyingFindDiscovery-Norm.csv")
temp = df
temp.to_csv('temp3.csv', index=False)
temp = pd.read_csv("temp3.csv", usecols=['slots'])
temp.to_csv('temp3.csv', index=False, header=False)

csv_file = open('temp3.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(16200):
        dataSets[count].append(int(j[var][0]))
    count = count + 1


# :ESSP Geo
df = pd.read_csv("varyingGeoDiscovery.csv")
temp = df
temp.to_csv('temp4.csv', index=False)
temp = pd.read_csv("temp4.csv", usecols=['slots'])
temp.to_csv('temp4.csv', index=False, header=False)

csv_file = open('temp4.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(16200):
        dataSets[count].append(int(j[var][0]))
    count = count + 1

# :Find Geo
df = pd.read_csv("varyingFindDiscovery-Geo.csv")
temp = df
temp.to_csv('temp5.csv', index=False)
temp = pd.read_csv("temp5.csv", usecols=['slots'])
temp.to_csv('temp5.csv', index=False, header=False)

csv_file = open('temp5.csv')
csv_reader = csv.reader(csv_file)

temp = pd.DataFrame([csv_reader], index=None)
for i, j in temp.iterrows():
    for var in range(16200):
        dataSets[count].append(int(j[var][0]))
    count = count + 1




fSize = 18
plt.rcParams['font.size'] = str(fSize)
plt.rcParams['font.family'] = 'Arial'
fig, ax = plt.subplots(1, 3, figsize=(12, 5),  layout="constrained")
colors = ['#73020C', '#426A8C']
colors1 = dict(color=colors[0])
colors2 = dict(color=colors[1])
bp0 = ax[0].boxplot(dataSets[0], positions=[1], boxprops=colors1, showfliers = False, autorange= True, showmeans=True)
bp = ax[0].boxplot(dataSets[1], positions=[2], boxprops=colors2, showfliers = False, autorange= True, showmeans=True)

for key in bp:
    print(f'{key}: {[item.get_ydata() for item in bp[key]]}\n')
for key in bp0:
    print(f'{key}: {[item.get_ydata() for item in bp0[key]]}\n')
print("***************************************************")
bp0 = ax[1].boxplot(dataSets[2], positions=[3], boxprops=colors1, showfliers = False, autorange= True, showmeans=True)
bp = ax[1].boxplot(dataSets[3], positions=[4], boxprops=colors2, showfliers = False, autorange= True, showmeans=True)

for key in bp:
    print(f'{key}: {[item.get_ydata() for item in bp[key]]}\n')
for key in bp0:
    print(f'{key}: {[item.get_ydata() for item in bp0[key]]}\n')
print("***************************************************")

bp0 = ax[2].boxplot(dataSets[4], positions=[5], boxprops=colors1, showfliers = False, autorange= True, showmeans=True)
bp = ax[2].boxplot(dataSets[5], positions=[6], boxprops=colors2, showfliers = False, autorange= True, showmeans=True)

for key in bp:
    print(f'{key}: {[item.get_ydata() for item in bp[key]]}\n')
for key in bp0:
    print(f'{key}: {[item.get_ydata() for item in bp0[key]]}\n')
print("***************************************************")


ax[0].set_xticklabels(['ESSP', 'Find'])
ax[1].set_xticklabels(['ESSP', 'Find'])
ax[2].set_xticklabels(['ESSP', 'Find'])
ax[0].set_title("Gau")
ax[1].set_title("Norm")
ax[2].set_title("Geo")

if (i == 0):
    ax[0].set_ylabel('Sync latency [slots]')
ax[0].yaxis.get_offset_text().set_fontsize(fSize)
ax[0].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax[1].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax[2].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.savefig("disCom.pdf", format="pdf", bbox_inches="tight")
plt.show()
os.remove("temp.csv")
os.remove("temp1.csv")
os.remove("temp2.csv")
os.remove("temp3.csv")
os.remove("temp4.csv")
os.remove("temp5.csv")





























# def get_summary_statistics(dataset):
    
#     mean = np.round(np.mean(dataset), 2)
#     median = np.round(np.median(dataset), 2)
#     min_value = np.round(dataset.min(), 2)
#     max_value = np.round(dataset.max(), 2)
#     quartile_1 = np.round(dataset.quantile(0.25), 2)
#     quartile_3 = np.round(dataset.quantile(0.75), 2)
#     # Interquartile range
#     iqr = np.round(quartile_3 - quartile_1, 2)
#     print('Min: %s' % min_value)
#     print('Mean: %s' % mean)
#     print('Max: %s' % max_value)
#     print('25th percentile: %s' % quartile_1)
#     print('Median: %s' % median)
#     print('75th percentile: %s' % quartile_3)
#     print('Interquartile range (IQR): %s' % iqr)
#     print('Setosa summary statistics')
# print('\n\nSetosa summary statistics')
# get_summary_statistics(setosa_petal_length)
# print('\n\nVersicolor summary statistics')
# get_summary_statistics(versicolor_petal_length)
# print('\n\nVirginica summary statistics')
# get_summary_statistics(virginica_petal_length)









# import numpy as np
# import pandas as pd
# from sklearn import datasets
# import matplotlib.pyplot as plt
# # Load Iris dataset
# iris = datasets.load_iris()
# # Preparing Iris dataset
# iris_data = pd.DataFrame(data=iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
# iris_target = pd.DataFrame(data=iris.target, columns=['species'])
# iris_df = pd.concat([iris_data, iris_target], axis=1)
# # Add species name
# iris_df['species_name'] = np.where(iris_df['species'] == 0, 'Setosa', None)
# iris_df['species_name'] = np.where(iris_df['species'] == 1, 'Versicolor', iris_df['species_name'])
# iris_df['species_name'] = np.where(iris_df['species'] == 2, 'Virginica', iris_df['species_name'])

# # Prepare petal length by species datasets
# setosa_petal_length = iris_df[iris_df['species_name'] == 'Setosa']['petal_length']
# versicolor_petal_length = iris_df[iris_df['species_name'] == 'Versicolor']['petal_length']
# virginica_petal_length = iris_df[iris_df['species_name'] == 'Virginica']['petal_length']

# # Visualize petal length distribution for all species
# # fig, ax = plt.subplots(figsize=(12, 7))
# # # Remove top and right border
# # ax.spines['top'].set_visible(False)
# # ax.spines['right'].set_visible(False)
# # ax.spines['left'].set_visible(False)
# # # Remove y-axis tick marks
# # ax.yaxis.set_ticks_position('none')
# # # Add major gridlines in the y-axis
# # ax.grid(color='grey', axis='y', linestyle='-', linewidth=0.25, alpha=0.5)
# # # Set plot title
# # ax.set_title('Distribution of petal length by species')
# # # Set species names as labels for the boxplot
# # dataset = [setosa_petal_length, versicolor_petal_length, virginica_petal_length]
# # labels = iris_df['species_name'].unique()
# # ax.boxplot(dataset, labels=labels)
# # plt.show()


# fig, ax = plt.subplots(figsize=(12, 7))
# # Remove top and right border
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# # Remove y-axis tick marks
# ax.yaxis.set_ticks_position('none')

# # Set plot title
# ax.set_title('Distribution of petal length by species')
# # Add major gridlines in the y-axis
# ax.grid(color='grey', axis='y', linestyle='-', linewidth=0.25, alpha=0.5)
# # Set species names as labels for the boxplot
# dataset = [setosa_petal_length, versicolor_petal_length, virginica_petal_length]
# labels = iris_df['species_name'].unique()

# # Set the colors for each distribution
# colors = ['#73020C', '#426A8C', '#D94D1A']
# colors_setosa = dict(color=colors[0])
# colors_versicolor = dict(color=colors[1])
# colors_virginica = dict(color=colors[2])
# # We want to apply different properties to each species, so we're going to plot one boxplot
# # for each species and set their properties individually
# # positions: position of the boxplot in the plot area
# # medianprops: dictionary of properties applied to median line
# # whiskerprops: dictionary of properties applied to the whiskers
# # capprops: dictionary of properties applied to the caps on the whiskers
# # flierprops: dictionary of properties applied to outliers
# ax.boxplot(dataset[0], positions=[1], labels=[labels[0]], boxprops=colors_setosa, medianprops=colors_setosa, whiskerprops=colors_setosa, capprops=colors_setosa, flierprops=dict(markeredgecolor=colors[0]))
# ax.boxplot(dataset[1], positions=[2], labels=[labels[1]], boxprops=colors_versicolor, medianprops=colors_versicolor, whiskerprops=colors_versicolor, capprops=colors_versicolor, flierprops=dict(markeredgecolor=colors[1]))
# ax.boxplot(dataset[2], positions=[3], labels=[labels[2]], boxprops=colors_virginica, medianprops=colors_virginica, whiskerprops=colors_virginica, capprops=colors_virginica, flierprops=dict(markeredgecolor=colors[2]))
# plt.show()






# def get_summary_statistics(dataset):
    
#     mean = np.round(np.mean(dataset), 2)
#     median = np.round(np.median(dataset), 2)
#     min_value = np.round(dataset.min(), 2)
#     max_value = np.round(dataset.max(), 2)
#     quartile_1 = np.round(dataset.quantile(0.25), 2)
#     quartile_3 = np.round(dataset.quantile(0.75), 2)
#     # Interquartile range
#     iqr = np.round(quartile_3 - quartile_1, 2)
#     print('Min: %s' % min_value)
#     print('Mean: %s' % mean)
#     print('Max: %s' % max_value)
#     print('25th percentile: %s' % quartile_1)
#     print('Median: %s' % median)
#     print('75th percentile: %s' % quartile_3)
#     print('Interquartile range (IQR): %s' % iqr)
#     print('Setosa summary statistics')
# print('\n\nSetosa summary statistics')
# get_summary_statistics(setosa_petal_length)
# print('\n\nVersicolor summary statistics')
# get_summary_statistics(versicolor_petal_length)
# print('\n\nVirginica summary statistics')
# get_summary_statistics(virginica_petal_length)



