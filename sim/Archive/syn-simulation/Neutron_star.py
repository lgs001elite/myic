import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import csv

time_threshold = 1000000
ic_num = 15  # 5, 10, 15,  30, 45
minCharge = 1
maxCharge = 100

var1Index = 0
var2Index = 0

greedySet = []
neutronStarSet = []
findSet = []
cycleSet = []


greedySyn = []
neutronStarSyn = []
findSyn = []
cycleSyn = []

def read_csv_to_array_of_ints(filename):
    array = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            int_row = [int(item) for item in row]
            array.append(int_row)
    return array


def exponential_integer_random(min_val, max_val, scale):
    while True:
        # Generate an exponential random value
        value = np.random.exponential(1 / scale)

        # Scale and shift the value to fit within the range
        mapped_value = min_val + int(value) % (max_val - min_val + 1)
        # Check if the value is within the specified range
        if min_val <= mapped_value <= max_val:
            return mapped_value


def normal_integer_random(min_val, max_val, mean, std_dev):
    while True:
        # Generate a normal random value
        normal_val = np.random.normal(mean, std_dev)

        # Round to nearest integer
        int_val = round(normal_val)

        # Check if the value is within the specified range
        if min_val <= int_val <= max_val:
            return int_val


def uniform_integer_random(min_val, max_val):
    # Generate a random integer in the specified range
    return np.random.randint(min_val, max_val)


def readCsv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    data = np.array(data)
    return data


def energy_model(model, index):
    global var1Index
    global var2Index
    if (index == 1):
        model = model + "1"
    if (index == 2):
        model = model + "2"
    if (model == "gauss1") or (model == "gauss2"):
        return normal_integer_random(minCharge, maxCharge, 50, 20)
    elif (model == "expo1") or (model == "expo2"):
        return exponential_integer_random(minCharge, maxCharge, 0.02)
    elif (model == "uniform1") or (model == "uniform2"):
        return uniform_integer_random(minCharge, maxCharge)
    elif model == "cars1":
        # return exponential_integer_random(281, 62734, 0.000224)
        file_path = "charging_traces/cars_0th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var1Index < arrLen):
            return (df[var1Index][0])
        else:
            var1Index = 0
            return (df[var1Index][0])
    elif model == "cars2":
        # return exponential_integer_random(171, 87054, 0.000333)
        file_path = "charging_traces/cars_1th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var2Index < arrLen):
            return (df[var2Index][0])
        else:
            var2Index = 0
            return (df[var2Index][0])
    elif model == "office1":
        file_path = "charging_traces/office_1th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var1Index < arrLen):
            return (df[var1Index][0])
        else:
            var1Index = 0
            return (df[var1Index][0])
    elif model == "office2":
        file_path = "charging_traces/office_2th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var2Index < arrLen):
            return (df[var2Index][0])
        else:
            var2Index = 0
            return (df[var2Index][0])
    elif model == "jogging1":
        file_path = "charging_traces/jogging_0th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var1Index < arrLen):
            return (df[var1Index][0])
        else:
            var1Index = 0
            return (df[var1Index][0])
    elif model == "jogging2":
        file_path = "charging_traces/jogging_1th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var2Index < arrLen):
            return (df[var2Index][0])
        else:
            var2Index = 0
            return (df[var2Index][0])
    elif model == "washer1":
        file_path = "charging_traces/washer_0th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var1Index < arrLen):
            return (df[var1Index][0])
        else:
            var1Index = 0
            return (df[var1Index][0])
    elif model == "washer2":
        file_path = "charging_traces/washer_1th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var2Index < arrLen):
            return (df[var2Index][0])
        else:
            var2Index = 0
            return (df[var2Index][0])
    elif model == "stairs1":
        file_path = "charging_traces/stairs_0th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var1Index < arrLen):
            return (df[var1Index][0])
        else:
            var1Index = 0
            return (df[var1Index][0])
    elif model == "stairs2":
        file_path = "charging_traces/stairs_1th.csv"
        df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df)
        if (var2Index < arrLen):
            return (df[var2Index][0])
        else:
            var2Index = 0
            return (df[var2Index][0])


# geometric ranom generator
def geoGenerator(lam):
    rNumber = np.random.geometric(p=lam, size=1)
    return int(rNumber[0])


# This function is for varying charging situation
def returnParameter(chargingTime):
    signalTag = 0
    with open("opt_scale.csv", 'r') as opt_scale:
        lines = csv.reader(opt_scale)
        countNum = 0
        for row in lines:
            if (countNum == 0):
                countNum = countNum + 1
                continue
            countNum = countNum + 1
            if (chargingTime >= int(row[0])):
                signalTag = 1
                return float(row[1])
                break
        if (signalTag == 0):
            return 0.8358041858099494


# Function entry for Find 
def find(model):
    global findSet
    global var1Index
    global var2Index
    timeCounter = 0
    senderCharge = energy_model(model, 1)
    var1Index = var1Index + 1  
    receiverCharge = energy_model(model, 2)
    var2Index = var2Index + 1 
    receiverBias = uniform_integer_random(0, receiverCharge)
    senderBias = uniform_integer_random(0, senderCharge)
    waitingTimeS = senderCharge + 1 + \
            geoGenerator(returnParameter(senderCharge)) + senderBias
            # rd.randint(0, energySet1[0])    
    waitingTimeR = receiverCharge + 1 + \
            geoGenerator(returnParameter(receiverCharge)) + receiverBias
            # rd.randint(0, energySet2[0])
    stopSignal = 1
    timeCounter = waitingTimeS
    synCounter = 0
    while (stopSignal != 0):
        if (timeCounter > time_threshold):
            findSyn.append(synCounter)
            break
        # print(timeCounter)
        # print("****")
        if (waitingTimeS > waitingTimeR):
            while (waitingTimeS > waitingTimeR):
                receiverCharge = energy_model(model, 2)
                var2Index = var2Index + 1 
                delay = geoGenerator(returnParameter(receiverCharge))
                waitingTimeR = receiverCharge + 1 + delay + waitingTimeR
        elif (waitingTimeS < waitingTimeR):
            while (waitingTimeS < waitingTimeR):
                senderCharge = energy_model(model, 1)
                var1Index = var1Index + 1 
                delay = geoGenerator(returnParameter(senderCharge))
                waitingTimeS = senderCharge + 1 + delay + waitingTimeS
                timeCounter = senderCharge + 1 + delay + timeCounter
        else:
            # stopSignal = 0
            synCounter = synCounter + 1
            timeCounter = timeCounter + waitingTimeS
            findSet.append(waitingTimeS)
            waitingTimeR = 0
            waitingTimeS = 0
            senderCharge = energy_model(model, 1)
            var1Index = var1Index + 1 
            delay = geoGenerator(returnParameter(senderCharge))
            waitingTimeS = senderCharge + 1 + delay + waitingTimeS


# Function entry for greedy
def greedy(model):
    global greedySet
    global var1Index
    global var2Index
    timeCounter = 0
    senderCharge = energy_model(model, 1)
    var1Index = var1Index + 1 
    receiverCharge = energy_model(model, 2)
    var2Index = var2Index + 1 
    receiverBias = uniform_integer_random(0, receiverCharge)
    senderBias = uniform_integer_random(0, senderCharge)
    waitingTimeS = senderCharge + 1 + senderBias
    waitingTimeR = receiverCharge + 1 + receiverBias
    timeCounter = waitingTimeS
    stopSignal = 1
    synCounter = 0
    while (stopSignal != 0):
        if (timeCounter > time_threshold):
            greedySyn.append(synCounter)
            break
        # print(timeCounter)
        if (waitingTimeS > waitingTimeR):
            while (waitingTimeS > waitingTimeR):
                receiverCharge = energy_model(model, 2)
                var2Index = var2Index + 1 
                waitingTimeR = receiverCharge + 1 + waitingTimeR
        elif (waitingTimeS < waitingTimeR):
            while (waitingTimeS < waitingTimeR):
                senderCharge = energy_model(model, 1)
                var1Index = var1Index + 1 
                waitingTimeS = senderCharge + 1 + waitingTimeS
                timeCounter = timeCounter + senderCharge + 1
        else:
            # stopSignal = 0
            synCounter = synCounter + 1
            timeCounter = timeCounter + waitingTimeS
            greedySet.append(waitingTimeS)
            waitingTimeS = 0
            waitingTimeR = 0
            senderCharge = energy_model(model, 1)
            var1Index = var1Index + 1 
            waitingTimeS = senderCharge + 1 + waitingTimeS


# Function entry for cycle
def cycle(model):
    global cycleSet
    global var1Index
    global var2Index
    timeCounter = 0
    senderCharge = energy_model(model, 1)
    var1Index = var1Index + 1   
    receiverCharge = energy_model(model, 2)
    var2Index = var2Index + 1   
    senderDelay = ic_num - (senderCharge + 1) % ic_num
    senderBias = uniform_integer_random(0, ic_num)
    receiverDelay = ic_num - (receiverCharge + 1) % ic_num
    receiverBias = uniform_integer_random(0, ic_num)
    waitingTimeS = senderCharge + 1 + \
            senderDelay + senderBias
    waitingTimeR = receiverCharge + 1 + \
            receiverDelay + receiverBias
    timeCounter = waitingTimeS
    # print(waitingTimeS)
    # print(waitingTimeR)
    stopSignal = 1
    synCounter = 0
    while (stopSignal != 0):
        if (timeCounter > time_threshold):
            # print(model + "__cycle__:" + str(waitingTimeS))
            cycleSyn.append(synCounter)
            break
        # print(timeCounter)
        if (waitingTimeS > waitingTimeR):
            while (waitingTimeS > waitingTimeR):
                receiverCharge = energy_model(model, 2)
                var2Index = var2Index + 1
                receiverDelay = ic_num - (receiverCharge + 1) % ic_num
                waitingTimeR = receiverCharge + 1 + receiverDelay + waitingTimeR
        elif (waitingTimeS < waitingTimeR):
            while (waitingTimeS < waitingTimeR):
                senderCharge = energy_model(model, 1)
                var1Index = var1Index + 1
                senderDelay = ic_num - (senderCharge + 1) % ic_num
                waitingTimeS = senderCharge + 1 + senderDelay + waitingTimeS
                timeCounter = senderCharge + 1 + senderDelay + timeCounter
        else:
            # print(model + "__cycle__:" + str(waitingTimeS))
            # stopSignal = 0
            synCounter = synCounter + 1
            timeCounter = timeCounter + waitingTimeS
            cycleSet.append(waitingTimeS)
            waitingTimeR = 0
            waitingTimeS = 0
            senderCharge = energy_model(model, 1)
            var1Index = var1Index + 1
            senderDelay = ic_num - (senderCharge + 1) % ic_num
            waitingTimeS = senderCharge + 1 + senderDelay + waitingTimeS


# Function entry for neutron_star
def neutron_star(model):
    global neutronStarSet
    global var1Index
    global var2Index
    timeCounter = 0
    # print(time_threshold)
    # for sender node
    sumSender = energy_model(model, 1) + 1
    bias = uniform_integer_random(0, ic_num)
    var1Index = var1Index + 1
    while (bias != 0):
        tch_sender = energy_model(model, 1)
        delay_sender = ic_num - ((tch_sender + 1) % ic_num) + 1
        var1Index = var1Index + 1
        bias = bias - 1
        sumSender = sumSender + delay_sender + tch_sender + 1
    tch_sender = energy_model(model, 1)
    delay_sender = ic_num - ((tch_sender + 1) % ic_num)
    var1Index = var1Index + 1
    sumSender = sumSender + delay_sender + tch_sender + 1
    timeCounter = sumSender
    # for receiver node
    sumReceiver = energy_model(model, 2) + 1
    bias = uniform_integer_random(0, ic_num)
    var2Index = var2Index + 1
    while (bias != 0):
        tch_receiver = energy_model(model, 2)
        delay_receiver = ic_num - ((tch_receiver + 1) % ic_num) + 1
        var2Index = var2Index + 1
        bias = bias - 1
        sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1
    tch_receiver = energy_model(model, 2)
    delay_receiver = ic_num - ((tch_receiver + 1) % ic_num)
    var2Index = var2Index + 1
    sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1
    # Initial bias adjustment
    bias_S = ic_num - sumSender%ic_num
    bias_R = ic_num - sumReceiver%ic_num
    sumSender = sumSender + bias_S
    sumReceiver = sumReceiver + bias_R
    
    # discovery assist
    #print(sumReceiver)
    #print(sumSender)
    #print("^^^^^^^")
    synCounter = 0
    while (sumSender != sumReceiver):
        #print(sumReceiver)
        #print(sumSender)
        #print("******")
        if (timeCounter > time_threshold):
            neutronStarSyn.append(synCounter)
            break
        # print(timeCounter)
        if (sumSender > sumReceiver):
            tch_receiver = energy_model(model, 2)
            delay_receiver = ic_num - ((tch_receiver + 1) % ic_num)
            var2Index = var2Index + 1
            sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1
        if (sumSender < sumReceiver):
            tch_sender = energy_model(model, 1)
            delay_sender = ic_num - ((tch_sender + 1) % ic_num)
            var1Index = var1Index + 1
            sumSender = sumSender + delay_sender + tch_sender + 1
            timeCounter = timeCounter + delay_sender + tch_sender + 1
        if (sumReceiver == sumSender):
            synCounter = synCounter + 1
            timeCounter = timeCounter + sumSender
            neutronStarSet.append(sumSender)
            sumReceiver = 0
            sumSender = 0
            tch_sender = energy_model(model, 1)
            delay_sender = ic_num - ((tch_sender + 1) % ic_num)
            var1Index = var1Index + 1
            sumSender = sumSender + delay_sender + tch_sender + 1


if __name__ == "__main__":
    for model in ["gauss", "expo", "uniform", "cars", "stairs", "office", "washer", "jogging"]:  # "gauss", "expo", "uniform", "cars", "stairs", "office", "washer", "jogging"
        var1Index = 0
        var2Index = 0
        greedySet = []
        neutronStarSet = []
        findSet = []
        cycleSet = []
        greedySyn = []
        neutronStarSyn = []   
        findSyn = []
        cycleSyn = []
        for i in range(100):  # 
            rd.seed(i)
            neutron_star(model)
            # print("***")
            cycle(model)
            # print("***")
            greedy(model)
            # print("***")
            find(model) 
            # print("***")
        findSet_sorted = np.sort(findSet)
        greedySet_sorted = np.sort(greedySet)
        cycleSet_sorted = np.sort(cycleSet)
        neutronStarSet_sorted = np.sort(neutronStarSet)
        print("********* " + model + "--- average syn time ********")
        if (len(findSet) > 0):
            print(np.mean(findSet))
        if (len(greedySet) > 0):
            print(np.mean(greedySet))
        if (len(cycleSet) > 0):
            print(np.mean(cycleSet))
        if (len(neutronStarSet) > 0):
            print(np.mean(neutronStarSet))
        print("*********** length ***********")
        print(len(findSet))
        print(len(greedySet))
        print(len(cycleSet))
        print(len(neutronStarSet))
        print("*********** maximum ***********")
        if (len(findSet) > 0):
            print(max(findSet))
        if (len(greedySet) > 0):
            print(max(greedySet))
        if (len(cycleSet) > 0):
            print(max(cycleSet))
        if (len(neutronStarSet) > 0):
            print(max(neutronStarSet))
        print("*********** syn_counter ***********")
        print(findSyn)
        print(greedySyn)
        print(cycleSyn)
        print(neutronStarSyn)
        cdf_find = np.arange(1, len(findSet_sorted) + 1) / len(findSet_sorted)
        cdf_greedy = np.arange(1, len(greedySet_sorted) + 1) / len(greedySet_sorted)
        cdf_cycle = np.arange(1, len(cycleSet_sorted) + 1) / len(cycleSet_sorted)
        cdf_neutronStar = np.arange(1, len(neutronStarSet_sorted) + 1) / len(neutronStarSet_sorted)
        plt.figure()
        plt.plot(findSet_sorted, cdf_find, label="find")
        plt.plot(greedySet_sorted, cdf_greedy, label="greedy")
        plt.plot(cycleSet_sorted, cdf_cycle, label="cycle")
        plt.plot(neutronStarSet_sorted, cdf_neutronStar, label="neutronStar")
        plt.title(model + " energy trace")
        plt.legend()
        plt.grid()
        plt.savefig("cdf_syn_" + model + ".pdf", format="pdf", bbox_inches="tight")
        # plt.show()

