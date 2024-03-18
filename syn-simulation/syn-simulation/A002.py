import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import csv

plt.rcParams['font.size'] = str(15)
plt.rcParams['font.family'] = 'Arial'
time_threshold = 10000000
minCharge = 1
maxCharge = [50, 100, 200, 300, 400, 500]

global var1Index
global var2Index

global static_one
global static_two

global working_cycle

lastSenderSum = 0

neutronStarSet = []
findSet = []

neutronStarSyn = []
findSyn = []

test1 = []
test2 = []


def uniform_integer_random(min_val, max_val):
    # Generate a random integer in the specified range
    return np.random.randint(min_val, max_val + 1)


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
    elif model == "uniform1":
        arrLen = len(test1)
        if (var1Index < arrLen):
            return (test1[var1Index])
        else:
            var1Index = 0
            return (test1[var1Index])
    elif model == "uniform2":
        arrLen = len(test2)
        if (var2Index < arrLen):
            return (test2[var2Index])
        else:
            var2Index = 0
            return (test2[var2Index])


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
            synCounter = synCounter + 1
            findSet.append(waitingTimeS - lastSenderSum)
            break
        if ((waitingTimeS - lastSenderSum) > time_threshold):
            synCounter = synCounter + 1
            findSet.append(waitingTimeS - lastSenderSum)
            break


# Function entry for neutron_star
def neutron_star(model):
    global lastSenderSum
    global var1Index
    global var2Index
    global static_one
    global static_two
    global working_cycle
    lastSenderSum = 0
    var1Index = 0
    var2Index = 0
    # for sender node
    sumSender = energy_model(model, 1)
    sumSender = sumSender + 1
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
    sumReceiver = energy_model(model, 2)
    sumReceiver = sumReceiver + 1
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
    bias_S = working_cycle - sumSender % working_cycle
    bias_R = working_cycle - sumReceiver % working_cycle
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
            synCounter = synCounter + 1
            neutronStarSet.append(sumSender - lastSenderSum)
            break
        if ((sumSender - lastSenderSum) > time_threshold):
            synCounter = synCounter + 1
            neutronStarSet.append(sumSender - lastSenderSum)
            break


if __name__ == "__main__":
    ave_find = []
    ave_neu = []
    for  char_threhold in maxCharge:
        working_cycle = 5
        maxCharge = char_threhold
        fig = plt.figure(constrained_layout=True, figsize=(15, 9))
        fig.suptitle('Synchronization performance comparison')
        while  working_cycle < (maxCharge + 10):
            print("**********" + "The cycles of the coordinator:" + str(working_cycle) + "***********")
            model = "static"
            neutronStarSet = []
            findSet = []
            # producing charging datasets
            for i in range(100):
                test1 = []
                test2 = []
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
                    static_one = uniform_integer_random(minCharge, maxCharge)
                    static_two = uniform_integer_random(minCharge, maxCharge)
                neutron_star(model)
                find(model) 
            print(np.mean(findSet))
            print(np.median(findSet))
            ave_find.append(np.mean(findSet))
            print(np.mean(neutronStarSet))
            print(np.median(neutronStarSet))
            ave_neu.append(np.mean(neutronStarSet))
            working_cycle = working_cycle + 5
        plt.plot(ave_find, label="find")
        plt.plot(ave_neu, label="neu")
        plt.legend()
        plt.savefig(str(maxCharge) + "_static_observe02.pdf", format='pdf')

