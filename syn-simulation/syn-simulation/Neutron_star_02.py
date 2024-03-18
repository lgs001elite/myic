import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import csv

time_threshold = 20000000 # 10000, 100000, 1000000
working_cycle = 4  # 5, 10, 15,  30, 45
minCharge = 1
maxCharge = 30

global var1Index
global var2Index

lastSenderSum = 0

greedySet = []
neutronStarSet = []
findSet = []
cycleSet = []


greedySyn = []
neutronStarSyn = []
findSyn = []
cycleSyn = []


test11 = [
51,
58,
50,
48,
43,
64,
42,
60,
58,
10,
32,
52,
59,
67,
37,
68,
12,
75,
32,
75,
26,
40,
22,
17,
52,
54,
62,
52,
55,
43,
70,
67,
25,
54,
96,
67,
56,
60,
31,
61,
18,
54,
38,
20,
64,
29,
24,
46,
29,
46,
67,
52,
54,
79,
34,
48,
72,
32,
64,
54,
15,
86,
71,
40,
27,
18,
74,
34,
43,
62,
78,
62,
86,
50,
31,
67,
76,
35,
47,
45,
62,
60,
44,
55,
57,
62,
24,
68,
64,
55,
60,
44,
37,
34,
61,
63,
41,
50,
31,
51,
57
]

test21 = [
57,
62,
24,
45,
50,
37,
41,
83,
62,
39,
46,
32,
69,
42,
66,
66,
42,
69,
42,
48,
78,
64,
58,
87,
55,
11,
79,
56,
70,
33,
40,
58,
77,
67,
56,
9,
43,
10,
49,
59,
71,
20,
48,
39,
67,
37,
41,
55,
36,
36,
30,
16,
64,
30,
59,
39,
37,
33,
45,
28,
15,
68,
15,
54,
41,
58,
38,
59,
42,
41,
52,
41,
49,
80,
44,
74,
46,
39,
36,
32,
70,
88,
35,
81,
32,
19,
65,
53,
14,
1,
63,
23,
66,
32,
53,
98,
52,
46,
28,
92,
34,
63,
62]


test12= [
54,
36,
85,
51,
55,
3,
84,
14,
12,
53,
13,
64,
20,
14,
24,
6,
6,
47,
59,
34,
25,
11,
34,
70,
39,
54,
67,
24,
45,
14,
20,
71,
4,
17,
7,
20,
69,
15,
24,
25,
15,
12,
29,
17,
5,
24,
34,
47,
34,
49,
30,
2,
2,
33,
50,
44,
16,
46,
99,
1,
21,
46,
4,
65,
11,
44,
1,
42,
1,
12,
88,
39,
41,
48,
5,
6,
17,
22,
13,
9,
78,
25,
59,
26,
52,
22,
5,
6,
24,
20,
49,
43,
52,
67,
79,
2,
56,
28,
2,
74,
16,
7,
22,
26,
1,
60,
20,
7,
31,
36,
30,
10,
11,
11,
38,
79,
63,
24,
14,
13,
41,
2,
69,
20,
10,
40,
17,
26,
84,
53,
12,
23,
5,
2,
52,
63,
15,
6,
50,
97,
95,
87,
26,
33,
11,
59,
32,
40,
89,
98
]

test22 = [
40,
11,
16,
93,
23,
4,
45,
28,
33,
12,
46,
63,
75,
2,
68,
16,
22,
55,
26,
23,
23,
12,
51,
3,
8,
34,
73,
6,
5,
74,
11,
42,
18,
34,
80,
23,
24,
16,
39,
10,
13,
53,
69,
4,
23,
13,
56,
15,
17,
18,
6,
69,
11,
28,
51,
15,
89,
39,
63,
59,
68,
94,
46,
63,
47,
5,
22,
7,
35,
9,
79,
19,
5,
12,
7,
54,
14,
50,
65,
86,
12,
43,
3,
14,
14,
88,
66,
5,
3,
71,
23,
56,
24,
82,
33,
47,
4,
21,
26,
55,
66,
57,
37,
22,
36,
10,
55,
28,
39,
49,
11,
42,
77,
15,
44,
30,
15,
24,
43,
36,
38,
18,
24,
9,
3,
12,
10,
32,
51,
9,
15,
32,
53,
70,
7,
9,
7,
3,
22,
9,
21,
41,
10,
1,
73,
9,
63,
76,
4,
53,
8
]



test1 = [
83,
71,
9,
41,
20,
23,
91,
26,
48,
45,
60,
34,
8,
43,
87,
56,
95,
95,
66,
69,
91,
9,
10,
69,
34,
45,
20,
69,
8,
20,
66,
87,
83,
8,
2,
60,
79,
95,
51,
44,
82,
41,
64,
7,
46,
69,
47,
40,
79,
63,
39,
55,
28,
35,
58,
99,
12,
10,
82,
51,
33,
31,
91,
81,
25,
95,
66,
97,
23,
27,
31,
67,
87,
4,
96,
7,
3,
43,
19,
21,
6,
54,
70,
22,
14,
12,
86,
32,
96,
19,
38,
15,
78,
8,
17,
78,
28,
36,
94,
63,
80,
77,
48
]

test2 = [
94,
60,
17,
31,
90,
77,
16,
40,
71,
65,
32,
35,
94,
61,
35,
67,
8,
19,
88,
82,
69,
81,
99,
61,
58,
31,
1,
44,
33,
54,
77,
53,
94,
69,
65,
21,
80,
86,
7,
29,
17,
27,
10,
57,
47,
54,
56,
1,
62,
83,
12,
48,
42,
56,
64,
71,
16,
59,
51,
38,
10,
94,
74,
55,
73,
15,
34,
36,
61,
25,
78,
90,
96,
96,
54,
27,
96,
33,
88,
75,
55,
47,
59,
51,
44,
65,
87,
83,
94,
99,
67
]


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


file_path = "charging_traces/stairs_0th.csv"
df1 = read_csv_to_array_of_ints(file_path)
file_path = "charging_traces/stairs_1th.csv"
df2 = read_csv_to_array_of_ints(file_path)

def energy_model(model, index):
    global var1Index
    global var2Index
    if (index == 1):
        model = model + "1"
    if (index == 2):
        model = model + "2"
    if (model == "gauss1") or (model == "gauss2"):
        return normal_integer_random(minCharge, maxCharge, 10, 5)
    elif (model == "expo1") or (model == "expo2"):
        return exponential_integer_random(minCharge, maxCharge, 0.1)
    elif (model == "uniform1") or (model == "uniform2"):
        return uniform_integer_random(minCharge, maxCharge)
    elif model == "static1":
        return 20
    elif model == "static2":
        return 30
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
        #file_path = "charging_traces/stairs_0th.csv"
        #df = read_csv_to_array_of_ints(file_path)
        arrLen = len(df1)
        if (var1Index < arrLen):
            return (df1[var1Index][0])
        else:
            var1Index = 0
            return (df1[var1Index][0])
    elif model == "stairs2":
        #file_path = "charging_traces/stairs_1th.csv"
        #df = read_csv_to_array_of_ints(file_path)
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
    global findSet
    global lastSenderSum
    global var1Index
    global var2Index
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
            # rd.randint(0, energySet1[0])    
    waitingTimeR = receiverCharge + 1 + \
            geoGenerator(returnParameter(receiverCharge)) + receiverBias
            # rd.randint(0, energySet2[0])
    # if (model == "static"):
    #     waitingTimeS = waitingTimeS + uniform_integer_random(0, 30)
    #     waitingTimeR = waitingTimeR + uniform_integer_random(0, 30)
    stopSignal = 1
    synCounter = 0
    while (stopSignal != 0):
        if (waitingTimeS > time_threshold):
            findSyn.append(synCounter)
            break
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
            lastSenderSum = waitingTimeS
            senderCharge = energy_model(model, 1)
            var1Index = var1Index + 1 
            delay = geoGenerator(returnParameter(senderCharge))
            waitingTimeS = senderCharge + 1 + delay + waitingTimeS


# Function entry for greedy
def greedy(model):
    global greedySet
    global lastSenderSum
    global var1Index
    global var2Index
    lastSenderSum = 0
    senderCharge = energy_model(model, 1)
    var1Index = var1Index + 1 
    receiverCharge = energy_model(model, 2)
    var2Index = var2Index + 1 
    receiverBias = uniform_integer_random(0, receiverCharge)
    senderBias = uniform_integer_random(0, senderCharge)
    waitingTimeS = senderCharge + 1 + senderBias
    waitingTimeR = receiverCharge + 1 + receiverBias
    # if (model == "static"):
    #     waitingTimeS = waitingTimeS + uniform_integer_random(0, 30)
    #     waitingTimeR = waitingTimeR + uniform_integer_random(0, 30)
    stopSignal = 1
    synCounter = 0
    while (stopSignal != 0):
        if (waitingTimeS > time_threshold):
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
        else:
            synCounter = synCounter + 1
            greedySet.append(waitingTimeS - lastSenderSum)
            lastSenderSum = waitingTimeS
            senderCharge = energy_model(model, 1)
            var1Index = var1Index + 1 
            waitingTimeS = senderCharge + 1 + waitingTimeS


# Function entry for cycle
def cycle(model):
    global cycleSet
    global lastSenderSum
    global var1Index
    global var2Index
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
    # if (model == "static"):
    #     waitingTimeR = waitingTimeR + uniform_integer_random(0, 30)
    #     waitingTimeS = waitingTimeS + uniform_integer_random(0, 30)
    stopSignal = 1
    synCounter = 0
    while (stopSignal != 0):
        if (waitingTimeS > time_threshold):
            # print(model + "__cycle__:" + str(waitingTimeS))
            cycleSyn.append(synCounter)
            break
        # print(timeCounter)
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
            synCounter = synCounter + 1
            cycleSet.append(waitingTimeS - lastSenderSum)
            lastSenderSum = waitingTimeS
            senderCharge = energy_model(model, 1)
            var1Index = var1Index + 1
            senderDelay = working_cycle - (senderCharge + 1) % working_cycle
            waitingTimeS = senderCharge + 1 + senderDelay + waitingTimeS


# Function entry for neutron_star
def neutron_star(model):
    global neutronStarSet
    global lastSenderSum
    global var1Index
    global var2Index
    lastSenderSum = 0
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
    while (sumSender != sumReceiver):
        if (sumSender > time_threshold):
            neutronStarSyn.append(synCounter)
            break
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
            lastSenderSum = sumSender
            tch_sender = energy_model(model, 1)
            delay_sender = working_cycle - ((tch_sender + 1) % working_cycle)
            var1Index = var1Index + 1
            sumSender = sumSender + delay_sender + tch_sender + 1


if __name__ == "__main__":
    for model in ["stairs"]:  # "gauss", "expo", "uniform", "stairs", 
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
            # cycle(model)
            # # print("***")
            # greedy(model)
            # # print("***")
            # find(model) 
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
        # print("*********** length ***********")
        print(findSyn)
        # print(greedySet)
        # print(cycleSet)
        # print(neutronStarSet)
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
        print(np.average(findSyn))
        print(np.average(greedySyn))
        print(np.average(cycleSyn))
        print(np.average(neutronStarSyn))
        # print(len(test1))
        # print(len(test2))
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

