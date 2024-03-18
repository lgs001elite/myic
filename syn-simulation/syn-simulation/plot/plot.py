import matplotlib.pyplot as plt
import numpy as np

gauss_t = np.array([8, 15, 9, 49, 45])
gauss_s = np.array([11.22, 14.75, 5.22, 76.3, 0])

uniform_t = np.array([3, 8, 4, 15, 0])
uniform_s = np.array([6.26, 7.57, 5.77, 46.3, 0])

expo_t = np.array([11, 28, 15, 49, 4])
expo_s = np.array([15.4, 20.29, 9.51, 75.89, 0])

stairs_t = np.array([3, 4, 4, 11, 7, 19, 3])
stairs_s = np.array([0.43, 0.35, 1.89, 10.2, 0, 11.75, 0])

static_t = np.array([5, 1, 1, 10, 8])
static_s = np.array([2.65, 3.02, 3.08, 17.7, 0])

syn_methods = ("Find", "Greedy", "Cycle", "Ours", "Non_align", "S1", "S2")

width = 0.5
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

ax[0].bar(syn_methods, stairs_t, width, color="tab:blue")
ax[0].plot(syn_methods, stairs_t, color="c")
ax[1].bar(syn_methods, stairs_s, width, color="tab:orange")
ax[1].plot(syn_methods, stairs_s, color="m")

fig.suptitle("Real-charging")
ax[0].set_title("Testbed")
ax[0].set_xlabel('Syn methods')
ax[0].set_ylabel('Syn success counter')
ax[1].set_title("Simulation")
ax[1].set_xlabel('Syn methods')
#ax[1].set_ylabel('Syn success counter')
plt.savefig("real_syn" +  ".pdf", format="pdf", bbox_inches="tight")
plt.show()


