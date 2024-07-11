


import subprocess
import sys

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} installed successfully.")
    finally:
        globals()[package] = __import__(package)

install_and_import('matplotlib')


import numpy as np
import random as rd
import matplotlib.pyplot as plt
import logging
import csv

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['font.size'] = str(15)
#plt.rcParams['font.family'] = 'Arial'
time_threshold = 3600000



scenarios = [ "1to300", "1to500",  "1to1000", "500to1000"]

neutronStarSet = []



def uniform_integer_random(min_val, max_val):
    # Generate a random integer in the specified range
    return np.random.randint(min_val, max_val + 1)


def energy_model(scenario):
    if scenario == "1to300": 
        return uniform_integer_random(1, 300)
    elif scenario =="1to500":
        return uniform_integer_random(1, 500)
    elif scenario == "1to1000":
        return uniform_integer_random(1, 1000)
    elif scenario == "500to1000":
        return uniform_integer_random(500, 1000)
    else:
        return 0

# Function entry for neutron_star
def NeutronStar(cycle, scenario):
    global neutronStarSet
    sumSender = 0
    sumReceiver = 0
    # for sender node
    tch_sender = energy_model(scenario)
    sumSender = tch_sender + 1 + uniform_integer_random(0,tch_sender )
    bias = sumSender%cycle
    if bias != 0:
        bias = cycle - bias
    sumSender = sumSender + bias
    # for receiver node
    tch_receiver = energy_model(scenario)
    sumReceiver = tch_receiver + 1 + uniform_integer_random(0,tch_receiver )
    bias = sumReceiver%cycle
    if bias != 0:
        bias = cycle - bias
    sumReceiver = sumReceiver + bias
       
    # Initial bias adjustment
    while (True):
        if (sumSender > time_threshold):
            neutronStarSet.append(sumSender)
            break
        if (sumSender > sumReceiver):
            tch_receiver = energy_model(scenario)
            cycle_receiver = tch_receiver + 1
            bias = cycle_receiver % cycle
            if bias != 0:
                bias = cycle -  bias
            sumReceiver = sumReceiver + cycle_receiver + bias
        elif (sumSender < sumReceiver):
            tch_sender = energy_model(scenario)
            cycle_sender = tch_sender + 1
            bias = cycle_sender % cycle
            if bias != 0:
                bias = cycle -  bias
            sumSender = sumSender + cycle_sender + bias
        else:
            neutronStarSet.append(sumSender)
            break

if __name__ == "__main__":
    fig, axs = plt.subplots(1, 4, constrained_layout=True, figsize=(12, 3))
    fig.suptitle("coordinator cycle factor")
    for index in range(4):
        ave_neu = []
        ave_pulsar = []
        scenario = scenarios[index]
        if scenario == "1to300":
            csvRecorder = open("1to300.csv", 'w', newline='')
            fieldnames=["seq", "number"]
            writer = csv.DictWriter(csvRecorder, fieldnames=fieldnames)
            for cycle in range(2, 302):
                neutronStarSet = []
                for repeat in range(100):
                    NeutronStar(cycle, scenario)
                ave_value = np.average(neutronStarSet)
                ave_neu.append(ave_value)
                writer.writerow({"seq":str(cycle), "number":str(ave_value)})
            csvRecorder.close()
        elif scenario == "1to500":
            csvRecorder = open("1to500.csv", 'w', newline='')
            fieldnames=["seq", "number"]
            writer = csv.DictWriter(csvRecorder, fieldnames=fieldnames)
            for cycle in range(2, 502):
                neutronStarSet = []
                pulsarSet = []
                for repeat in range(100):
                    NeutronStar(cycle, scenario)
                ave_value = np.average(neutronStarSet)
                ave_neu.append(ave_value)
                writer.writerow({"seq":str(cycle), "number":str(ave_value)})
            csvRecorder.close()
        elif scenario == "1to1000":
            csvRecorder = open("1to1000.csv", 'w', newline='')
            fieldnames=["seq", "number"]
            writer = csv.DictWriter(csvRecorder, fieldnames=fieldnames)
            for cycle in range(2, 1002):
                neutronStarSet = []
                for repeat in range(100):
                    NeutronStar(cycle, scenario)
                ave_value = np.average(neutronStarSet)
                ave_neu.append(ave_value)
                writer.writerow({"seq":str(cycle), "number":str(ave_value)})
            csvRecorder.close()
        elif scenario == "500to1000":
            csvRecorder = open("500to1000.csv", 'w', newline='')
            fieldnames=["seq", "number"]
            writer = csv.DictWriter(csvRecorder, fieldnames=fieldnames)
            for cycle in range(2, 1002):
                neutronStarSet = []
                for repeat in range(100):
                    NeutronStar(cycle, scenario)
                ave_value = np.average(neutronStarSet)
                ave_neu.append(ave_value)
                writer.writerow({"seq":str(cycle), "number":str(ave_value)})
            csvRecorder.close()
        else:
            print("error")

        axs[index].plot(ave_neu)
        axs[index].set_title(scenarios[index])
        axs[index].set_xlabel("Cycle size")
        axs[index].set_ylabel("Average time [slots]")
        axs[index].ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    plt.savefig("cycle_size_syn.pdf", format='pdf')
    plt.close("all")

