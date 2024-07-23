
import argparse, os
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import config

config.configure(mpl, plt)

CHARGING_TYPES = ["random", "constant", "file_stairs_0th", "file_jogging_0th"]
CHARGING_TYPES_TITLE = {"random": "Random", "constant": "Static", "file_stairs_0th": "Stairs Trace", "file_jogging_0th": "Jogging Trace"}
SIMULATION_COUNT = 100
DEVICE_TYPES = ["immediate", "FindDevice", "FlyncDevice", "CoordinatorAsReference"]
DEVICE_TYPES_TITLE = {"immediate": "Greedy", "FindDevice": "Find", "FlyncDevice": "Flync-Find", "CoordinatorAsReference": "Pulsar"}
NUM_OF_DEVICES = [2, 10 , 25]
COLORS = {"immediate": 'tab:orange', "FindDevice": 'tab:blue', "FlyncDevice": 'tab:purple', "CoordinatorAsReference": 'tab:green'}

def read_data(data_dir, device_type, charging_type, num_of_devices):
    last_timeslots_filename = f"{data_dir}/{device_type}_{num_of_devices}_{charging_type}_{SIMULATION_COUNT}_last_timeslots.npy"
    collision_count_filename = f"{data_dir}/{device_type}_{num_of_devices}_{charging_type}_{SIMULATION_COUNT}_collision_counts.npy"

    print(f"DeviceType: {device_type}, ChargingType: {charging_type}, NumOfDevices: {num_of_devices}")

    collision_count = None
    if os.path.exists(collision_count_filename) is True:
        collision_count = np.load(collision_count_filename)
        print(f"MedianCollisionCount: {np.median(collision_count)}, AverageCollisionCount: {np.mean(collision_count)}")
    if os.path.exists(last_timeslots_filename) is False:
        return None, None
    last_timeslots = np.load(last_timeslots_filename, allow_pickle=True)
    print(f"MedianLastTimeSlots: {np.median(last_timeslots)}, AverageLastTimeSlots: {np.mean(last_timeslots)}")

    return last_timeslots, collision_count

class CustomScaleFormatter(ScalarFormatter):
        def _set_format(self):
            self.format = "%1.1f"

def plot_data(data_dir):
    

    fig, ax = plt.subplots(nrows=1, ncols=4, 
                           figsize=config.set_size(config.width, height_div=5, fraction=1.0))
    
    device_types_count = len(DEVICE_TYPES)
    num_of_devices_count = len(NUM_OF_DEVICES)
    BAR_WIDTH = 0.6
    for i, charging_type in enumerate(CHARGING_TYPES):
        _ax = ax[i]
        for j, device_type in enumerate(DEVICE_TYPES):
            print("\n\n\n\n")
            for k, num_of_devices in enumerate(NUM_OF_DEVICES):
                print("\n")
                last_timeslots, _ = read_data(data_dir, device_type, charging_type, num_of_devices)

                bar_index = k * (device_types_count + 1) + (j + 1)
                if last_timeslots is None or len(last_timeslots) < 0.9 * SIMULATION_COUNT:
                    if last_timeslots is not None:
                        print(f"Incomplete data for {device_type}, {charging_type}, {num_of_devices}, {len(last_timeslots)}")
                    else:
                        print(f"Missing data for {device_type}, {charging_type}, {num_of_devices}")
                    # plot cross for missing data
                    if i == 1:
                        y_pos = 0.125 * 1e5
                    elif i == 3:
                        y_pos = 0.34 * 1e6
                    _ax.plot(bar_index, y_pos, marker='x', color='tab:red', markersize=10)
                else:
                    linewidth = 1.0
                    _ax.boxplot(last_timeslots, positions=[bar_index], widths=BAR_WIDTH, showfliers=False, patch_artist=True, 
                            boxprops=dict(facecolor='white', color=COLORS[device_type], linewidth=linewidth),
                            flierprops=dict(marker='o', markerfacecolor='r', markersize=5, linestyle='none'),
                            whiskerprops=dict(color=COLORS[device_type], linewidth=linewidth),
                            capprops=dict(color=COLORS[device_type], linewidth=linewidth),
                            medianprops=dict(color=COLORS[device_type], linewidth=linewidth))


        xticks = [2.5 + (i * (device_types_count+1)) for i in range(num_of_devices_count)]         
        xtickslabels = NUM_OF_DEVICES 
        _ax.set_xticks(xticks)
        _ax.set_xticklabels(xtickslabels, fontsize=14)            
        _ax.set_title(CHARGING_TYPES_TITLE[charging_type], fontsize=14)
        _ax.set_xlabel("\# Battery-free Devices", fontsize=14)
        _ax.tick_params(axis='both', which='major', labelsize=14)

        # Set y-axis formatter
        y_formatter = CustomScaleFormatter()
        y_formatter.set_powerlimits((0, 0))
        _ax.yaxis.set_major_formatter(y_formatter)
        # _ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
        
        if i == 0:
            _ax.set_ylabel("Latency (\# Time Slots)", fontsize=14)

        for j in range(1, num_of_devices_count):
            _ax.axvline(x=(j * (device_types_count+1)), color='gray', linestyle='dotted', linewidth=0.5)   
        
        # _ax.grid(linestyle='dotted', linewidth=0.5)
    # Legend
    for device_type in DEVICE_TYPES:
        ax[2].plot([], label=DEVICE_TYPES_TITLE[device_type], color=COLORS[device_type], linewidth=1.0)
    # add solid background color
    ax[2].legend(fontsize=14, loc="upper left", frameon=True, facecolor='white', edgecolor='gray', framealpha=1.0)
    
    fig.tight_layout(pad=0.5)
    plt.show()
    fig.savefig(f"../figures/simulation.pdf", format="pdf", dpi=config.dpi, bbox_inches='tight')

def compare_data(data_dir, device_type_1, device_type_2):
    print(f"Comparing {device_type_1} and {device_type_2}")
    for charging_type in CHARGING_TYPES:
        for num_of_devices in NUM_OF_DEVICES:
            last_timeslots_1, _ = read_data(data_dir, device_type_1, charging_type, num_of_devices)
            last_timeslots_2, _ = read_data(data_dir, device_type_2, charging_type, num_of_devices)
            if last_timeslots_1 is None or last_timeslots_2 is None:
                raise ValueError(f"Missing data for {device_type_1}, {device_type_2}, {charging_type}, {num_of_devices}")
            assert len(last_timeslots_1) == len(last_timeslots_2)
            gain_ratio = np.median(last_timeslots_2) / np.median(last_timeslots_1)
            print(f"ChargingType: {charging_type}, NumOfDevices: {num_of_devices}, GainRatio: {gain_ratio}")

    # Print collision rates
    for charging_type in CHARGING_TYPES:
        for num_of_devices in NUM_OF_DEVICES:
            _, collision_count_1 = read_data(data_dir, device_type_1, charging_type, num_of_devices)
            _, collision_count_2 = read_data(data_dir, device_type_2, charging_type, num_of_devices)
            
            collision_count_1 = np.median(collision_count_1) if collision_count_1 is not None else 0
            collision_count_2 = np.median(collision_count_2) if collision_count_2 is not None else 0
            print(f"ChargingType: {charging_type}, NumOfDevices: {num_of_devices}, Pulsar: {collision_count_1}, Find: {collision_count_2}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulation Plot")
    parser.add_argument("--data_dir", type=str, default="./data/simulation/"),

    args = parser.parse_args()
    data_dir = args.data_dir

    plot_data(data_dir)
    # compare_data(data_dir, "CoordinatorAsReference", "FindDevice")
