import argparse
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import config

config.configure(mpl, plt)

SIMULATION_COUNT = 100
DEVICES_COUNT = [10, 25, 2]
DEVICE_TYPE = "CoordinatorAsReference"
CHARGING_TYPE = "random"
PERCENT_LIST = list(range(100, 1001, 50))
LABELS = {2: "2 Battery-free Devices", 10: "10 Battery-free Devices", 25: "25 Battery-free Devices"}
MARKERS = {2: 'x', 10: 'o', 25: 's'}

def get_coordinators_slots():
    coordinators_slots_dict = {}
    for device_count in DEVICES_COUNT:
        coordinators_slots_dict[device_count] = []
        for percent in PERCENT_LIST:
            coordinators_slots = int((percent / 100.0) * device_count)
            if coordinators_slots <= device_count:
                coordinators_slots = device_count + 1
            coordinators_slots_dict[device_count].append(coordinators_slots)
    return coordinators_slots_dict

def read_data(data_dir, device_type, charging_type, num_of_devices, coordinators_slots):
    last_timeslots_filename = f"{data_dir}/{device_type}_{num_of_devices}_{charging_type}_{SIMULATION_COUNT}_{coordinators_slots}_last_timeslots.npy"
    collision_count_filename = f"{data_dir}/{device_type}_{num_of_devices}_{charging_type}_{SIMULATION_COUNT}_{coordinators_slots}_collision_counts.npy"

    print(f"DeviceType: {device_type}, ChargingType: {charging_type}, NumOfDevices: {num_of_devices}, CoordinatorsSlots: {coordinators_slots}")

    if os.path.exists(collision_count_filename) is True:
        print(f"MedianCollisionCount: {np.median(np.load(collision_count_filename))}")
    if os.path.exists(last_timeslots_filename) is False:
        return None
    last_timeslots = np.load(last_timeslots_filename, allow_pickle=True)
    print(f"MedianLastTimeSlots: {np.median(last_timeslots)}")

    return last_timeslots

def plot_data(data_dir):
    fig, ax = plt.subplots(figsize=config.set_size(config.width, height_div=3, fraction=0.5))

    coordinators_slots_dict = get_coordinators_slots()

    for device in DEVICES_COUNT:
        median_last_timeslots_lst = []
        for coordinators_slots in coordinators_slots_dict[device]:
            last_timeslots = read_data(data_dir, DEVICE_TYPE, CHARGING_TYPE, device, coordinators_slots)
            assert len(last_timeslots) == SIMULATION_COUNT
            median_last_timeslots_lst.append(np.median(last_timeslots))

        ax.plot(range(len(median_last_timeslots_lst)), median_last_timeslots_lst, label=LABELS[device], marker=MARKERS[device], markersize=4.0, linestyle='-', alpha=.75)

    ax.set_xlabel("Slots in Slot Distribution Cycle (" + r'$\times$' + " \# Battery-free Nodes)", fontsize=14)
    ax.set_ylabel("Median Latency\n(\# Time Slots)", fontsize=14)

    xticks = np.arange(len(PERCENT_LIST))
    xticklabels = [percent/100 for percent in PERCENT_LIST]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax.tick_params(axis='both', which='major', labelsize=12)

    ax.legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2, framealpha=1, facecolor='white', edgecolor='gray')

    fig.tight_layout(pad=0.5)
    plt.show()
    fig.savefig(f"../figures/parameters.pdf", format="pdf", dpi=config.dpi, bbox_inches='tight')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parameters Plot")
    parser.add_argument("--data_dir", type=str, default="./data/parameters/"),

    args = parser.parse_args()
    data_dir = args.data_dir

    plot_data(data_dir)