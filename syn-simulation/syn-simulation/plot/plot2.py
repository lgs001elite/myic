import matplotlib.pyplot as plt
import numpy as np

gauss_ave = np.array([162.14, 127.5, 22.88, 26.1, 42.47])

uniform_ave = np.array([270.43, 229.31, 37.44, 42.9, 73.5])

expo_ave = np.array([122.69, 94.32, 23.03, 26.2, 33.08])

stairs_ave = np.array([829.88, 842.34, 72.65, 112.49,  83.01])

static_ave = np.array([501.6, 553.96, 90.37, 112.33, 179.73])


syn_methods = ("Find", "Greedy", "Cycle", "Ours", "S-cycle")

width = 0.8
fig, ax = plt.subplots()

# Gauss
#plt.step(syn_methods, gauss_ave, label='Gauss')
plt.plot(syn_methods, gauss_ave, 'o--',  label='Gauss')

# Expo
#plt.step(syn_methods, expo_ave, label='Expo')
plt.plot(syn_methods, expo_ave, 'v--',  label='Expo')

# Uniform
#plt.step(syn_methods, uniform_ave, label='Uniform')
plt.plot(syn_methods, uniform_ave, 's--',  label='Uniform')

#Real
#plt.step(syn_methods, stairs_ave, label='Stairs')
plt.plot(syn_methods, stairs_ave, '+--',  label='Stairs')

# Static
#plt.step(syn_methods, static_ave, label='Static')
plt.plot(syn_methods, static_ave, 'x--',  label='Static')

ax.set_title("Syn-average")
ax.legend(title='Energy conditions:')
ax.set_xlabel('Syn methods')
ax.set_ylabel('Average syn time [slots]')
plt.savefig("ave_syn" + ".pdf", format="pdf", bbox_inches="tight")
plt.show()







