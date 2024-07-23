import pandas as pd
import numpy as np
import config
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

config.configure(mpl, plt)
TRACE_TYPE = ["Cars", "Jogging", "Office", "Stairs"]
TRACE_FILE = {
    "Cars": "cars_0th.csv", 
    "Jogging": "jogging_0th.csv",
    "Office": "office_1th.csv",
    "Stairs": "stairs_0th.csv"
}
    

def read_data(data_dir, filename):
    THRESHOLD = 1000
    data = pd.read_csv(data_dir + filename)
    data_list = []
    index = 0
    while(True):
        data_list.append(data.iat[index,0])
        index = index + 1
        if (index > THRESHOLD):
            break
    return data_list

class CustomScaleFormatter(ScalarFormatter):
        def _set_format(self):
            self.format = "%1.1f"

def plot_data(data_dir):
    # fig, ax = plt.subplots(2, 2, figsize=(10, 3), layout="constrained")
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=config.set_size(config.width, height_div=3.5, fraction=0.5))

    color = "black"
    linewidth = 1.0
    linestyle = "-"

    # Plot car
    car_data = read_data(data_dir, TRACE_FILE["Cars"])
    # car_data = car_data[300:799]
    _ax = ax[0][0]
    _ax.plot(car_data, color=color, linewidth=linewidth, linestyle=linestyle)
    x1, x2, y1, y2 = 200, 300, 300, 2500  # subregion of the original image
    axins = _ax.inset_axes([0.05, 0.5, 0.48, 0.45],xlim=(x1, x2), ylim=(y1, y2))
    axins.set_xticks([])
    axins.set_yticks([])
    axins.plot(car_data, color=color, linewidth=linewidth, linestyle=linestyle)
    _ax.indicate_inset_zoom(axins, edgecolor="tab:red", alpha=0.3, linestyle="-") # alpha: transpancy
    _ax.set_xticks([])

    # Plot jogging
    jogging_data = read_data(data_dir, TRACE_FILE["Jogging"])
    # jogging_data = jogging_data[300:799]
    _ax = ax[0][1]
    _ax.plot(jogging_data, color=color, linewidth=linewidth, linestyle=linestyle)
    x1, x2, y1, y2 = 200, 300, 50, 1500  # subregion of the original image
    axins = _ax.inset_axes([0.05, 0.5, 0.48, 0.45],xlim=(x1, x2), ylim=(y1, y2))
    axins.set_xticks([])
    axins.set_yticks([])
    axins.plot(jogging_data,color=color, linewidth=linewidth, linestyle=linestyle)
    _ax.indicate_inset_zoom(axins, edgecolor="tab:red", alpha=0.3, linestyle="-")
    _ax.set_xticks([])

    # Plot office
    office_data = read_data(data_dir, TRACE_FILE["Office"])
    # office_data = office_data[0:499]
    _ax = ax[1][0]
    _ax.plot(office_data, color=color, linewidth=linewidth, linestyle=linestyle)
    # _ax.set_xticks([])
    x1, x2, y1, y2 = 200, 300, 89, 95  # subregion of the original image
    axins = _ax.inset_axes([0.07, 0.5, 0.48, 0.45],xlim=(x1, x2), ylim=(y1, y2))
    axins.set_xticks([])
    axins.set_yticks([])
    axins.plot(jogging_data, color=color, linewidth=linewidth, linestyle=linestyle)
    axins.plot(office_data, color=color, linewidth=linewidth, linestyle=linestyle)
    _ax.indicate_inset_zoom(axins, edgecolor="tab:red", alpha=0.3, linestyle="-")

    # Plot stairs
    stairs_data = read_data(data_dir, TRACE_FILE["Stairs"])
    # stairs_data = stairs_data[300:799]
    _ax = ax[1][1]
    _ax.plot(stairs_data, color=color, linewidth=linewidth, linestyle=linestyle)
    x1, x2, y1, y2 = 650, 820, 46.5, 48.5  # subregion of the original image
    axins = _ax.inset_axes([0.5, 0.5, 0.47, 0.45],xlim=(x1, x2), ylim=(y1, y2))
    axins.set_xticks([])
    axins.set_yticks([])
    axins.plot(stairs_data, color=color, linewidth=linewidth, linestyle=linestyle)
    _ax.indicate_inset_zoom(axins, edgecolor="tab:red", alpha=0.3, linestyle="-")
    # _ax.set_xticks([])
    # _ax.set_xticks([])
    

    for i, trace in enumerate(TRACE_TYPE):
        row, col = int(i/2), i%2
        _ax = ax[row][col]
        _ax.set_title(trace, fontsize=12, pad=4)
        _ax.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
        y_formatter = CustomScaleFormatter()
        y_formatter.set_powerlimits((0, 0))
        _ax.yaxis.set_major_formatter(y_formatter)
        _ax.tick_params(axis='both', which='major', labelsize=12)
        _ax.yaxis.offsetText.set_fontsize(12)

    ax[1][0].set_xlabel('Charging Cycle Sequence', fontsize=12)
    ax[1][1].set_xlabel('Charging Cycle Sequence', fontsize=12)

    fig.text(0.0, 0.50, 'Charging Time (ms)', fontsize=12,
             va='center', ha="center", rotation='vertical')
    fig.tight_layout(pad=0.5)
    plt.subplots_adjust(hspace=0.3, wspace=0.110)
    plt.show()
    fig.savefig(f"../figures/real_trace.pdf", format="pdf", dpi=config.dpi, bbox_inches='tight')


if __name__ == "__main__":
    data_dir = "./data/real_trace/"
    plot_data(data_dir)

    
    










