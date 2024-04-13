import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import csv

plt.rcParams['font.size'] = str(15)
plt.rcParams['font.family'] = 'Arial'
time_threshold = 10000000
time_threshold_small = 2000
working_cycles = [4]#[3, 6, 9, 11, 17, 19, 23, 25, 31]
working_cycle  = 5 
minCharge = 100
maxCharge = 500

global var1Index
global var2Index

global static_one
global static_two

lastSenderSum = 0

greedySet = []
neutronStarSet = []
neutronStarPlusSet = []
findSet = []
cycleSet = []


greedySyn = []
neutronStarSyn = []
findSyn = []
cycleSyn = []

test1 = []
test2 = []

markerSet=["X", "v", "o", "D", "."]
lineSet=["-", "--", "-.", ":", "solid"]

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
    return np.random.randint(min_val, max_val + 1)



file_path = "charging_traces/stairs_0th.csv"
df1 = read_csv_to_array_of_ints(file_path)
file_path = "charging_traces/stairs_1th.csv"
df2 = read_csv_to_array_of_ints(file_path)

def energy_model(model, index):
    global var1Index
    global var2Index
    global static_two
    global static_one
    if (index == 1):
        model = model + "1"
    if (index == 2):
        model = model + "2"
    # print(model)
    if model == "static1":
        return static_one
    elif model == "static2":
        return static_two
    elif (model == "gauss1") or (model == "expo1") or (model == "uniform1"):
        # print("test****")
        arrLen = len(test1)
        # print(arrLen)
        # print(test1)
        if (var1Index < arrLen):
            return (test1[var1Index])
        else:
            var1Index = 0
            return (test1[var1Index])
    elif (model == "gauss2") or (model == "expo2") or (model == "uniform2"):
        arrLen = len(test2)
        if (var2Index < arrLen):
            return (test2[var2Index])
        else:
            var2Index = 0
            return (test2[var2Index])
    elif model == "test1":
        arrLen = len(test1)
        if (var1Index < arrLen):
            return (test1[var1Index])
        else:
            var1Index = 0
            return (test1[var1Index])
    elif model == "test2":
        arrLen = len(test2)
        if (var2Index < arrLen):
            return (test2[var2Index])
        else:
            var2Index = 0
            return (test2[var2Index])
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
        arrLen = len(df1)
        if (var1Index < arrLen):
            return (df1[var1Index][0])
        else:
            var1Index = 0
            return (df1[var1Index][0])
    elif model == "stairs2":
        arrLen = len(df2)
        if (var2Index < arrLen):
            return (df2[var2Index][0])
        else:
            var2Index = 0
            return (df2[var2Index][0])


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
    global lastSenderSum
    global var1Index
    global var2Index
    global static_one
    global static_two
    var1Index = 0
    var2Index = 0
    lastSenderSum = 0
    senderCharge = energy_model(model, 1)
    var1Index = var1Index + 1  
    receiverCharge = energy_model(model, 2)
    var2Index = var2Index + 1
    receiverBias = uniform_integer_random(0, receiverCharge)
    senderBias = uniform_integer_random(0, senderCharge)
    # The above code is declaring a variable called `waitingTimeS`.
    # print(senderCharge)
    # print("***")
    waitingTimeS = senderCharge + 1 + \
            geoGenerator(returnParameter(senderCharge)) + senderBias   
    waitingTimeR = receiverCharge + 1 + \
            geoGenerator(returnParameter(receiverCharge)) + receiverBias
    synCounter = 0
    while (True):
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
        else:
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            #print(waitingTimeS)
            findSet.append(waitingTimeS - lastSenderSum)
            break
            # lastSenderSum = waitingTimeS
            # senderCharge = energy_model(model, 1)
            # var1Index = var1Index + 1 
            # delay = geoGenerator(returnParameter(senderCharge))
            # waitingTimeS = senderCharge + 1 + delay + waitingTimeS
        if ((waitingTimeS - lastSenderSum) > time_threshold):
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            findSet.append(waitingTimeS - lastSenderSum)
            break
            # lastSenderSum = waitingTimeS
            # senderCharge = energy_model(model, 1)
            # var1Index = var1Index + 1 
            # delay = geoGenerator(returnParameter(senderCharge))
            # waitingTimeS = senderCharge + 1 + waitingTimeS
        # if (synCounter == 100):
        #     break


# Function entry for greedy
def greedy(model):
    global lastSenderSum
    global var1Index
    global var2Index
    global static_one
    global static_two
    var1Index = 0
    var2Index = 0
    lastSenderSum = 0
    senderCharge = energy_model(model, 1)
    var1Index = var1Index + 1 
    receiverCharge = energy_model(model, 2)
    var2Index = var2Index + 1 
    receiverBias = uniform_integer_random(0, receiverCharge)
    senderBias = uniform_integer_random(0, senderCharge)
    waitingTimeS = senderCharge + 1 + senderBias
    waitingTimeR = receiverCharge + 1 + receiverBias
    synCounter = 0
    while (True):
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
        else:
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            greedySet.append(waitingTimeS - lastSenderSum)
            break
            # lastSenderSum = waitingTimeS
            # senderCharge = energy_model(model, 1)
            # var1Index = var1Index + 1 
            # waitingTimeS = senderCharge + 1 + waitingTimeS
        if ((waitingTimeS - lastSenderSum) > time_threshold):
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            greedySet.append(waitingTimeS - lastSenderSum)
            break
            # lastSenderSum = waitingTimeS
            # senderCharge = energy_model(model, 1)
            # var1Index = var1Index + 1 
            # waitingTimeR = waitingTimeS
            # waitingTimeS = senderCharge + 1 + waitingTimeS
        # if (synCounter == 100):
        #     break


# Function entry for cycle
def cycle(model):
    global lastSenderSum
    global var1Index
    global var2Index
    global static_one
    global static_two
    var1Index = 0
    var2Index = 0
    lastSenderSum = 0
    senderCharge = energy_model(model, 1)
    var1Index = var1Index + 1   
    receiverCharge = energy_model(model, 2)
    var2Index = var2Index + 1 

    senderDelay = working_cycle - (senderCharge + 1) % working_cycle
    senderBias = uniform_integer_random(0, working_cycle)

    receiverDelay = working_cycle - (receiverCharge + 1) % working_cycle
    receiverBias = uniform_integer_random(0, working_cycle)

    waitingTimeS = senderCharge + 1 + \
            senderDelay + senderBias
    waitingTimeR = receiverCharge + 1 + \
            receiverDelay + receiverBias
    synCounter = 0
    while (True):
        if (waitingTimeS > waitingTimeR):
            while (waitingTimeS > waitingTimeR):
                receiverCharge = energy_model(model, 2)
                var2Index = var2Index + 1
                receiverDelay = working_cycle - (receiverCharge + 1) % working_cycle
                waitingTimeR = receiverCharge + 1 + receiverDelay + waitingTimeR
        elif (waitingTimeS < waitingTimeR):
            while (waitingTimeS < waitingTimeR):
                senderCharge = energy_model(model, 1)
                var1Index = var1Index + 1
                senderDelay = working_cycle - (senderCharge + 1) % working_cycle
                waitingTimeS = senderCharge + 1 + senderDelay + waitingTimeS
        else:
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            cycleSet.append(waitingTimeS - lastSenderSum)
            break
            # lastSenderSum = waitingTimeS
            # senderCharge = energy_model(model, 1)
            # var1Index = var1Index + 1
            # senderDelay = working_cycle - (senderCharge + 1) % working_cycle
            # waitingTimeS = senderCharge + 1 + senderDelay + waitingTimeS
        if ((waitingTimeS - lastSenderSum) > time_threshold):
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            cycleSet.append(waitingTimeS - lastSenderSum)
            break
            # lastSenderSum = waitingTimeS
            # senderCharge = energy_model(model, 1)
            # var1Index = var1Index + 1
            # waitingTimeR = waitingTimeS
            # waitingTimeS = senderCharge + 1 + waitingTimeS
        # if (synCounter == 100):
        #     break


# Function entry for neutron_star
def neutron_star(model):
    global lastSenderSum
    global var1Index
    global var2Index
    global static_one
    global static_two
    lastSenderSum = 0
    var1Index = 0
    var2Index = 0
    # for sender node
    sumSender = energy_model(model, 1) + 1
    bias = uniform_integer_random(0, working_cycle)
    var1Index = var1Index + 1
    while (bias != 0):
        tch_sender = energy_model(model, 1)
        delay_sender = working_cycle - ((tch_sender + 1) % working_cycle) + 1
        var1Index = var1Index + 1
        bias = bias - 1
        sumSender = sumSender + delay_sender + tch_sender + 1
    tch_sender = energy_model(model, 1)
    delay_sender = working_cycle - ((tch_sender + 1) % working_cycle)
    var1Index = var1Index + 1
    sumSender = sumSender + delay_sender + tch_sender + 1
    # for receiver node
    sumReceiver = energy_model(model, 2) + 1
    bias = uniform_integer_random(0, working_cycle)
    var2Index = var2Index + 1
    while (bias != 0):
        tch_receiver = energy_model(model, 2)
        delay_receiver = working_cycle - ((tch_receiver + 1) % working_cycle) + 1
        var2Index = var2Index + 1
        bias = bias - 1
        sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1
    tch_receiver = energy_model(model, 2)
    delay_receiver = working_cycle - ((tch_receiver + 1) % working_cycle)
    var2Index = var2Index + 1
    sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1
    # Initial bias adjustment
    bias_S = working_cycle - sumSender%working_cycle
    bias_R = working_cycle - sumReceiver%working_cycle
    sumSender = sumSender + bias_S
    sumReceiver = sumReceiver + bias_R
    # discovery assist
    synCounter = 0
    # with overleaving avoidment
    while (True):
        if (sumSender > sumReceiver):
            tch_receiver = energy_model(model, 2)
            delay_receiver = working_cycle - ((tch_receiver + 1) % working_cycle)
            var2Index = var2Index + 1
            sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1
        if (sumSender < sumReceiver):
            tch_sender = energy_model(model, 1)
            delay_sender = working_cycle - ((tch_sender + 1) % working_cycle)
            var1Index = var1Index + 1
            sumSender = sumSender + delay_sender + tch_sender + 1
        if (sumReceiver == sumSender):
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            neutronStarSet.append(sumSender - lastSenderSum)
            break
            # lastSenderSum = sumSender
            # tch_sender = energy_model(model, 1)
            # delay_sender = working_cycle - ((tch_sender + 1) % working_cycle)
            # var1Index = var1Index + 1
            # sumSender = sumSender + delay_sender + tch_sender + 1
        if ((sumSender - lastSenderSum) > time_threshold):
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            neutronStarSet.append(sumSender - lastSenderSum)
            break
            # lastSenderSum = sumSender
            # tch_sender = energy_model(model, 1)
            # var1Index = var1Index + 1
            # sumReceiver = sumSender
            # sumSender = sumSender  + tch_sender + 1
        # if (synCounter == 100):
        #     break


# Function entry for neutron_star
def neutron_star_plus(model):
    global lastSenderSum
    global var1Index
    global var2Index
    global static_one
    global static_two
    lastSenderSum = 0
    var1Index = 0
    var2Index = 0
    # anchor
    anchor_sender = 0
    anchor_receiver = 0
    # for sender node
    sumSender = energy_model(model, 1) + 1
    bias = uniform_integer_random(0, working_cycle)
    var1Index = var1Index + 1
    while (bias != 0):
        tch_sender = energy_model(model, 1)
        delay_sender = working_cycle - ((tch_sender + 1) % working_cycle) + 1
        var1Index = var1Index + 1
        bias = bias - 1
        sumSender = sumSender + delay_sender + tch_sender + 1
    tch_sender = energy_model(model, 1)
    delay_sender = working_cycle - ((tch_sender + 1) % working_cycle)
    var1Index = var1Index + 1
    sumSender = sumSender + delay_sender + tch_sender + 1
    # for receiver node
    sumReceiver = energy_model(model, 2) + 1
    bias = uniform_integer_random(0, working_cycle)
    var2Index = var2Index + 1
    while (bias != 0):
        tch_receiver = energy_model(model, 2)
        delay_receiver = working_cycle - ((tch_receiver + 1) % working_cycle) + 1
        var2Index = var2Index + 1
        bias = bias - 1
        sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1
    tch_receiver = energy_model(model, 2)
    delay_receiver = working_cycle - ((tch_receiver + 1) % working_cycle)
    var2Index = var2Index + 1
    sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1
    # Initial bias adjustment
    bias_S = working_cycle - sumSender%working_cycle
    bias_R = working_cycle - sumReceiver%working_cycle
    sumSender = sumSender + bias_S
    sumReceiver = sumReceiver + bias_R
    # discovery assist
    synCounter = 0
    # plus
    # anchor_sender   = delay_sender
    # anchor_receiver = delay_receiver
    # init_bias_r = sumSender - sumReceiver
    # init_bias_s = sumReceiver- sumSender
    # print(init_bias_r)
    # print("hello bugs")
    # plus
    # if init_bias_r > 0:
    #     if (init_bias_r > delay_receiver):
    #         sumReceiver = sumReceiver + init_bias_r - delay_receiver
    #     else:
    #         temp_bias = delay_receiver % (init_bias_r + anchor_sender)
    #         sumReceiver = sumReceiver + anchor_sender - temp_bias
    # # plus
    # if init_bias_s > 0 :
    #     if (init_bias_s > delay_sender):
    #         sumSender = sumSender + init_bias_s - delay_sender
    #     else:
    #         temp_bias = delay_sender % (init_bias_s + anchor_receiver)
    #         sumSender = sumSender + anchor_receiver - temp_bias
    while (True):
    # with overleaving avoidment
        biasSwitch_sender = uniform_integer_random(0,2)
        biasSwitch_receiver = uniform_integer_random(0,2)
        if (sumSender > sumReceiver):
            # print(sumReceiver)
            # print(sumSender)
            # print("Hello world")
            tch_receiver = energy_model(model, 2)
            delay_receiver = working_cycle - ((tch_receiver + 1) % working_cycle)
            var2Index = var2Index + 1
            sumReceiver = sumReceiver + delay_receiver + tch_receiver + 1 
            if (biasSwitch_receiver == 0):
                sumReceiver = sumReceiver + working_cycle
        if (sumSender < sumReceiver):
            tch_sender = energy_model(model, 1)
            delay_sender = working_cycle - ((tch_sender + 1) % working_cycle)
            var1Index = var1Index + 1
            sumSender = sumSender + delay_sender + tch_sender + 1
            if (biasSwitch_sender == 0):
                sumSender = sumSender + working_cycle
        if (sumReceiver == sumSender):
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            init_bias_r = 0
            init_bias_s = 0
            synCounter = synCounter + 1
            neutronStarPlusSet.append(sumSender - lastSenderSum)
            break
            # lastSenderSum = sumSender
            # tch_sender = energy_model(model, 1)
            # delay_sender = working_cycle - ((tch_sender + 1) % working_cycle)
            # var1Index = var1Index + 1
            # sumSender = sumSender + delay_sender + tch_sender + 1
            # anchor_sender   = delay_sender
            # anchor_receiver = delay_receiver
        if ((sumSender - lastSenderSum) > time_threshold):
            # static_one = uniform_integer_random(minCharge, maxCharge)
            # static_two = uniform_integer_random(minCharge, maxCharge)
            synCounter = synCounter + 1
            neutronStarPlusSet.append(sumSender - lastSenderSum)
            break
        #     lastSenderSum = sumSender
        #     tch_sender = energy_model(model, 1)
        #     var1Index = var1Index + 1
        #     sumReceiver = sumSender
        #     sumSender = sumSender + delay_sender + tch_sender + 1
        #     anchor_sender   = delay_sender
        #     anchor_receiver = delay_receiver
        # if (synCounter == 100):
        #     break



if __name__ == "__main__":
    fig = plt.figure(constrained_layout=True, figsize=(15, 9))
    fig.suptitle('Synchronization performance comparison')
    subfigs = fig.subfigures(nrows=3, ncols=1)
    plot_counter_row = 0
    ave_greedy = []
    ave_find = []
    ave_neu = []
    ave_neuPlus = []
    for cycleSize in working_cycles:
        print("***********" + "The cycles of the coordinator:" + str(cycleSize) + "***********")
        working_cycle = cycleSize
        plot_counter_column = 0
        subfigs[plot_counter_row].suptitle("Coordinator with " + str(cycleSize) + " slots")
        axs = subfigs[plot_counter_row].subplots(nrows=1, ncols=5)
        axs[plot_counter_column].set_ylabel("CDF")
        for model in ["stairs"]: #["gauss", "expo", "uniform", "stairs", "static"]:
            greedySet = []
            neutronStarSet = []
            neutronStarPlusSet = []
            findSet = []
            cycleSet = []
            # producing charging datasets
            for i in range(100):
                rd.seed(i)
                test1 = []
                test2 = []
                if (model == "gauss"):
                    sumCounter = 0
                    while (sumCounter < time_threshold):
                        var = normal_integer_random(minCharge, maxCharge, 300, 10)
                        sumCounter = sumCounter + var
                        test1.append(var)
                    sumCounter = 0
                    while (sumCounter < time_threshold):
                        var = normal_integer_random(minCharge, maxCharge, 300, 10)
                        sumCounter = sumCounter + var
                        test2.append(var)
                if (model == "expo"):
                    sumCounter = 0
                    while (sumCounter < time_threshold):
                        var = exponential_integer_random(minCharge, maxCharge, 0.01)
                        sumCounter = sumCounter + var
                        test1.append(var)
                    sumCounter = 0
                    while (sumCounter < time_threshold):
                        var = exponential_integer_random(minCharge, maxCharge, 0.01)
                        sumCounter = sumCounter + var
                        test2.append(var)
                if (model == "uniform"):
                    sumCounter = 0
                    while (sumCounter < time_threshold):
                        var = uniform_integer_random(minCharge, maxCharge)
                        sumCounter = sumCounter + var
                        test1.append(var)
                    sumCounter = 0
                    while (sumCounter < time_threshold):
                        var = uniform_integer_random(minCharge, maxCharge)
                        sumCounter = sumCounter + var
                        test2.append(var)
                if (model == "static"):
                    static_one =  100#uniform_integer_random(minCharge, maxCharge)
                    static_two =  100 #uniform_integer_random(minCharge, maxCharge)
                    #print(str(static_one - static_two) + ",***")
                # print(static_one)
                # print(static_two)
                #print("Values here")
                neutron_star(model)
                neutron_star_plus(model)
                greedy(model)
                find(model) 
                #print(str(i + 1)+"%")
            
            print("********* " + model + "--- average syn time ********")
            print(np.mean(findSet))
            ave_find.append(np.mean(findSet))
            print(np.mean(greedySet))
            ave_greedy.append(np.mean(greedySet))
            #print(np.mean(cycleSet))
            print(np.mean(neutronStarSet))
            ave_neu.append(np.mean(neutronStarSet))
            print(np.mean(neutronStarPlusSet))
            ave_neuPlus.append(neutronStarPlusSet)
    # plt.plot(ave_neuPlus, label = "neuPlus")
    # plt.plot(ave_find, label="find")
    # plt.plot(ave_greedy, label="greedy")
    # plt.plot(ave_neu, label="neu")
    # plt.legend()
    # plt.savefig("observe.pdf", format='pdf')
    # plt.show()
            # print("*********** maximum ***********")
            # print(max(findSet))
            # print(max(greedySet))
            # #print(max(cycleSet))
            # print(max(neutronStarSet))
            # print(max(neutronStarPlusSet))
            # print("*********** syn_counter ***********")
            # print(len(neutronStarSet))
            # #print(np.average(neutronStarSet))
            # print(len(neutronStarPlusSet))
            # #print(np.average(neutronStarPlusSet))
            # print(len(findSet))
            # #print(np.average(findSet))
            #print(len(greedySet))
            #print(np.average(greedySet))
            # print(len(cycleSet))
            # print(np.average(cycleSet))

    #         # find results
    #         find_results = []
    #         len_g = len(neutronStarSet)
    #         for i in range(len_g):
    #             find_results.append(findSet[i]/neutronStarSet[i])
    #         # # greedy results
    #         greedy_results = []
    #         for i in range(len_g):
    #             greedy_results.append(greedySet[i]/neutronStarSet[i])
    #         # neutronStar results
    #         # neutronStar_results = []
    #         # for i in range(len_g):
    #         #     neutronStar_results.append(neutronStarSet[i]/greedySet[i])
    #         # neutronStarPlus results
    #         neutronStarPlus_results = []
    #         for i in range(len_g):
    #             neutronStarPlus_results.append(neutronStarPlusSet[i]/neutronStarSet[i]) 
    #         greedySet_sorted = np.sort(greedy_results)
    #         findSet_sorted = np.sort(find_results)
    #         # cycleSet_sorted = np.sort(cycleSet)
    #         #neutronStarSet_sorted = np.sort(neutronStar_results)
    #         neutronStarPlusSet_sorted = np.sort(neutronStarPlus_results)
    #         len_fsorted = len(findSet_sorted)
    #         len_gsorted = len(greedySet_sorted)
    #         #len_nsorted = len(neutronStarSet_sorted)
    #         len_npsorted = len(neutronStarPlusSet_sorted)
    #         #len_csorted = len(cycleSet_sorted)
    #         #cdf_cycle = np.arange(1, len_csorted + 1) / len_csorted
    #         cdf_find = np.arange(1, len_fsorted + 1) / len_fsorted
    #         cdf_greedy = np.arange(1, len_gsorted + 1) / len_gsorted
    #         #cdf_neutronStar = np.arange(1, len_nsorted + 1) / len_nsorted
    #         cdf_neutronStarPlus = np.arange(1, len_npsorted + 1) / len_npsorted
    #         #axs[plot_counter_column].plot(cycleSet_sorted, cdf_cycle, label="Cycle", marker = markerSet[0], ls= lineSet[0], linewidth=2)
    #         if ((plot_counter_row == 0) and (plot_counter_column == 4)):
    #             axs[plot_counter_column].plot(findSet_sorted, cdf_find, label="Find", marker = markerSet[1], ls= lineSet[1], linewidth=2, markersize=6, markevery=10)
    #             axs[plot_counter_column].plot(greedySet_sorted, cdf_greedy, label="Greedy", marker = markerSet[2], ls= lineSet[2], linewidth=2, markersize=6, markevery=10)
    #             #axs[plot_counter_column].plot(neutronStarSet_sorted, cdf_neutronStar, label="NeutronStar", marker = markerSet[3], ls= lineSet[3], linewidth=2, markersize=5)
    #             axs[plot_counter_column].plot(neutronStarPlusSet_sorted, cdf_neutronStarPlus, label="NeutronStarPlus", marker = markerSet[0], ls= lineSet[0], linewidth=2, markersize=6, markevery=10)
    #             axs[plot_counter_column].legend()
    #         else:
    #             axs[plot_counter_column].plot(findSet_sorted, cdf_find, marker = markerSet[1], ls= lineSet[1], linewidth=2, markersize=6, markevery=10)
    #             axs[plot_counter_column].plot(greedySet_sorted, cdf_greedy,  marker = markerSet[2], ls= lineSet[2], linewidth=2, markersize=6, markevery=10)
    #             #axs[plot_counter_column].plot(neutronStarSet_sorted, cdf_neutronStar, label="NeutronStar", marker = markerSet[3], ls= lineSet[3], linewidth=2, markersize=5)
    #             axs[plot_counter_column].plot(neutronStarPlusSet_sorted, cdf_neutronStarPlus,  marker = markerSet[0], ls= lineSet[0], linewidth=2, markersize=6, markevery=10)
    #         axs[plot_counter_column].ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    #         axs[plot_counter_column].set_title(model)
    #         axs[plot_counter_column].set_xlabel("[Syn / NeutronStar]")
    #         plot_counter_column = plot_counter_column + 1
    #     plot_counter_row = plot_counter_row + 1
    # #plt.legend()
    # plt.savefig("cdf_syn_04_" + ".pdf", format="pdf", bbox_inches="tight")


                

