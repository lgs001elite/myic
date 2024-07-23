import argparse
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import config

config.configure(mpl, plt)
SIMULATION_COUNT = 100
DEVICES_COUNT = list(range(10, 101, 10))

def read_data(data_dir, device_type, charging_type, num_of_devices):
    last_timeslots_filename = f"{data_dir}/{device_type}_{num_of_devices}_{charging_type}_{SIMULATION_COUNT}_last_timeslots.npy"
    collision_count_filename = f"{data_dir}/{device_type}_{num_of_devices}_{charging_type}_{SIMULATION_COUNT}_collision_counts.npy"

    print(f"DeviceType: {device_type}, ChargingType: {charging_type}, NumOfDevices: {num_of_devices}")

    if os.path.exists(collision_count_filename) is True:
        print(f"MedianCollisionCount: {np.median(np.load(collision_count_filename))}")
    if os.path.exists(last_timeslots_filename) is False:
        return None
    last_timeslots = np.load(last_timeslots_filename, allow_pickle=True)
    print(f"MedianLastTimeSlots: {np.median(last_timeslots)}")

    return last_timeslots

def linear_scaling(data_dir):
    last_timeslots_2_devices = read_data(data_dir, "CoordinatorAsReference", "random", 2)
    assert len(last_timeslots_2_devices) == SIMULATION_COUNT
    median_last_timeslots_2_devices = np.median(last_timeslots_2_devices)

    scaling_lst = []
    for device in DEVICES_COUNT:
        scaling = (device / 2) * median_last_timeslots_2_devices
        scaling_lst.append(scaling)

    return scaling_lst

def plot_data(data_dir):
    fig, ax = plt.subplots(figsize=config.set_size(config.width, height_div=4, fraction=0.5))

    # read data for each devices
    last_timeslots_dict = {}
    median_last_timeslots_lst = []
    for device in DEVICES_COUNT:
        last_timeslots = read_data(data_dir, "CoordinatorAsReference", "random", device)
        assert len(last_timeslots) == SIMULATION_COUNT
        last_timeslots_dict[device] = last_timeslots
        median_last_timeslots_lst.append(np.median(last_timeslots))

    BAR_WIDTH = 0.4
    color = "black"
    linewidth = 1.25
    for idx, device in enumerate(DEVICES_COUNT):
        ax.boxplot(last_timeslots_dict[device], positions=[idx], widths=BAR_WIDTH, showfliers=False, patch_artist=True, 
                            boxprops=dict(facecolor='white', color=color, linewidth=linewidth),
                            flierprops=dict(marker='o', markerfacecolor='r', markersize=5, linestyle='none'),
                            whiskerprops=dict(color=color, linewidth=linewidth),
                            capprops=dict(color=color, linewidth=linewidth),
                            medianprops=dict(color=color, linewidth=linewidth))
    
    xticks = np.arange(len(DEVICES_COUNT))
    ax.plot(xticks, median_last_timeslots_lst, marker='o', markersize=2.5, 
            linewidth=linewidth, color='tab:orange', label="Pulsar", linestyle='-', alpha=.75) 

    # Plot linear scaling
    scaling_lst = linear_scaling(data_dir)
    ax.plot(xticks, scaling_lst, linestyle='--', color='tab:blue', label="Linear Scaling")

    
    xticklabels = [str(device) for device in DEVICES_COUNT]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)

    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.set_xlabel("\# Battery-free Devices", fontsize=14)
    ax.set_ylabel("Latency\n(\# Time Slots)", fontsize=14)
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    fig.tight_layout(pad=0.5)
    plt.show()
    fig.savefig(f"../figures/scalability.pdf", format="pdf", dpi=config.dpi, bbox_inches='tight')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scalability Plot")
    parser.add_argument("--data_dir", type=str, default="./data/simulation/"),

    args = parser.parse_args()
    data_dir = args.data_dir

    plot_data(data_dir)
    