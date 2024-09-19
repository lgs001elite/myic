


import subprocess
import sys
import time
import random


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
plt.rcParams['font.family'] = 'Arial'
time_threshold = 3600000



scenarios = ["[300]", "[1,500]", "front-[300,500]", "back-[300,500]"]


neutronStarSet = []

repetitive = 10000

threshold = 502

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']


 # Generate a dynamic random seed using the current time
def generate_dynamic_seed():
    return int(time.time() * 1000)  # Current time in milliseconds

def uniform_integer_random(min_val, max_val):
    # Generate a random integer in the specified range
    return random.randint(min_val, max_val + 1)


def energy_model(scenario):
    randSeed = generate_dynamic_seed()
    random.seed(randSeed)
    if scenario == "[1,100]": 
        return uniform_integer_random(1, 100)
    elif scenario =="[1,300]":
        return uniform_integer_random(1, 300)
    elif scenario =="front-[300,500]":
        return uniform_integer_random(300, 500)
    elif scenario =="back-[300,500]":
        return uniform_integer_random(300, 500)
    elif scenario == "[1,500]":
        return uniform_integer_random(1, 500)
    elif scenario == "[1,1000]":
        return uniform_integer_random(1, 1000)
    elif scenario == "[100,500]":
        return uniform_integer_random(100, 500)
    elif scenario == "[400,500]":
        return uniform_integer_random(400, 500)
    elif scenario == "[500,1000]":
        return uniform_integer_random(500, 1000)
    elif scenario == "[300]":
        return 300
    else:
        print("scenario error!")
        return 0

# Function entry for neutron_star
def NeutronStar(cycle, scenario):
    global neutronStarSet
    sumSender = 0
    sumReceiver = 0
    #randSeed = generate_dynamic_seed()
    #random.seed(randSeed)
    # for sender node
    tch_sender = energy_model(scenario)
    sumSender = tch_sender + 1 + uniform_integer_random(0, 500)
    bias = sumSender%cycle
    if bias != 0:
        bias = cycle - bias
    sumSender = sumSender + bias
    # for receiver node
    tch_receiver = energy_model(scenario)
    sumReceiver = tch_receiver + 1 + uniform_integer_random(0, 500)
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
    fig, axs = plt.subplots(2, 2, constrained_layout=True)
    import matplotlib as mpl
    mpl.rcParams["legend.loc"] = 'best' 
    #fig.suptitle("coordinator cycle factor")
    for index in range(4):
        ave_neu = []
        ave_pulsar = []
        scenario = scenarios[index]
        #randSeed = generate_dynamic_seed()
        #random.seed(randSeed)
        if scenario == "back-[300,500]":
            csvRecorder = open("back-[300,500].csv", 'w', newline='')
            fieldnames=["seq", "number"]
            writer = csv.DictWriter(csvRecorder, fieldnames=fieldnames)
            for cycle in range(300, threshold):
                neutronStarSet = []
                for repeat in range(repetitive):
                    NeutronStar(cycle, scenario)
                ave_value = np.average(neutronStarSet)
                ave_neu.append(ave_value)
                writer.writerow({"seq":str(cycle), "number":str(ave_value)})
            csvRecorder.close()
        elif scenario == "front-[300,500]":
            csvRecorder = open("front-[300,500].csv", 'w', newline='')
            fieldnames=["seq", "number"]
            writer = csv.DictWriter(csvRecorder, fieldnames=fieldnames)
            for cycle in range(2, 300):
                neutronStarSet = []
                for repeat in range(repetitive):
                    NeutronStar(cycle, scenario)
                ave_value = np.average(neutronStarSet)
                ave_neu.append(ave_value)
                writer.writerow({"seq":str(cycle), "number":str(ave_value)})
            csvRecorder.close()
        elif scenario == "[1,500]":
            csvRecorder = open("[1,500].csv", 'w', newline='')
            fieldnames=["seq", "number"]
            writer = csv.DictWriter(csvRecorder, fieldnames=fieldnames)
            for cycle in range(2, threshold):
                neutronStarSet = []
                for repeat in range(repetitive):
                    NeutronStar(cycle, scenario)
                ave_value = np.average(neutronStarSet)
                ave_neu.append(ave_value)
                writer.writerow({"seq":str(cycle), "number":str(ave_value)})
            csvRecorder.close()
        elif scenario == "[300]":
            csvRecorder = open("[300].csv", 'w', newline='')
            fieldnames=["seq", "number"]
            writer = csv.DictWriter(csvRecorder, fieldnames=fieldnames)
            for cycle in range(2, threshold):
                neutronStarSet = []
                for repeat in range(repetitive):
                    NeutronStar(cycle, scenario)
                ave_value = np.average(neutronStarSet)
                ave_neu.append(ave_value)
                writer.writerow({"seq":str(cycle), "number":str(ave_value)})
            csvRecorder.close()
        else:
            print("error")
        if index == 0:
            x_ticks = np.arange(2, threshold, 1)
            axs[0][0].plot(x_ticks, ave_neu, label=scenario, color=colors[index])
            axs[0][0].set_ylabel("Average syn [slots]")
            axs[0][0].ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
            axs[0][0].ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
        elif index == 1:
            x_ticks = np.arange(2, threshold, 1)
            axs[0][1].plot(x_ticks, ave_neu, label=scenario, color=colors[index])
            axs[0][1].ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
            axs[0][1].ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
        elif index == 2:
            axs[1][0].set_ylabel("Average syn [slots]")
            axs[1][0].set_xlabel("Cycle size")
            x_ticks = np.arange(2, 300, 1)
            axs[1][0].plot(x_ticks, ave_neu, label=scenario, color=colors[index])
            axs[1][0].ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
            axs[1][0].ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
        else:
            axs[1][1].ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
            axs[1][1].ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
            axs[1][1].set_xlabel("Cycle size")
            x_ticks = np.arange(300, threshold, 1)
            axs[1][1].plot(x_ticks, ave_neu, label=scenario, color=colors[index])
    axs[0][0].legend()
    axs[0][1].legend()
    axs[1][0].legend()
    axs[1][1].legend()
    x_ticks = np.arange(300, threshold, 1)
    #axs[1][1].set_xticks(x_ticks)
    
    plt.savefig("cycle_size_syn.pdf", format='pdf')
    plt.show()
    plt.close("all")

