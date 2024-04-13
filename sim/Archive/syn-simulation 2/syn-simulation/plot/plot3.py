

import matplotlib.pyplot as plt

plt.rcParams['font.size'] = str(10)
plt.rcParams['font.family'] = 'Arial'

names = ["Find", "Greedy", "NoAlign"]
bar_colors = ['tab:red', 'tab:blue', 'tab:orange']
Gauss_n = [41, 34, 4]
Uniform_n = [12, 7, 15]
Expo_n = [38, 21, 45]
Stairs_n = [16, 15, 16]
Static_n = [5, 9, 2]

ave_find = (41 + 12 + 38 + 16 + 5) / 5
ave_greedy = (34 + 7 + 21 + 15 + 9) / 5
ave_NoAlign = (4 + 15 + 45 + 16 + 2) / 5

print(ave_find)
print(ave_greedy)
print(ave_NoAlign)

# 22.4
# 17.2
# 16.4

fig, axs = plt.subplots(1, 5, figsize=(15, 3), sharey=True)
axs[0].bar(names, Gauss_n, color=bar_colors)
axs[0].set_title("Gauss")
axs[0].set_ylabel("[Extra syn number]")
#axs[0].set_xlabel("Syn models")
axs[1].bar(names, Uniform_n, color=bar_colors)
axs[1].set_title("Uniform")
#axs[1].set_xlabel("Syn models")
axs[2].bar(names, Expo_n, color=bar_colors)
axs[2].set_title("Expo")
#axs[2].set_xlabel("Syn models")
axs[3].bar(names, Stairs_n, color=bar_colors)
axs[3].set_title("Stairs")
#axs[3].set_xlabel("Syn models")
axs[4].bar(names, Static_n, color=bar_colors)
#axs[4].set_xlabel("Syn models")
axs[4].set_title("Static")
# fig.supxlabel('[Syn numbers within 2000 slots]')

plt.savefig("numbers_syn" + ".pdf", format="pdf", bbox_inches="tight")


#Guass_r = [8, 15, 49]
#Gauss_s = [11.22, 14.75, 56]
#Gauss_n = [41, 34, 4]

#Uniform_r = [3, 8, 15]
#Uniform_s = [6.26, 7.57, 26.38]
#Uniform_n = [12, 7, 15]


#Expo_r = [11, 28, 49]
#Expo_s = [15.4, 20.29, 59.8]
# Expo_n = [38, 21, 45]

#Stairs_r = [3, 4, 11]
#Stairs_s = [0.43, 0.35, 10.2]
# Stairs_n = [16, 15, 16]

#Static_r = [5, 1, 10]
#Static_s = [2.65, 3.02, 10.73]
# Static_n = [5, 9, 2]